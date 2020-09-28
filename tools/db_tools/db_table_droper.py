import psycopg2

from db_feeder.database import PGS
from db_feeder.db_record import db_keys
from quote_lib.ticker_symbol import quote_dict


class TableDroper(PGS):
    def __init__(self):
        super().__init__()

        

    def delete_table(self,db_key=None,tb_name=None,drop_all=False):
        if db_key and tb_name:
            try:
                self.connect(db_key)
                cur = self.connection.cursor()
                sql = f'DROP TABLE IF EXISTS {tb_name}'
                cur.execute(sql)
                self.connection.commit()
                print('table dropped succesfully')

            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()

        elif db_key and drop_all == True:
            try:               
                self.connect(db_key)
                
                cur = self.connection.cursor()
                for tb_key,tb_value in quote_dict.items():
                    tb_name = quote_dict[tb_key]
                    print(tb_name)
                    sql = f'DROP TABLE IF EXISTS {tb_name}'
                    cur.execute(sql)
                    self.connection.commit()

            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()
                else:
                    print('All Okay')



if __name__ == "__main__":
    x = TableDroper()
    x.delete_table('sample',drop_all=True)





        
       

        
        
