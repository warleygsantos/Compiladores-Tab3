import logging

FORMAT = '%(asctime)s %(levelname)s:%(name)s:%(lineno)s\t-> %(message)s'
logging.basicConfig(filename='analisadorLexico.log',level=logging.INFO,format=FORMAT, datefmt='%d-%m %H:%M:%S')

def info(string):
	logging.info(string)