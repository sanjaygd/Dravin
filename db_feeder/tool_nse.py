import psycopg2
import datetime as dt
from datetime import datetime
from pprint import pprint

from nsetools import Nse

from db_feeder.database import PGS
from quote_lib.ticker_symbol import quote_dict_nse



class InitialData(PGS):

    """
    This script collects the opening price, close price when market starts(nse_sod) and
    collects the day high and day low when market closes(nse_eod)

    """

    def __init__(self):
        self.nse = Nse()
        super().__init__()


    def nse_sod(self):
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
                    _today = datetime.today()
                    yesterday = _today - dt.timedelta(days=1)
                    sql1 = f"SELECT opening_price,previous_close  FROM {data_dict['symbol']} WHERE date='{yesterday}'"
                    cur.execute(sql1)   
                    yest_data = cur.fetchone()
                    if yest_data is not None:
                        op,pp = yest_data
                        if data_dict['opening_price'] != op   and   data_dict['previous_close'] != pp:
                            sql = f'INSERT INTO {data_dict["symbol"]}(date,time,symbol,opening_price,previous_close) values {data}'                
                            cur.execute(sql)
                            self.connection.commit()
                            self.log_info('Open market data inserted succesfully')
                        else:
                            self.log_warning('data not updated with nse tool')
                            break
                    else:
                        self.log_warning("yesterday's data not found")
                    
                    # print(data_dict['symbol'])
                except (Exception, psycopg2.Error) as error :
                    self.log_error(error)

                finally:
                    if self.connection:
                        cur.close()
                        self.connection.close()

            else:
                self.log_warning("Some data missing")
            
            
    def nse_eod(self):
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
                    self.log_info('nse_eod data updated successfully')
                    print(table_name)
                except (Exception, psycopg2.Error) as error :
                    self.log_error(error)

                finally:
                    if self.connection:
                        cur.close()
                        self.connection.close()
            else:
                self.log_warning("Some data missing")



if __name__ == "__main__":
    ini = InitialData()
    # ini.nse_sod()
    # ini.nse_eod()




