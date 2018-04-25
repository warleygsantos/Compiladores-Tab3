import logging
import utilitarios

FORMAT = '%(asctime)s %(levelname)s:%(name)s:%(lineno)s\t-> %(message)s'
#logging.basicConfig(filename='analisador-lexico.log',level=logging.INFO,format=FORMAT, datefmt='%H:%M:%S')
logging.basicConfig(level=logging.INFO,format=FORMAT, datefmt='%H:%M:%S')

logging.info('Beging')
file = open('FONTE.ALG', 'r')

tokens = {
	1: 'Literal', 2: 'id', 3: 'Comentário', 4: 'EOF', 5:'OPR', 6:'OPR', 7:'OPR', 8:'RCB', 9:'OPM', 10:'AB_P', 11:'FC_P',
	12:'PT_V', 13:'Num', 14:'Num', 15:'Num', 21:'Tab', 22:'Salto', 23:'Espaço'
}

tabela = {
	#Corresponte a tabela de transições do DFA.
	#
	#Estados que não possuem regra de transição não tem nescessidade de estar presente na tabela.
	0:
		#Estado Inicial
		{'	':21, ' ':23, '\n':22, '"':16, 'L':2, 'D':13, '{':17, 'EOF':4, '=':5, '<':6, '>':7, '-':9, '+':9, '*':9,
		'/':9, '(':10, ')':11, ';':12},
	2:
		#Estado 2.
		{'L':2, 'D':2, '_':2},
	6:
		#Estado 6.
		{'=':5, '-':8},
	7:
		#Estado 7.
		{'=':5},
	13:
		#Estado 13.
		{'.':18, 'D':13, 'e':19, 'E':19},
	14:
		#Estado 14.
		{'D':14, 'e':14, 'E':14},
	15:
		#Estado 15.
		{'D':15},
	16:
		#Estado 16.
		{'	':16, ' ':16, '\n':16, '"':1, '.':16, 'L':16, 'D':16, '_':16, '{':16, '}':16, '=':16, '<':16, '>':16,
		'-':16, '+':16,	'*':16, '/':16, '(':16, ')':16, ';':16, 'e':16, 'E':16, ':':16, '\\':16},
	17:
		#Estado 17.
		{'	':17, ' ':17, '\n':17, '"':17, '.':17, 'L':17, 'D':17, '_':17, '{':17, '}':3, '=':17, '<':17, '>':17,
		'-':17, '+':17,	'*':17, '/':17, '(':17, ')':17, ';':17, 'e':17, 'E':17, ':':17, '\\':17},
	18:
		#Estado 18.
		{'D':14},
	19:
		#Estado 19.
		{'D':15, '-':20, '+':20},
	20:
		#Estado 20.
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
		elif (utilitarios.isLiteral(c)):
			c = 'L'
		elif (utilitarios.isNumeral(c)):
			c = 'D'
		try:
			estado = tabela[estado][c]
			lexema = lexema + buffe
			coluna = coluna + 1
		except Exception:
			continua = False
			if (c is not 'EOF'):
				file.seek(file.tell() - 1)
			if utilitarios.isFinalState(estado):
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
