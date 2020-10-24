import datetime as dt
from datetime import datetime

import psycopg2

from db_feeder.database import PGS
from db_feeder.nse_grab import Datafeed
from quote_lib.ticker_symbol import nifty_50_list


class LiveFeeder(PGS):

    """
    This class is use to store the data to the local database
    which is collected by et_grab. This script loads the evry 5 mins data and
    evry 15 mins data to the database

    """
    
    def start_feed(self,db_key=None,tb_name=None,data=None,bypass=None):
        if db_key and data and tb_name: 
            try:
                self.connect(db_key,_from='pg_writer')
                cur = self.connection.cursor()
                sql = f'INSERT INTO {tb_name}(symbol,date,last_update_time,insert_time,_open,high,low,preclose,ltp,cng,pcng,volume,value,request_count,ma_20,ma_200) values {data}'
                cur.execute(sql)
                self.connection.commit()
                self.log_info(f"pg_writer loaded data to {tb_name} successfully")

            except (Exception, psycopg2.Error) as error :
                self.log_error(error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()

        elif db_key:
            try:
                self.connect(db_key)
                cur = self.connection.cursor()
                data_ini = Datafeed()
                data_set = data_ini.get_feed()
                for ticker_dict in data_set:
                    for tb_name,data in ticker_dict.items():                        
                        sql = f'INSERT INTO {tb_name}(symbol,date,last_update_time,insert_time,open,high,low,preclose,ltp,cng,pcng,volume,value,request_count,advances,declines) values {data}'
                        cur.execute(sql)
                        self.connection.commit()
                self.log_info('pg_writer loaded 5 min candle data successufully')

                

            except (Exception, psycopg2.Error) as error :
                self.log_error(error)
                print(error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()



if __name__ == "__main__":
    x = LiveFeeder()
    x.start_feed(db_key='feed')
