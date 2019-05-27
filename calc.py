import sys
sys.path.insert(0, "../..")

import ply.lex as lex

# count variable
include = 0
declared_functions = 0
declared_variable = 0
conditional_statement = 0
loop = 0
called_functions = 0


# reserved
reserved = (
    'INT', 'RETURN', 'VOID', 'FOR', 'ELSE', 'IF', 'WHILE', 'BREAK',
)

# List of token names.   This is always required
tokens = reserved + (

    # Literals (identifier, integer constant, float constant, string constant,
    # char const)
    'ID', 'TYPEID', 'ICONST', 'FCONST', 'SCONST', 'CCONST',

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

    'INCLUDE',
    'DOT',
    'LCROC',
    'RCROC'
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

# #include
t_INCLUDE = r'\#include '
t_DOT = r'\.h'
t_LCROC = r'\<'
t_RCROC = r'\>'

'''
# A regular expression rule with some action code
def t_NUMBER(t:
    r'\d+'
    t.value = int(t.value)
    return t
'''

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Identifiers and reserved words

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t

# Integer literal
t_ICONST = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FCONST = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
t_SCONST = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_CCONST = r'(L)?\'([^\\\n]|(\\.))*?\''

# Comments
def t_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

'''
# Preprocessor directive (ignored)
def t_preprocessor(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1
'''

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

##################################################################################

import sys
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

# from calclex import tokens

# translation-unit:


def p_translation_unit_1(p):
    'translation_unit : external_declaration'
    p[0] = p[1]


def p_translation_unit_2(p):
    'translation_unit : translation_unit external_declaration'
    p[1].extend(p[2])
    p[0] = p[1]

def p_translation_unit_3(p): ################################################################ 추가한거!!!!
    'translation_unit : INCLUDE LCROC ID include_endings' # LCROC include_stuff RCROC'
    global include;
    include += 1
    pass
##############################################################################################
def p_include_endings_1(p):
    'include_endings : DOT RCROC'
    pass

def p_include_endings_2(p):
    'include_endings : RCROC'
    pass

# external-declaration:


def p_external_declaration_1(p):
    'external_declaration : function_definition'
    p[0] = [p[1]]
    global declared_functions
    declared_functions += 1


def p_external_declaration_2(p):
    'external_declaration : declaration'
    p[0] = p[1]

# function-definition:


def p_function_definition_1(p):
    'function_definition : declaration_specifiers declarator declaration_list compound_statement'
    pass


def p_function_definition_2(p):
    'function_definition : declarator declaration_list compound_statement'
    pass


def p_function_definition_3(p):
    'function_definition : declarator compound_statement'
    pass


def p_function_definition_4(p):
    'function_definition : declaration_specifiers declarator compound_statement'
    pass

# declaration:


def p_declaration_1(p):
    'declaration : declaration_specifiers init_declarator_list SEMI'
    pass


def p_declaration_2(p):
    'declaration : declaration_specifiers SEMI'
    pass


# declaration-list:


def p_declaration_list_1(p):
    'declaration_list : declaration'
    pass


def p_declaration_list_2(p):
    'declaration_list : declaration_list declaration '
    pass

# declaration-specifiers


def p_declaration_specifiers_1(p):
    'declaration_specifiers : type_specifier declaration_specifiers'
    pass


def p_declaration_specifiers_2(p):
    'declaration_specifiers : type_specifier'
    pass


# type-specifier:


def p_type_specifier(p):
    '''type_specifier : VOID
                      | INT
                      | TYPEID
                      '''
    pass


# init-declarator-list:


def p_init_declarator_list_1(p):
    'init_declarator_list : init_declarator'
    global declared_variable
    declared_variable += 1
    pass


def p_init_declarator_list_2(p):
    'init_declarator_list : init_declarator_list COMMA init_declarator'
    pass

# init-declarator


def p_init_declarator_1(p):
    'init_declarator : declarator'
    pass


def p_init_declarator_2(p):
    'init_declarator : declarator EQUALS initializer'
    pass

# specifier-qualifier-list:


def p_specifier_qualifier_list_1(p):
    'specifier_qualifier_list : type_specifier specifier_qualifier_list'
    pass


def p_specifier_qualifier_list_2(p):
    'specifier_qualifier_list : type_specifier'
    pass


# declarator:


def p_declarator_1(p):
    'declarator : direct_declarator'
    pass

# direct-declarator:


def p_direct_declarator_1(p):
    'direct_declarator : ID'
    pass


def p_direct_declarator_2(p):
    'direct_declarator : LPAREN declarator RPAREN'
    pass


def p_direct_declarator_3(p):
    'direct_declarator : direct_declarator LBRACKET constant_expression_opt RBRACKET'
    pass


def p_direct_declarator_4(p):
    'direct_declarator : direct_declarator LPAREN parameter_type_list RPAREN '
    pass


def p_direct_declarator_5(p):
    'direct_declarator : direct_declarator LPAREN identifier_list RPAREN '
    pass


def p_direct_declarator_6(p):
    'direct_declarator : direct_declarator LPAREN RPAREN '
    pass


# parameter-type-list:


def p_parameter_type_list_1(p):
    'parameter_type_list : parameter_list'
    pass


# parameter-list:


def p_parameter_list_1(p):
    'parameter_list : parameter_declaration'
    pass


def p_parameter_list_2(p):
    'parameter_list : parameter_list COMMA parameter_declaration'
    pass

# parameter-declaration:


def p_parameter_declaration_1(p):
    'parameter_declaration : declaration_specifiers declarator'
    pass


def p_parameter_declaration_2(p):
    'parameter_declaration : declaration_specifiers abstract_declarator_opt'
    pass

# identifier-list:


def p_identifier_list_1(p):
    'identifier_list : ID'
    pass


def p_identifier_list_2(p):
    'identifier_list : identifier_list COMMA ID'
    pass

# initializer:


def p_initializer_1(p):
    'initializer : assignment_expression'
    pass


def p_initializer_2(p):
    '''initializer : LBRACE initializer_list RBRACE
                   | LBRACE initializer_list COMMA RBRACE'''
    pass

# initializer-list:


def p_initializer_list_1(p):
    'initializer_list : initializer'
    pass


def p_initializer_list_2(p):
    'initializer_list : initializer_list COMMA initializer'
    pass

# type-name:


def p_type_name(p):
    'type_name : specifier_qualifier_list abstract_declarator_opt'
    pass


def p_abstract_declarator_opt_1(p):
    'abstract_declarator_opt : empty'
    pass


def p_abstract_declarator_opt_2(p):
    'abstract_declarator_opt : abstract_declarator'
    pass

# abstract-declarator:


def p_abstract_declarator_1(p):
    'abstract_declarator : direct_abstract_declarator'
    pass

# direct-abstract-declarator:


def p_direct_abstract_declarator_1(p):
    'direct_abstract_declarator : LPAREN abstract_declarator RPAREN'
    pass


def p_direct_abstract_declarator_2(p):
    'direct_abstract_declarator : direct_abstract_declarator LBRACKET constant_expression_opt RBRACKET'
    pass


def p_direct_abstract_declarator_3(p):
    'direct_abstract_declarator : LBRACKET constant_expression_opt RBRACKET'
    pass


def p_direct_abstract_declarator_4(p):
    'direct_abstract_declarator : direct_abstract_declarator LPAREN parameter_type_list_opt RPAREN'
    pass


def p_direct_abstract_declarator_5(p):
    'direct_abstract_declarator : LPAREN parameter_type_list_opt RPAREN'
    pass

# Optional fields in abstract declarators


def p_constant_expression_opt_1(p):
    'constant_expression_opt : empty'
    pass


def p_constant_expression_opt_2(p):
    'constant_expression_opt : constant_expression'
    pass


def p_parameter_type_list_opt_1(p):
    'parameter_type_list_opt : empty'
    pass


def p_parameter_type_list_opt_2(p):
    'parameter_type_list_opt : parameter_type_list'
    pass

# statement:


def p_statement(p):
    '''
    statement :  expression_statement
              | compound_statement
              | selection_statement
              | iteration_statement
              | jump_statement
              '''
    pass


# expression-statement:


def p_expression_statement(p):
    'expression_statement : expression_opt SEMI'
    pass

# compound-statement:


def p_compound_statement_1(p):
    'compound_statement : LBRACE declaration_list statement_list RBRACE'
    pass


def p_compound_statement_2(p):
    'compound_statement : LBRACE statement_list RBRACE'
    pass


def p_compound_statement_3(p):
    'compound_statement : LBRACE declaration_list RBRACE'
    pass


def p_compound_statement_4(p):
    'compound_statement : LBRACE RBRACE'
    pass

# statement-list:


def p_statement_list_1(p):
    'statement_list : statement'
    pass


def p_statement_list_2(p):
    'statement_list : statement_list statement'
    pass

# selection-statement


def p_selection_statement_1(p):
    'selection_statement : IF LPAREN expression RPAREN statement'
    global conditional_statement
    conditional_statement += 1
    pass


def p_selection_statement_2(p):
    'selection_statement : IF LPAREN expression RPAREN statement ELSE statement '
    global conditional_statement
    conditional_statement += 1
    pass


# iteration_statement:


def p_iteration_statement_1(p):
    'iteration_statement : WHILE LPAREN expression RPAREN statement'
    global loop
    loop += 1
    pass


def p_iteration_statement_2(p):
    'iteration_statement : FOR LPAREN expression_opt SEMI expression_opt SEMI expression_opt RPAREN statement '
    global loop
    loop += 1
    pass


def p_jump_statement_3(p):
    'jump_statement : BREAK SEMI'
    pass


def p_jump_statement_4(p):
    'jump_statement : RETURN expression_opt SEMI'
    pass


def p_expression_opt_1(p):
    'expression_opt : empty'
    pass


def p_expression_opt_2(p):
    'expression_opt : expression'
    pass

# expression:


def p_expression_1(p):
    'expression : assignment_expression'
    pass


def p_expression_2(p):
    'expression : expression COMMA assignment_expression'
    pass

# assigmenp_expression:


def p_assignment_expression_1(p):
    'assignment_expression : conditional_expression'
    pass


def p_assignment_expression_2(p):
    'assignment_expression : unary_expression assignment_operator assignment_expression'
    pass

# assignment_operator:


def p_assignment_operator(p):
    '''
    assignment_operator : EQUALS
                        '''
    pass

# conditional-expression


def p_conditional_expression_1(p):
    'conditional_expression : logical_or_expression'
    pass

# constant-expression


def p_constant_expression(p):
    'constant_expression : conditional_expression'
    pass

# logical-or-expression


def p_logical_or_expression_1(p):
    'logical_or_expression : logical_and_expression'
    pass


def p_logical_or_expression_2(p):
    'logical_or_expression : logical_or_expression LOR logical_and_expression'
    pass

# logical-and-expression


def p_logical_and_expression_1(p):
    'logical_and_expression : inclusive_or_expression'
    pass


def p_logical_and_expression_2(p):
    'logical_and_expression : logical_and_expression LAND inclusive_or_expression'
    pass

# inclusive-or-expression:


def p_inclusive_or_expression_1(p):
    'inclusive_or_expression : exclusive_or_expression'
    pass

# exclusive-or-expression:


def p_exclusive_or_expression_1(p):
    'exclusive_or_expression :  and_expression'
    pass


# AND-expression


def p_and_expression_1(p):
    'and_expression : equality_expression'
    pass


def p_and_expression_2(p):
    'and_expression : and_expression AND equality_expression'
    pass


# equality-expression:
def p_equality_expression_1(p):
    'equality_expression : relational_expression'
    pass


def p_equality_expression_2(p):
    'equality_expression : equality_expression EQ relational_expression'
    pass


# relational-expression:
def p_relational_expression_1(p):
    'relational_expression : shift_expression'
    pass


def p_relational_expression_2(p):
    'relational_expression : relational_expression LT shift_expression'
    pass


def p_relational_expression_3(p):
    'relational_expression : relational_expression GT shift_expression'
    pass


def p_relational_expression_4(p):
    'relational_expression : relational_expression LE shift_expression'
    pass


def p_relational_expression_5(p):
    'relational_expression : relational_expression GE shift_expression'
    pass

# shift-expression


def p_shift_expression_1(p):
    'shift_expression : additive_expression'
    pass


# additive-expression


def p_additive_expression_1(p):
    'additive_expression : multiplicative_expression'
    pass


def p_additive_expression_2(p):
    'additive_expression : additive_expression PLUS multiplicative_expression'
    pass


def p_additive_expression_3(p):
    'additive_expression : additive_expression MINUS multiplicative_expression'
    pass

# multiplicative-expression


def p_multiplicative_expression_1(p):
    'multiplicative_expression : cast_expression'
    pass


def p_multiplicative_expression_2(p):
    'multiplicative_expression : multiplicative_expression TIMES cast_expression'
    pass


def p_multiplicative_expression_3(p):
    'multiplicative_expression : multiplicative_expression DIVIDE cast_expression'
    pass


def p_multiplicative_expression_4(p):
    'multiplicative_expression : multiplicative_expression MOD cast_expression'
    pass

# cast-expression:


def p_cast_expression_1(p):
    'cast_expression : unary_expression'
    pass


def p_cast_expression_2(p):
    'cast_expression : LPAREN type_name RPAREN cast_expression'
    pass

# unary-expression:


def p_unary_expression_1(p):
    'unary_expression : postfix_expression'
    pass


def p_unary_expression_2(p):
    'unary_expression : PLUSPLUS unary_expression'
    pass


def p_unary_expression_3(p):
    'unary_expression : MINUSMINUS unary_expression'
    pass


def p_unary_expression_4(p):
    'unary_expression : unary_operator cast_expression'
    pass


# unary-operator


def p_unary_operator(p):
    '''unary_operator : AND
                    | TIMES
                    | PLUS
                    | MINUS
                    | LNOT '''
    pass

# postfix-expression:


def p_postfix_expression_1(p):
    'postfix_expression : primary_expression'
    pass


def p_postfix_expression_2(p):
    'postfix_expression : postfix_expression LBRACKET expression RBRACKET'
    pass


def p_postfix_expression_3(p):
    'postfix_expression : postfix_expression LPAREN argument_expression_list RPAREN'
    pass


def p_postfix_expression_4(p):
    'postfix_expression : postfix_expression LPAREN RPAREN'
    pass


def p_postfix_expression_5(p):
    'postfix_expression : postfix_expression PLUSPLUS'
    pass


def p_postfix_expression_6(p):
    'postfix_expression : postfix_expression MINUSMINUS'
    pass

# primary-expression:


def p_primary_expression(p):
    '''primary_expression :  ID
                        |  constant
                        |  SCONST
                        |  LPAREN expression RPAREN'''
    pass

# argument-expression-list:


def p_argument_expression_list(p):
    '''argument_expression_list :  assignment_expression
                              |  argument_expression_list COMMA assignment_expression'''
    pass

# constant:


def p_constant(p):
    '''constant : ICONST
               | FCONST
               | CCONST'''
    pass


def p_empty(p):
    'empty : '
    pass


def p_error(p):
    print("Whoa. We're hosed")

import profile
# Build the grammar
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')  # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)

    # count variable
    print('include %d: ' % include)
    print('declared_functions %d: ' % declared_functions)
    print('declared_variable %d: ' % declared_variable)
    print('conditional_statement %d: ' % conditional_statement)
    print('loop %d: ' % loop)
    print('called_functions %d: ' % called_functions)


