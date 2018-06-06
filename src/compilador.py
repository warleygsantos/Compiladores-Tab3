import csv

import myLogging as log
import utilitarios

log.info('Beging')

################################################## TABLES DEFINITION ###################################################
tokens = {
    #Matching STATE and TOKEN.
    1:'literal',
    2:'id',
    3:'Comentário',
    4:'EOF',
    5:'opr',
    6:'opr',
    7:'opr',
    8:'rcb',
    9:'opm',
    10:'AB_P',
    11:'FC_P',
    12:'PT_V',
    13:'num',
    14:'num',
    15:'num',
    21:'Tab',
    22:'Salto',
    23:'Espaço'
}

idTable = {
    #Lexeme is the key.
    'inicio'    : {'token':'inicio',    'tipo':''},
    'varinicio' : {'token':'varinicio', 'tipo':''},
    'varfim'    : {'token':'varfim',    'tipo':''},
    #'id'        : {'token':'id',        'tipo':''},
    'int'       : {'token':'int',       'tipo':''},
    'real'      : {'token':'real',      'tipo':''},
    'lit'       : {'token':'lit',       'tipo':''},
    'leia'      : {'token':'leia',      'tipo':''},
    'escreva'   : {'token':'escreva',   'tipo':''},
    'literal'   : {'token':'literal',   'tipo':''},
    'num'       : {'token':'num',       'tipo':''},
    'rcb'       : {'token':'rcb',       'tipo':''},
    'opm'       : {'token':'opm',       'tipo':''},
    'opr'       : {'token':'opr',       'tipo':''},
    'se'        : {'token':'se',        'tipo':''},
    'entao'     : {'token':'entao',     'tipo':''},
    'senao'     : {'token':'senao',     'tipo':''},
    'fimse'     : {'token':'fimse',     'tipo':''},
    'fim'       : {'token':'fim',       'tipo':''}
}

