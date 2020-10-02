import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from db_feeder.database import PGS
from db_feeder.db_record import db_keys


class DBCreater(PGS):

    def create_db(self,db_key=None,db_name=None):
        if db_name:
            try:
                if not db_key:
                    db_key = 'postgres'
                    self.connect(db_key)
                    self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                    cur = self.connection.cursor()
                    sql = f'CREATE DATABASE {db_name}'
                    cur.execute(sql)
                    self.connection.commit()
                    print('db created succefully')

            except (Exception, psycopg2.Error) as error :
                print(error)

            finally:
                if self.connection:
                    # cur.close()
                    self.connection.close()
        else:
            print('Please provide the db_name')



                

if __name__ == "__main__":
    x = DBCreater()
    x.create_db()

            
