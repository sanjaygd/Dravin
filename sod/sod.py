from datetime import datetime

import psycopg2

from db_feeder.database import PGS


class ProxyUsage(PGS):
    """
    This script guids the proxy.py scripts how to collect proxy servers

    """

    def make_proxy_status(self):
        try:
            self.log_info('#########')
            self.connect('proxy',_from="sod.make_proxy_status")
            cur = self.connection.cursor()
            timestamp = datetime.now()
            _date = timestamp.strftime('%Y-%m-%d')
            _time = timestamp.strftime('%H:%M:%S')
            data = (_date,_time,'true')
            sql = f'INSERT INTO proxy_status(date, time, sod) values {data}'
            cur.execute(sql)
            self.connection.commit()
            self.log_info('Proxy status marked for today succesfully')
            

        except (Exception, psycopg2.Error) as error :
            self.log_error(error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()


    def make_proxy_status_off(self):
        try:
            self.connect('proxy',_from='sod.make_proxy_status_off')
            cur = self.connection.cursor()
            timestamp = datetime.now()
            _date = timestamp.strftime('%Y-%m-%d')
            _time = timestamp.strftime('%H:%M:%S')
            sql = f"UPDATE proxy_status SET sod='false' where date='{_date}'"
            cur.execute(sql)
            self.connection.commit()
            self.log_info('Proxy status turned off(False)')

        except (Exception, psycopg2.Error) as error :
            self.log_error(error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()



if __name__ == "__main__":
    ini = ProxyUsage()
    # ini.make_proxy_status()
    # ini.make_proxy_status_off()