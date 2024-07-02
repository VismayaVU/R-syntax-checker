import ply.lex as lex
import ply.yacc as yacc

flag = 0

tokens = (
    'NUMBER', 'STRING', 'TRUE', 'FALSE', 'IDENTIFIER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EXPONENT', 'EQUALS',
    'NOTEQUALS', 'GREATER', 'LESS', 'GREATEREQ', 'LESSEQ', 'AND', 'OR',
    'NOT', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'IF', 'ELSE', 'ASSIGN', 'WHILE'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPONENT = r'\^'
t_EQUALS = r'=='
t_NOTEQUALS = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATEREQ = r'>='
t_LESSEQ = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_IF = r'if'
t_ELSE = r'else'
t_TRUE = r'TRUE'
t_FALSE = r'FALSE'
t_STRING = r'"[a-zA-Z0-9]*"'
t_NUMBER = r'[0-9]+'
t_IDENTIFIER = r'[a-zA-Z][a-zA-Z0-9]*'
t_ASSIGN = r'<-'
t_WHILE = r'while'
t_ignore = ' \t\n'

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'TRUE': 'TRUE',
    'FALSE': 'FALSE'
}

def t_IDENTIFER(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at index {t.lexpos}")
    t.lexer.skip(1)

def p_while_loop(p):
    'while_loop : WHILE LPAREN condition RPAREN statement_block'
    p[0] = ('while-loop', p[3], p[5])

def p_condition(p):
    'condition : expression'
    p[0] = ('condition', p[1])

def p_statement_block(p):
    'statement_block : LBRACE statement_list RBRACE'
    p[0] = ('statement-block', p[2])

def p_expression(p):
    '''expression : literal 
                | variable 
                | binary_operation 
                | unary_operation'''
    p[0] = ('expression', p[1])

def p_literal(p):
    '''literal : number 
                | STRING 
                | boolean'''
    p[0] = ('literal', p[1])

def p_variable(p):
    '''variable : IDENTIFIER'''
    p[0] = ('variable', p[1])

def p_binary_operation(p):
    '''binary_operation : expression binary_operator expression'''
    p[0] = ('binary-operation', p[1], p[2], p[3])

def p_unary_operation(p):
    '''unary_operation : unary_operator expression'''
    p[0] = ('unary-operation', p[1], p[2])

def p_number(p):
    '''number : NUMBER'''
    p[0] = ('number', p[1])

def p_boolean(p):
    '''boolean : TRUE 
                | FALSE'''
    p[0] = ('boolean', p[1])

def p_identifier(p):
    '''identifier : IDENTIFIER'''
    p[0] = ('identifier', p[1])

def p_binary_operator(p):
    '''binary_operator : PLUS 
                        | MINUS 
                        | TIMES 
                        | DIVIDE 
                        | EXPONENT 
                        | EQUALS 
                        | NOTEQUALS 
                        | GREATER 
                        | LESS 
                        | GREATEREQ 
                        | LESSEQ 
                        | AND 
                        | OR'''
    p[0] = ('binary-operator', p[1])

def p_unary_operator(p):
    '''unary_operator : NOT 
                        | MINUS'''
    p[0] = ('unary-operator', p[1])

def p_statement_list(p):
    '''statement_list : statement statement_list 
                        | statement
                        | empty'''
    if len(p) == 4:
        p[0] = ('statement-list', p[1], p[3])
    else:
        p[0] = ('statement-list', p[1])

def p_statement(p):
    '''statement : assignment SEMICOLON
                    | while_loop 
                    | if_statement 
                    | expression '''
    p[0] = ('statement', p[1])

def p_assignment(p):
    '''assignment : identifier ASSIGN expression'''
    p[0] = ('assignment', p[1], p[3])

def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN statement_block else_clause'''
    p[0] = ('if-statement', p[3], p[5], p[6])

def p_else_clause(p):
    '''else_clause : ELSE statement_block 
                    | empty'''
    if len(p) == 3:
        p[0] = ('else-clause', p[2])
    else:
        p[0] = ('else-clause', None)

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    global flag
    flag = 1

parser = yacc.yacc()
lexer = lex.lex()

while True:
   flag = 0
   try:
       s = input('Enter the while loop to check: ')
   except EOFError:
       break
   if not s: 
        flag = 0
        continue
   result = parser.parse(s)
   if flag == 0:
        print("VALID SYNTAX")