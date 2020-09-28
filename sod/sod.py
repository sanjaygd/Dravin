from datetime import datetime

import psycopg2

from db_feeder.database import PGS


class ProxyUsage(PGS):

    def make_proxy_status(self):
        try:
            self.connect('proxy')
            cur = self.connection.cursor()
            timestamp = datetime.now()
            _date = timestamp.strftime('%Y-%m-%d')
            _time = timestamp.strftime('%H:%M:%S')
            data = (_date,_time,'true')
            sql = f'INSERT INTO proxy_status(date, time, sod) values {data}'
            # print(sql)
            cur.execute(sql)
            self.connection.commit()
            print('data inserted succesfully')

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PGSQL", error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()



if __name__ == "__main__":
    ini = ProxyUsage()
    ini.make_proxy_status()