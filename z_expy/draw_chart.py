import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import os

from datetime import datetime


 


quote_symbol = ['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 
                'BHARTIARTL', 'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DRREDDY', 'EICHERMOT', 'GAIL', 
                'GRASIM', 'HCLTECH', 'HDFC', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 
                'ICICIBANK', 'INDUSINDBK', 'INFRATEL', 'INFY', 'IOC', 'ITC', 'JSWSTEEL', 'KOTAKBANK', 'LT', 
                'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBIN', 'SHREECEM', 
                'SUNPHARMA', 'TATAMOTORS', 'TATASTEEL', 'TCS', 'TECHM', 'TITAN', 'ULTRACEMCO', 'UPL', 
                'WIPRO', 'ZEEL',
                
                'BIOCON', 'DABUR', 'PFC', 'DIVISLAB', 'MCDOWELL-N', 'MOTHERSUMI', 'BERGEPAINT', 
                'CONCOR', 'INDIGO', 'MARICO', 'LUPIN', 'COLPAL', 'ICICIPRULI', 'GODREJCP', 'SIEMENS', 
                'PETRONET', 'ADANITRANS', 'PIDILITIND', 'PAGEIND', 'HINDZINC', 'TORNTPHARM', 'SBILIFE', 
                'ACC', 'GICRE', 'CADILAHC', 'AMBUJACEM', 'DLF', 'ICICIGI', 'HDFCAMC', 'HAVELLS', 'PGHH', 
                'BANDHANBNK', 'MUTHOOTFIN', 'SBICARD', 'NAUKRI', 'DMART', 'SRTRANSFIN', 'IGL', 'AUROPHARMA', 
                'ABBOTINDIA', 'NHPC', 'BAJAJHLDNG', 'UBL', 'OFSS', 'PEL', 'PNB', 'NMDC', 'HINDPETRO', 
                'BANKBARODA', 'BOSCHLTD'
                ]


this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)
ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)
today = datetime.now()
data_dir =os.path.join('daily_data','02-09-2020')  #today.strftime("%d-%m-%Y")
path_to_data_dir = os.path.join(ENTIRE_PROJECT_DIR,data_dir)
# print(path_to_data_dir)
# file_name = os.path.join(path_to_data_dir,'ADANIPORTS.csv')




pick_stock = []

for symbol in quote_symbol:
    file_name = os.path.join(path_to_data_dir,f'{symbol}.csv') 
    # print(file_name)
    df = pd.read_csv(file_name)
    for row in df.iterrows():
        if (df['prev_close'][0]) > (df['open'][0]):
            gap_down = (df['prev_close'][0])/(df['open'][0]) 
            gap_down_per = gap_down-1
            if gap_down_per > 0.005 and gap_down_per < 1.5:
                pick_stock.append(symbol)
                print(symbol, ': ', gap_down)
       
        break


print(pick_stock)

    





# print(df)

# plt.figure(figsize=(12.2,4.5))
# plt.plot(df['ltp'],label='ltp')
# plt.xticks(rotation=45)
# plt.title('Close price histery')
# plt.xlabel('Time')
# plt.ylabel('Price in INR')
# plt.show()
