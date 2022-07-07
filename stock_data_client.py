
import yfinance as yf

class StockDataClient:
    


    def __init__(self, ticker, period):

        self.__ticker=ticker;
        self.__stock=yf.Ticker(ticker)
        self.__period=str(period)+"d"

    def set_ticker(self, ticker):
        self.__ticker=ticker
        

    def get_ticker(self):
           return self.__ticker


    def set_period(self, period):
        self.__period=str(period)+"d"

    def get_period(self):
         return self.__period

    def get_close_price(self):
        return self.__stock.history(period=self.__period, interval='1d').Close
        
    
        
