'''
Paquetes:
    Video: 35
    Lista de reproduccion: Curso Python desde 0
    Canal: Pildoras informaticas

    Definicion:
        Un paquete es un directorio, es decir, una carpeta que contiene Modulos de Python
        sirve para agrupar y organizar archivos de python en un solo lugar, asi como tambien,
        nos sirve para que el interprete de python pueda reconocer esa carpeta o ruta creada.
        para esto, tenemos que crear un archivo con extension ".py" llamado __init__.py
        Y de esta manera, en esa carpeta o directorio creado, podemos guardas archivos python.
    Ejemplo:
        Como Lo utilizamos:
        siempre vamos a tener una carpeta principal donde creamos los proyectos de Python:
        supongamos que esa carpeta principal se llama python y dentro de esa carpeta tenemos
        el archivo main, ahora lo que haremos es crar otra carpeta dentro de la carpeta python.
        en esta nueva carpeta agregamos un nuevo archivo llamado __init__.py ademos de los
        modulos que queremos crear y dentro de nuestro archivo main invocamos a esos archivos
        de la siguiente manera:

                from carpetaPaqueta.moduloPaquete import funcion_clase

                descripcion:
                    carpetaPaquete es el nombre de la carpeta creada dentro de la carpeta Pthon
                    moduloPaquete es el nombre de lal modulo dentro de esa carpeta.
                    funcion clase es el nombre de la funcion o la clase que queremos importar.
'''