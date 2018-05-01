import logging
import utilitarios

FORMAT = '%(asctime)s %(levelname)s:%(name)s:%(lineno)s\t-> %(message)s'
logging.basicConfig(filename='analisador-lexico.log',level=logging.INFO,format=FORMAT, datefmt='%d-%m %H:%M:%S')

logging.info('Beging')
file = open('FONTE.ALG', 'r')

fonte = file.read()

tokens = {
	1: 'Literal',
	2: 'id',
	3: 'Comentário',
	4: 'EOF',
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

tabelaID = {
	#lexema eh a chave para acessar os registros
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

tabela = {
	#Corresponte a tabela de transições do DFA.
	0:
		#Transicoes do Estado Inicial. {'CARACTER_LIDO' : NOVO_ESTADO}
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
		#Transicoes do estado 1. {'CARACTER_LIDO' : NOVO_ESTADO}
		{},
	2:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{
			'L':2,
			'D':2,
			'_':2
		},
	3:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{},
	4:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{},
	5:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{},
	6:
		#Transicoes do estado 6. {'CARACTER_LIDO' : NOVO_ESTADO}
		{
			'=':5,
			'-':8
		},
	7:
		#Transicoes do estado 7. {'CARACTER_LIDO' : NOVO_ESTADO}
		{
			'=':5
		},
	8:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{},
	9:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{},
	10:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{},
	11:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{},
	12:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{},
	13:
		#Transicoes do estado 13. {'CARACTER_LIDO' : NOVO_ESTADO}
		{
			'.':18,
			'D':13,
			'e':19,
			'E':19
		},
	14:
		#Transicoes do estado 14. {'CARACTER_LIDO' : NOVO_ESTADO}
		{
			'D':14,
			'e':14,
			'E':14
		},
	15:
		#Transicoes do estado 15. {'CARACTER_LIDO' : NOVO_ESTADO}
		{
			'D':15
		},
	16:
		#Transicoes do estado 16. {'CARACTER_LIDO' : NOVO_ESTADO}
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
		#Transicoes do estado 17. {'CARACTER_LIDO' : NOVO_ESTADO}
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
		#Transicoes do estado 18. {'CARACTER_LIDO' : NOVO_ESTADO}
		{
			'D':14
		},
	19:
		#Transicoes do estado 19. {'CARACTER_LIDO' : NOVO_ESTADO}
		{
			'D':15,
			'-':20,
			'+':20
		},
	20:
		#Transicoes do estado 20. {'CARACTER_LIDO' : NOVO_ESTADO}
		{
			'D':15
		},
	21:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{},
	22:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{},
	23:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{}
}

tell	= 0
nLinhas = 1
nColuna 	= 1
def leToken():
	global tell
	global nLinhas
	global nColuna

	continua	= True
	estado 		= 0
	token 		= ''
	lexema 		= ''
	tipo 		= ''

	while(continua):
		if(tell < len(fonte)):
			c = fonte[tell]
		else:
			c = 'EOF'
		buffe = c
		if (utilitarios.isLiteral(c)):
			c = 'L'
		elif (utilitarios.isNumeral(c)):
			c = 'D'

		disc = tabela[estado]
		if(c in disc):
			estado = disc[c]
			lexema = lexema + buffe
			tell = tell + 1
			nColuna = nColuna + 1
			if (c is '\n'):
				nLinhas = nLinhas + 1
				nColuna = 1
		else:
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
				tipo = "Erro na linha: {}, Coluna: {}".format(nLinhas, nColuna)
				logging.info('Token:{:<20}Lexema:{:<20}Tipo:{}'.format(token, lexema, tipo))
				return {'token':token, 'tipo':tipo, 'lexema':lexema}

print('\t{:_^52}'.format(''))
print ('\t|{:^12}|{:^24}|{:^12}|'.format('TOKEN', 'LEXEMA', 'TIPO'))
print('\t|{:-^50}|'.format(''))

token = 'continue'
while (token is not 'EOF' and token is not 'ERRO'):
	tupla = leToken()

	token 	= tupla['token']
	lexema 	= tupla['lexema']
	tipo 	= tupla['tipo']

	if(token is 'id'):
		if (lexema not in tabelaID):
			#Se o toke for 'id' e o lexema correspondente nao estiver na tabela
			tabelaID[lexema] = {'token':token, 'tipo':tipo}
			print('\t|{:12}|{:24}|{:12}|'.format(token, lexema, tipo))
		else:
			into = tabelaID.get(lexema)
			print('\t|{:12}|{:24}|{:12}|'.format(into['token'], lexema, into['tipo']))
	else:
		print('\t|{:12}|{:24}|{:12}|'.format(tupla['token'], lexema, tupla['tipo']))
print('\t{:-^52}'.format(''))