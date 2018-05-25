import myLogging as log
import utilitarios
import analisadorLexico as al

log.info('Beging Compiler')

#Open and read the source code file.
file = open('FONTE.ALG', 'r')
sourceCode = file.read()

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

print('{:_^68}'.format(''))
print ('|{:^12}|{:^40}|{:^12}|'.format('TOKEN', 'LEXEMA', 'TIPO'))
print('|{:-^66}|'.format(''))

token = 'continue'
while (token is not 'EOF' and token is not 'ERRO'):
	tupla = al.leToken(sourceCode)

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
	print('|{:12}|{:40}|{:12}|'.format(token, lexema, tipo))
print('{:-^68}'.format(''))