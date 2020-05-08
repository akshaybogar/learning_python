import logging

extra_data = {"user": "akshay.bogar@abc.com"}

def main():
    fmtstr = 'User:%(user)s: %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d \
    %(message)s'
    logging.basicConfig(level=logging.DEBUG, filename='output.txt',
    filemode='w', format=fmtstr)
    logging.info('This is an info message', extra=extra_data)
    logging.warning('This is a warning message',extra=extra_data)

if __name__ == '__main__':
    main()
