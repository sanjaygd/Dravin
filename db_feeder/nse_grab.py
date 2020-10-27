
import requests
import time

from datetime import datetime,date

from db_feeder.database import PGS


class Datafeed(PGS):
    def __init__(self):
        super().__init__('nse_grab')


    def get_feed(self):
        status_code = None   
        data_list = []

        url_oc = "https://www.nseindia.com/option-chain"
        url = f"https://www.nseindia.com/api/equity-stockIndices?index=NIFTY 50"
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                'like Gecko) '
                                'Chrome/80.0.3987.149 Safari/537.36',
                'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br',
                'Connection' : 'keep-alive',
                }
        
        session = None
        request = None
        cookies = None
        data = None
        status_code = None
        count = 0
        try:
            session = requests.Session()
            request = session.get(url_oc, headers=headers, timeout=5)
            cookies = dict(request.cookies)
            data = None
            status_code = None
            count = 0
        except Exception as er:
                print(er)
        
        while status_code != 200:
            count+=1 
            try:
                response = session.get(url, headers=headers, timeout=5, cookies=cookies)
                data = response.json()
                # print(response.text)
                status_code = response.status_code
                cookies = dict(response.cookies)
                print(count)
                if count == 20:
                    break
                
            except Exception as er:
                # print(er)
                if count == 20:
                    break   
        try:
            
            bundle = data['data']
            # advances = data['advance']['advances']
            # advances = int(advances)
            # declines = data['advance']['declines']
            # declines = int(declines)
            for ele in bundle[1:]:
                tick = {}
                symbol = ele['symbol']
                if symbol in ['M&M','BAJAJ-AUTO']:
                    if symbol == 'M&M':
                        symbol = 'M_M'
                    elif symbol == 'BAJAJ-AUTO':
                        symbol = 'BAJAJ_AUTO'
                _open = ele['open']
                high = ele['dayHigh']
                low = ele['dayLow']
                preclose = ele['previousClose']
                ltp = ele['lastPrice']
                cng = ele['change']
                pcng = ele['pChange']
                volume = ele['totalTradedVolume']
                value = ele['totalTradedValue']
                last_update_time = ele['lastUpdateTime']
                time_obj = datetime.strptime(last_update_time, '%d-%b-%Y %H:%M:%S')
                last_update_time = time_obj.strftime('%H:%M:%S')
                request_count = count
                timestamp = datetime.now()
                _date = timestamp.strftime('%Y-%m-%d')
                insert_time = timestamp.strftime('%H:%M:%S')
                
                data = (symbol,_date,last_update_time,insert_time,_open,high,low,preclose,ltp,cng,pcng,volume,value,request_count)
                tick[symbol] = data
                data_list.append(tick)
                
        except Exception as er:
            self.log_error(er)
            print(er)
        # print(data_list)
        return data_list




if __name__ == "__main__":
    ini = Datafeed()
    ini.get_feed()