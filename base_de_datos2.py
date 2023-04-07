# consultamos una tabla

import psycopg2 # este es un modulo conocido como conector a traves de python y posgre


# conexion a la base de datos.
conexion1 = psycopg2.connect(database="bd1", user="postgres", password="jh0j0d1cr3")
cursor1=conexion1.cursor()


cursor1.execute("select codigo, descripcion, precio from articulos")
# al ejecutar este codigo la base de datos nos devuelve una tupla entre parentesis

#luego imprimimos cada elemento de la tupla
for elemento in cursor1:
    print(elemento)

# cerramos la conexion.
conexion1.close()