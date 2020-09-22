import requests

from bs4 import BeautifulSoup


class DataFeed():
    def __init__(self):
        try:
            self.url = 'https://economictimes.indiatimes.com/markets/nifty-100/indexsummary/indexid-2510,exchange-50.cms'
        except Exception as ex:
            print(ex)  #data base entry need be done



    def get_feed(self):
        quot_data = []
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text,'lxml')
        q_list = soup.find_all('div',{'class':'dataList'}) 

        for qoute in q_list:
            data = ()
            ticker = {}
            symbol = qoute.find('p',{'class':'flt w120'}).text
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

            
            data = (ltp,pcng,volume,turnover) 

            ticker[symbol] = data

            quot_data.append(ticker)
        

        print(quot_data)
        # print(len(quot_data))
        return quot_data


    


if __name__ == "__main__":
    data_feed = DataFeed()
    data_feed.get_feed()
    