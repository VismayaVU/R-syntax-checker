import ply.lex as lex
import ply.yacc as yacc

flag = 0

tokens = ('ID', 'NUM', 'COMMA', 'LPAREN', 'RPAREN', 'ASSIGN', 'array', 'dim', 'c', 'SEMICOLON', 'EQUALS')

t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'<-'
t_array = r'array'
t_dim = r'dim'
t_c = r'c'
t_SEMICOLON = r';'
t_EQUALS = R'='

reserved = {
            'array' : 'array',
            'dim' : 'dim',
            'c' : 'c'
            }

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')  
    return t

def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_statement(p):
    '''statement : ID ASSIGN array LPAREN vector dim EQUALS LPAREN N RPAREN RPAREN SEMICOLON'''

def p_vector_recursive(p):
    '''vector : c LPAREN ID RPAREN COMMA vector 
            | c LPAREN ID RPAREN COMMA
            | c LPAREN N RPAREN COMMA vector
            | c LPAREN N RPAREN COMMA'''

def p_N_recursive(p):
    '''N : NUM COMMA N 
            | NUM'''

def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    global flag
    flag = 1

parser = yacc.yacc()

while True:
   flag = 0
   try:
       s = input('Enter the array declaration to check: ')
   except EOFError:
       break
   if not s: 
        flag = 0
        continue
   result = parser.parse(s)
   if flag == 0:
        print("VALID SYNTAX")