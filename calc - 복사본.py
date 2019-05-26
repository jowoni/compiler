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

##################################################################################

import sys
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

# from calclex import tokens

# translation-unit:


def p_translation_unip_1(p):
    'translation_unit : external_declaration'
    p[0] = p[1]


def p_translation_unip_2(p):
    'translation_unit : translation_unit external_declaration'
    p[1].extend(p[2])
    p[0] = p[1]

# external-declaration:


def p_external_declaration_1(p):
    'external_declaration : function_definition'
    p[0] = [p[1]]


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
    'declaration : declaration_specifiers inip_declarator_list SEMI'
    pass


def p_declaration_2(p):
    'declaration : declaration_specifiers SEMI'
    pass

# declaration-list:


def p_declaration_lisp_1(p):
    'declaration_list : declaration'
    pass


def p_declaration_lisp_2(p):
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


def p_inip_declarator_lisp_1(p):
    'inip_declarator_list : inip_declarator'
    pass


def p_inip_declarator_lisp_2(p):
    'inip_declarator_list : inip_declarator_list COMMA inip_declarator'
    pass

# init-declarator


def p_inip_declarator_1(p):
    'inip_declarator : declarator'
    pass


def p_inip_declarator_2(p):
    'inip_declarator : declarator EQUALS initializer'
    pass

# specifier-qualifier-list:


def p_specifier_qualifier_lisp_1(p):
    'specifier_qualifier_list : type_specifier specifier_qualifier_list'
    pass


def p_specifier_qualifier_lisp_2(p):
    'specifier_qualifier_list : type_specifier'
    pass


# declarator:


def p_declarator_1(p):
    'declarator : direcp_declarator'
    pass

# direct-declarator:


def p_direcp_declarator_1(p):
    'direcp_declarator : ID'
    pass


def p_direcp_declarator_2(p):
    'direcp_declarator : LPAREN declarator RPAREN'
    pass


def p_direcp_declarator_3(p):
    'direcp_declarator : direcp_declarator LBRACKET constanp_expression_opt RBRACKET'
    pass


def p_direcp_declarator_4(p):
    'direcp_declarator : direcp_declarator LPAREN parameter_type_list RPAREN '
    pass


def p_direcp_declarator_5(p):
    'direcp_declarator : direcp_declarator LPAREN identifier_list RPAREN '
    pass


def p_direcp_declarator_6(p):
    'direcp_declarator : direcp_declarator LPAREN RPAREN '
    pass


# parameter-type-list:


def p_parameter_type_lisp_1(p):
    'parameter_type_list : parameter_list'
    pass


# parameter-list:


def p_parameter_lisp_1(p):
    'parameter_list : parameter_declaration'
    pass


def p_parameter_lisp_2(p):
    'parameter_list : parameter_list COMMA parameter_declaration'
    pass

# parameter-declaration:


def p_parameter_declaration_1(p):
    'parameter_declaration : declaration_specifiers declarator'
    pass


def p_parameter_declaration_2(p):
    'parameter_declaration : declaration_specifiers abstracp_declarator_opt'
    pass

# identifier-list:


def p_identifier_lisp_1(p):
    'identifier_list : ID'
    pass


def p_identifier_lisp_2(p):
    'identifier_list : identifier_list COMMA ID'
    pass

# initializer:


def p_initializer_1(p):
    'initializer : assignmenp_expression'
    pass


def p_initializer_2(p):
    '''initializer : LBRACE initializer_list RBRACE
                   | LBRACE initializer_list COMMA RBRACE'''
    pass

# initializer-list:


def p_initializer_lisp_1(p):
    'initializer_list : initializer'
    pass


def p_initializer_lisp_2(p):
    'initializer_list : initializer_list COMMA initializer'
    pass

# type-name:


def p_type_name(p):
    'type_name : specifier_qualifier_list abstracp_declarator_opt'
    pass


def p_abstracp_declarator_opp_1(p):
    'abstracp_declarator_opt : empty'
    pass


def p_abstracp_declarator_opp_2(p):
    'abstracp_declarator_opt : abstracp_declarator'
    pass

# abstract-declarator:


def p_abstracp_declarator_1(p):
    'abstracp_declarator : direcp_abstracp_declarator'
    pass

# direct-abstract-declarator:


def p_direcp_abstracp_declarator_1(p):
    'direcp_abstracp_declarator : LPAREN abstracp_declarator RPAREN'
    pass


def p_direcp_abstracp_declarator_2(p):
    'direcp_abstracp_declarator : direcp_abstracp_declarator LBRACKET constanp_expression_opt RBRACKET'
    pass


def p_direcp_abstracp_declarator_3(p):
    'direcp_abstracp_declarator : LBRACKET constanp_expression_opt RBRACKET'
    pass


