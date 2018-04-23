import logging

FORMAT = '%(asctime)s %(levelname)s:%(name)s:%(lineno)s -> %(message)s'
logging.basicConfig(filename='analisador-lexico.log',level=logging.DEBUG,format=FORMAT, datefmt='%H:%M:%S')

logging.info('Beging')
