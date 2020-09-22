import sqlite3



class SqLite3():

    def create_table(self,tb_name):
        # sql = f'CREATE TABLE {tb_name} (symbol,pcng,ltp,volume,turnover)'
        sql = """CREATE TABLE IF NOT EXISTS {tb_name} (
                time real PRIMARY KEY,
                date real NOT NULL,
                symbol text DEFAULT "{tb_name}",
                ltp integer NOT NULL,
                pcng integer NOT NULL,
                volume integer NOT NULL,
                turnover integer NOT NULL
            ) WITHOUT ROWID;""".format(tb_name=tb_name)
        print(sql)
        
        # with self.connect:
        #     self.cur.execute(sql)
        
    # def insert(self,tb_name,data):
    #     sql = f'INSERT INTO {tb_name} VALUES (?, ?, ?, ?, ?)'
    #     # sql = "'INSERT INTO {} VALUES (?, ?, ?, ?, ?)', {}".format(tb_name,data)
    #     with self.connect:
    #         self.cur.execute(sql,data)



lite = SqLite3('nifty10.db')
# lite.create_table(tb_name='axisbank')

# # lite.create_table('test3')
# dta = ('axisb','218.10', '0.00', '272.01', '598.75')
# lite.insert('test3',dta)



    

    
    

    





# connect = sqlite3.connect('employee.db')

# c = connect.cursor()

# c.execute("""CREATE TABLE company (
#             symbol,
#             pcng,
#             ltp,
#             volume,
#             turnover
#             )""")


# with connect:
#     c.execute("INSERT INTO company VALUES ('IndusInd Bank', '0.06', '610.35', '113.47', '692.53')")

# c.execute('SELECT * FROM company')
# print(c.fetchone())
# connect.commit()
# connect.close()

# quote_symbol = ['ABBOTINDIA', 'ACC', 'ADANIPORTS', 'ADANITRANS', 'AMBUJACEM', 'ASIANPAINT', 
#                 'AUROPHARMA', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJAJHLDNG', 'BAJFINANCE', 
#                 'BANDHANBNK', 'BANKBARODA', 'BERGEPAINT', 'BHARTIARTL', 'BIOCON', 'BOSCHLTD', 'BPCL', 
#                 'BRITANNIA', 'CADILAHC', 'CIPLA', 'COALINDIA', 'COLPAL', 'CONCOR', 'DABUR', 'DIVISLAB', 
#                 'DLF', 'DMART', 'DRREDDY', 'EICHERMOT', 'GAIL', 'GICRE', 'GODREJCP', 'GRASIM', 'HAVELLS',
#                 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 
#                 'HINDPETRO', 'HINDUNILVR', 'HINDZINC', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'IGL', 
#                 'INDIGO', 'INDUSINDBK', 'INFRATEL', 'INFY', 'IOC', 'ITC', 'JSWSTEEL', 'KOTAKBANK', 'LT', 
#                 'LUPIN', 'M&M', 'MARICO', 'MARUTI', 'MCDOWELL-N', 'MOTHERSUMI', 'MUTHOOTFIN', 'NAUKRI', 
#                 'NESTLEIND', 'NHPC', 'NMDC', 'NTPC', 'OFSS', 'ONGC', 'PAGEIND', 'PEL', 'PETRONET', 
#                 'PFC', 'PGHH', 'PIDILITIND', 'PNB', 'POWERGRID', 'RELIANCE', 'SBICARD', 'SBILIFE', 
#                 'SBIN', 'SHREECEM', 'SIEMENS', 'SRTRANSFIN', 'SUNPHARMA', 'TATAMOTORS', 'TATASTEEL', 
#                 'TCS', 'TECHM', 'TITAN', 'TORNTPHARM', 'UBL', 'ULTRACEMCO', 'UPL', 'WIPRO', 'ZEEL']





    # 'Avenue Supermarts Ltd.',
    # 'Info Edge',
    # 'United Spirits',