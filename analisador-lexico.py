import logging

FORMAT = '%(asctime)s %(levelname)s:%(name)s:%(lineno)s -> %(message)s'
logging.basicConfig(filename='analisador-lexico.log',level=logging.DEBUG,format=FORMAT, datefmt='%H:%M:%S')

logging.info('Beging')
file = open('FONTE.ALG', 'r')

def isLiteral(caracter):
	return caracter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def isNumeral(caracter):
	return caracter in '0123456789'

def isFinalState(number):
	return number in range(1, 13)

tabela = {
# Estado Inicial
	0: 
		{'TAB': 0, 'SPACE': 0, 'ENTER': 0, '"': 16, 'L':2, 'D':13, '{':17, 'EOF':4, '=':5, '<':6, '>':7, '-':9, '+':9,
		'*':9, '/':9, '(':10, ')':11, ';':12},
	2:
		{'L':2, 'D':2, '_':2},
	# Estado 6
	6:
		{'=':5, '-':8},
	7:
		{'=':5},
	13:
		{'.': 18, 'D':13, 'e':19, 'E':19},
	14:
		{'D':14, 'e':14, 'E':14},
	15:
		{'D':15},
	16:
		{'TAB': 16, 'SPACE': 16, 'ENTER': 16, '"': 1, '.':16, 'L':16, 'D':16, '_':16, '{':16, '}':16, '=':16, '<':16,
		'>':16, '-':16, '+':16,	'*':16, '/':16, '(':16, ')':16, ';':16, 'e':16, 'E':16},
	17:
		{'TAB': 17, 'SPACE': 17, 'ENTER': 17, '"': 17, '.':17, 'L':17, 'D':17, '_':17, '{':17, '}':3, '=':17, '<':17,
		'>':17, '-':17, '+':17,	'*':17, '/':17, '(':17, ')':17, ';':17, 'e':17, 'E':17},
	18:
		{'D':14},
	19:
		{'D':15, '-':20, '+':20},
	20:
		{'D':15}
}

def leToken():
	continua = True
	string = ''
	s = 0
	while(continua):
		buffe = file.read(1);
		c = buffe

		if (isLiteral(c)):
			buffe = 'L'
		elif (isNumeral(c)):
			buffe = 'D'

		try:
			s = tabela[s][buffe]
			string = string + c
		except Exception:
			continua = False
			if isFinalState(s):
				print (string)
				print ("E estado final")
			else:
				print ("Nao e estado final")

leToken()
leToken()
leToken()
leToken()
leToken()
leToken()
leToken()
leToken()


#s = tabela[s]['=']
