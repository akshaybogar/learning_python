import logging

def main():
    #If level not set to debug, debug and info logs will be discarded and
    #filemode defaults to append.
    logging.basicConfig(level=logging.DEBUG,
    filename='output.txt',
    filemode='w')
    logging.debug('This is a debug message')
    logging.info('This is info message')
    logging.error('This is an error message')
    logging.warning('This is a warning message')
    logging.critical('This is a critical message')

if __name__ == '__main__':
    main()
