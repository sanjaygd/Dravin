import datetime as dt
from datetime import datetime


import psycopg2

from db_feeder.database import PGS
from db_feeder.nse_grab import Datafeed
from quote_lib.ticker_symbol import nifty_50_list



class PivotPoints(PGS):
    def __init__(self):
        super().__init__('pivot_points')

    def previous_day(self):
        pre_day = None
        _today = datetime.now().date().strftime('%A')
        today = datetime.now().date()
        if _today == 'Monday':
            pre_day  = today - dt.timedelta(days=3)
        
        return pre_day
        
        

    def pivots(self):
        try:
            self.connect('feed')
            cur = self.connection.cursor()
            ini = Datafeed()
            data_set = ini.get_feed()
            if len(data_set) != 0:
                for ticker_dict in data_set:
                    for tb_name,data in ticker_dict.items():
                        symbol,_date,last_update_time,insert_time,_open,high,low,preclose,ltp,cng,pcng,volume,value,request_count = data
                        
                        high = float(high)
                        low = float(low)
                        ltp = float(ltp)
                        _sum = high+low+ltp
                        cpr = round(_sum/3,3)
                        r1 = round((2*cpr)-low,3)
                        r2 = round(cpr+(high-low),4)
                        r3 = round(r1+(high-low),4)
                        s1 = round((2*cpr)-high,2)
                        s2 = round(cpr-(high-low),4)
                        s3 = round(s1-(high-low),3)
                        
                        lb = round((high+low)/2,4)
                        ub = round(cpr-lb+cpr,4)
                        cpr1 = None
                        cpr2 = None
                        if ub>lb:
                            cpr1 = ub
                            cpr2 = lb
                        else:
                            cpr1 = lb
                            cpr2 = ub

                        band_width= round((cpr1-cpr2)/cpr2*100,4)
                        date = datetime.now().date().strftime('%Y-%m-%d')
                        time = datetime.now().time().strftime('%H:%M:%S')
                        data = (date,time,cpr,cpr1,cpr2,r1,r2,r3,s1,s2,s3,band_width,high,low)
                        sql = f"INSERT INTO {tb_name}_piv (date,time,cpr,cpr1,cpr2,r1,r2,r3,s1,s2,s3,band_width,pre_high,pre_low) values {data}"
                        cur.execute(sql)
                        self.connection.commit()
                self.log_info("Pivot points entries has been completed for tody's date")
        except (Exception, psycopg2.Error) as error :
            self.log_error(f"{error}")
            print(error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
            else:
                print('All Okay')


if __name__ == "__main__":
    ini = PivotPoints()
    # ini.previous_day()
    ini.pivots()