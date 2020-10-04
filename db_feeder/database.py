import os
import psycopg2

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
        super().__init__("Postgress")
        


    @property
    def connection(self):
        return self._connection
        

    def connect(self,db_key=None,db_name=None,_from=None):
        xxx=None
        is_connected=False

        # if self._connection is not None:
        #     try:
        #         self._connection.ping()
        #         is_connected=True
        #     except Exception as ex:
        #         print(ex) 

        
        if not is_connected:
            xxx = os.environ.get('P_PASSWORD')

            if db_key:
                try:
                    self._connection = psycopg2.connect(
                        user = self._user,
                        password = xxx,
                        host = '127.0.0.1',
                        port = "5432",
                        database = db_key
                    )
                    put = 'PGS' if _from is None else _from
                    self.log_info(f'Connected to {db_key}  successfully from {put}')

                except Exception as ex:
                    self.log_error(ex)


if __name__ == "__main__":
    ini = PGS()
    # ini.connect('sample')