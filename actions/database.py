import pathlib
from sqlalchemy import create_engine, Column, String, DateTime, Boolean, Integer, JSON, func, Text, inspect
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import uuid



Base = declarative_base()

# class Account(Base):
#     __tablename__ = 'accounts'
#     id = Column(String, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
#     created_at = Column(DateTime, default=datetime.datetime.now())
#     scheduled_timestamp = Column(DateTime)
#     data = Column(JSON)
#     validated = Column(Boolean, default=False)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(String, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    oems_algorithm_id = Column(Integer)
    order_id = Column(String)
    status = Column(String)
    data = Column(JSON)
    validated = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.datetime.now())


class Metrics(Base):
    __tablename__ = 'metrics'
    id = Column(String, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    exchange = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    scheduled_timestamp = Column(DateTime)
    portfolio_account_metrics = Column(JSON)
    portfolio_return_metrics = Column(JSON)
    portfolio_risk_metrics = Column(JSON)
    portfolio_execution_quality_metrics = Column(JSON)
    position_execution_quality_metrics = Column(JSON)
    position_risk_metrics = Column(JSON)
    position_return_metrics = Column(JSON)
    timeframe = Column(String)


class OKXAccount(Base):
    __tablename__ = 'accounts'

    id = Column(String, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    scheduled_timestamp = Column(DateTime)
    data = Column(Text)  # JSON data serialized as text
    validated = Column(Boolean, default=False)

    def __init__(self, id, created_at, scheduled_timestamp, data, validated):
        self.id = id
        self.created_at = created_at
        self.scheduled_timestamp = scheduled_timestamp
        self.data = data
        self.validated = validated

    def to_json(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'scheduled_timestamp': self.scheduled_timestamp.isoformat(),
            'data': self.data,
            'validated': self.validated
        }

    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data['id'],
            created_at=datetime.datetime.fromisoformat(json_data['created_at']),
            scheduled_timestamp=datetime.datetime.fromisoformat(json_data['scheduled_timestamp']),
            data=json_data['data'],
            validated=json_data['validated']
        )


# Create an SQLite database
engine = create_engine('sqlite:///actions/trading.db')
inspector = inspect(engine)
if not inspector.get_table_names():
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()