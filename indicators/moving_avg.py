from functools import reduce

import psycopg2


from db_feeder.database import PGS
from quote_lib.ticker_symbol import nifty_50_list


class MA(PGS):
    def __init__(self):
        super().__init__('moving_avg')

    def ma_20(self,db_key='feed'):
        try:
            self.connect(db_key)
            cur = self.connection.cursor()
            
            for tb_name in nifty_50_list:
                sql = f'SELECT symbol,date,insert_time,ltp from {tb_name} ORDER BY row_count DESC LIMIT 20'
                cur.execute(sql)
                result = cur.fetchall()
                # print(result)
                sumation = sum([x for _,__,___,x in result])
                avg = sumation/20

                
                tb_name = None
                date = None,
                insert_time = None,
                for i in result:
                    symbol,date,insert_time,ltp = i
                    break
                print(symbol,date, insert_time, avg)
                sql2 = f"UPDATE {symbol} SET ma_20={avg} WHERE date='{date}' and insert_time='{insert_time}'"
                cur.execute(sql2)
                self.connection.commit()

        except (Exception, psycopg2.Error) as error :
                self.log_error(error)
                print(error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()

    
    def ma_200(self,db_key='feed'):
        try:
            self.connect(db_key)
            cur = self.connection.cursor()
            
            for tb_name in nifty_50_list:
                sql = f'SELECT symbol,date,insert_time,ltp from {tb_name} ORDER BY row_count DESC LIMIT 200'
                cur.execute(sql)
                result = cur.fetchall()
                # print(result)
                sumation = sum([x for _,__,___,x in result])
                avg = sumation/20

                
                tb_name = None
                date = None,
                insert_time = None,
                for i in result:
                    symbol,date,insert_time,ltp = i
                    break
                print(symbol,date, insert_time, avg)
                sql2 = f"UPDATE {symbol} SET ma_200={avg} WHERE date='{date}' and insert_time='{insert_time}'"
                cur.execute(sql2)
                self.connection.commit()

        except (Exception, psycopg2.Error) as error :
                self.log_error(error)
                print(error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()


if __name__ == "__main__":
    ini = MA()
    ini.ma_20()