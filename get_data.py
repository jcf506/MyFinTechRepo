import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import alpaca_trade_api as tradeapi
from time import sleep
import quandl 
import os
quandl.ApiConfig.api_key = os.getenv("QUANDL_API_KEY")
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
api = tradeapi.REST(alpaca_api_key, alpaca_secret_key, api_version='v2')



### Functionality Helper Functions ###
def get_symbols(api):
    """
    Return an updated list of the symbols of the tradeable assets
    """
    assets = api.list_assets()
    tradeable = [asset for asset in assets if asset.tradable ]
    symbols = [asset.symbol for asset in tradeable]
    return(symbols)

def get_prices(symbols):
    """
    Return an updated list of the symbols of the tradeable assets
    """
    timeframe = '1D'
    start_date = pd.Timestamp("2018-06-18", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2020-06-23", tz="America/New_York").isoformat()

    stockprices = []

    i = 0
    for asset in symbols:
        print(asset)
        df = api.get_barset(
            asset,
            timeframe,
            limit=None,
            start=start_date,
            end=end_date,
            after=None,
            until=None,
        ).df


        
        dfq = quandl.get_table('SHARADAR/DAILY', ticker=asset)
        #print(df)
        if df.empty:
            print("     - Empty - Skip")
        elif dfq.empty:
            print("     - Empty - Skip")
        else:
            # format alpaca df for joining
            df = df.stack(level=0)
            df = df.rename_axis(('date', 'ticker'))
            df = df.reset_index()
            df['date'] = df['date'].dt.date
            df = df.set_index(["date", "ticker"])
            
            dfq = dfq.set_index(["date", "ticker"])
            dfb = df.join(dfq)
            print(dfb.head(2))
            #stockprices.append({"Ticker" : asset, "Metrics": dfb})
            stockprices.append(dfb)
            # print("Length:", len(stockprices))
            i += 1
            if i%3 == 0: 
                sleep(1)
    dfstockprices = pd.concat(stockprices)
    dfstockprices.to_csv("fullprocess.csv")