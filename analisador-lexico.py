import logging
import utilitarios

FORMAT = '%(asctime)s %(levelname)s:%(name)s:%(lineno)s\t-> %(message)s'
logging.basicConfig(filename='analisador-lexico.log',level=logging.INFO,format=FORMAT, datefmt='%d-%m %H:%M:%S')

logging.info('Beging')

tokens = {
	#Matching STATE and TOCKEN.
	1:'Literal',
	2:'id',
	3:'Comentário',
	4:'EOF',
	5:'OPR',
	6:'OPR',
	7:'OPR',
	8:'RCB',
	9:'OPM',
	10:'AB_P',
	11:'FC_P',
	12:'PT_V',
	13:'Num',
	14:'Num',
	15:'Num',
	21:'Tab',
	22:'Salto',
	23:'Espaço'
}

idTable = {
	#Lexeme is the key.
	'inicio'	: {'token':'inicio', 	'tipo':''},
	'varinicio'	: {'token':'varinicio', 'tipo':''},
	'varfim'	: {'token':'varfim', 	'tipo':''},
	'escreva'	: {'token':'escreva',	'tipo':''},
	'leia'		: {'token':'leia', 		'tipo':''},
	'se'		: {'token':'se', 		'tipo':''},
	'entao'		: {'token':'entao', 	'tipo':''},
	'senao'		: {'token':'senao', 	'tipo':''},
	'fimse'		: {'token':'fimse', 	'tipo':''},
	'fim'		: {'token':'fim', 		'tipo':''},
	'inteiro'	: {'token':'inteiro', 	'tipo':''},
	'literal'	: {'token':'literal',	'tipo':''},
	'real'		: {'token':'real', 		'tipo':''}
}

transitionsTable = {
	#Transition table.
	0:
		#Initial state transitions. {'CHARACTER' : NEW_STATE}
		{
			'	'	:21,
			' '		:23,
			'\n'	:22,
			'"'		:16,
			'L'		:2,
			'D'		:13,
			'{'		:17,
			'EOF'	:4,
			'='		:5,
			'<'		:6,
			'>'		:7,
			'-'		:9,
			'+'		:9,
			'*'		:9,
			'/'		:9,
			'('		:10,
			')'		:11,
			';'		:12
		},

	1:
		#State transitions 1. {'CHARACTER' : NEW_STATE}
		{},
	2:
		#State transitions 2. {'CHARACTER' : NEW_STATE}
		{
			'L':2,
			'D':2,
			'_':2
		},
	3:
		#State transitions 2. {'CHARACTER' : NEW_STATE}
		{},
	4:
		#State transitions 2. {'CHARACTER' : NEW_STATE}
		{},
	5:
		#State transitions 2. {'CHARACTER' : NEW_STATE}
		{},
	6:
		#State transitions 6. {'CHARACTER' : NEW_STATE}
		{
			'=':5,
			'-':8
		},
	7:
		#State transitions 7. {'CHARACTER' : NEW_STATE}
		{
			'=':5
		},
	8:
		#State transitions 2. {'CHARACTER' : NEW_STATE}
		{},
	9:
		#State transitions 2. {'CHARACTER' : NEW_STATE}
		{},
	10:
		#State transitions 2. {'CHARACTER' : NEW_STATE}
		{},
	11:
		#State transitions 2. {'CHARACTER' : NEW_STATE}
		{},
	12:
		#State transitions 2. {'CHARACTER' : NEW_STATE}
		{},
	13:
		#State transitions 13. {'CHARACTER' : NEW_STATE}
		{
			'.':18,
			'D':13,
			'e':19,
			'E':19
		},
	14:
		#State transitions 14. {'CHARACTER' : NEW_STATE}
		{
			'D':14,
			'e':14,
			'E':14
		},
	15:
		#State transitions 15. {'CHARACTER' : NEW_STATE}
		{
			'D':15
		},
	16:
		#State transitions 16. {'CHARACTER' : NEW_STATE}
		{
			'	'	:16,
			' '		:16,
			'\n'	:16,
			'"'		:1,
			'.'		:16,
			'L'		:16,
			'D'		:16,
			'_'		:16,
			'{'		:16,
			'}'		:16,
			'='		:16,
			'<'		:16,
			'>'		:16,
			'-'		:16,
			'+'		:16,
			'*'		:16,
			'/'		:16,
			'('		:16,
			')'		:16,
			';'		:16,
			'e'		:16,
			'E'		:16,
			':'		:16,
			'\\'	:16
		},
	17:
		#State transitions 17. {'CHARACTER' : NEW_STATE}
		{
			'	'	:17,
			' '		:17,
			'\n'	:17,
			'"'		:17,
			'.'		:17,
			'L'		:17,
			'D'		:17,
			'_'		:17,
			'{'		:17,
			'}'		:3,
			'='		:17,
			'<'		:17,
			'>'		:17,
			'-'		:17,
			'+'		:17,
			'*'		:17,
			'/'		:17,
			'('		:17,
			')'		:17,
			';'		:17,
			'e'		:17,
			'E'		:17,
			':'		:17,
			'\\'	:17
		},
	18:
		#State transitions 18. {'CHARACTER' : NEW_STATE}
		{
			'D':14
		},
	19:
		#State transitions 19. {'CHARACTER' : NEW_STATE}
		{
			'D':15,
			'-':20,
			'+':20
		},
	20:
		#State transitions 20. {'CHARACTER' : NEW_STATE}
		{
			'D':15
		},
	21:
		#State transitions 21. {'CHARACTER' : NEW_STATE}
		{},
	22:
		#State transitions 22. {'CHARACTER' : NEW_STATE}
		{},
	23:
		#State transitions 23. {'CHARACTER' : NEW_STATE}
		{}
}

