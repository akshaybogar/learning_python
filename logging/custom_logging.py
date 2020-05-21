import logging
import os

extra_data = {"user": "akshay.bogar@abc.com"}

def main():
    fmtstr = 'User:%(user)s: %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d \
    %(message)s'
    logging.basicConfig(level=logging.DEBUG, filename='output.txt',
    filemode='w', format=fmtstr)
    logger = logging.getLogger('Custom logging')
    logger = logging.LoggerAdapter(logger, extra_data)
    logger.info('This is an info message')
    logger.warning('This is a warning message')

if __name__ == '__main__':
    main()
