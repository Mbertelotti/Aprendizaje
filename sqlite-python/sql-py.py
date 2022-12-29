import sqlite3
import pandas as pd

conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute("""create table prueba (
                                ID integer primary key autoincrement,
                                descripcion text,
                                precio real
                        )""")

    
except:
    pass
tabla=[["naranjas", 23.50],["peras", 34],["bananas", 25]]
for linea in tabla:
    conexion.execute("insert into prueba(descripcion,precio) values (?,?)", linea)
conexion.commit()


# resultado=conexion.execute("""
# select *
# from prueba
# """)
# for x in resultado:
#     print(x)


df = pd.read_sql_query("SELECT * FROM prueba", conexion)
print(df)

conexion.close()
