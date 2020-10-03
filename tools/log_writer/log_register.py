import logging
import os

from datetime import date



class Monitor():
    def __init__(self,log_name):
        self.this_file_path = os.path.abspath(__file__)
        self.BASE_DIR = os.path.dirname(self.this_file_path)
        self.PROJECT_SUB_DIR = os.path.dirname(self.BASE_DIR)
        self.PROJECT_MAIN_DIR = os.path.dirname(self.PROJECT_SUB_DIR)
        self.LOG_DIR = os.path.join(self.PROJECT_MAIN_DIR,'log')
        self.toady = date.today()
        self.file_name = f"{self.toady}.log"
        self.LOG_FILE = os.path.join(self.LOG_DIR,self.file_name)

        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
        self.file_handler = logging.FileHandler(self.LOG_FILE)
        self.file_handler.setFormatter(self.formatter)
        if not self.logger.handlers:
            self.logger.addHandler(self.file_handler)



    def log_debug(self,msg):
        self.logger.debug(f'{msg}')

    def log_info(self,msg):
        self.logger.info(f'{msg}')

    def log_warning(self,msg):
        self.logger.warning(f'{msg}')

    def log_error(self,msg):
        self.logger.error(f'{msg}')

    def log_critical(self,msg):
        self.logger.critical(f'{msg}')



    

    


if __name__ == "__main__":
    ini = Monitor('some_name')