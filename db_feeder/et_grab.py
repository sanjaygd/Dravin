import requests
from datetime import datetime,date

from bs4 import BeautifulSoup

from db_feeder.database import PGS
from quote_lib.ticker_symbol import quote_dict
from proxy_server.proxy import ProxyServer

class DataFeed(PGS):

    """
    This class is use to collect the data from the stock market

    """

    def get_feed(self):
        quot_data = []
        succuss_to_connect = None
        # try_count = 0
        response = None
        proxy_failed = False
        url = 'https://economictimes.indiatimes.com/markets/nifty-100/indexsummary/indexid-2510,exchange-50.cms'
        
        self.log_info('****')
        self.connect('proxy',_from='et_grab') 
        cur = self.connection.cursor()
        sql = 'SELECT ip,time FROM ip_address'
        cur.execute(sql)
        ip_list = cur.fetchall()
        cur.close()
        self.connection.close()
        
        try:
            proxy_count = 0               
            for ips in ip_list[::-1]:
                ip,_time = ips
                using_proxy = {'https':ip}
                print(using_proxy)
                proxy_count += 1
                print(proxy_count)
                
                try:
                    if not proxy_count == 5:
                        response = requests.request('get',url,proxies=using_proxy,timeout=3)
                        succuss_to_connect = True
                        break
                    if proxy_count == 5:
                        response = requests.get(url)
                        succuss_to_connect = True
                        proxy_failed =True
                        break
                except:
                    continue

            
        except requests.exceptions.ConnectionError as ex:
            succuss_to_connect=False
            self.log_error(ex)
            
        if succuss_to_connect:
            soup = BeautifulSoup(response.text,'lxml')
            q_list = soup.find_all('div',{'class':'dataList'}) 

            for qoute in q_list:
                data = ()
                ticker = {}
                symbol = qoute.find('p',{'class':'flt w120'}).text 
                try:               
                    symbol = quote_dict[symbol]
                except KeyError:
                    # print(symbol, 'New entry')
                    continue
                ltp = qoute.find('li',{'class':'w70 alignC'}).find('span',{'class':'ltp'}).text
                ltp = float(ltp)            
                try:
                    pcng = qoute.find('li',{'class':'w70 alignR'}).find('span',{'class':'pchange up'}).text
                    pcng = float(pcng)
                    # if pcng is None:
                    #     pcng = qoute.find('li',{'class':'w70 alignR'}).find('span',{'class':'pchange down'}).text

                except AttributeError as ex:
                    pass

                volume = qoute.find('li',{'class':'w50 alignR'}).find('span',{'class':'vol'}).text
                volume = float(volume)
                turnover = qoute.find_all('li',{'class':'w60 alignR'})[1].text
                turnover = float(turnover)

                timestamp = datetime.now()
                _date = timestamp.strftime('%Y-%m-%d')
                _time = timestamp.strftime('%H:%M:%S')
                
                data = (_date,_time,symbol,ltp,pcng,volume,turnover) 

                ticker[symbol] = data

                quot_data.append(ticker)
        else:
            self.log_warning('Cound not able to connect ET from et_grab')
        

        # print(quot_data)
        # print(len(quot_data))
        self.log_info(f'et_grab done successfully! and number of companies listed today {len(quot_data)}')
        if proxy_failed:
            self.log_warning('Proxy failed fetch through original ip. From et_grab.DataFeed.get_feedd')
        return quot_data


if __name__ == "__main__":
    data_feed = DataFeed('et_grab')
    data_feed.get_feed()
    