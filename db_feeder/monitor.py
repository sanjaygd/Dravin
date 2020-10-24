# import datetime as dt
# from datetime import datetime

# import psycopg2

# from db_feeder.database import PGS
# from quote_lib.ticker_symbol import quote_dict


# class Monitor(PGS):
#     def __init__(self):
#         super().__init__('monitor')


#     def start_monitor(self,candle=None):
#         _today = datetime.now().date()

#         for tb_key,tb_value in quote_dict.items():
#             tb_name = quote_dict[tb_key]

#             try:
#                 self.connect('opening_market')
#                 cur = self.connection.cursor()
#                 if candle == 5:
#                     sql = f"SELECT COUNT(*) FROM {tb_name} where date='{_today}'"
#                     cur.execute(sql)
#                     count = cur.fetchone()
#                     print(count)
                    
#                     print('table created succesfully')

#             except (Exception, psycopg2.Error) as error :
#                 print ("Error while connecting to PGSQL", error)

#             finally:
#                 if self.connection:
#                     cur.close()
#                     self.connection.close()