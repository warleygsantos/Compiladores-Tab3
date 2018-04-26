import logging
import utilitarios

FORMAT = '%(asctime)s %(levelname)s:%(name)s:%(lineno)s\t-> %(message)s'
logging.basicConfig(filename='analisador-lexico.log',level=logging.INFO,format=FORMAT, datefmt='%H:%M:%S')

logging.info('Beging')
file = open('FONTE.ALG', 'r')

#fonte = file.read()

tokens = {
	1: 'Literal', 2: 'id', 3: 'Comentário', 4: 'EOF', 5:'OPR', 6:'OPR', 7:'OPR', 8:'RCB', 9:'OPM', 10:'AB_P', 11:'FC_P',
	12:'PT_V', 13:'Num', 14:'Num', 15:'Num', 21:'Tab', 22:'Salto', 23:'Espaço'
}

tabela = {
	#Corresponte a tabela de transições do DFA.
	#
	#Estados que não possuem regra de transição não tem nescessidade de estar na tabela.
	0:
		#Transicoes do Estado Inicial. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'	':21, ' ':23, '\n':22, '"':16, 'L':2, 'D':13, '{':17, 'EOF':4, '=':5, '<':6, '>':7, '-':9, '+':9, '*':9,
		'/':9, '(':10, ')':11, ';':12},
	2:
		#Transicoes do estado 2. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'L':2, 'D':2, '_':2},
	6:
		#Transicoes do estado 6. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'=':5, '-':8},
	7:
		#Transicoes do estado 7. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'=':5},
	13:
		#Transicoes do estado 13. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'.':18, 'D':13, 'e':19, 'E':19},
	14:
		#Transicoes do estado 14. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'D':14, 'e':14, 'E':14},
	15:
		#Transicoes do estado 15. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'D':15},
	16:
		#Transicoes do estado 16. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'	':16, ' ':16, '\n':16, '"':1, '.':16, 'L':16, 'D':16, '_':16, '{':16, '}':16, '=':16, '<':16, '>':16,
		'-':16, '+':16,	'*':16, '/':16, '(':16, ')':16, ';':16, 'e':16, 'E':16, ':':16, '\\':16},
	17:
		#Transicoes do estado 17. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'	':17, ' ':17, '\n':17, '"':17, '.':17, 'L':17, 'D':17, '_':17, '{':17, '}':3, '=':17, '<':17, '>':17,
		'-':17, '+':17,	'*':17, '/':17, '(':17, ')':17, ';':17, 'e':17, 'E':17, ':':17, '\\':17},
	18:
		#Transicoes do estado 18. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'D':14},
	19:
		#Transicoes do estado 19. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'D':15, '-':20, '+':20},
	20:
		#Transicoes do estado 20. {'CARACTER_LIDO' : NOVO_ESTADO}
		{'D':15}
}

tell	= 0

def leToken():
	global tell

	continua	= True
	estado 		= 0
	token 		= ''
	lexema 		= ''
	tipo 		= ''
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
			tell = tell + 1
		except Exception:
			continua = False
			if (c is not 'EOF'):
#				file.seek(file.tell() - 1) # tell() retorna valores estranhos quando le em \n. Issue432373 para mais detalhes.
				file.seek(tell)
			if utilitarios.isFinalState(estado):
				token = tokens[estado]
				if(token in ('Comentário', 'Tab', 'Salto', 'Espaço')):
					logging.info('Token {} ignorado'.format(token))
					return leToken()
				logging.info('Token: {}\tLexema: {}\tTipo: {}'.format(token, lexema, tipo))
				return {'token':token, 'lexema':lexema, 'tipo':tipo}
			else:
				token = 'ERRO'
				return {'token':token, 'causa':'Não identificado'}

x = '1'

#print(fonte)

while (x is not 'EOF'):
	tupla = leToken()
	x = tupla['token']

	print('Token: {}\tLexema: {}\t\tTipo: {}'.format(tupla['token'], tupla['lexema'], tupla['tipo']))