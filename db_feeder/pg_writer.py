import psycopg2

from db_feeder.database import PGS
from db_feeder.db_record import db_keys
from db_feeder.et_grab import DataFeed
from db_feeder.et_grab import DataFeed
from quote_lib.ticker_symbol import quote_dict


class LiveFeeder(PGS):
    
    def start_feed(self,db_key=None,tb_name=None,data=None):
        five_min_candle = 5
        ten_min_candle = 10
        if db_key and data and tb_name: 
            try:
                self.connect(db_key)
                cur = self.connection.cursor()
                sql = f'INSERT INTO {tb_name}(date,time,symbol,ltp,pcng,volume,turnover) values {data}'
                print(sql)
                cur.execute(sql)
                self.connection.commit()
                print('data inserted succesfully')

            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()

        elif db_key:
            try:
                self.connect(db_key)
                cur = self.connection.cursor()
                data_ini = DataFeed()
                data_set = data_ini.get_feed()
                for ticker_dict in data_set:
                    for tb_name,data in ticker_dict.items():
                        print(data)
                        # data = ticker_dict[tb_name]                        
                        sql = f'INSERT INTO {tb_name}(date,time,symbol,ltp,pcng,volume,turnover) values {data}'                
                        cur.execute(sql)
                        self.connection.commit()
            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()




if __name__ == "__main__":
    x = LiveFeeder()
    x.start_feed(db_key='sample')
