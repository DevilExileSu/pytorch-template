import os
import sys
import logging
from utils.util import ensure_dir

class Logger(object):
    def __init__(self):
        path  = 'logs/'
        ensure_dir(path)
        handler = {
            logging.DEBUG: path + "debug.log",
            logging.INFO: path + "info.log"
        }
        self.__loggers = {}
        logLevels = handler.keys()
        fmt = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
        for level in logLevels:
            logger = logging.getLogger(str(level))
            logger.setLevel(level)
            if os.path.exists(handler[level]):
                # remove the old file
                os.remove(handler[level])
            
            log_path = os.path.abspath(handler[level])
            fh = logging.FileHandler(log_path)
            fh.setFormatter(fmt)
            fh.setLevel(level)

            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(level)
            logger.addHandler(fh)
            logger.addHandler(sh)
            self.__loggers.update({level: logger})
    def info(self, message):
        self.__loggers[logging.INFO].info(message)
    def debug(self, message):
        self.__loggers[logging.DEBUG].debug(message)
