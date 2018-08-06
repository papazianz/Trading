"""
Created on Aug 5th, 2018 

-Nick Papazian

"""

from Keys import *
import datetime
from time import sleep
from binance.client import Client

client = Client(api_key, api_secret)

def sys():
    #Check System Status
    try:
        status = client.get_system_status()
        print("\nExchange Status: ", status)
    except():
        print('\nNo connection to server')

def BTC_Bot():
    symbol= 'BTCUSDT'
    quantity= .0025

    order= False
    while order==False:
        BTC= client.get_historical_klines(symbol= symbol, interval= '15m', start_str= '1 hour ago utc')
        if (float(BTC[-1][4])-float(BTC[-2][4]))>500:
            print('Buying .0025 BTC')
            client.order_market_buy(symbol= symbol, quantity= quantity)
            order= False
        elif (float(BTC[-1][4])-float(BTC[-2][4]))>500:
            print('Selling .0025 BTC')
            client.order_limit_sell(symbol= symbol, quantity= quantity)
            order= True
        else:
            print('doing nothing')

sys()
BTC_Bot()