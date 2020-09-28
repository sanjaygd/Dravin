import psycopg2

from db_feeder.database import PGS
from db_feeder.db_record import db_keys
from quote_lib.ticker_symbol import quote_dict


class TableMaker(PGS):
    def __init__(self):
        super().__init__()
        

    def create_tables(self,db_key=None,tb_name=None,nifty100=False):
        if db_key and tb_name:
            try:
                self.connect(db_key)
                cur = self.connection.cursor()
                sql = f'''CREATE TABLE IF NOT EXISTS {tb_name}(date DATE NOT NULL, time TIME NOT NULL PRIMARY KEY, symbol VARCHAR(25) NOT NULL, ltp INTEGER, pcng INTEGER, volume INTEGER, turnover INTEGER );'''
                cur.execute(sql)
                self.connection.commit()
                print('table created succesfully')

            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()

        elif db_key and nifty100:
            try:               
                self.connect(db_key)
                
                cur = self.connection.cursor()
                for tb_key,tb_value in quote_dict.items():
                    tb_name = quote_dict[tb_key]
                    print(tb_name)
                    sql = f'''CREATE TABLE IF NOT EXISTS {tb_name}(row_count SERIAL, date DATE NOT NULL, time TIME NOT NULL PRIMARY KEY, symbol VARCHAR(25) NOT NULL, ltp INTEGER, pcng INTEGER, volume INTEGER, turnover INTEGER );'''
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
    x = TableMaker()
    x.create_tables('sample')


# x.test()

# y = PGS()

# print(y)



        
       

        
        
