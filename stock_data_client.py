
import yfinance as yf
import datetime as t


class StockDataClient:
    


    def __init__(self, ticker, period):

        self.__ticker = ticker;
        self.__stock = yf.Ticker(ticker)
        self.__period = t.datetime.strptime("21-01-01", "%y-%m-%d") + t.timedelta(days = period)

    def set_ticker(self, ticker):
        self.__ticker = ticker
        

    def get_ticker(self):
           return self.__ticker


    def set_period(self, period):
        self.__period = str(period)+"d"

    def get_period(self):
         return self.__period

    def get_close_price(self):
        return self.__stock.history(start = '2021-01-01',end = self.__period , interval = '1d').Close
        
    
        
