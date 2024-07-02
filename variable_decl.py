import ply.lex as lex
import ply.yacc as yacc

flag = 0

tokens = ('ID', 'NUM', 'ASSIGN', 'SEMICOLON', 'FLOAT')

t_ASSIGN = r'<-'
t_SEMICOLON = r';'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

def t_FLOAT(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
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

def p_statement_assign(p):
    '''statement : ID ASSIGN NUM SEMICOLON statement
                    | ID ASSIGN NUM SEMICOLON
                    | ID ASSIGN FLOAT SEMICOLON statement
                    | ID ASSIGN FLOAT SEMICOLON'''

def p_error(p):
    print("Syntax error")
    global flag
    flag = 1

parser = yacc.yacc()

while True:
   flag = 0
   try:
       s = input('Enter the variable declaration to check: ')
   except EOFError:
       break
   if not s: 
        flag = 0
        continue
   result = parser.parse(s)
   if flag == 0:
        print("VALID SYNTAX")