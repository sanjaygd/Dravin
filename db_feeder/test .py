from db_feeder.database import Postgres


class Test(Postgres):
    def simple(self):
        self.connect('sample')
        print(self.connection)

        self.connection.close()
        print('test here',self.connection)



t = 10 % 5 == 0
print(t)



# x = Test()
# x.simple()