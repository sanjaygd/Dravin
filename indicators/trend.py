import psycopg2

from db_feeder.database import PGS
from quote_lib.ticker_symbol import nifty_50_list

class Trend(PGS):
    def __init__(self):
        super().__init__('trend')


    def ad_de(self):
        advance = 0
        decline = 0
        try:
            self.connect('feed')
            cur = self.connection.cursor()
            for tb_name in nifty_50_list:
                sql = f'SELECT symbol,pcng from {tb_name} ORDER BY row_count DESC LIMIT 1'
                cur.execute(sql)
                result = cur.fetchone()
                _,pcng = result
                pcng = float(pcng)
                if pcng > 0:
                    advance+=1
                elif pcng < 0:
                    decline+=1
        except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
        print(advance,decline)
        return advance,decline

    def quick_trend(self):
        advance = 0
        decline = 0
        try:
            self.connect('feed')
            cur = self.connection.cursor()
            for tb_name in nifty_50_list:
                sql = f'SELECT symbol,pcng from {tb_name} ORDER BY row_count DESC LIMIT 3'
                cur.execute(sql)
                result = cur.fetchall()
                a,b,c = result
                # print(a,b,c)
                _,x = a
                _,y = b
                _,z = c
                if z > x:
                    advance+=1
                elif z < x:
                    decline+=1
                
        except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
        print(advance,decline)
        return advance,decline



if __name__ == "__main__":
    ini = Trend()
    ini.ad_de()
    ini.quick_trend()