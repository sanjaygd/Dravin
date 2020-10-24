import psycopg2

from db_feeder.database import PGS
from quote_lib.ticker_symbol import quote_dict
from quote_lib.ticker_symbol import nifty_50_list


class TableMaker(PGS):
    def __init__(self):
        super().__init__('db_table_maker')
        

    def create_tables(self,db_key=None,tb_name=None,nifty50=False, candle_15=False):
        if db_key and tb_name:
            try:
                self.connect(db_key)
                cur = self.connection.cursor()
                sql = f'''CREATE TABLE IF NOT EXISTS {tb_name}(row_count SERIAL PRIMARY KEY, symbol VARCHAR(25) NOT NULL, date DATE NOT NULL, last_update_time TIME NOT NULL, insert_time TIME NOT NULL, open DECIMAL NOT NULL, high DECIMAL NOT NULL, low DECIMAL NOT NULL, preclose DECIMAL NOT NULL, ltp DECIMAL NOT NULL, cng DECIMAL NOT NULL, pcng DECIMAL NOT NULL, volume DECIMAL NOT NULL, value DECIMAL NOT NULL, request_count INTEGER NOT NULL,advances INTEGER NOT NULL, declines INTEGER NOT NULL, ma_20 DECIMAL NULL, ma_200 DECIMAL null)'''
                cur.execute(sql)
                self.connection.commit()
                print('table created succesfully')

            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()

        elif db_key and nifty50:
            try:               
                self.connect(db_key)
                
                cur = self.connection.cursor()
                for tb_name in nifty_50_list:
                    print(tb_name)
                    sql = f'''CREATE TABLE IF NOT EXISTS {tb_name}(row_count SERIAL PRIMARY KEY, symbol VARCHAR(25) NOT NULL, date DATE NOT NULL, last_update_time VARCHAR(50) NOT NULL, insert_time TIME NOT NULL, open DECIMAL NOT NULL, high DECIMAL NOT NULL, low DECIMAL NOT NULL, preclose DECIMAL NOT NULL, ltp DECIMAL NOT NULL, cng DECIMAL NOT NULL, pcng DECIMAL NOT NULL, volume DECIMAL NOT NULL, value DECIMAL NOT NULL, request_count INTEGER NOT NULL,advances INTEGER NOT NULL, declines INTEGER NOT NULL, ma_20 DECIMAL NULL, ma_200 DECIMAL null)'''
                    cur.execute(sql)
                    self.connection.commit()

            except (Exception, psycopg2.Error) as error:
                print ("Error while connecting to PGSQL", error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()
                else:
                    print('All Okay')

        elif db_key and candle_15:
            try:               
                self.connect(db_key)
                
                cur = self.connection.cursor()
                for tb_key,tb_value in quote_dict.items():
                    tb_name = f"{quote_dict[tb_key]}_15"
                    print(tb_name)
                    sql = f'''CREATE TABLE IF NOT EXISTS {tb_name}(row_count SERIAL PRIMARY KEY, date DATE NOT NULL, time TIME NOT NULL, symbol VARCHAR(25) NOT NULL, ltp DECIMAL, pcng DECIMAL, volume DECIMAL, turnover DECIMAL );'''
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
    

    def create_proxy_ip_table(self,db_key='proxy'):
        try:               
            self.connect(db_key)
            
            cur = self.connection.cursor()
            sql = f"CREATE TABLE IF NOT EXISTS ip_address(ip VARCHAR(50) NOT NULL,time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
            cur.execute(sql)
            self.connection.commit()
            print('ip_address table created successfully')

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
    x.create_tables(db_key='sample', tb_name='demo1')
    # x.create_proxy_ip_table()
    






        
       

        
        
