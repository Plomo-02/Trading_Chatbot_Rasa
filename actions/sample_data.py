from datetime import datetime
import json
import pandas as pd
from actions.database import *
from sqlalchemy.sql import exists

from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

# Definizione della classe ORM per OKXAccountHolding
from typing import List
import pandas as pd



class OKXAccountData:
    def __init__(self, adjEq, borrowFroz, details, imr, isoEq, mgnRatio, mmr, notionalUsd, ordFroz, totalEq, uTime, upl):
        self.adjEq = float(adjEq)
        self.borrowFroz = float(borrowFroz)
        self.details = details  # List of OKXAccountHolding objects
        self.imr = float(imr)
        self.isoEq = float(isoEq)
        self.mgnRatio = float(mgnRatio)
        self.mmr = float(mmr)
        self.notionalUsd = float(notionalUsd)
        self.ordFroz = float(ordFroz)
        self.totalEq = float(totalEq)
        self.uTime = uTime
        self.upl = float(upl)



# Example instantiation
okx_account_data = {
        'adjEq': '0.0',
        'borrowFroz': '0.0',
        'details': [
            {
                'ccy': 'BTC', 'eq': '1.0', 'eqUsd': '30000', 'availBal': '0.0', 'availEq': '0.0',
                'borrowFroz': '0.0', 'cashBal': '0.0', 'clSpotInUseAmt': '0.0', 'crossLiab': '0.0',
                'disEq': '0.0', 'fixedBal': '0.0', 'frozenBal': '0.0', 'imr': '0.0', 'interest': '0.0',
                'isoEq': '0.0', 'isoLiab': '0.0', 'isoUpl': '0.0', 'liab': '0.0', 'maxLoan': '0.0',
                'mgnRatio': '0.0', 'mmr': '0.0', 'notionalLever': '0.0', 'ordFrozen': '0.0',
                'rewardBal': '0.0', 'smtSyncEq': '0.0', 'spotInUseAmt': '0.0', 'spotIsoBal': '0.0',
                'stgyEq': '0.0', 'twap': '0.0', 'uTime': None, 'upl': '0.0', 'uplLiab': '0.0'
            },
            {
                'ccy': 'USDT', 'eq': '100000', 'eqUsd': '100000', 'availBal': '0.0', 'availEq': '0.0',
                'borrowFroz': '0.0', 'cashBal': '0.0', 'clSpotInUseAmt': '0.0', 'crossLiab': '0.0',
                'disEq': '0.0', 'fixedBal': '0.0', 'frozenBal': '0.0', 'imr': '0.0', 'interest': '0.0',
                'isoEq': '0.0', 'isoLiab': '0.0', 'isoUpl': '0.0', 'liab': '0.0', 'maxLoan': '0.0',
                'mgnRatio': '0.0', 'mmr': '0.0', 'notionalLever': '0.0', 'ordFrozen': '0.0',
                'rewardBal': '0.0', 'smtSyncEq': '0.0', 'spotInUseAmt': '0.0', 'spotIsoBal': '0.0',
                'stgyEq': '0.0', 'twap': '0.0', 'uTime': None, 'upl': '0.0', 'uplLiab': '0.0'
            }
        ],
        'imr': '0.0', 'isoEq': '0.0', 'mgnRatio': '0.0', 'mmr': '0.0', 'notionalUsd': '0.0', 'ordFroz': '0.0',
        'totalEq': '130000', 'uTime': '0', 'upl': '0.0'
    }

okx_account = OKXAccount(
    id='1',
    created_at=datetime.datetime(2023, 1, 1, 0, 0, 0),
    scheduled_timestamp=datetime.datetime(2023, 1, 1, 0, 0, 0),
    data=json.dumps(okx_account_data),
    validated=True
)
    # Aggiunta degli oggetti al sessione di SQLAlchemy

  

