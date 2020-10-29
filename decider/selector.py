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
            
            for tb_name in nifty_50_list:
                # ltp = None
                # _open = None
                # pcng = None
                # cpr = None
                # ma_20 = None
                # ma_200 = None
                # pre_high = None
                # pre_low = None
                sql = f"SELECT symbol,ltp,open,pcng,ma_20,ma_200 FROM {tb_name} ORDER BY row_count DESC LIMIT 1"
                cur.execute(sql)
                result = cur.fetchone()
                symbol,ltp,_open,pcng,ma_20,ma_200 = result
                print(symbol)
                today = datetime.now().date().strftime('%Y-%m-%d')

                sql1 = f"SELECT cpr,pre_high,pre_low from {tb_name}_piv WHERE date='{today}'"
                cur.execute(sql1)
                result = cur.fetchone()
                cpr,pre_high,pre_low = result

                print(ltp>_open, ltp>pre_high , pcng<=1.7 , ltp>cpr , ltp>ma_20 , ltp>ma_200 , ma_20>ma_200)
                if ltp>_open and ltp>pre_high and pcng<=1.7 and ltp>cpr and ltp>ma_20 and ltp>ma_200 and ma_20>ma_200:
                    print(symbol, 'is prefered for long trade')
                elif ltp<_open and ltp<pre_low and pcng>=-1.7 and ltp<cpr and ltp<ma_20 and ltp<ma_200 and ma_20<ma_200:
                    print(symbol, 'prefered for short trade')
                else:
                    print('found nothing')
        except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
            else:
                print('All Okay')



if __name__ == "__main__":
    ini = Selector()
    ini.select()