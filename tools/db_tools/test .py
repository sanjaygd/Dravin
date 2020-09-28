from db_feeder.database import PGS


class Test(PGS):
    def simple(self):
        self.connect('sample')
        print(self.connection)

        self.connection.close()
        print('test here',self.connection)

tb_name = 'acc'

sql = f'this is for test {tb_name}'

# x = Test()
# x.simple()