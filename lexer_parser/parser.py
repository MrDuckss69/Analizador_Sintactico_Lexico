import ply.yacc as yacc
from lexer_parser.lexer import tokens

# Definir la gramática
# Regla de inicio
def p_program(p):
    '''program : INT MAIN LPAREN RPAREN LBRACE declarations RBRACE '''
    p[0] = 'Programa correcto'

# Definir declaraciones (puedes agregar más reglas según lo necesites)
def p_declarations(p):
    '''declarations : declaration
                    | declaration declarations'''
    p[0] = p[1]

# Definir declaración de variables
def p_declaration(p):
    '''declaration : INT FREE SEMICOLON'''
    p[0] = f'Declaración: {p[2]}'

# Manejo de errores
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
        raise SyntaxError(f"Error de sintaxis en la línea {p.lineno}: '{p.value}'")
    else:
        print("Error de sintaxis en EOF")
        raise SyntaxError("Error de sintaxis en EOF")

# Construir el parser
parser = yacc.yacc()

def sintactico(text):
    try:
        result = parser.parse(text)
        return result, None
    except SyntaxError as e:
        return None, str(e)
