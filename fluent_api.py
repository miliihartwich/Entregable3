# Fluent API para construir consultas en USQL
class FluentUSQL:
    def __init__(self):
        self.query = ""

    def traeme(self):
        self.query += "TRAEME "
        return self

    def todo(self):
        self.query += "TODO "
        return self

    def de_la_tabla(self, table):
        self.query += f"DE LA TABLA {table} "
        return self

    def donde(self, condition):
        self.query += f"DONDE {condition} "
        return self

    def setea(self, column, value):
        self.query += f"SETEA {column} = {value} "
        return self

    def mete_en(self, table, columns):
        cols = ", ".join(columns)
        self.query += f"METE EN {table} ({cols}) "
        return self

    def los_valores(self, values):
        vals = ", ".join([f"'{v}'" if isinstance(v, str) else str(v) for v in values])
        self.query += f"LOS VALORES ({vals}) "
        return self

    def build(self):
        return self.query.strip()

# Ejemplo de uso de la Fluent API
query = FluentUSQL() \
    .traeme() \
    .todo() \
    .de_la_tabla("users") \
    .donde("age > 18") \
    .build()

print(query)  # TRAEME TODO DE LA TABLA users DONDE age > 18

# Otro ejemplo con INSERT
insert_query = FluentUSQL() \
    .mete_en("users", ["name", "age"]) \
    .los_valores(["Juan", 25]) \
    .build()

print(insert_query)  # METE EN users (name, age) LOS VALORES ('Juan', 25)