error = {
	#
	0:
		'Simbolo disperso.',
	16:
		'Constante literal nao terminada.',
	17:
		'Comentario nao terminado.',
	18:
		'Constante numerica esperada.',
	19:
		'Constante numerica esperada.',
	20:
		'Constante numerica esperada.',
}

#Open and read the source code file.
file = open('FONTE.ALG', 'r')
sourceCode = file.read()

tell	= 0 #Current position of the source file.
nRow 	= 1 #Current line of the source file.
nColumn = 1 #Current column of the source file.

def leToken():
	global tell
	global nRow
	global nColumn

	continua	= True
	estado 		= 0
	token 		= ''
	lexema 		= ''
	tipo 		= ''

	while(continua):
		if(tell < len(sourceCode)):
			#Read character by character and check if is EOF.
			c = sourceCode[tell]
		else:
			c = 'EOF'
		buffe = c

		if (utilitarios.isLiteral(c)):
			#Check if is literal.
			c = 'L'
		elif (utilitarios.isNumeral(c)):
			#Check if is numeric.
			c = 'D'

		disc = transitionsTable[estado]
		if(c in disc):
			#If transition is valid update values of the lexeme string, tell, nComunm and nRows.
			estado = disc[c]
			lexema = lexema + buffe
			tell = tell + 1
			nColumn = nColumn + 1
			if (c is '\n'):
				nRow = nRow + 1
				nColumn = 1
			if(c is '\t'):
				nColumn = nColumn + 3
		else:
			#Ignore or return accept or reject.
			continua = False
			if utilitarios.isFinalState(estado):
				token = tokens[estado]
				if(token in ('Comentário', 'Tab', 'Salto', 'Espaço')):
					logging.info('Ignorou token {}'.format(token))
					return leToken()
				logging.info('Token:{:<20}tLexema:{:<20}Tipo:{}'.format(token, lexema, tipo))
				return {'token':token, 'lexema':lexema, 'tipo':tipo}
			else:
				token = 'ERRO'
				tipo = "Erro na linha: {}, Coluna: {} - {}".format(nRow, nColumn, error[estado])
				logging.info('Token:{:<20}Lexema:{:<20}Tipo:{}'.format(token, lexema, tipo))
				return {'token':token, 'tipo':tipo, 'lexema':lexema}


print('{:_^68}'.format(''))
print ('|{:^12}|{:^40}|{:^12}|'.format('TOKEN', 'LEXEMA', 'TIPO'))
print('|{:-^66}|'.format(''))

token = 'continue'
while (token is not 'EOF' and token is not 'ERRO'):
	tupla = leToken()

	token 	= tupla['token']
	lexema 	= tupla['lexema']
	tipo 	= tupla['tipo']

	if(token is 'id'):
		if (lexema not in idTable):
			#Se o toke for 'id' e o lexema correspondente nao estiver na tabela
			idTable[lexema] = {'token':token, 'tipo':tipo}
		else:
			into = idTable.get(lexema)
			token = into['token']
			tipo = into['tipo']
	else:
		token = tupla['token']
		tipo = tupla['tipo']
	lexema = lexema.replace("\n", " ")
	print('|{:12}|{:40}|{:12}|'.format(token, lexema, tipo))
print('{:-^68}'.format(''))