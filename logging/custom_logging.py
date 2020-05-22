import logging
import os

extra_data = {"user": "akshay.bogar@abc.com"}

def main():
    fmtstr = 'User:%(user)s: %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d \
    %(message)s'
    '''
     Below statement will change setting for all loggers which may lead to errors.
     To change settings only for custom loggers we may use FileHandlers and Streamhandlers
     logger = logging.getLogger('Custom logging')
     handler = logging.StreamHandler()
     handler.setFormatter(fmtstr)
     file_handler = logging.FileHandler(filename='output.log')
     file_handler.setFormatter(fmtstr)
     logger.addHandler(handler)
     logger.addHandler(file_handler)
     return logger
    '''
    logging.basicConfig(level=logging.DEBUG, filename='output.txt',
    filemode='w', format=fmtstr)
    logger = logging.getLogger('Custom logging')
    logger = logging.LoggerAdapter(logger, extra_data)
    logger.info('This is an info message')
    logger.warning('This is a warning message')

if __name__ == '__main__':
    main()
