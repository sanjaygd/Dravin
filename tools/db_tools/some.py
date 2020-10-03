from tools.log_writer.log_register import Monitor

class Expy(Monitor):
    # def __init__(self):
    #     super().__init__()


    def testing(self):
        self.log_info("I have written something for test")



if __name__ == "__main__":
    ini = Expy()
    ini.testing()
    
    


