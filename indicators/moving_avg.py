from functools import reduce

import psycopg2


from db_feeder.database import PGS
from quote_lib.ticker_symbol import nifty_50_list


class MA(PGS):
    def __init__(self):
        super().__init__('moving_avg')

    def ma(self,db_key='feed'):
        try:
            self.connect(db_key)
            cur = self.connection.cursor()
            
            for tb_name in nifty_50_list:
                sql = f'SELECT symbol,date,insert_time,ltp from {tb_name} ORDER BY row_count DESC LIMIT 20'
                cur.execute(sql)
                result_20 = cur.fetchall()
                # print(result)
                sumation_20 = sum([x for _,__,___,x in result_20])
                avg_20 = sumation_20/20
                sql1 = f'SELECT symbol,date,insert_time,ltp from {tb_name} ORDER BY row_count DESC LIMIT 200'
                cur.execute(sql1)
                result_200 = cur.fetchall()
                sumation_200 = sum([x for _,__,___,x in result_200])
                avg_200 = sumation_200/200

                
                # tb_name = None
                date = None,
                insert_time = None,
                for i in result_20:
                    symbol,date,insert_time,ltp = i
                    break
                # print(symbol,date, insert_time, avg_20)
                sql2 = f"UPDATE {tb_name} SET ma_20={avg_20}, ma_200={avg_200} WHERE date='{date}' and insert_time='{insert_time}'"
                cur.execute(sql2)
                self.connection.commit()
            self.log_info('Moving averages are updated successfully')
            self.log_info('****************************')
        except (Exception, psycopg2.Error) as error :
                self.log_error(error)
                print(error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()



if __name__ == "__main__":
    ini = MA()
    ini.ma()