AFDTable = {
    #Transition table.
    0:
        #Initial state transitions. {'CHARACTER' : NEW_STATE}
        {
            '\t'   :21,
            ' '     :23,
            '\n'    :22,
            '"'     :16,
            'L'     :2,
            'D'     :13,
            '{'     :17,
            'EOF'   :4,
            '='     :5,
            '<'     :6,
            '>'     :7,
            '-'     :9,
            '+'     :9,
            '*'     :9,
            '/'     :9,
            '('     :10,
            ')'     :11,
            ';'     :12
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
            'e':19,
            'E':19
        },
    15:
        #State transitions 15. {'CHARACTER' : NEW_STATE}
        {
            'D':15
        },
    16:
        #State transitions 16. {'CHARACTER' : NEW_STATE}
        {
            '\t'   :16,
            ' '     :16,
            '\n'    :16,
            '"'     :1,
            '.'     :16,
            'L'     :16,
            'D'     :16,
            '_'     :16,
            '{'     :16,
            '}'     :16,
            '='     :16,
            '<'     :16,
            '>'     :16,
            '-'     :16,
            '+'     :16,
            '*'     :16,
            '/'     :16,
            '('     :16,
            ')'     :16,
            ';'     :16,
            'e'     :16,
            'E'     :16
        },
    17:
        #State transitions 17. {'CHARACTER' : NEW_STATE}
        {
            '\t'   :17,
            ' '     :17,
            '\n'    :17,
            '"'     :17,
            '.'     :17,
            'L'     :17,
            'D'     :17,
            '_'     :17,
            '{'     :17,
            '}'     :3,
            '='     :17,
            '<'     :17,
            '>'     :17,
            '-'     :17,
            '+'     :17,
            '*'     :17,
            '/'     :17,
            '('     :17,
            ')'     :17,
            ';'     :17,
            'e'     :17,
            'E'     :17
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
    #Error mapping table.
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

################################################# STATIC VARIABLES #####################################################
tell    = 0 #Current position of reading the source code file.
nRow    = 1 #Current line of the source file. Used to return error.
nColumn = 1 #Current column of the source file. Used to return error.

###################################################### LEXICAL #########################################################
def lexico(sourceCode):
    '''
    Retorna VERDADEIRO caso o caracter lido for uma letra. Caso contrário FALSO.
    '''
    global tell
    global nRow
    global nColumn

    continua    = True
    estado      = 0
    token       = ''
    lexema      = ''
    tipo        = ''

    while(continua):
        if(tell < len(sourceCode)):
            #Read character by character and check if is EOF.
            c = sourceCode[tell]
        else:
            c = 'EOF'
        buffe = c

        if ((c is 'e' or c is 'E') and (estado is 13 or estado is 14)):
            #Check if is e or E numeric
            c = c
        elif (utilitarios.isLiteral(c)):
            #Check if is literal.
            c = 'L'
        elif (utilitarios.isNumeral(c)):
            #Check if is numeric.
            c = 'D'
        disc = AFDTable[estado]
        if(c in disc or ((estado is 16 or estado is 17) and c is not 'EOF')):
            #If transition is valid: Change state and update values of the lexeme string, tell, nComunm and nRows.
            if(estado is not 16 and estado is not 17):
                #See the transitions table and get new state.
                estado = disc[c]
            else:
                #Keep the states 16 and 17 (constant literal and comment) in unexpected symbols.
                estado = disc.get(c, estado)
            lexema = lexema + buffe
            tell = tell + 1
            nColumn = nColumn + 1
            if (c is '\n'):
                nRow = nRow + 1
                nColumn = 1
        else:
            #Ignore or return: accept or reject.
            continua = False
            if utilitarios.isFinalState(estado):
                token = tokens[estado]
                if(token in ('Comentário', 'Tab', 'Salto', 'Espaço')):
                    log.info('Ignorou token {}'.format(token))
                    return lexico(sourceCode)
                elif(token is 'id'):
                    if(lexema in idTable.keys()):
                        token = idTable[lexema]['token']
                    elif(lexema not in idTable):
                        #Se o token for 'id' e o lexema correspondente nao estiver na tabela
                        idTable[lexema] = {'token':token, 'tipo':tipo}
                log.info('Token:{:<20}Lexema:{:<20}Tipo:{}'.format(token, lexema, tipo))
                return {'token':token, 'lexema':lexema, 'tipo':tipo}
            else:
                token = 'ERRO'
                tipo = "Erro na linha: {}, Coluna: {} - {}".format(nRow, nColumn, error[estado])
                log.info('Token:{:<20}Lexema:{:<20}Tipo:{}'.format(token, lexema, tipo))
                return {'token':token, 'tipo':tipo, 'lexema':lexema}

######################################################## SINTATICO #####################################################

enumeracao = {
    1:
        {'A':'P\'',    'B':'P',   'len':1},
    2:
        {'A':'P',    'B':'inicio V A',   'len':3},
    3:
        {'A':'V',    'B':'varinicio LV',   'len':2},
    4:
        {'A':'LV',    'B':'D LV',   'len':2},
    5:
        {'A':'LV',    'B':'varfim;',   'len':2},
    6:
        {'A':'D',    'B':'id TIPO;',   'len':3},
    7:
        {'A':'TIPO',    'B':'inteiro',   'len':1},
    8:
        {'A':'TIPO',    'B':'real',   'len':1},
    9:
        {'A':'TIPO',    'B':'lit',   'len':1},
    10:
        {'A':'A',    'B':'ES A',   'len':2},
    11:
        {'A':'ES',    'B':'leia id;',   'len':3},
    12:
        {'A':'ES',    'B':'escreva ARG;',   'len':3},
    13:
        {'A':'ARG',    'B':'literal',   'len':1},
    14:
        {'A':'ARG',    'B':'num',   'len':1},
    15:
        {'A':'ARG',    'B':'id',   'len':1},
    16:
        {'A':'A',    'B':'CMD A',   'len':2},
    17:
        {'A':'CMD',    'B':'id rcb LD;',   'len':4},
    18:
        {'A':'LD',    'B':'OPRD opm OPRD',   'len':3},
    19:
        {'A':'LD',    'B':'OPRD',   'len':1},
    20:
        {'A':'OPRD',    'B':'id',   'len':1},
    21:
        {'A':'OPRD',    'B':'num',   'len':1},
    22:
        {'A':'A',    'B':'COND A',   'len':2},
    23:
        {'A':'COND',    'B':'CABECALHO CORPO',   'len':2},
    24:
        {'A':'CABECALHO',    'B':'se (EXP_R) então',   'len':5},
    25:
        {'A':'EXP_R',    'B':'OPRD opr OPRD',   'len':3},
    26:
        {'A':'CORPO',    'B':'ES CORPO',   'len':2},
    27:
        {'A':'CORPO',    'B':'CMD CORPO',   'len':2},
    28:
        {'A':'CORPO',    'B':'COND CORPO',   'len':2},
    29:
        {'A':'CORPO',    'B':'fimse',   'len':1},
    30:
        {'A':'A',    'B':'fim',   'len':1}
}


#Open and read the source code file.
file = open('FONTE.ALG', 'r')
sourceCode = file.read()

stack = [0]
syntacticTable = utilitarios.csv_dict()

a = lexico(sourceCode)
while(True):
    if(a['token'] == 'ERRO'):
        print('Erro lexico: {}'.format(a['tipo']))
        break
    action = syntacticTable[stack[0]][a['token']]
    if(action == 'ACC'):
        print('Aceito')
        break
    nAction = int(action.lstrip('SsRr'))

    if(action[0] is 'S' or action[0] is 's'):
        stack.insert(0, nAction)
        a = lexico(sourceCode)
    elif(action[0] is 'R' or action[0] is 'r'):
        for n in range(0, enumeracao[nAction]['len']):
            stack.pop(0)
        stack.insert(0, int(syntacticTable[stack[0]][enumeracao[nAction]['A']]))
        print('{} -> {}'.format(enumeracao[nAction]['A'], enumeracao[nAction]['B']))