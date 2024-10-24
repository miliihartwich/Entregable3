import ply.yacc as yacc
from lexer import tokens

# Definición de las reglas de producción de SQL
def p_query_select(p):
    '''query : TRAEME TODO DE_LA_TABLA table_name DONDE condition'''
    p[0] = f"SELECT * FROM {p[4]} WHERE {p[6]}"

def p_table_name(p):
    '''table_name : IDENTIFIER'''
    p[0] = p[1]

def p_condition(p):
    '''condition : IDENTIFIER EN_ESTO list_values'''
    p[0] = f"{p[1]} IN {p[4]}"

def p_list_values(p):
    '''list_values : LPAREN IDENTIFIER RPAREN'''
    p[0] = f"({p[2]})"

def p_error(p):
    print(f"Error de sintaxis: {p.value}")

# Construir el parser
parser = yacc.yacc()
