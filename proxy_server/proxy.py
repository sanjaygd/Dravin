import requests

from datetime import date

import psycopg2
from bs4 import BeautifulSoup
from random import choice

from db_feeder.database import PGS


class ProxyServer(PGS):
    """
    This script collects proxy server ip address and stores it in local database

    """
    def __init__(self):
        self.response = None
        super().__init__()

    def get_proxy(self):
        url = 'https://www.sslproxies.org/'
        try:
            self.log_info('*********')
            self.connect('proxy',_from='proxy.get_proxy')
            cur = self.connection.cursor()
            _today = date.today()
            sql = f"SELECT date,sod FROM proxy_status where date='{_today}'"
            cur.execute(sql)
            today_status = cur.fetchone()
            _date,status = today_status
            proxy_list = []
            if status == True:
                try:
                    r = requests.get(url)
                    soup = BeautifulSoup(r.content,'html5lib')
                    t = list(map(lambda x:x[0]+':'+x[1],list(zip(map(lambda x: x.text,soup.findAll('td')[::8]), map(lambda x: x.text, soup.findAll('td')[1::8])))))
                    for ele in t:
                        if not len(ele) < 15:
                            tup = (ele,)
                            proxy_list.append(tup)
                    sql = f"UPDATE proxy_status SET sod='false' where date = '{_today}'"
                    cur.execute(sql)
                    self.connection.commit()
                    self.log_info('Proxy status updated successfully at start of the day')
                except requests.exceptions.ConnectionError as error:
                    self.log_error(error)

            elif status == False:
                
                sql = 'SELECT ip,time FROM ip_address'
                cur.execute(sql)
                ip_list = cur.fetchall()
                proxy_count = 0
                for ips in ip_list[::-1]:
                    ip,_time = ips                    
                    using_proxy = {'https':ip}
                    proxy_count +=1
                    print(using_proxy)
                    
                    try:
                        if not proxy_count == 20:
                            r = requests.request('get',url,proxies=using_proxy,timeout=3)
                            self.response = r
                            break
                        if proxy_count == 20:
                            r = requests.get(url)
                            self.response = r
                            break
                    except:
                        continue

                soup = BeautifulSoup(self.response.content,'html5lib')
                t = list(map(lambda x:x[0]+':'+x[1],list(zip(map(lambda x: x.text,soup.findAll('td')[::8]), map(lambda x: x.text, soup.findAll('td')[1::8])))))
                for ele in t:
                    if not len(ele) < 15:
                        tup = (ele,)
                        proxy_list.append(tup)
                self.log_info('Proxies updated successfully')
                
                
        except (Exception, psycopg2.Error) as error :
                self.log_error(error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
        return proxy_list


    def store_proxy(self):
        data = self.get_proxy()
        if len(data)>1:
            try:
                self.connect('proxy',_from="proxy_store_proxy")
                cur = self.connection.cursor()
                sql1 = f'DELETE FROM ip_address'
                cur.execute(sql1)
                sql2 = f'INSERT INTO {"ip_address"}("ip") values (%s)'
                cur.executemany(sql2,data)
                self.connection.commit()
                self.log_info("proxies stored successfully!")

            except (Exception, psycopg2.Error) as error :
                self.log_info(error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()
        else:
            self.log_warning('There is No data available onproxy table')



if __name__ == "__main__":    
    x = ProxyServer()
    # x.get_proxy()
    # x.store_proxy()