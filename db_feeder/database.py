import os
import psycopg2


class PGS():
    def __init__(self):
        self._user = os.environ.get('P_USERNAME')
        self._connection = None
        self._cursor = None
        self._autocommit = None
        


    @property
    def connection(self):
        return self._connection
        

        

    def connect(self,db_key=None,db_name=None):
        xxx=None
        is_connected=False

        if self._connection is not None:
            try:
                self._connection.ping()
                is_connected=True
            except:
                pass #log need to add here

        
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
                    

                except Exception as ex:
                    print(ex)
                    print('Can not able to connect')

            

        


