import argparse
import getpass
import os

from tools.db_tools import (
                            db_maker,
                            db_table_cleaner,
                            db_table_droper,
                            db_table_maker,
                            some
                            )



if __name__ == "__main__":

    class PwdAction(argparse.Action):

        def __call__(self, parser, namespace, values, option_string=None):
            mypass = getpass.getpass()
            setattr(namespace, self.dest, mypass)
            

    

    parser = argparse.ArgumentParser(description='Comanding stock predictor')
    parser.add_argument('-f', action=PwdAction, nargs=0)
    parser.add_argument('-pwd','--password', action=PwdAction, nargs=0,metavar='',help='password')
    parser.add_argument('-dn', '--create_db',type=str,metavar='', help='Creates database for given name')
    parser.add_argument('-dtc', '--table_cleaning',type=str,metavar='',nargs='+', help='Cleans database table')
    parser.add_argument('-dtd', '--table_droper',type=str,metavar='',nargs='+', help='Drops the table from database')
    parser.add_argument('-dtm', '--table_maker',type=str, metavar='',nargs='+', help='Creates table for given database')

    argument = parser.parse_args()


# ---------------------DB creation------------------------------
    if argument.create_db:
        args = argument.create_db
        ini = db_maker.DBCreater()
        ini.create_db(db_name = args)
        output = f'database {args} created succefully'
        print(output)
    

# ----------------- Table cleaning -----------------------------
    elif argument.table_cleaning:
        args = argument.table_cleaning
        db_key = None
        tb_name = None
        delete_all = False
        if len(args) == 2:
            db_key = args[0]
            if args[1] == 'True':
                delete_all = True
            else:
                tb_name = args[1]
        else:
            print('argument limit exceeded, required only two')

        ini = db_table_cleaner.TableCleaner()
        ini.clean_table(db_key=db_key,tb_name=tb_name,delete_all=delete_all)


# ----------------------- Table Droper ------------------

    elif argument.table_droper:
        args = argument.table_droper
        password = argument.password
        db_key = None
        tb_name = None
        drop_all = False
        if len(args) == 2:
            db_key = args[0]
            if args[1] == 'True':
                drop_all = True
            else:
                tb_name = args[1]
        else:
            print('argument limit exceeded, required only two')

        ini = db_table_droper.TableDroper()
        ini.delete_table(db_key=db_key,tb_name=tb_name,drop_all=drop_all)

        
# -------------------------- Table maker---------------------------


    elif argument.table_maker:
        args = argument.table_maker
        if not argument.password:
            print('Password required to create table')
        password = argument.password
        xxx = os.environ.get('CLI_PASSWORD')
        db_key=None
        tb_name=None
        nifty100=False
        candle_15 = False
        if password == xxx and args:
            if len(args) == 2:
                db_key = args[0]
                if args[1] == 'True':
                    nifty100 = True
                elif args[1] == 'y':
                    candle_15 = True
                else:
                    tb_name = args[1]
            else:
                print('argument limit exceeded, required only two')

            ini = db_table_maker.TableMaker()
            ini.create_tables(db_key=db_key,tb_name=tb_name,nifty100=nifty100,candle_15=candle_15)
            
        else:
            print('Invalid password')

