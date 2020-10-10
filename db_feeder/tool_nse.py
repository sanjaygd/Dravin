import psycopg2
import datetime as dt
from datetime import datetime
from pprint import pprint

from nsetools import Nse

from db_feeder.database import PGS
from quote_lib.ticker_symbol import quote_dict_nse



class BoundaryData(PGS):

    """
    This script collects the opening price, close price when market starts(nse_sod) and
    collects the day high and day low when market closes(nse_eod)

    """

    def __init__(self):
        self.nse = Nse()
        super().__init__('tool_nse')


    def nse_sod(self,by_pass=None):      

        for key,value in quote_dict_nse.items():
            ticker_symbol = quote_dict_nse[key]
            result = self.nse.get_quote(ticker_symbol)
            data_dict = {}

            data_dict['symbol'] = result['symbol']
            if data_dict['symbol'] in ['BAJAJ-AUTO','M&amp;M','MCDOWELL-N']:
                if data_dict['symbol'] == 'BAJAJ-AUTO':
                    data_dict['symbol'] = 'BAJAJ_AUTO'
                elif data_dict['symbol'] == 'M&amp;M':
                    data_dict['symbol'] = 'M_M'
                elif data_dict['symbol'] == 'MCDOWELL-N':
                    data_dict['symbol'] = 'MCDOWELL_N'
                
            data_dict['opening_price'] = result['open']   
            data_dict['previous_close'] = result['previousClose']

            timestamp = datetime.now()
            _date = timestamp.strftime('%Y-%m-%d')
            _time = timestamp.strftime('%H:%M:%S')

            data = (_date,_time,data_dict['symbol'],data_dict['opening_price'],data_dict['previous_close'])



            if (data_dict['symbol'] is not None and data_dict['opening_price'] is not None and data_dict['previous_close']):
                try:
                    self.connect('opening_market',_from='tool_nse_sod')
                    cur = self.connection.cursor()
                    _today = dt.date.today()
                    todays_name = timestamp.strftime('%A')
                    yesterday=None
                    if todays_name == 'Monday':
                        yesterday = _today - dt.timedelta(days=3)
                    else:
                        yesterday = _today - dt.timedelta(days=1)

                    sql = f"SELECT symbol from {data_dict['symbol']} WHERE date='{_today}'"
                    cur.execute(sql)
                    todays_entry = cur.fetchone()

                    if todays_entry is None:
                        sql = f"SELECT opening_price,previous_close  FROM {data_dict['symbol']} WHERE date='{_today}'"
                        cur.execute(sql)
                        check_point = cur.fetchone()
                        if check_point is None:
                            sql1 = f"SELECT opening_price,previous_close  FROM {data_dict['symbol']} WHERE date='{yesterday}'"
                            cur.execute(sql1)   
                            yest_data = cur.fetchone()

                            if yest_data is not None:
                                op,pp = yest_data
                                if data_dict['opening_price'] != op   and   data_dict['previous_close'] != pp:
                                    sql = f'INSERT INTO {data_dict["symbol"]}(date,time,symbol,opening_price,previous_close) values {data}'                
                                    cur.execute(sql)
                                    self.connection.commit()                            
                                else:
                                    self.log_warning('data not updated with nse tool')
                                    break
                            elif by_pass:
                                sql = f'INSERT INTO {data_dict["symbol"]}(date,time,symbol,opening_price,previous_close) values {data}'                
                                cur.execute(sql)
                                self.connection.commit()
                                print(data_dict['symbol'])
                            else:
                                self.log_warning("yesterday's data not found")
                        else:
                            self.log_info(f"opening market data already update for {data_dict['symbol']}")
                    else:
                        print('today data already updated')
                        continue   
                except (Exception, psycopg2.Error) as error :
                    self.log_error(error)

                finally:
                    if self.connection:
                        cur.close()
                        self.connection.close()

            else:
                self.log_warning("Some data missing")        
                
    def nse_eod(self):
        self.log_info('started loading nse_eod')
        for key,value in quote_dict_nse.items():
            ticker_symbol = quote_dict_nse[key]
            result = self.nse.get_quote(ticker_symbol)
            data_dict = {}

            data_dict['symbol'] = result['symbol']
            if data_dict['symbol'] in ['BAJAJ-AUTO','M&amp;M','MCDOWELL-N']:
                if data_dict['symbol'] == 'BAJAJ-AUTO':
                    data_dict['symbol'] = 'BAJAJ_AUTO'
                elif data_dict['symbol'] == 'M&amp;M':
                    data_dict['symbol'] = 'M_M'
                elif data_dict['symbol'] == 'MCDOWELL-N':
                    data_dict['symbol'] = 'MCDOWELL_N'

            data_dict['day_high'] = result['dayHigh']
            data_dict['day_low'] = result['dayLow']   
            
            if (data_dict['symbol'] is not None and data_dict['day_high'] is not None and data_dict['day_low']):
                try:
                    self.connect('opening_market',_from='tool_nse_eod')
                    cur = self.connection.cursor()
                    table_name = data_dict['symbol']
                    
                    sql = f"UPDATE {table_name} SET day_high = {data_dict['day_high']}, day_low = {data_dict['day_low']} WHERE date='{dt.date.today()}'"                
                    cur.execute(sql)
                    self.connection.commit()
                    
                    print(table_name)
                except (Exception, psycopg2.Error) as error :
                    self.log_error(error)

                finally:
                    if self.connection:
                        cur.close()
                        self.connection.close()
            else:
                self.log_warning("Some data missing")
        self.log_info('end of loading nse_eod')



if __name__ == "__main__":
    ini = BoundaryData()
    # ini.nse_sod(by_pass=True)
    ini.nse_eod()




