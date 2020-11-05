from datetime import datetime
import psycopg2

from db_feeder.database import PGS
from quote_lib.ticker_symbol import nifty_50_list


class Inspector(PGS):
    def __init__(self):
        super().__init__('inspect')


    def monitor(self,db_key='feed'):
        self.connect(db_key)
        
        today = datetime.now().date().strftime('%Y-%m-%d')
        try:
            self.connect(db_key)
            cur = self.connection.cursor()
            for tb_name in nifty_50_list: 
                sql = f"SELECT COUNT(*) FROM {tb_name} WHERE date='{today}'"
                cur.execute(sql)
                res = cur.fetchone()
                print(res)
        except (Exception, psycopg2.Error) as error :
            print (error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
            else:
                print('All Okay')



if __name__ == "__main__":
    ini = Inspector()
    ini.monitor()