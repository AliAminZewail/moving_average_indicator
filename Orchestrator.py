import stock_data_client as sd
import processing as p
import csv_exporter as ex

def orchestrate(ticker, period):
    stock_1=sd.StockDataClient(ticker, period)
    stock_close_price_data=stock_1.get_close_price()
    data_processing_1=p.DataProcessing()
    moving_average=data_processing_1.get_moving_average(stock_close_price_data)
    export__file_1=ex.DataExporter()
    export__file_1.export_file(moving_average)
    print("file saved successfully : "+export__file_1.get_file_name())

