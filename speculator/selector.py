from datetime import datetime

import psycopg2

from db_feeder.database import PGS
from indicators.trend import Trend
from quote_lib.ticker_symbol import nifty_50_list,weightage


class BandWidthLookUp(PGS):
    def __init__(self):
        super().__init__('selector')

    def check_narrow_bandwidth(self,db_key='pivot'):
        try:
            self.connect(db_key)
            cur = self.connection.cursor()
            today = datetime.now().date().strftime('%Y-%m-%d')
            bw_dict = {}
            prefered_stocks=[]
            for tb_name in nifty_50_list:
                sql = f"SELECT symbol,band_width from {tb_name} where date='{today}'"
                cur.execute(sql)
                res = cur.fetchone()
                symbol,bw = res
                bw_dict[symbol] = float(bw)
            sorted_pivots = {k:v for k,v in sorted(bw_dict.items(), key=lambda item: item[1])}
            prefered_stocks = list(sorted_pivots.items())[0:5]
                
        except (Exception, psycopg2.Error) as error :
            print (error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
            else:
                print('All Okay')
        return prefered_stocks

        

    def store_prefered_stocks(self,db_key='opportunity'):
        try:
            p4 = self.check_narrow_bandwidth()
            self.connect(db_key)
            cur = self.connection.cursor()
            today = datetime.now().date().strftime('%Y-%m-%d')
            insert_time = datetime.now().time().strftime('%H:%M:%S')
            
            for element in p4:
                symbol,bw = element
                data = (today,insert_time,symbol,bw)
                sql = f"INSERT INTO selector (date,insert_time,symbol,band_width) values {data}"
                cur.execute(sql)
                self.connection.commit()
            self.log_info('Prefered stocks stored in selector')
        except (Exception, psycopg2.Error) as error :
            print (error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
            else:
                print('All Okay')
        


if __name__ == "__main__":
    ini = BandWidthLookUp()
    # ini.check_narrow_bandwidth()
    ini.store_prefered_stocks()