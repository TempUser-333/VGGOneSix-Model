import logging


FORMAT = '%(process)s %(levelno)5d %(levelname)10s %(threadName)10s\
          %(funcName)10s %(asctime)10s %(msecs)10s'
          
logging.basicConfig(level=logging.DEBUG,
                    filename='logger_files/tracker.log',
                    filemode='a',
                    datefmt='%H:%M:%S',
                    format=FORMAT)
logger = logging.getLogger(__name__)
