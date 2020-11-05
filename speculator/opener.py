from datetime import datetime

import psycopg2

from db_feeder.database import PGS
from indicators.trend import Trend
from quote_lib.ticker_symbol import nifty_50_list


class Opener(PGS):
    def __init__(self):
        super().__init__('opener')

    def fetch_speculated_stocks(self,db_key='opportunity'):
        speculated_stocks = []
        try:
            self.connect(db_key)
            cur = self.connection.cursor()
            today = datetime.now().date().strftime('%Y-%m-%d')
            sql = f"SELECT symbol FROM selector WHERE date='{today}' ORDER BY row_count"
            cur.execute(sql)
            speculated_stocks = cur.fetchall()

        except (Exception, psycopg2.Error) as error :
            print (error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
            else:
                print('All Okay')
        print(speculated_stocks)



    def check_for_opportunity(self,db_key='feed'):
        try:
            self.connect(db_key)
            cur = self.connection.cursor()
            sql = f"SELECT symbol from "

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
    ini.fetch_speculated_stocks()