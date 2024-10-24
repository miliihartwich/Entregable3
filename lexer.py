import ply.lex as lex

# Palabras clave traducidas
tokens = (
    'TRAEME', 'TODO', 'DE_LA_TABLA', 'DONDE', 'IDENTIFIER', 'EN_ESTO', 'LPAREN', 'RPAREN'
)

# Diccionario de palabras clave y su mapeo a SQL
t_TRAEME = r'TRAEME'
t_TODO = r'TODO'
t_DE_LA_TABLA = r'DE LA TABLA'
t_DONDE = r'DONDE'
t_EN_ESTO = r'EN ESTO'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Identificadores (nombres de tablas, campos, etc.)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Definir cómo manejar errores léxicos
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Inicializar el lexer
lexer = lex.lex()
