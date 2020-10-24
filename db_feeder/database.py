import os
import psycopg2

from tools.ini_writer.cred_picker import Agent
from tools.log_writer.log_register import Monitor


class PGS(Monitor):
    """
    This class is use to connect the rquired database

    """
    def __init__(self,log_name=None):
        self._user = os.environ.get('P_USERNAME')
        self._connection = None
        self._cursor = None
        self._autocommit = None
        super().__init__(log_name)
        


    @property
    def connection(self):
        return self._connection
        

    def connect(self,db_key=None,db_name=None,_from=None):

        if db_key:
            ini = Agent()
            user,xxx = ini.read_cred()
            try:
                self._connection = psycopg2.connect(
                    user = user,
                    password = xxx,
                    host = '127.0.0.1',
                    port = "5432",
                    database = db_key
                )

                if _from == 'tool_nse_eod' or _from == 'tool_nse_sod':
                    pass
                else:
                    put = 'PGS' if _from is None else _from
                    self.log_info(f'Connected to {db_key}  successfully from {put}')

            except Exception as ex:
                self.log_error(ex)


if __name__ == "__main__":
    ini = PGS()
    ini.connect('sample')