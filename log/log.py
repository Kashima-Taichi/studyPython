import logging

logging.basicConfig(filename='test.log', level=logging.INFO)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.info('debug')

logging.info('info %s %s', 'test', 'test2')
