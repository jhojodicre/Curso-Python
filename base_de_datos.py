import psycopg2 # este es un modulo conocido como conector a traves de python y posgre


# conexion a la base de datos.
conexion1 = psycopg2.connect(database="bd1", user="postgres", password="jh0j0d1cr3")
cursor1=conexion1.cursor()

# comando que queremos ejecutar en la base de datos.
sql="insert into articulos(descripcion, precio) values (%s,%s)"
# datos que queremos insertar
datos=("naranjas", 23.50)
# insertamos los datos.
cursor1.execute(sql, datos)

# se repiten los mismos pasos.
datos=("peras", 34)
cursor1.execute(sql, datos)
datos=("bananas", 25)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()

# una vez ejecutado el programa podemos hacer una consulta desde el administrador de postgre
# a travez del query tools con el siguiente codigo
# select codigo descripcion,precio from articulos