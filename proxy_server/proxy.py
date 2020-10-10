import requests

from datetime import date
from datetime import datetime as dt

import psycopg2
from bs4 import BeautifulSoup
from random import choice

from db_feeder.database import PGS


class ProxyServer(PGS):
    """
    This script collects proxy server ip address and stores it in local database

    """


    def get_proxy(self):
        url = 'https://www.sslproxies.org/'
        response = None
        
        proxy_list = []
        try:
            
            self.connect('proxy',_from='proxy.get_proxy')
            cur = self.connection.cursor()
            _today = date.today()
            time_now = dt.now()
            timestamp = time_now.strftime('%H:%M:%S')
            sql = f"SELECT date,sod FROM proxy_status where date='{_today}'"
            cur.execute(sql)
            today_status = cur.fetchone()
            _date,status = today_status
            
            proxy_failed =False
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
                    print(proxy_count)
                    try:
                        if not proxy_count == 20:
                            r = requests.request('get',url,proxies=using_proxy,timeout=3)
                            response = r
                            break
                        if proxy_count == 20:
                            r = requests.get(url)
                            response = r
                            proxy_failed =True
                            break
                    except:
                        continue

                soup = BeautifulSoup(response.content,'html5lib')
                t = list(map(lambda x:x[0]+':'+x[1],list(zip(map(lambda x: x.text,soup.findAll('td')[::8]), map(lambda x: x.text, soup.findAll('td')[1::8])))))
                for ele in t:
                    if not len(ele) < 15:
                        tup = (ele,)
                        proxy_list.append(tup)
                self.log_info('Proxies updated successfully')
                if proxy_failed:
                    self.log_warning('Proxy failed trial count exeeded 20')
                    tdy = f'{_today}'
                    data = (tdy,timestamp,'Trial count exeeded')
                    sql1 = f'INSERT INTO proxy_failure(date,time,reason) values{data}'
                    cur.execute(sql1)
                    self.connection.commit()
                
        except (Exception, psycopg2.Error) as error :
                self.log_error(error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
        return proxy_list


    def store_proxy(self):
        data = self.get_proxy()
        _today = date.today()
        time_now = dt.now()
        timestamp = time_now.strftime('%H:%M:%S')
        if len(data)>1:
            try:
                self.connect('proxy',_from="proxy.store_proxy")
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
            self.log_warning('There is No data available onproxy table, False response')
            try:
                self.connect('proxy',_from="proxy.store_proxy")
                cur = self.connection.cursor()
                tdy = f'{_today}'
                data = (tdy,timestamp,'False response')
                sql = f'INSERT INTO proxy_failure(date,time,reason) values{data}'
                cur.execute(sql)
                self.connection.commit()

            except (Exception, psycopg2.Error) as error :
                self.log_info(error)

            finally:
                if self.connection:
                    cur.close()
                    self.connection.close()



if __name__ == "__main__":    
    x = ProxyServer()
    # x.get_proxy()
    x.store_proxy()