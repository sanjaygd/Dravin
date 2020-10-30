from datetime import datetime

import psycopg2

from db_feeder.database import PGS
from indicators.trend import Trend



class Opener(PGS):
    def __init__(self):
        super().__init__('opener')

    def entry(self):
        ini = Trend()
        market_trend = ini.quick_trend()
        print(market_trend)
        ad,de = market_trend
        symbol = None
        ltp = None
        last_update_time = None
        pcng = None
        try:
            self.connect('feed')
            cur = self.connection.cursor()
            sql = f"SELECT symbol,ltp,last_update_time,pcng FROM nifty_50 ORDER BY row_count DESC LIMIT 1"
            cur.execute(sql)
            result = cur.fetchone()
            symbol,ltp,last_update_time,pcng = result
        except (Exception, psycopg2.Error) as error :
                print (error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
            else:
                print('All Okay')

        try:
            self.connect('opportunity')
            cur = self.connection.cursor()
            today = datetime.now().date().strftime('%Y-%m-%d')
            time_now = datetime.now().time().strftime('%H:%M:%S')
            sql = f"SELECT type,status from selector ORDER BY row_count DESC LIMIT 1"
            cur.execute(sql)
            _,status = cur.fetchone()

            if ad>=38 and status != 'open':
                data = (today,last_update_time,time_now,symbol,ltp,pcng,'long','open')
                sql1 = f"INSERT INTO selector (date,last_update_time,insert_time,symbol,ltp,last_update_time,pcng,type) values {data} "
                cur.execute(sql1)
                self.connection.commit()
            elif de>=38 and status != 'open':
                data = (today,last_update_time,time_now,symbol,ltp,pcng,'short')
                sql2 = f"INSERT INTO selector (date,last_update_time,insert_time,symbol,ltp,last_update_time,pcng,type) values {data} "
                cur.execute(sql2)
                self.connection.commit()
        except (Exception, psycopg2.Error) as error :
                print (error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
            else:
                print('All Okay')




if __name__ == "__main__":
    ini = Opener()
    ini.entry()    