import ply.lex as lex

# Lista de tokens (agregar IF)
tokens = ['RESERVED', 'FREE', 'INT', 'MAIN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 
          'PLUS', 'EQUALS', 'LEQ', 'FOR', 'IF', 'PRINTLN', 'NUMBER', 'STRING']

# Palabras reservadas
reserved = {
    'for': 'FOR',
    'if': 'IF',
    'int': 'INT',
    'main': 'MAIN',
    'System.out.println': 'PRINTLN',
}


# Reglas para los tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_EQUALS = r'='
t_LEQ = r'<='

# Reconocer numeros enteros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Reconocer cosas entre comillas
def t_STRING(t):
    r'\".*?\"'
    return t

# Identificadores y palabras reservadas
def t_FREE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'FREE')
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de caracteres ilegales
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Función de análisis léxico
def lexico(text):
    lexer.input(text)
    tokens_list = []
    line_info = []

    for token in lexer:
        tipo_palabra = ''
        if token.type == 'RESERVED':
            tipo_palabra = 'Palabra Reservada'
        elif token.type == 'INT':
            tipo_palabra = 'Tipo de Dato'
        elif token.type == 'MAIN':
            tipo_palabra = 'Reservada Main'
        elif token.type == 'FOR':
            tipo_palabra = 'Palabra Reservada'
        elif token.type == 'PRINTLN':
            tipo_palabra = 'Método Print'
        elif token.type == 'LPAREN':
            tipo_palabra = 'Paréntesis de Apertura'
        elif token.type == 'RPAREN':
            tipo_palabra = 'Paréntesis de Cierre'
        elif token.type == 'LBRACE':
            tipo_palabra = 'Llave de Apertura'
        elif token.type == 'RBRACE':
            tipo_palabra = 'Llave de Cierre'
        elif token.type == 'SEMICOLON':
            tipo_palabra = 'Punto y Coma'
        elif token.type == 'PLUS':
            tipo_palabra = 'Operador Suma'
        elif token.type == 'EQUALS':
            tipo_palabra = 'Operador Asignación'
        elif token.type == 'LEQ':
            tipo_palabra = 'Operador Menor o Igual'
        elif token.type == 'NUMBER':
            tipo_palabra = 'Número'
        elif token.type == 'STRING':
            tipo_palabra = 'Cadena'
        else:
            tipo_palabra = 'Identificador'

        tokens_list.append((token.lineno, token.type, token.value))
        line_info.append((token.lineno, tipo_palabra, token.value))

    return tokens_list, line_info
