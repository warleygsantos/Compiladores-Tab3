import logging

FORMAT = '%(asctime)s %(levelname)s:%(name)s:%(lineno)s -> %(message)s'
logging.basicConfig(filename='analisador-lexico.log',level=logging.INFO,format=FORMAT, datefmt='%H:%M:%S')
#logging.basicConfig(level=logging.INFO,format=FORMAT, datefmt='%H:%M:%S')

logging.info('Beging')
file = open('FONTE.ALG', 'r')

def isLiteral(caracter):
	"""Responsável por verificar se o caracter lido é uma letra.

	Retorna VERDADEIRO caso o caracter lido for uma letra. Caso contrário FALSO.
	"""
	return caracter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def isNumeral(caracter):
	"""Responsável por verificar se caracter lido é um numero.

	Retorna VERDADEIRO caso o caracter lido for um número. Caso contrário FALSO.
	"""
	return caracter in '0123456789'

def isFinalState(index):
	"""Resposável por verificar se o indice corresponde a um Estado Final.

	Os estados finais do DFA implementado são {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21, 22, 23}
	"""
	return index in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 21, 22, 23)

tokes = {
	1: 'Literal', 2: 'id', 3: 'Comentário', 4: 'EOF', 5:'OPR', 6:'OPR', 7:'OPR', 8:'RCB', 9:'OPM', 10:'AB_P', 11:'FC_P',
	12:'PT_V', 13:'Num', 14:'Num', 15:'Num', 21:'Tab', 22:'Salto', 23:'Espaço'
}

tabela = {
# Estado Inicial
	0: 
		{'Tab': 21, 'Espaço': 23, 'Salto': 22, '"': 16, 'L':2, 'D':13, '{':17, 'EOF':4, '=':5, '<':6, '>':7, '-':9, '+':9,
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
		{'Tab': 16, 'Espaço': 16, 'Salto': 16, '"': 1, '.':16, 'L':16, 'D':16, '_':16, '{':16, '}':16, '=':16, '<':16,
		'>':16, '-':16, '+':16,	'*':16, '/':16, '(':16, ')':16, ';':16, 'e':16, 'E':16},
	17:
		{'Tab': 17, 'Espaço': 17, 'Salto': 17, '"': 17, '.':17, 'L':17, 'D':17, '_':17, '{':17, '}':3, '=':17, '<':17,
		'>':17, '-':17, '+':17,	'*':17, '/':17, '(':17, ')':17, ';':17, 'e':17, 'E':17},
	18:
		{'D':14},
	19:
		{'D':15, '-':20, '+':20},
	20:
		{'D':15}
}

linha = 0
coluna = 0

def leToken():
	continua = True
	string = ''
	estado = 0


	global linha
	global coluna
	coluna = 0

	while(continua):
		c = file.read(1)
		buffe = c

		if (isLiteral(c)):
			c = 'L'
		elif (isNumeral(c)):
			c = 'D'
		elif (c is '\n'):
			c = 'Salto'
			buffe = c
			linha = linha + 1
		elif (c is ' '):
			c = 'Espaço'
			buffe = c
		elif (c is '	'):
			c = 'Tab'
			buffe = c
		try:
			estado = tabela[estado][c]
			string = string + buffe
			coluna = coluna + 1
			logging.info('Estado mudou para {}'.format(estado))
		except Exception:
			continua = False
			file.seek(file.tell() - 1)
			if isFinalState(estado):
				print (string + ' -> ' + tokes[estado] + "{},{}".format(linha, coluna))
			else:
				print (c)

while True:
#for x in range(0, 7):
	leToken()