# Sample data for orders
sample_order_data = {
    "live": {
        "instType": "SPOT",
        "instId": "MATIC-USDT",
        "tgtCcy": "",
        "ccy": "",
        "ordId": "1556935276122767360",
        "clOrdId": "17189026861",
        "algoClOrdId": "",
        "algoId": "",
        "tag": "",
        "px": "0.576",
        "sz": "1",
        "notionalUsd": "0.57580992",
        "ordType": "limit",
        "side": "buy",
        "posSide": "",
        "tdMode": "cash",
        "accFillSz": "0",
        "fillNotionalUsd": "",
        "avgPx": "0",
        "state": "live",
        "lever": "0",
        "pnl": "0",
        "feeCcy": "MATIC",
        "fee": "0",
        "rebateCcy": "USDT",
        "rebate": "0",
        "category": "normal",
        "uTime": "1718902687035",
        "cTime": "1718902687035",
        "source": "",
        "reduceOnly": "false",
        "cancelSource": "",
        "quickMgnType": "",
        "stpId": "",
        "stpMode": "cancel_maker",
        "attachAlgoClOrdId": "",
        "lastPx": "0.5747",
        "isTpLimit": "false",
        "slTriggerPx": "",
        "slTriggerPxType": "",
        "tpOrdPx": "",
        "tpTriggerPx": "",
        "tpTriggerPxType": "",
        "slOrdPx": "",
        "fillPx": "",
        "tradeId": "",
        "fillSz": "0",
        "fillTime": "",
        "fillPnl": "0",
        "fillFee": "0",
        "fillFeeCcy": "",
        "execType": "",
        "fillPxVol": "",
        "fillPxUsd": "",
        "fillMarkVol": "",
        "fillFwdPx": "",
        "fillMarkPx": "",
        "amendSource": "",
        "reqId": "",
        "amendResult": "",
        "code": "0",
        "msg": "",
        "pxType": "",
        "pxUsd": "",
        "pxVol": "",
        "linkedAlgoOrd": {
            "algoId": ""
        },
        "attachAlgoOrds": []
    },
    "filled": {
        "instType": "SPOT",
        "instId": "MATIC-USDT",
        "tgtCcy": "",
        "ccy": "",
        "ordId": "1556935276122767360",
        "clOrdId": "17189026861",
        "algoClOrdId": "",
        "algoId": "",
        "tag": "",
        "px": "0.576",
        "sz": "1",
        "notionalUsd": "0.57580992",
        "ordType": "limit",
        "side": "buy",
        "posSide": "",
        "tdMode": "cash",
        "accFillSz": "1",
        "fillNotionalUsd": "0.574310415",
        "avgPx": "0.5745",
        "state": "filled",
        "lever": "0",
        "pnl": "0",
        "feeCcy": "MATIC",
        "fee": "-0.001",
        "rebateCcy": "USDT",
        "rebate": "0",
        "category": "normal",
        "uTime": "1718902687036",
        "cTime": "1718902687035",
        "source": "",
        "reduceOnly": "false",
        "cancelSource": "",
        "quickMgnType": "",
        "stpId": "",
        "stpMode": "cancel_maker",
        "attachAlgoClOrdId": "",
        "lastPx": "0.5747",
        "isTpLimit": "false",
        "slTriggerPx": "",
        "slTriggerPxType": "",
        "tpOrdPx": "",
        "tpTriggerPx": "",
        "tpTriggerPxType": "",
        "slOrdPx": "",
        "fillPx": "0.5745",
        "tradeId": "6176408",
        "fillSz": "1",
        "fillTime": "1718902687035",
        "fillPnl": "0",
        "fillFee": "-0.001",
        "fillFeeCcy": "MATIC",
        "execType": "T",
        "fillPxVol": "",
        "fillPxUsd": "",
        "fillMarkVol": "",
        "fillFwdPx": "",
        "fillMarkPx": "",
        "amendSource": "",
        "reqId": "",
        "amendResult": "",
        "code": "0",
        "msg": "",
        "pxType": "",
        "pxUsd": "",
        "pxVol": "",
        "linkedAlgoOrd": {
            "algoId": ""
        },
        "attachAlgoOrds": []
    }
}

# Inserisci i dati di esempio nella tabella 'orders'
sample_order = [Order(
    id="a37eda33-405e-4e89-8705-86bdfbf564ec",
    oems_algorithm_id=0,
    order_id="1556935276122767360",
    status="filled",
    data=sample_order_data,
    validated=False,
    created_at=datetime.datetime.now(),  # current execution timestamp
    updated_at=datetime.datetime.now()   # current execution timestamp
)]

