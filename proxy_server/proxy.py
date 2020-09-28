import requests

from datetime import date

import psycopg2
from bs4 import BeautifulSoup
from random import choice


from db_feeder.database import PGS


class ProxyServer(PGS):
    def __init__(self):
        super().__init__()

    def get_proxy(self):
        url = 'https://www.sslproxies.org/'
        try:
            self.connect('proxy')
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
                    print('updated successfully')
                except requests.exceptions.ConnectionError:
                    print('Connection error')

            elif status == False:
                
                sql = 'SELECT ip,time FROM ip_address'
                cur.execute(sql)
                ip_list = cur.fetchall()
                for ips in ip_list:
                    ip,_time = ips

                    while True:
                        using_proxy = {'https':ip}
                        print(using_proxy)
                        response = []
                        try:
                            print('test1')
                            r = requests.request('get',url,proxies=using_proxy,timeout=5)
                            response.append(r)
                            break
                        except:
                            pass

                    soup = BeautifulSoup(response[0].content,'html5lib')
                    t = list(map(lambda x:x[0]+':'+x[1],list(zip(map(lambda x: x.text,soup.findAll('td')[::8]), map(lambda x: x.text, soup.findAll('td')[1::8])))))
                    for ele in t:
                        if not len(ele) < 15:
                            tup = (ele,)
                            proxy_list.append(tup)
                    print('updated with proxy id')
                    break
        except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PGSQL", error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()
        return proxy_list


    def store_proxy(self):
        data = self.get_proxy()
        try:
            self.connect('proxy')
            cur = self.connection.cursor()
            sql1 = f'DELETE FROM ip_address'
            cur.execute(sql1)
            sql2 = f'INSERT INTO {"ip_address"}("ip") values (%s)'
            # print(sql)
            cur.executemany(sql2,data)
            self.connection.commit()
            print('data inserted succesfully')

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PGSQL", error)

        finally:
            if self.connection:
                cur.close()
                self.connection.close()



if __name__ == "__main__":    
    x = ProxyServer()
    # x.get_proxy()
    x.store_proxy()