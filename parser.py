import ply.yacc as yacc
from lexer import tokens

# Diccionario de traducción inversa de SQL a USQL
sql_to_usql = {
    "SELECT": "TRAEME",
    "*": "TODO",
    "FROM": "DE LA TABLA",
    "WHERE": "DONDE",
    "GROUP BY": "AGRUPANDO POR",
    "JOIN": "MEZCLANDO",
    "ON": "EN",
    "DISTINCT": "LOS DISTINTOS",
    "COUNT": "CONTANDO",
    "INSERT INTO": "METE EN",
    "VALUES": "LOS VALORES",
    "UPDATE": "ACTUALIZA",
    "SET": "SETEA",
    "DELETE FROM": "BORRA DE LA",
    "ORDER BY": "ORDENA POR",
    "LIMIT": "COMO MUCHO",
    "HAVING": "WHERE DEL GROUP BY",
    "EXISTS": "EXISTE",
    "IN": "EN ESTO:",
    "BETWEEN": "ENTRE",
    "LIKE": "PARECIDO A",
    "IS NULL": "ES NULO",
    "ALTER TABLE": "CAMBIA LA TABLA",
    "ADD COLUMN": "AGREGA LA COLUMNA",
    "DROP COLUMN": "ELIMINA LA COLUMNA",
    "CREATE TABLE": "CREA LA TABLA",
    "DROP TABLE": "TIRA LA TABLA",
    "DEFAULT": "POR DEFECTO",
    "UNIQUE": "UNICO",
    "PRIMARY KEY": "CLAVE PRIMA",
    "FOREIGN KEY": "CLAVE REFERENTE",
    "NOT NULL": "NO NULO",
    "CAST": "TRANSFORMA A"
}

# Diccionario para traducir de USQL a SQL
usql_to_sql = {v: k for k, v in sql_to_usql.items()}

# Función para traducir USQL a SQL
def usql_to_sql_translate(usql_query):
    for usql_keyword, sql_keyword in usql_to_sql.items():
        usql_query = usql_query.replace(usql_keyword, sql_keyword)
    return usql_query

# Función para traducir SQL a USQL
def sql_to_usql_translate(sql_query):
    for sql_keyword, usql_keyword in sql_to_usql.items():
        sql_query = sql_query.replace(sql_keyword, usql_keyword)
    return sql_query

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

# Función que maneja la traducción bidireccional
def translate(query, direction='USQL_to_SQL'):
    if direction == 'USQL_to_SQL':
        return usql_to_sql_translate(query)
    elif direction == 'SQL_to_USQL':
        return sql_to_usql_translate(query)
    else:
        raise ValueError("Dirección no válida. Use 'USQL_to_SQL' o 'SQL_to_USQL'.")
    
#Verificación
# Traducción de USQL a SQL
usql_query = "TRAEME TODO DE LA TABLA users DONDE age EN ESTO (18)"
sql_result = translate(usql_query, direction='USQL_to_SQL')
print(sql_result)  # SELECT * FROM users WHERE age IN (18)

# Traducción de SQL a USQL
sql_query = "SELECT * FROM users WHERE age IN (18)"
usql_result = translate(sql_query, direction='SQL_to_USQL')
print(usql_result)  # TRAEME TODO DE LA TABLA users DONDE age EN ESTO (18)
