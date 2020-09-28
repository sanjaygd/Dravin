import os
import sqlite3

from nse_grab import DataFeed



class SqLite3():
    def __init__(self,root_key,db_key):
        self.this_file_path = os.path.abspath(__file__)
        self.BASE_DIR = os.path.dirname(self.this_file_path)
        self.ENTIRE_PROJECT_DIR = os.path.dirname(self.BASE_DIR)
        self.DB_DIR = os.path.join(self.ENTIRE_PROJECT_DIR,'db')
        self.DB_SUBDIR = os.path.join(self.DB_DIR,root_key)
        self.formated_key = f'{db_key}.db'
        self.DB_SPACE = os.path.join(self.DB_SUBDIR,self.formated_key)

    def data_writer(self,tb_name=None,data=None):
        connection = sqlite3.connect(self.DB_SPACE)
        with connection:
            cursor = connection.cursor()

            if tb_name and data:
               sql = f'INSERT INTO {tb_name} VALUES (?, ?, ?, ?, ?)'
               cursor.execute(sql,data) 

            else:
                extract_data = DataFeed()
                data_list = extract_data.get_feed()

                with connection:
                    cursor = connection.cursor()

                    for data_dict in data_list[0:2]:
                        print(data_dict)
                        for key,value in data_dict.items():
                            print(key,value)
                            sql = f'INSERT INTO {key} VALUES (?, ?, ?, ?, ?, ?, ?)'
                            cursor.execute(sql,value) 
        # connection.close()


        
        # with self.connect:
        #     self.cur.execute(sql)
        
    # def insert(self,tb_name,data):
    #     sql = f'INSERT INTO {tb_name} VALUES (?, ?, ?, ?, ?)'
    #     # sql = "'INSERT INTO {} VALUES (?, ?, ?, ?, ?)', {}".format(tb_name,data)
    #     with self.connect:
    #         self.cur.execute(sql,data)



lite = SqLite3('demo','test1')
lite.data_writer()
# lite.create_table(tb_name='axisbank')

# # lite.create_table('test3')
# dta = ('axisb','218.10', '0.00', '272.01', '598.75')
# lite.insert('test3',dta)



    

    
    

    




