import csv
import os
from datetime import datetime


# quote_symbol = ['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 
#                 'BHARTIARTL', 'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DRREDDY', 'EICHERMOT', 
#                 'GAIL', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 
#                 'HINDALCO', 'HINDUNILVR', 'ICICIBANK', 'INDUSINDBK', 'INFRATEL', 'INFY', 'IOC', 
#                 'ITC', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 
#                 'POWERGRID', 'RELIANCE', 'SBIN', 'SHREECEM', 'SUNPHARMA', 'TATAMOTORS', 'TATASTEEL', 
#                 'TCS', 'TECHM', 'TITAN', 'ULTRACEMCO', 'UPL', 'WIPRO', 'ZEEL']

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




class FileGenerator():

    def __init__(self):
        self.this_file_path = os.path.abspath(__file__)
        self.BASE_DIR = os.path.dirname(self.this_file_path)
        self.ENTIRE_PROJECT_DIR = os.path.dirname(self.BASE_DIR)
        self.today = datetime.now()
        self.data_dir =os.path.join('daily_data',self.today.strftime("%d-%m-%Y"))
        self.path_to_data_dir = os.path.join(self.ENTIRE_PROJECT_DIR,self.data_dir)  

    def create_data_dir(self):
        """
        Needs daily_data dir in ENTIRE_PROJECT_DIR
        """
        try:
            os.mkdir(self.path_to_data_dir)
        except FileExistsError:
            print("Oh... Directory already exist for today's date ")


    def create_data_files(self):
        """
        Creats csv file in dail_data directory
        """
        field_names = ['time','symbol','open','high','low','prev_close',
                                'ltp','pcng','volume','value','52wh','52wl']

        for symbol in quote_symbol:
            file_name = os.path.join(self.path_to_data_dir,f'{symbol}.csv')

            with open(file_name,'w') as new_file:
                csv_writer = csv.DictWriter(new_file, fieldnames=field_names)
                csv_writer.writeheader()





if __name__ == "__main__":
    instan = FileGenerator()
    instan.create_data_dir()
    instan.create_data_files()
    





