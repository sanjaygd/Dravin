from datetime import datetime

import psycopg2

from db_feeder.database import PGS
from quote_lib.ticker_symbol import quote_dict


class TableCleaner(PGS):

    def clean_table(self,db_key=None,tb_name=None,delete_all=False,tdy=None):
        if db_key and tb_name:
            try:
                self.connect(db_key,_from='db_table_cleaner.clean_table')
                cur = self.connection.cursor()
                sql = f'DELETE FROM {tb_name}'
                cur.execute(sql)
                self.connection.commit()
                print(f'table {tb_name} cleaned successfully')
            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()

        elif db_key and delete_all == True:
            try:               
                self.connect(db_key)
                
                cur = self.connection.cursor()
                for tb_key,tb_value in quote_dict.items():
                    tb_name = quote_dict[tb_key]
                    sql = f'DELETE FROM {tb_name}'
                    cur.execute(sql)
                    self.connection.commit()
                    print(f'table {tb_name} cleaned successfully')
                    

            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()
                else:
                    print('All Okay')

        elif tdy == True:
            try:               
                self.connect(db_key='opening_market')
                
                cur = self.connection.cursor()
                for tb_key,tb_value in quote_dict.items():
                    tb_name = quote_dict[tb_key]
                    _today = datetime.now().date()
                    sql = f"DELETE FROM {tb_name} WHERE date='{_today}'"
                    cur.execute(sql)
                    self.connection.commit()
                    print(f"table {tb_name} cleaned successfully for today date {_today}")
                    

            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()
                else:
                    print('All Okay')

if __name__ == "__main__":
    x = TableCleaner()
    x.clean_table(tdy=True)