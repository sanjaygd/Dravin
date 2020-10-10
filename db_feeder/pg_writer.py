import datetime as dt
from datetime import datetime

import psycopg2

from db_feeder.database import PGS
from db_feeder.et_grab import DataFeed
from quote_lib.ticker_symbol import quote_dict


class LiveFeeder(PGS):

    """
    This class is use to store the data to the local database
    which is collected by et_grab. This script loads the evry 5 mins data and
    evry 15 mins data to the database

    """
    
    def start_feed(self,db_key=None,tb_name=None,data=None):
        if db_key and data and tb_name: 
            try:
                self.connect(db_key,_from='pg_writer')
                cur = self.connection.cursor()
                sql = f'INSERT INTO {tb_name}(date,time,symbol,ltp,pcng,volume,turnover) values {data}'
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
                data_ini = DataFeed('et_grab')
                data_set = data_ini.get_feed()
                candle_15_min = False
                for ticker_dict in data_set:
                    for tb_name,data in ticker_dict.items():                        
                        sql = f'INSERT INTO {tb_name}(date,time,symbol,ltp,pcng,volume,turnover) values {data}'                
                        cur.execute(sql)
                        self.connection.commit()

                        sql1 = f"SELECT time,row_count from {tb_name}_15 ORDER BY row_count DESC LIMIT 1"
                        cur.execute(sql1)
                        result = cur.fetchone()
                        
                        old_t,_ = result 
                        time_now = datetime.now().time()
                        time_now_string = time_now.strftime('%H:%M')
                        time_930 = dt.time(9,30,0)
                        time_930_string = dt.time(9,30).strftime('%H:%M')
                        time_931_string = dt.time(9,31).strftime('%H:%M')
                       

                        old_t_time_delta = dt.timedelta(hours=old_t.hour, minutes=old_t.minute, seconds=old_t.second)
                        time_now_time_delta = dt.timedelta(hours=time_now.hour, minutes=time_now.minute, seconds=time_now.second)
                        diff = time_now_time_delta - old_t_time_delta

                        time_interval = dt.timedelta(hours=0,minutes=14,seconds=0)
                        
                        if time_now_string == time_930_string or time_now_string == time_931_string:
                            sql = f'INSERT INTO {tb_name}_15(date,time,symbol,ltp,pcng,volume,turnover) values {data}'                
                            cur.execute(sql)
                            self.connection.commit()
                            candle_15_min = True

                        elif time_now > time_930 and diff >= time_interval:
                            sql = f'INSERT INTO {tb_name}_15(date,time,symbol,ltp,pcng,volume,turnover) values {data}'                
                            cur.execute(sql)
                            self.connection.commit()
                            candle_15_min = True            

                self.log_info('pg_writer loaded 5 min candle data successufully')
                if candle_15_min:
                    self.log_info('pg_writer loaded 15 min candle data successufully')

            except (Exception, psycopg2.Error) as error :
                self.log_error(error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()



if __name__ == "__main__":
    x = LiveFeeder()
    x.start_feed(db_key='sample')
