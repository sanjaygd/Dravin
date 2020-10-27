import datetime as dt
from datetime import datetime


import psycopg2

from db_feeder.database import PGS
from db_feeder.nse_grab import Datafeed
from quote_lib.ticker_symbol import nifty_50_list



class PivotPoints(PGS):
    def __init__(self):
        super().__init__('pivot_points')

    def previous_day(self):
        pre_day = None
        _today = datetime.now().date().strftime('%A')
        today = datetime.now().date()
        if _today == 'Monday':
            pre_day  = today - dt.timedelta(days=3)
        
        return pre_day
        
        

    def pivots(self):
        try:
            self.connect('feed')
            cur = self.connection.cursor()
            ini = Datafeed()
            data_set = ini.get_feed()
            if len(data_set) != 0:
                for ticker_dict in data_set:
                    for tb_name,data in ticker_dict.items():
                        symbol,_date,last_update_time,insert_time,_open,high,low,preclose,ltp,cng,pcng,volume,value,request_count = data
                        
                        _sum = high+low+ltp
                        cpr = round(float(_sum)/3,2)
                        r1 = round(float((2*cpr)-low),2)
                        r2 = cpr+float(high-low)
                        r3 = r1+float(high-low)
                        s1 = round(float((2*cpr)-high),2)
                        print(r1)

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PGSQL", error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
            else:
                print('All Okay')


if __name__ == "__main__":
    ini = PivotPoints()
    # ini.previous_day()
    ini.pivots()