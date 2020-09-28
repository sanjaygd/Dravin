class Base():
    def __init__(self,log=None,do_not_log=False):
        self.log = log
        self.do_not_log = do_not_log

        if log is None and do_not_log == False:
            self.log = 
