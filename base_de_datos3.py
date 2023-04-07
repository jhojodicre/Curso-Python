#borrar un registro de la base de datos
#actualizar un valor de un campo de la base de datos

import psycopg2 # este es un modulo conocido como conector a traves de python y posgre


# conexion a la base de datos.
conexion1 = psycopg2.connect(database="bd1", user="postgres", password="jh0j0d1cr3")
cursor1=conexion1.cursor()

#borramos la primera fila de la base de datos articulos
cursor1.execute("delete from articulos where codigo=1")

#actualizamos un valor de la base de datos.
cursor1.execute("update articulos set precio=50 where codigo=3")

# hacemos el commit,
conexion1.commit()
cursor1.execute("select codigo, descripcion, precio from articulos")
#luego imprimimos cada elemento de la tupla
for elemento in cursor1:
    print(elemento)

# cerramos la conexion.
conexion1.close()