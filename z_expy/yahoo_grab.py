import requests
import csv
import time

from bs4 import BeautifulSoup


from file_gen import quote_symbol


class GetData():
    
    
    def get_data(self):
        pick_stocks = {}
        i = 1

        for symbol in quote_symbol:

            url = f'https://in.finance.yahoo.com/quote/{symbol}.NS'

            response = requests.get(url)

            soup = BeautifulSoup(response.text,'lxml')



            price = soup.find_all('div',{'class':'D(ib) Mend(20px)'})[0].find('span').text
            # print('currenr price : ',price)
            # print(soup)
            pre_price = soup.find_all('div',{'class':
                        'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) '\
                        'smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'
                                            })[0].find('tr').find('span',{'class':'Trsdu(0.3s)'}).text

            # print('previous close :', pre_price)

            open_price = soup.find_all('div',{
                                                'class':
                                                'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'
                                            })[0].find_all('td', {'class':'Ta(end) Fw(600) Lh(14px)'})[1].find('span',{'class':'Trsdu(0.3s)'}).text
            # print('open price :', open_price)

            

            open_price = float(open_price.split()[0].replace(',', ''))
            pre_price = float(pre_price.split()[0].replace(',', ''))
            print(i)
            i+=1
            print(symbol)
            print(pre_price)
            print(open_price)

            if pre_price > open_price:
                gap_down = pre_price/open_price
                gap_down_per = gap_down-1
                if gap_down_per > 0.005 and gap_down_per < 0.015:
                    pick_stocks[symbol] = gap_down_per
                    print(gap_down_per)

        print(pick_stocks)



run = GetData()
run.get_data()