
quote_dict = { 'ACC':'ACC', 'Abbott India':'ABBOTINDIA', 'Adani Ports SEZ':'ADANIPORTS', 'Adani Transmission Ltd.':'ADANITRANS', 'Ambuja Cements':'AMBUJACEM', 
                'Asian Paints':'ASIANPAINT', 'Aurobindo Pharm':'AUROPHARMA','Avenue Supermarts Ltd.':'DMART', 'Axis Bank':'AXISBANK', 'BPCL':'BPCL', 'Bajaj Auto':'BAJAJ_AUTO', 
                'Bajaj Finance':'BAJFINANCE', 'Bajaj Finserv':'BAJAJFINSV', 'Bajaj Holdings':'BAJAJHLDNG', 'Bandhan Bank Ltd.':'BANDHANBNK', 'Bank of Baroda':'BANKBARODA', 
                'Berger Paints':'BERGEPAINT', 'Bharti Airtel':'BHARTIARTL', 'Bharti Infratel':'INFRATEL', 'Biocon':'BIOCON', 'Bosch':'BOSCHLTD', 'Britannia Inds.':'BRITANNIA', 
                'Cadila Health':'CADILAHC', 'Cipla':'CIPLA', 'Coal India Ltd':'COALINDIA', 'Colgate-Palmo':'COLPAL', 'Concor':'CONCOR', 'DLF':'DLF', 'Dabur India':'DABUR', 
                'Divis Laboratories':'DIVISLAB', 'Dr. Reddys Laborat':'DRREDDY', 'Eicher Motors':'EICHERMOT', 'GAIL':'GAIL', 
                'General Insurance Corporation of India':'GICRE', 'Godrej Consumer':'GODREJCP', 'Grasim Inds.':'GRASIM', 'HCL Tech':'HCLTECH', 'HDFC':'HDFC', 
                'HDFC Asset Management Company Ltd.':'HDFCAMC', 'HDFC Bank':'HDFCBANK', 'HDFC Life Insurance Company Ltd.':'HDFCLIFE', 'HPCL':'HINDPETRO', 
                'Havells India':'HAVELLS', 'Hero MotoCorp':'HEROMOTOCO', 'Hind. Unilever':'HINDUNILVR', 'Hindalco Inds.':'HINDALCO', 'Hindustan Zinc':'HINDZINC', 
                'ICICI Bank':'ICICIBANK', 'ICICI Lombard General Insurance Company Ltd.':'ICICIGI', 
                'ICICI Prudential Life Insurance Company Ltd.':'ICICIPRULI', 'IGL':'IGL', 'ITC':'ITC', 'Indian Oil Corp':'IOC', 'IndusInd Bank':'INDUSINDBK', 
                'Info Edge':'NAUKRI','Infosys':'INFY', 'InterGlobe Aviation Ltd.':'INDIGO', 'JSW Steel':'JSWSTEEL', 'Kotak Bank':'KOTAKBANK', 'Larsen & Toubro':'LT', 
                'Lupin':'LUPIN', 'M&M':'M_M', 'Marico':'MARICO', 'Maruti Suzuki':'MARUTI', 'Motherson Sumi':'MOTHERSUMI', 'Muthoot Finance':'MUTHOOTFIN', 'NHPC':'NHPC', 'NMDC':'NMDC', 
                'NTPC':'NTPC', 'Nestle India':'NESTLEIND', 'ONGC':'ONGC', 'Oracle Fin':'OFSS', 'P&G':'PGHH', 'PFC':'PFC', 'PNB':'PNB', 'Page Industries':'PAGEIND', 
                'Petronet LNG':'PETRONET', 'Pidilite Ind':'PIDILITIND', 'Piramal Ent.':'PEL', 'PowerGrid':'POWERGRID', 'RIL':'RELIANCE', 'SBI':'SBIN', 'SBI Cards\n':'SBICARD', 
                'SBI Life Insurance Company Ltd.':'SBILIFE', 'Shree Cements':'SHREECEM', 'Shriram Tran Fin':'SRTRANSFIN', 'Siemens':'SIEMENS', 'Sun Pharma':'SUNPHARMA', 
                'TCS':'TCS', 'Tata Motors':'TATAMOTORS', 'Tata Steel':'TATASTEEL', 'Tech Mahindra':'TECHM', 'Titan Company ':'TITAN', 'Torrent Pharma':'TORNTPHARM', 'UPL ':"UPL", 
                'UltraTech Cem.':'ULTRACEMCO', 'United Brewerie':'UBL','United Spirits':'MCDOWELL_N', 'Wipro':'WIPRO', 'Zee Ent.':'ZEEL'

            }



