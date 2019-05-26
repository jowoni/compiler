import sys
sys.path.insert(0, "../..")

import ply.lex as lex

# reserved
reserved = (
    'INT', 'RETURN', 'VOID', 'FOR', 'ELSE', 'IF', 'WHILE', 'BREAK',
)

# List of token names.   This is always required
tokens = reserved + (

    # Literals (identifier, integer constant, float constant, string constant,
    # char const)
    'ID', # 'TYPEID', 'ICONST', 'FCONST', 'SCONST', 'CCONST',

    # Operators (+,-,*,/,%, &, ||, &&, !, <, <=, >, >=, ==)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'AND', 'LOR',
    'LAND', 'LNOT', 'LT', 'LE', 'GT', 'GE', 'EQ',

    # Assignment (=)
    'EQUALS',

    # Increment/decrement (++,--)
    'PLUSPLUS', 'MINUSMINUS',

    # Delimeters ( ) [ ] { } , ;
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'SEMI',
)

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_AND = r'&'
t_LOR = r'\|\|'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='

# Assignment operators

t_EQUALS = r'='

# Increment/decrement
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'

# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMI = r';'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Identifiers and reserved words

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t

# Preprocessor directive (ignored)
def t_preprocessor(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1

# Integer literal
t_ICONST = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FCONST = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
t_SCONST = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_CCONST = r'(L)?\'([^\\\n]|(\\.))*?\''

# Build the lexer
lexer = lex.lex()