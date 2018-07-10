import csv

def isLiteral(caracter):
    '''Entre com isLiteral(caracter) para verificar se caracter corresponde a uma letra do alfabelo.
    Exemplo: isLiteral(d)
        Retorna: True

    Retorna VERDADEIRO caso o caracter lido for uma letra. Caso contrário FALSO.
    '''
    return caracter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def isNumeral(caracter):
    '''Entre com isNumeral(caracter) para verificar se caracter corresponde a um numero.
    Exemplo: isNumeral(4)
        Retorna: True

    Retorna VERDADEIRO caso o caracter lido for um numero. Caso contrário FALSO.
    '''
    return caracter in '0123456789'

def isFinalState(index):
    '''Entre com isFinalState(index) para verificar se index corresponde a um Estado Final.
    Exemplo: isFinalState(21)
        Retorna: True

    Os estados finais do DFA implementado são {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21, 22, 23}
    '''
    return index in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 21, 22, 23)

def csv_dict():
    reader = csv.DictReader(open('tabelaSintatica.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list