quote_list = ['ABBOTINDIA', 'ACC', 'ADANIPORTS', 'ADANITRANS', 'AMBUJACEM', 'ASIANPAINT', 
                'AUROPHARMA', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJAJHLDNG', 'BAJFINANCE', 
                'BANDHANBNK', 'BANKBARODA', 'BERGEPAINT', 'BHARTIARTL', 'BIOCON', 'BOSCHLTD', 'BPCL', 
                'BRITANNIA', 'CADILAHC', 'CIPLA', 'COALINDIA', 'COLPAL', 'CONCOR', 'DABUR', 'DIVISLAB', 
                'DLF', 'DMART', 'DRREDDY', 'EICHERMOT', 'GAIL', 'GICRE', 'GODREJCP', 'GRASIM', 'HAVELLS',
                'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 
                'HINDPETRO', 'HINDUNILVR', 'HINDZINC', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'IGL', 
                'INDIGO', 'INDUSINDBK', 'INFRATEL', 'INFY', 'IOC', 'ITC', 'JSWSTEEL', 'KOTAKBANK', 'LT', 
                'LUPIN', 'M&M', 'MARICO', 'MARUTI', 'MCDOWELL-N', 'MOTHERSUMI', 'MUTHOOTFIN', 'NAUKRI', 
                'NESTLEIND', 'NHPC', 'NMDC', 'NTPC', 'OFSS', 'ONGC', 'PAGEIND', 'PEL', 'PETRONET', 
                'PFC', 'PGHH', 'PIDILITIND', 'PNB', 'POWERGRID', 'RELIANCE', 'SBICARD', 'SBILIFE', 
                'SBIN', 'SHREECEM', 'SIEMENS', 'SRTRANSFIN', 'SUNPHARMA', 'TATAMOTORS', 'TATASTEEL', 
                'TCS', 'TECHM', 'TITAN', 'TORNTPHARM', 'UBL', 'ULTRACEMCO', 'UPL', 'WIPRO', 'ZEEL']





