import csv

class DataExporter:
    
    def __init__(self, file_name = 'moving_average_stock.csv'):
         self.__file_name = file_name


    def get_file_name(self):
        return self.__file_name


    def export_file(self, moving_avg):
        header=['date', 'moving average']
        with open(self.__file_name, 'w', encoding='UTF8', newline='') as f:
            writer=csv.writer(f)
            writer.writerow(header)
            writer.writerows(moving_avg)
    
