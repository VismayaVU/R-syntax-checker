import ply.lex as lex
import ply.yacc as yacc

flag = 0

tokens = (
    'NUMBER',
    'STRING',
    'TRUE',
    'FALSE',
    'IDENTIFIER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EXPONENT',
    'EQUALS',
    'NOT_EQUALS',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'AND',
    'OR',
    'NOT',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'IF',
    'ASSIGN'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPONENT = r'\^'
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_TRUE = r'TRUE'
t_FALSE = r'FALSE'
t_STRING = r'"[a-zA-Z0-9]*"'
t_NUMBER = r'[0-9]+'
t_IDENTIFIER = r'[a-zA-Z][a-zA-Z0-9]*'
t_IF = r'if'
t_ASSIGN = r'<-'

reserved = {
    'if': 'IF',
    'TRUE': 'TRUE',
    'FALSE': 'FALSE'
}

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def t_IDENTIFER(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  
    return t

def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN statement_block'''

def p_expression_literal(p):
    '''expression : literal'''

def p_expression_variable(p):
    '''expression : variable'''

def p_expression_binary_operation(p):
    '''expression : binary_operation'''

def p_expression_unary_operation(p):
    '''expression : unary_operation'''

def p_literal(p):
    '''literal : NUMBER
               | STRING
               | TRUE
               | FALSE'''

def p_variable(p):
    'variable : IDENTIFIER'

def p_binary_operation(p):
    '''binary_operation : expression binary_operator expression'''

def p_unary_operation(p):
    '''unary_operation : unary_operator expression'''

def p_binary_operator(p):
    '''binary_operator : PLUS
                      | MINUS
                      | TIMES
                      | DIVIDE
                      | EXPONENT
                      | EQUALS
                      | NOT_EQUALS
                      | GREATER
                      | LESS
                      | GREATER_EQUAL
                      | LESS_EQUAL
                      | AND
                      | OR'''

def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression'''

def p_unary_operator(p):
    '''unary_operator : NOT
                     | MINUS'''

def p_statement_block(p):
    'statement_block : LBRACE statement_list RBRACE'

def p_statement_list(p):
    '''statement_list : statement SEMICOLON statement_list
                     | statement SEMICOLON'''

def p_statement(p):
    '''statement : if_statement
                 | expression
                 | assignment'''

def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}")
    global flag
    flag = 1

lexer = lex.lex()
parser = yacc.yacc()

while True:
   flag = 0
   try:
       s = input('Enter the if-construct to check: ')
   except EOFError:
       break
   if not s: 
        flag = 0
        continue
   result = parser.parse(s)
   if flag == 0:
        print("VALID SYNTAX")