# Sample data for metrics
metrics = [
    Metrics(
        id='1e7d8b10-88a4-4e9d-bc0c-9a5d29bc66c8',
        exchange='OK',
        created_at=pd.Timestamp('2023-06-01T12:00:00Z'),
        scheduled_timestamp=pd.Timestamp('2023-12-01T12:00:00Z'),
        timeframe='2023-06-01 to 2023-12-01',
        portfolio_account_metrics={
            'net_asset_value': 150000.00,
            'assets': 140000.00,
            'cash': 10000.00,
            'margin': 5000.00,
            'buying_power': 20000.00,
            'margin_utilization': 25.00,
            'margin_available': 15000.00,
            'volume': 0,
            'turnover': 0,
            'number_of_trades': 0
        },
        portfolio_return_metrics={
            'unrealized_pnl': 5000.00,
            'realized_pnl': 2000.00,
            'avg_pnl_per_trade': 100.00,
            'avg_positive_pnl': 150.00,
            'avg_negative_pnl': -50.00,
            'fees': 300.00,
            'cagr': 10.00,
            'win_rate': 60.00,
            'up_time': 70.00,
            'down_time': 30.00,
            'total_trades': 20,
            'long_trades': 15,
            'short_trades': 5
        },
        portfolio_risk_metrics={
            'concentration': 30.00,
            'value_at_risk': 10000.00,
            'volatility': 5.00,
            'standard_deviation': 4.50,
            'beta': 1.20,
            'sharpe': 1.50,
            'max_drawdown': 20.00,
            'drawdown_period': 30,
            'drawdown_recovery': 20,
            'max_runup': 25.00,
            'runup_period': 15
        },
        position_execution_quality_metrics={
            'unrealized_pnl': 3000.00,
            'realized_pnl': 1000.00,
            'fees': 150.00
        },
        position_risk_metrics={
            'concentration': 20.00,
            'value_at_risk': 5000.00,
            'sharpe_ratio': 1.30,
            'beta': 0.90,
            'volatility': 4.00,
            'standard_deviation': 4.00,
            'max_drawdown': 15.00,
            'drawdown_period': 20,
            'drawdown_recovery': 10,
            'max_runup': 18.00,
            'runup_period': 12
        },
        position_return_metrics={}
    ),
    Metrics(
        id='2e9d8b12-77a4-4e1d-bc0c-7a5d29bc66c8',
        exchange='BINANCE',
        created_at=pd.Timestamp('2023-06-15T12:00:00Z'),
        scheduled_timestamp=pd.Timestamp('2023-12-15T12:00:00Z'),
        timeframe='2023-06-15 to 2023-12-15',
        portfolio_account_metrics={
            'net_asset_value': 250000.00,
            'assets': 230000.00,
            'cash': 20000.00,
            'margin': 10000.00,
            'buying_power': 30000.00,
            'margin_utilization': 33.33,
            'margin_available': 20000.00,
            'volume': 0,
            'turnover': 0,
            'number_of_trades': 0
        },
        portfolio_return_metrics={
            'unrealized_pnl': 7000.00,
            'realized_pnl': 3000.00,
            'avg_pnl_per_trade': 150.00,
            'avg_positive_pnl': 200.00,
            'avg_negative_pnl': -60.00,
            'fees': 400.00,
            'cagr': 12.00,
            'win_rate': 65.00,
            'up_time': 75.00,
            'down_time': 25.00,
            'total_trades': 25,
            'long_trades': 20,
            'short_trades': 5
        },
        portfolio_risk_metrics={
            'concentration': 25.00,
            'value_at_risk': 15000.00,
            'volatility': 6.00,
            'standard_deviation': 5.00,
            'beta': 1.30,
            'sharpe': 1.70,
            'max_drawdown': 18.00,
            'drawdown_period': 28,
            'drawdown_recovery': 18,
            'max_runup': 30.00,
            'runup_period': 20
        },
        position_execution_quality_metrics={
            'unrealized_pnl': 4000.00,
            'realized_pnl': 2000.00,
            'fees': 200.00
        },
        position_risk_metrics={
            'concentration': 22.00,
            'value_at_risk': 7000.00,
            'sharpe_ratio': 1.50,
            'beta': 1.10,
            'volatility': 5.50,
            'standard_deviation': 5.50,
            'max_drawdown': 17.00,
            'drawdown_period': 25,
            'drawdown_recovery': 15,
            'max_runup': 22.00,
            'runup_period': 16
        },
        position_return_metrics={}
    )
]

metrics_ids = ['1e7d8b10-88a4-4e9d-bc0c-9a5d29bc66c8', '2e9d8b12-77a4-4e1d-bc0c-7a5d29bc66c8']
add_metrics = False

for metrics_id in metrics_ids:
    if not session.query(exists().where(Metrics.id == metrics_id)).scalar():
            add_metrics = True

if add_metrics:
    session.add_all(metrics)

if not session.query(exists().where(Order.order_id == '1556935276122767360')).scalar():
    session.add_all(sample_order)
if not session.query(exists().where(OKXAccount.id == '1')).scalar():       
    session.add(okx_account)
    
session.commit()
