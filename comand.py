import argparse
import getpass
import os

from db_feeder import  (
                        pg_writer,
                        tool_nse
                        )
from proxy_server import proxy
from sod import sod
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
    parser.add_argument('-pwd','--password', action=PwdAction, nargs=0,metavar='',help='password')
    """
1. -pwd use to provide password
    """
    parser.add_argument('-dn', '--create_db',type=str,metavar='', help='Creates database for given name')
    """
2.  -dn Database creater requires database name to be enter. (-dn database_name)
    """
    parser.add_argument('-dtc', '--table_cleaning',type=str,metavar='',nargs='+', help='Cleans database table')
    """
3.  -dtc Table cleaner rquires two arguments 1.databse name(m) 
    2.table name or delete all=True(o) 
    (-dtc sample tb_name or True)
    """
    parser.add_argument('-dtd', '--table_droper',type=str,metavar='',nargs='+', help='Drops the table from database')
    """
4.  -dtd Table droper requires 3 argument 
    1.database name(m) 
    2.table name or drop_all=True or candle_15=y (o)
    3.password(m)
    (_dtd sample 'ACC or True or y')
    
    """
    parser.add_argument('-dtm', '--table_maker',type=str, metavar='',nargs='+', help='Creates table for given database')
    """
5.  -dtm Table maker requires 3 arguments
    1.Database name
    2.Table name or nifty100=True or candle_15=y
    3.Password
    (-dtm sample tb_name or True or y)
    """

    parser.add_argument('-sod', '--start_of_the_day', type=str, metavar='',nargs='+',help='Makes the proxy status for start of the day')
    """
6. -sod Start of the day marker rquire only on argement
    1.Status to be on or off
    (-sod on or off)
    """

    parser.add_argument('-pgw', '--pg_writer', type=str, metavar='',nargs='+',help='Loads data to database')
    """
7.  -pgw pg_writer requires only one argument 
    1. y
    (-pgw y)
    """

    parser.add_argument('-tn', '--tool_nse', type=str,metavar='',nargs='+',help='Loads the market data at begining or end of the day')
    """
8.  -tn tool nse requires two arguement
    1. sod or eod
    (-tn sod n or eod n) Note: y for by_pass yesterda's check point.

    """

    parser.add_argument('-px', '--proxy_server', type=str,metavar='',help='Updates proxy server every 5 mins')
    """
9. -px proxy_server requires only one arguement
    1. y
    (-px y)
    """

    parser.add_argument('-mn', '--monitor', type=str, metavar='',nargs='+', help='Creates table for monitor')
    """
10. -mn monitor requires two arguement and one is optional
    1. f or ft
    2.db_key = 'some db' (o)
    (-mn f or ft)
    """

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

        ini = db_table_cleaner.TableCleaner('db_table_cleaner')
        ini.clean_table(db_key=db_key,tb_name=tb_name,delete_all=delete_all)


# ----------------------- Table Droper ------------------

    elif argument.table_droper:
        args = argument.table_droper
        password = argument.password
        db_key = None
        tb_name = None
        drop_all = False
        candle_15 = False
        if len(args) == 2:
            db_key = args[0]
            if args[1] == 'True':
                drop_all = True
            elif args[1] == 'y':
                candle_15 = True
            else:
                tb_name = args[1]
        else:
            print('argument limit exceeded, required only two')

        ini = db_table_droper.TableDroper()
        ini.delete_table(db_key=db_key,tb_name=tb_name,drop_all=drop_all,candle_15=candle_15)

        
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


# ------------------------ SOD-----------------------------------

    elif argument.start_of_the_day:
        args = argument.start_of_the_day
        switch_on = False
        switch_off = False
        if len(args) == 1:
            if args[0] == 'on':
                switch_on = True
            elif args[0] == 'off':
                switch_off = True
        else:
            print('argument limit exceeded, required only one')

        ini = sod.ProxyUsage()
        if switch_on:
            ini.make_proxy_status()
        elif switch_off:
            ini.make_proxy_status_off()
        
            
# --------------------------- pg_writer-----------------------

    elif argument.pg_writer:
        args = argument.pg_writer
        if len(args) == 1:
            if args[0] == 'y':
                ini = pg_writer.LiveFeeder('pg_writer')
                ini.start_feed(db_key='feed')
            else:
                print('Given argument is wrong')
           
        else:
            print('argument limit exceeded, required only one')


# ----------------------- tool_nse----------------------------

    elif argument.tool_nse:
        args = argument.tool_nse
        if len(args) <= 2 :
            ini = tool_nse.BoundaryData()
            
            if args[0] == 'sod' and args[1] == 'y':
                by_pass = True
                ini.nse_sod(by_pass=by_pass)
            elif args[0] == 'sod':
                ini.nse_sod()
            elif args[0] == 'eod':
                ini.nse_eod()
            else:
                print('Argument not recognized')
        else:
            print('argument limit exceeded, required only one') 



# --------------------------- Proxy server -----------------------

    elif argument.proxy_server:
        args = argument.proxy_server
        if len(args) == 1:
            if args[0] == 'y':
                ini = proxy.ProxyServer('proxy')
                ini.store_proxy()
            else:
                print('Argument not recognized')
        else:
            print('argument limit exceeded, required only one')

            

# ---------------------Monitor_table---------------------------

    elif argument.monitor:
        args = argument.monitor
        if len(args) < 2:
            ini = db_table_maker.TableMaker()
            if args[0] == 'f':  
                ini.create_monitor_table(candle='f')
            elif args[0] == 'ft':
                ini.create_monitor_table(candle='ft')