# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3




class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []



class ActionPortfolioPerformance(Action):

    def name(self) -> Text:
        return "action_portfolio_performance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Logic to fetch portfolio performance data from database
        performance_data = get_portfolio_performance()
        
        dispatcher.utter_message(text=f"Your portfolio total_pnl for the last month is: {performance_data['total_pnl']}")
        dispatcher.utter_message(text=f"Your portfolio avg_return for the last month is: {performance_data['avg_return']}")
        return []

class ActionCurrentValue(Action):

    def name(self) -> Text:
        return "action_current_value"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Logic to fetch current value of holdings from database
        ccy_list, total_usd = get_current_value()
        
        holdings_str = ", ".join([f"{k}: {v}" for d in ccy_list for k, v in d.items()])

        # Prepare the prompt for the API
        text = f"Here are the current value of your holdings is: {total_usd}, divided in: {holdings_str}"
        


        
        dispatcher.utter_message(text=text)
    

        return []
class ActionRecentTradingActivities(Action):

    def name(self) -> Text:
        return "action_recent_trading_activities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Logic to fetch recent trading activities from database
        trading_activities = get_recent_trading_activities()

        
        dispatcher.utter_message(text=f"Your recent trading activities are: {trading_activities}")
        return []

class ActionLastTradeFee(Action):

    def name(self) -> Text:
        return "action_last_trade_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Logic to fetch the fee of the last trade from database
        live_fee, filled_fee = get_last_trade_fee()
        
        dispatcher.utter_message(text=f"The fee for your last trade was: live fee: {live_fee}, filled fee: {filled_fee}")
        return []

class ActionCurrentPositions(Action):

    def name(self) -> Text:
        return "action_current_positions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Logic to fetch current positions from database
        current_positions = get_current_positions()
        
        dispatcher.utter_message(text=f"Your current positions are: {current_positions}")
        return []


def get_portfolio_performance ():

    metrics = get_metrics()

    performance = calculate_portfolio_performance(metrics)

    return performance

def get_metrics():

    conn = sqlite3.connect("actions/trading.db")
    print("Connessione al database stabilita.")


    query = f"""
    SELECT scheduled_timestamp, portfolio_return_metrics 
    FROM metrics 
    WHERE scheduled_timestamp ;
    """

    cursor = conn.execute(query)

    rows = cursor.fetchall()

    metrics_list = []

    for row in rows:
        timestamp, metrics_json = row
        metrics = json.loads(metrics_json)
        metrics_list.append(metrics)

    conn.close()

    return metrics_list

def calculate_portfolio_performance(metrics_data):

    unrealized_pnl = 0
    realized_pnl = 0
    avg_pnl_per_trade = 0
    fees = 0
    total_trades = 0

    for metrics in metrics_data:
        unrealized_pnl += metrics.get("unrealized_pnl", 0)
        realized_pnl += metrics.get('realized_pnl', 0)
        avg_pnl_per_trade += metrics.get('avg_pnl_per_trade', 0)
        fees += metrics.get('fees', 0)
        total_trades += metrics.get('total_trades', 0)

    total_pnl = unrealized_pnl + realized_pnl - fees

    avg_return = avg_pnl_per_trade * total_trades
    
    return {
        "total_pnl" : total_pnl,
        "avg_return" : avg_return
    }

def get_current_value():

    conn = sqlite3.connect("actions/trading.db")
    print("Connessione al database stabilita.")


    query = f"""
    SELECT data 
    FROM accounts 
    """

    cursor = conn.execute(query)

    rows = cursor.fetchall()
    total_eq = None

    ccy_list = []
    for row in rows:
        json_string = row[0]
        
        data_dict = json.loads(json_string)

        for eqUsd in data_dict["details"]:
            ccy_list.append({eqUsd["ccy"]:eqUsd["eqUsd"]})

        total_eq = data_dict["totalEq"]

    return ccy_list, total_eq

def get_recent_trading_activities():
    conn = sqlite3.connect("actions/trading.db")

    query_accounts = """
    SELECT created_at, scheduled_timestamp, data
    FROM accounts
    WHERE validated = 1
    """
    account_data = conn.execute(query_accounts).fetchall()

    query_orders = """
    SELECT created_at, order_id, status, data
    FROM orders
    WHERE status = 'filled'
    """
    orders_data = conn.execute(query_orders).fetchall()

    query_metrics = """
    SELECT created_at, exchange, portfolio_account_metrics, portfolio_return_metrics
    FROM metrics
    """ 
    metrics_data = conn.execute(query_metrics).fetchall()

    conn.close()

    accounts_summary = []

    for account in account_data:
        created_at, scheduled_timestamp, data = account
        data_dict = json.loads(data)
        totalEq = data_dict.get('totalEq', 'N/A')
        accounts_summary.append({
            'created_at': created_at,
            'scheduled_timestamp': scheduled_timestamp,
            'total_equity': totalEq,
            'details': data_dict.get('details', [])
        })
    
    order_summary = []

    for order in orders_data:
        created_at, order_id, status, data = order
        data_dict = json.loads(data)
        order_summary.append({
            'created_at': created_at,
            'order_id': order_id,
            'status': status,
            'details': data_dict.get('filled', {})
        })

    metrics_summary = []

    for metric in metrics_data:
        created_at, exchange, portfolio_account_metrics, portfolio_return_metrics = metric
        account_metrics = json.loads(portfolio_account_metrics)
        return_metrics = json.loads(portfolio_return_metrics)
        metrics_summary.append({
            'created_at': created_at,
            'exchange': exchange,
            'net_asset_value': account_metrics.get('net_asset_value', 'N/A'),
            'unrealized_pnl': return_metrics.get('unrealized_pnl', 'N/A'),
            'realized_pnl': return_metrics.get('realized_pnl', 'N/A')
        })

    summary = {
        'accounts' : accounts_summary,
        'orders' : order_summary,
        'metrics' : metrics_summary
    }

    return summary

def get_last_trade_fee():
    conn = sqlite3.connect("actions/trading.db")

    query = """
    SELECT data
    FROM orders
    WHERE created_at = (
    SELECT MAX(created_at) 
    FROM orders
    );
    """

    data_json = conn.execute(query).fetchall()

    data = json.loads(data_json[0][0])
    live = data.get("live","N/A")
    live_fee = live.get("fee","N/A")
    filled = data.get("filled","N/A")
    filled_fee = filled.get("fee","N/A")


    return live_fee,filled_fee

def get_current_positions():
    conn = sqlite3.connect("actions/trading.db")
    query = """
    SELECT data
    FROM orders
    """
    rows = conn.execute(query).fetchall()
    conn.close()

    live_positions = []

    for row in rows:
        data_json = row[0]
        try:
            # Stampa di debug
            print(f"Trying to load JSON: {data_json}")

            data = json.loads(data_json)
            live = data.get("live", "N/A")
            live_positions.append(live)
        except json.JSONDecodeError as e:
            print(f"Errore nel caricamento del JSON: {e}")
            # Puoi decidere come gestire gli errori di decodifica, ad esempio saltare questi record
            live_positions.append("Errore nel JSON")

    return live_positions



