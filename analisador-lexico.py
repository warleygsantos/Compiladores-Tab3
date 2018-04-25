import logging

FORMAT = '%(asctime)s %(levelname)s:%(name)s:%(lineno)s\t-> %(message)s'
#logging.basicConfig(filename='analisador-lexico.log',level=logging.INFO,format=FORMAT, datefmt='%H:%M:%S')
logging.basicConfig(level=logging.INFO,format=FORMAT, datefmt='%H:%M:%S')

logging.info('Beging')
file = open('FONTE.ALG', 'r')

def isLiteral(caracter):
	'''Responsável por verificar se o caracter lido é uma letra.

	Retorna VERDADEIRO caso o caracter lido for uma letra. Caso contrário FALSO.
	'''
	return caracter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def isNumeral(caracter):
	'''Responsável por verificar se caracter lido é um numero.

	Retorna VERDADEIRO caso o caracter lido for um número. Caso contrário FALSO.
	'''
	return caracter in '0123456789'

def isFinalState(index):
	'''Resposável por verificar se o indice corresponde a um Estado Final.

	Os estados finais do DFA implementado são {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21, 22, 23}
	'''
	return index in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 21, 22, 23)

tokens = {
	1: 'Literal', 2: 'id', 3: 'Comentário', 4: 'EOF', 5:'OPR', 6:'OPR', 7:'OPR', 8:'RCB', 9:'OPM', 10:'AB_P', 11:'FC_P',
	12:'PT_V', 13:'Num', 14:'Num', 15:'Num', 21:'Tab', 22:'Salto', 23:'Espaço'
}

tabela = {
# Estado Inicial
	0: 
		{'	': 21, ' ': 23, '\n': 22, '"': 16, 'L':2, 'D':13, '{':17, 'EOF':4, '=':5, '<':6, '>':7, '-':9, '+':9,
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
		'>':16, '-':16, '+':16,	'*':16, '/':16, '(':16, ')':16, ';':16, 'e':16, 'E':16, ':':16, '\\':16},
	17:
		{'	': 17, ' ': 17, '\n': 17, '"': 17, '.':17, 'L':17, 'D':17, '_':17, '{':17, '}':3, '=':17, '<':17,
		'>':17, '-':17, '+':17,	'*':17, '/':17, '(':17, ')':17, ';':17, 'e':17, 'E':17, ':':17, '\\':17},
	18:
		{'D':14},
	19:
		{'D':15, '-':20, '+':20},
	20:
		{'D':15}
}

linha 	= 0
coluna	= 0
x 		= '1'

def leToken():
	global linha
	global coluna

	continua	= True
	estado 		= 0
	token 		= ''
	lexema 		= ''
	tipo 		= ''
	coluna		= 0

	while(continua):
		c = file.read(1)
		buffe = c

		if(c is ''):
			c = 'EOF'
			buffe = c
		elif (isLiteral(c)):
			c = 'L'
		elif (isNumeral(c)):
			c = 'D'
		try:
			estado = tabela[estado][c]
			lexema = lexema + buffe
			coluna = coluna + 1
		except Exception:
			continua = False
			if (c is not 'EOF'):
				file.seek(file.tell() - 1)
			if isFinalState(estado):
				token = tokens[estado]
				if(token in ('Num', 'Literal', 'id')):
					tipo = 'Nao definido'
					logging.info('Token: {}\tLexema: {}\tTipo: {}'.format(token, lexema, tipo))
				elif(token in ('OPR', 'RCB', 'OPM', 'AB_P', 'FC_P', 'PT_V')):
					logging.info('Token: {}\tLexema: {}'.format(token, lexema))
				elif(token in ('Comentário', 'Tab', 'Salto', 'Espaço')):
					logging.info('Token {} ignorado'.format(token))
					return leToken()
				elif(token in ('EOF')):
					logging.info('Final de arquivo')
			else:
				token = 'ERRO'
	return token


while (x is not 'EOF'):
	x = leToken()
	#logging.info(x)
