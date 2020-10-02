import psycopg2

from db_feeder.database import PGS
from db_feeder.db_record import db_keys
from quote_lib.ticker_symbol import quote_dict


class TableMaker(PGS):
    def __init__(self):
        super().__init__()
        

    def create_tables(self,db_key=None,tb_name=None,nifty100=False, candle_15=False):
        if db_key and tb_name:
            try:
                self.connect(db_key)
                cur = self.connection.cursor()
                sql = f'''CREATE TABLE IF NOT EXISTS {tb_name}(date DATE NOT NULL, time TIME NOT NULL PRIMARY KEY, symbol VARCHAR(25) NOT NULL, ltp DECIMAL, pcng DECIMAL, volume DECIMAL, turnover DECIMAL );'''
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
                    sql = f'''CREATE TABLE IF NOT EXISTS {tb_name}(row_count SERIAL, date DATE NOT NULL, time TIME NOT NULL PRIMARY KEY, symbol VARCHAR(25) NOT NULL, ltp DECIMAL, pcng DECIMAL, volume DECIMAL, turnover DECIMAL );'''
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

        elif db_key and candle_15:
            try:               
                self.connect(db_key)
                
                cur = self.connection.cursor()
                for tb_key,tb_value in quote_dict.items():
                    tb_name = quote_dict[tb_key]
                    print(tb_name)
                    sql = f'''CREATE TABLE IF NOT EXISTS {tb_name}_15(row_count SERIAL, date DATE NOT NULL, time TIME NOT NULL PRIMARY KEY, symbol VARCHAR(25) NOT NULL, ltp DECIMAL, pcng DECIMAL, volume DECIMAL, turnover DECIMAL );'''
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

        

    def create_open_market(self,db_key='opening_market',tb_name=None):
        if db_key:
            try:               
                self.connect(db_key)
                
                cur = self.connection.cursor()
                for tb_key,tb_value in quote_dict.items():
                    tb_name = quote_dict[tb_key]
                    print(tb_name)
                    sql = f'''CREATE TABLE IF NOT EXISTS {tb_name}(row_count SERIAL, date DATE NOT NULL, time TIME NOT NULL PRIMARY KEY, symbol VARCHAR(25) NOT NULL, opening_price DECIMAL, previous_close DECIMAL,day_high DECIMAL NULL, day_low DECIMAL NULL);'''
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


    def create_proxy_status_table(self,db_key='proxy'):
        try:               
            self.connect(db_key)
            
            cur = self.connection.cursor()
            sql = f"CREATE TABLE IF NOT EXISTS proxy_status(date DATE NOT NULL, time TIME NOT NULL, sod BOOLEAN NOT NULL)"
            cur.execute(sql)
            self.connection.commit()
            print('proxy status table created successfully')

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
    # x.create_tables('sample')
    # x.create_open_market()
    # x.create_proxy_ip_table()
    x.create_proxy_status_table()


# x.test()

# y = PGS()

# print(y)



        
       

        
        
