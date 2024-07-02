import ply.lex as lex
import ply.yacc as yacc

flag = 0

tokens = (
    'REPEAT', 'LEFT_BRACE', 'RIGHT_BRACE',
    'LEFT_PAREN', 'RIGHT_PAREN', 'SEMICOLON',
    'BREAK', 'IF',
    'ASSIGN', 'IDENTIFIER',
    'NUMBER', 'STRING', 'TRUE', 'FALSE',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
    'EQUALS', 'NOT_EQUALS', 'GREATER', 'LESS',
    'GREATER_EQUAL', 'LESS_EQUAL', 'AND', 'OR',
    'NOT'
)

reserved = {
            'repeat' : 'REPEAT',
            'break' : 'BREAK',
            'if' : 'IF',
            'TRUE' : 'TRUE',
            'FALSE' : 'FALSE'
}

t_REPEAT = r'repeat'
t_LEFT_BRACE = r'{'
t_RIGHT_BRACE = r'}'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_SEMICOLON = r';'
t_BREAK = r'break'
t_IF = r'if'
t_ASSIGN = r'<-'
t_NUMBER = r'[0-9]+'
t_STRING = r'"[a-zA-Z0-9]*"'
t_TRUE = r'TRUE'
t_FALSE = r'FALSE'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_ignore = ' \t\n'

def t_IDENTIFER(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def p_repeat_loop(p):
    '''repeat_loop : REPEAT statement_block'''

def p_statement_block(p):
    '''statement_block : LEFT_BRACE statement_list RIGHT_BRACE'''

def p_statement_list(p):
    '''statement_list : statement SEMICOLON statement_list
                      | statement SEMICOLON
                      | if_statement
                      | BREAK SEMICOLON'''

def p_statement(p):
    '''statement : assignment
                 | expression'''

def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression'''

def p_if_statement(p):
    '''if_statement : IF LEFT_PAREN expression RIGHT_PAREN statement_block'''

def p_expression(p):
    '''expression : literal 
                    | variable 
                    | binary_operation 
                    | unary_operation'''

def p_literal(p):
    '''literal : NUMBER 
                | STRING 
                | TRUE
                | FALSE'''

def p_variable(p):
    '''variable : IDENTIFIER'''

def p_binary_operation(p):
    '''binary_operation : expression binary_operator expression'''

def p_unary_operation(p):
    '''unary_operation : unary_operator expression'''

def p_binary_operator(p):
    '''binary_operator : PLUS 
                        | MINUS 
                        | TIMES 
                        | DIVIDE 
                        | POWER 
                        | EQUALS 
                        | NOT_EQUALS 
                        | GREATER 
                        | LESS 
                        | GREATER_EQUAL 
                        | LESS_EQUAL 
                        | AND 
                        | OR'''

def p_unary_operator(p):
    '''unary_operator : NOT 
                        | MINUS'''

def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}")
    global flag
    flag = 1

lexer = lex.lex()
parser = yacc.yacc()

while True:
   flag = 0
   try:
       s = input('Enter the repeat(do-while) loop to check: ')
   except EOFError:
       break
   if not s: 
        flag = 0
        continue
   result = parser.parse(s)
   if flag == 0:
        print("VALID SYNTAX")