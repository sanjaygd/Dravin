import configparser
import os




class Agent():
    def __init__(self):
        self.ini_config = configparser.ConfigParser()
        self.this_file_path = os.path.abspath(__file__)
        self.BASE_DIR = os.path.dirname(self.this_file_path)
        self.PROJECT_SUB_DIR = os.path.dirname(self.BASE_DIR)
        self.PROJECT_MAIN_DIR = os.path.dirname(self.PROJECT_SUB_DIR)
        self.conf_dir = os.path.join(self.PROJECT_MAIN_DIR,'cred')
        



    def store_cred(self,user,pwd,sect='DATABASE',opt1='user',opt2='password',file_name='cred.ini'):
        self.ini_config.add_section(sect)
        self.ini_config.set(sect,opt1,user)
        self.ini_config.set(sect,opt2,pwd)
        path_to_file = os.path.join(self.conf_dir,file_name)
        with open(path_to_file,'w') as fl:
            self.ini_config.write(fl)


    def read_cred(self,sect='DATABASE',opt1='user',opt2='password',file_name='cred.ini'):
        path_to_file = os.path.join(self.conf_dir,file_name)
        
        self.ini_config.read(path_to_file)
        usr = self.ini_config.get(sect,opt1)
        pwd = self.ini_config.get(sect,opt2)
        return (usr,pwd)


    

if __name__ == "__main__":
    ini = Agent()
    # ini.store_cred('dravin','wealth')
    ini.read_cred()