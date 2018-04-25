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
