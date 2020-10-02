import psycopg2

from db_feeder.database import PGS
from db_feeder.db_record import db_keys
from db_feeder.et_grab import DataFeed
from db_feeder.et_grab import DataFeed
from quote_lib.ticker_symbol import quote_dict


class LiveFeeder(PGS):
    
    def start_feed(self,db_key=None,tb_name=None,data=None):
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
                entry_point = 3
                for ticker_dict in data_set:
                    for tb_name,data in ticker_dict.items():                        
                        sql = f'INSERT INTO {tb_name}(date,time,symbol,ltp,pcng,volume,turnover) values {data}'                
                        cur.execute(sql)
                        self.connection.commit()

                        sql1 = f"SELECT row_count,symbol FROM {tb_name} ORDER BY row_count DESC LIMIT 1"
                        cur.execute(sql1)
                        result = cur.fetchone()
                        row_count,symbol = result
                        if row_count % entry_point == 0:
                            sql = f'INSERT INTO {tb_name}_15(date,time,symbol,ltp,pcng,volume,turnover) values {data}'                
                            cur.execute(sql)
                            self.connection.commit()
                            print('15 min candle data updated successfully')


            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()




if __name__ == "__main__":
    x = LiveFeeder()
    x.start_feed(db_key='sample')
