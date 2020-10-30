from datetime import datetime

import psycopg2

from db_feeder.database import PGS
from quote_lib.ticker_symbol import nifty_50_list



class Selector(PGS):
    def __init__(self):
        super().__init__('selector')

    def select(self):
        

        try:
            self.connect('feed')
            # print(self.connection)
            cur = self.connection.cursor()
            long_count = 0
            short_count = 0
            for tb_name in nifty_50_list:
                # ltp = None
                # _open = None
                # pcng = None
                # cpr = None
                # ma_20 = None
                # ma_200 = None
                # pre_high = None
                # pre_low = None
                sql = f"SELECT symbol,ltp,last_update_time,open,pcng,ma_20,ma_200 FROM {tb_name} ORDER BY row_count DESC LIMIT 1"
                cur.execute(sql)
                result = cur.fetchone()
                symbol,ltp,last_update_time,_open,pcng,ma_20,ma_200 = result

                print(symbol,pcng)
                today = datetime.now().date().strftime('%Y-%m-%d')
                time_now = datetime.now().time().strftime('%H:%M:%S')
                sql1 = f"SELECT cpr1,cpr2,pre_high,pre_low from {tb_name}_piv WHERE date='{today}'"
                cur.execute(sql1)
                result = cur.fetchone()
                cpr1,cpr2,pre_high,pre_low = result

                pcng = float(pcng)
                ltp = float(ltp)
                _open = float(_open)
                pre_high = float(pre_high)
                pre_low = float(pre_low)
                cpr1 = float(cpr1)
                cpr2 = float(cpr2)
                if ltp>_open and ltp>pre_high and pcng<=1.7 and ltp>cpr1 and ltp>ma_20 and ltp>ma_200 and ma_20>ma_200:
                    long_count+=1
                    
                    data = (today,last_update_time,time_now,symbol,ltp,pcng,_open,pre_high,pre_low,cpr1,cpr2,'long')
                    sql2 = f"INSERT INTO selector (date,last_update_time,insert_time,symbol,ltp,pcng,open,pre_high,pre_low,cpr1,cpr2,type) values {data}"
                    print(sql2)
                    cur.execute(sql2)
                    self.connection.commit()
                    self.log_info( f'{symbol} is prefered for long trade')
                    print( f'{symbol} is prefered for long trade')
                elif ltp<_open and ltp<pre_low and pcng>=-1.7 and ltp<cpr2 and ltp<ma_20 and ltp<ma_200 and ma_20<ma_200:
                    short_count+=1
                    data = (today,last_update_time,time_now,symbol,ltp,pcng,_open,pre_high,pre_low,cpr1,cpr2,'short')
                    sql2 = f"INSERT INTO selector (date,last_update_time,insert_time,symbol,ltp,pcng,open,pre_high,pre_low,cpr1,cpr2,type) values {data}"
                    print(sql2)
                    cur.execute(sql2)
                    self.connection.commit()
                    self.log_info(f'{symbol} prefered for short trade')
                    print(f'{symbol} prefered for short trade')
                else:
                    print('found nothing')
            self.log_info(f"No. of bull stocks : {long_count}. No. of bear stocks {short_count}")
        except (Exception, psycopg2.Error) as error :
                print (error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
            else:
                print('All Okay')



if __name__ == "__main__":
    ini = Selector()
    ini.select()