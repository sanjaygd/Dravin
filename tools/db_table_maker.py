import os
import sqlite3
import quote_lib
from quote_lib.ticker_symbol import quote_dict



class TableMaker():
    def __init__(self,root_key,db_key):
        self.this_file_path = os.path.abspath(__file__)
        self.BASE_DIR = os.path.dirname(self.this_file_path)
        self.ENTIRE_PROJECT_DIR = os.path.dirname(self.BASE_DIR)
        self.DB_DIR = os.path.join(self.ENTIRE_PROJECT_DIR,'db')
        self.DB_SUBDIR = os.path.join(self.DB_DIR,root_key)
        self.formated_key = f'{db_key}.db'
        self.DB_SPACE = os.path.join(self.DB_SUBDIR,self.formated_key)        


    def create_table(self,tb_name=None):
        connection = sqlite3.connect(self.DB_SPACE)
        with connection:
            cursor = connection.cursor()
            if tb_name:
                sql = """CREATE TABLE IF NOT EXISTS {tb_name} (
                        date timestamp NOT NULL,
                        time timestamp PRIMARY KEY,
                        date real NOT NULL,
                        symbol text DEFAULT "{tb_name}",
                        ltp integer NOT NULL,
                        pcng integer NOT NULL,
                        volume integer NOT NULL,
                        turnover integer NOT NULL
                    ) WITHOUT ROWID;""".format(tb_name=tb_name)
                       
                cursor.execute(sql)
            else:
                for tb_key,tb_value in quote_dict.items():
                    tb_name = quote_dict[tb_key]
                    
                    print(tb_name)
                    sql = """CREATE TABLE IF NOT EXISTS {tb_name} (
                            time text PRIMARY KEY,
                            date text NOT NULL,
                            symbol text DEFAULT "{tb_name}",
                            ltp integer NOT NULL,
                            pcng integer NOT NULL,
                            volume integer NOT NULL,
                            turnover integer NOT NULL
                        ) WITHOUT ROWID;""".format(tb_name=tb_name)                            
                    cursor.execute(sql)

        connection.close()


if __name__ == "__main__":
    x = TableMaker('demo','test1')
    x.create_table()


