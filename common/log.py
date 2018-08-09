__author__ = 'zhaoyao'
import logging
import os
import time


cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
log_path = os.path.join(cur_path,"logs")

class LOG():

    def setlog(self):

        self.logger = logging.getLogger()
        self.logname = os.path.join(log_path,"%s.log"%time.strftime("%Y_%m_%d"))
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(filename)s [line:%(lineno)d]- %(levelname)s : %(message)s')
        self.file_handler  = logging.FileHandler(self.logname,encoding="utf-8")
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)
        #控制器输出,创建Handler
        self.console_handler  = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)
        self.console_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.console_handler)

    def debug_info(self,message):
        self.setlog()
        self.logger.info(message)
        self.logger.removeHandler(self.file_handler)
        self.logger.removeHandler(self.console_handler)
    def debug_debug(self,message):
        self.setlog()
        self.logger.debug(message)
        self.logger.removeHandler(self.file_handler)
        self.logger.removeHandler(self.console_handler)
    def debug_warn(self,message):
        self.setlog()
        self.logger.warn(message)
        self.logger.removeHandler(self.file_handler)
        self.logger.removeHandler(self.console_handler)
    def debug_error(self,message):
        self.setlog()
        self.logger.error(message)
        self.logger.removeHandler(self.file_handler)
        self.logger.removeHandler(self.console_handler)
if __name__ == '__main__':
    log = LOG()
    log.debug_info('debug')
    log.debug_debug('info')
    log.debug_warn('warn')
    log.debug_error('error')



