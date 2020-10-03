import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from db_feeder.database import PGS



class DBCreater(PGS):

    def create_db(self,db_key=None,db_name=None):
        if db_name:
            try:
                if not db_key:
                    db_key = 'postgres'
                    self.connect(db_key,_from='db_maker.create_db')
                    self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                    cur = self.connection.cursor()
                    sql = f'CREATE DATABASE {db_name}'
                    cur.execute(sql)
                    self.connection.commit()
                    self.log_info(f'Database named {db_name} created successfully')

            except (Exception, psycopg2.Error) as error :
                self.log_error(error)

            finally:
                if self.connection:
                    self.connection.close()
        else:
            self.log_warning('Database name not given. Please provide the db_name')
            



                

if __name__ == "__main__":
    x = DBCreater()
    # x.create_db()

            