def p_direcp_abstracp_declarator_4(p):
    'direcp_abstracp_declarator : direcp_abstracp_declarator LPAREN parameter_type_lisp_opt RPAREN'
    pass


def p_direcp_abstracp_declarator_5(p):
    'direcp_abstracp_declarator : LPAREN parameter_type_lisp_opt RPAREN'
    pass

# Optional fields in abstract declarators


def p_constanp_expression_opp_1(p):
    'constanp_expression_opt : empty'
    pass


def p_constanp_expression_opp_2(p):
    'constanp_expression_opt : constanp_expression'
    pass


def p_parameter_type_lisp_opp_1(p):
    'parameter_type_lisp_opt : empty'
    pass


def p_parameter_type_lisp_opp_2(p):
    'parameter_type_lisp_opt : parameter_type_list'
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


def p_compound_statemenp_1(p):
    'compound_statement : LBRACE declaration_list statemenp_list RBRACE'
    pass


def p_compound_statemenp_2(p):
    'compound_statement : LBRACE statemenp_list RBRACE'
    pass


def p_compound_statemenp_3(p):
    'compound_statement : LBRACE declaration_list RBRACE'
    pass


def p_compound_statemenp_4(p):
    'compound_statement : LBRACE RBRACE'
    pass

# statement-list:


def p_statemenp_lisp_1(p):
    'statemenp_list : statement'
    pass


def p_statemenp_lisp_2(p):
    'statemenp_list : statemenp_list statement'
    pass

# selection-statement


def p_selection_statemenp_1(p):
    'selection_statement : IF LPAREN expression RPAREN statement'
    pass


def p_selection_statemenp_2(p):
    'selection_statement : IF LPAREN expression RPAREN statement ELSE statement '
    pass


# iteration_statement:


def p_iteration_statemenp_1(p):
    'iteration_statement : WHILE LPAREN expression RPAREN statement'
    pass


def p_iteration_statemenp_2(p):
    'iteration_statement : FOR LPAREN expression_opt SEMI expression_opt SEMI expression_opt RPAREN statement '
    pass


def p_jump_statemenp_3(p):
    'jump_statement : BREAK SEMI'
    pass


def p_jump_statemenp_4(p):
    'jump_statement : RETURN expression_opt SEMI'
    pass


def p_expression_opp_1(p):
    'expression_opt : empty'
    pass


def p_expression_opp_2(p):
    'expression_opt : expression'
    pass

# expression:


def p_expression_1(p):
    'expression : assignmenp_expression'
    pass


def p_expression_2(p):
    'expression : expression COMMA assignmenp_expression'
    pass

# assigmenp_expression:


def p_assignmenp_expression_1(p):
    'assignmenp_expression : conditional_expression'
    pass


def p_assignmenp_expression_2(p):
    'assignmenp_expression : unary_expression assignmenp_operator assignmenp_expression'
    pass

# assignmenp_operator:


def p_assignmenp_operator(p):
    '''
    assignmenp_operator : EQUALS
                        '''
    pass

# conditional-expression


def p_conditional_expression_1(p):
    'conditional_expression : logical_or_expression'
    pass

# constant-expression


def p_constanp_expression(p):
    'constanp_expression : conditional_expression'
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
    'relational_expression : shifp_expression'
    pass


def p_relational_expression_2(p):
    'relational_expression : relational_expression LT shifp_expression'
    pass


def p_relational_expression_3(p):
    'relational_expression : relational_expression GT shifp_expression'
    pass


def p_relational_expression_4(p):
    'relational_expression : relational_expression LE shifp_expression'
    pass


def p_relational_expression_5(p):
    'relational_expression : relational_expression GE shifp_expression'
    pass

# shift-expression


def p_shifp_expression_1(p):
    'shifp_expression : additive_expression'
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
    'multiplicative_expression : casp_expression'
    pass


def p_multiplicative_expression_2(p):
    'multiplicative_expression : multiplicative_expression TIMES casp_expression'
    pass


def p_multiplicative_expression_3(p):
    'multiplicative_expression : multiplicative_expression DIVIDE casp_expression'
    pass


def p_multiplicative_expression_4(p):
    'multiplicative_expression : multiplicative_expression MOD casp_expression'
    pass

# cast-expression:


def p_casp_expression_1(p):
    'casp_expression : unary_expression'
    pass


def p_casp_expression_2(p):
    'casp_expression : LPAREN type_name RPAREN casp_expression'
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
    'unary_expression : unary_operator casp_expression'
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
    'postfix_expression : postfix_expression LPAREN argumenp_expression_list RPAREN'
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


def p_argumenp_expression_list(p):
    '''argumenp_expression_list :  assignmenp_expression
                              |  argumenp_expression_list COMMA assignmenp_expression'''
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

