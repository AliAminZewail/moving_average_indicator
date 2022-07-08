
class DataProcessing:

    def __init__(self):
        self.__moving_average=[]
        

    def get_moving_average(self, close_price):
        com_price=0
        operator=1
        
        for cur_day,cur_price in close_price.items():
            mov_avg=(cur_price + com_price) / operator
            operator += 1
            com_price += cur_price
            self.__moving_average.append([cur_day.date(), mov_avg])
        return self.__moving_average





