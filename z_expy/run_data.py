import csv
import pandas as pd
import os
import time
import schedule

from datetime import datetime
from nsetools import Nse


from file_gen import quote_symbol



class GetData():
    
    def __init__(self):
        self.nse = Nse()
        self.quote_symbol = quote_symbol
        self.today = datetime.now()
        self.time_now = self.today.strftime("%H:%M:%S")

    def get_quote_data(self):
        data_list = []
        for symbol in quote_symbol:
            data = {}
            
            quote_data = self.nse.get_quote(symbol)

            data['time']=self.time_now
            data['symbol']=quote_data['symbol']
            data['open']=quote_data['open']
            data['high']=quote_data['dayHigh']
            data['low']=quote_data['dayLow']
            data['prev_close']=quote_data['previousClose']
            data['ltp']=quote_data['lastPrice']
            data['pcng']=quote_data['pChange']
            data['volume']=quote_data['totalTradedVolume']
            data['value']=quote_data['totalTradedValue']
            data['52wh']=quote_data['high52']
            data['52wl']=quote_data['low52']


            data_list.append(data)

        return data_list



class DataWriter():
    def __init__(self):
        self.this_file_path = os.path.abspath(__file__)
        self.BASE_DIR = os.path.dirname(self.this_file_path)
        self.ENTIRE_PROJECT_DIR = os.path.dirname(self.BASE_DIR)
        self.today = datetime.now()
        self.data_dir = os.path.join('daily_data',self.today.strftime("%d-%m-%Y"))
        self.path_to_data_dir = os.path.join(self.ENTIRE_PROJECT_DIR,self.data_dir)
        self.quote_symbol = quote_symbol
        self.fetch_data = GetData()
        self.data_list = self.fetch_data.get_quote_data()

    def write_data(self):
        count = 0
        data_list = self.data_list
        field_names = ['time','symbol','open','high','low','prev_close',
                        'ltp','pcng','volume','value','52wh','52wl']

        for symbol in quote_symbol:
            file_name = os.path.join(self.path_to_data_dir,f'{symbol}.csv')            
            with open(file_name,'a') as data_file:
                for row in data_list:
                    writer = csv.DictWriter(data_file, fieldnames=field_names)
                    writer.writerow(row)
                    del data_list[0]
                    break



                        


if __name__ == "__main__":
    write = DataWriter()
    write.write_data()


