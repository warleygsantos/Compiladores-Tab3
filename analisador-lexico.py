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

tokes = {
	1: 'Literal', 2: 'id', 3: 'Comentário', 4: 'EOF', 5:'OPR', 6:'OPR', 7:'OPR', 8:'RCB', 9:'OPM', 10:'AB_P', 11:'FC_P',
	12:'PT_V', 13:'Num', 14:'Num', 15:'Num'
}

tabela = {
# Estado Inicial
	0: 
		{'	': 0, ' ': 0, '\n': 0, '"': 16, 'L':2, 'D':13, '{':17, 'EOF':4, '=':5, '<':6, '>':7, '-':9, '+':9,
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
		{'	': 16, ' ': 16, '\n': 16, '"': 1, '.':16, 'L':16, 'D':16, '_':16, '{':16, '}':16, '=':16, '<':16,
		'>':16, '-':16, '+':16,	'*':16, '/':16, '(':16, ')':16, ';':16, 'e':16, 'E':16},
	17:
		{'	': 17, ' ': 17, '\n': 17, '"': 17, '.':17, 'L':17, 'D':17, '_':17, '{':17, '}':3, '=':17, '<':17,
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
				print (string + ' -> ' + tokes[s])
			else:
				print ("Nao e estado final")

while True:
	leToken()

#s = tabela[s]['=']