quote_dict_nse = { 'ACC':'ACC', 'Abbott India':'ABBOTINDIA', 'Adani Ports SEZ':'ADANIPORTS', 'Adani Transmission Ltd.':'ADANITRANS', 'Ambuja Cements':'AMBUJACEM', 
                'Asian Paints':'ASIANPAINT', 'Aurobindo Pharm':'AUROPHARMA','Avenue Supermarts Ltd.':'DMART', 'Axis Bank':'AXISBANK', 'BPCL':'BPCL', 'Bajaj Auto':'BAJAJ-AUTO', 
                'Bajaj Finance':'BAJFINANCE', 'Bajaj Finserv':'BAJAJFINSV', 'Bajaj Holdings':'BAJAJHLDNG', 'Bandhan Bank Ltd.':'BANDHANBNK', 'Bank of Baroda':'BANKBARODA', 
                'Berger Paints':'BERGEPAINT', 'Bharti Airtel':'BHARTIARTL', 'Bharti Infratel':'INFRATEL', 'Biocon':'BIOCON', 'Bosch':'BOSCHLTD', 'Britannia Inds.':'BRITANNIA', 
                'Cadila Health':'CADILAHC', 'Cipla':'CIPLA', 'Coal India Ltd':'COALINDIA', 'Colgate-Palmo':'COLPAL', 'Concor':'CONCOR', 'DLF':'DLF', 'Dabur India':'DABUR', 
                'Divis Laboratories':'DIVISLAB', 'Dr. Reddys Laborat':'DRREDDY', 'Eicher Motors':'EICHERMOT', 'GAIL':'GAIL', 
                'General Insurance Corporation of India':'GICRE', 'Godrej Consumer':'GODREJCP', 'Grasim Inds.':'GRASIM', 'HCL Tech':'HCLTECH', 'HDFC':'HDFC', 
                'HDFC Asset Management Company Ltd.':'HDFCAMC', 'HDFC Bank':'HDFCBANK', 'HDFC Life Insurance Company Ltd.':'HDFCLIFE', 'HPCL':'HINDPETRO', 
                'Havells India':'HAVELLS', 'Hero MotoCorp':'HEROMOTOCO', 'Hind. Unilever':'HINDUNILVR', 'Hindalco Inds.':'HINDALCO', 'Hindustan Zinc':'HINDZINC', 
                'ICICI Bank':'ICICIBANK', 'ICICI Lombard General Insurance Company Ltd.':'ICICIGI', 
                'ICICI Prudential Life Insurance Company Ltd.':'ICICIPRULI', 'IGL':'IGL', 'ITC':'ITC', 'Indian Oil Corp':'IOC', 'IndusInd Bank':'INDUSINDBK', 
                'Info Edge':'NAUKRI','Infosys':'INFY', 'InterGlobe Aviation Ltd.':'INDIGO', 'JSW Steel':'JSWSTEEL', 'Kotak Bank':'KOTAKBANK', 'Larsen & Toubro':'LT', 
                'Lupin':'LUPIN', 'M&M':'M&M', 'Marico':'MARICO', 'Maruti Suzuki':'MARUTI', 'Motherson Sumi':'MOTHERSUMI', 'Muthoot Finance':'MUTHOOTFIN', 'NHPC':'NHPC', 'NMDC':'NMDC', 
                'NTPC':'NTPC', 'Nestle India':'NESTLEIND', 'ONGC':'ONGC', 'Oracle Fin':'OFSS', 'P&G':'PGHH', 'PFC':'PFC', 'PNB':'PNB', 'Page Industries':'PAGEIND', 
                'Petronet LNG':'PETRONET', 'Pidilite Ind':'PIDILITIND', 'Piramal Ent.':'PEL', 'PowerGrid':'POWERGRID', 'RIL':'RELIANCE', 'SBI':'SBIN', 'SBI Cards\n':'SBICARD', 
                'SBI Life Insurance Company Ltd.':'SBILIFE', 'Shree Cements':'SHREECEM', 'Shriram Tran Fin':'SRTRANSFIN', 'Siemens':'SIEMENS', 'Sun Pharma':'SUNPHARMA', 
                'TCS':'TCS', 'Tata Motors':'TATAMOTORS', 'Tata Steel':'TATASTEEL', 'Tech Mahindra':'TECHM', 'Titan Company ':'TITAN', 'Torrent Pharma':'TORNTPHARM', 'UPL ':"UPL", 
                'UltraTech Cem.':'ULTRACEMCO', 'United Brewerie':'UBL','United Spirits':'MCDOWELL-N', 'Wipro':'WIPRO', 'Zee Ent.':'ZEEL'

            }

nifty_50_list = [   'ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJFINSV', 'BAJAJ_AUTO', 'BAJFINANCE', 
                    'BHARTIARTL', 'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 
                    'EICHERMOT', 'GAIL', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCBANK', 'HDFCLIFE', 
                    'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'ICICIBANK', 'INDUSINDBK', 'INFY', 'IOC', 
                    'ITC', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'MARUTI', 'M_M', 'NESTLEIND', 'NTPC', 'ONGC', 
                    'POWERGRID', 'RELIANCE', 'SBILIFE', 'SBIN', 'SHREECEM', 'SUNPHARMA', 'TATAMOTORS', 
                    'TATASTEEL', 'TCS', 'TECHM', 'TITAN', 'ULTRACEMCO', 'UPL', 'WIPRO'
                    ]


