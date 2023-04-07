'''A continuacion vamos a describir que es un modulo.
Un modulo es un archivo de python con extencion .py o pyc (Python Compilado)
Este archivo puede contener dentro de su codigo, funciones, clases, variables, de todo
sirve para organizar y reutilizar el codigo (modularizacion y Reutilizacion)
'''
# en este modulo vamos a importar otro modulo.

import tkinter
# dentro de ese modulo "tkinter" que acabamos de importar, exiten muchas clases y funciones
# haciendolo de esa manera solo le estamos diciendo al interprete de python que vamos a utilizar ese modulo

# vamos a usar un objeto (instancia) de ese modulo
# para hacerlo debemos de mencionar el nombre del modulo
# seguido del nombre del objeto que queremos crear y
ventana = tkinter.Tk()

# si queremos crear otro objeto del mismo modulo
# debemos repetir lo mismo.

frameUno = tkinter.Frame()

# hemos creado dos objetos diferentes del mismo modulo

'''
para evitar tener que escribir cada vez mas el nombre del modulo
mas el objeto que queremos crear, hacemos lo siguiente:
'''

from tkinter import Tk

# de esta manera solo importamos la clase Tk del modulo tkinter

# para crear una instancia de esa clase, lo hacemos de la siguiente manera.

ventana2 = Tk()

# o si no, podemos importar todas las clases del modulo para evitarnos un monton de cosas.

from tkinter import *
# todos estos modulos son importados desde la ruta syspath


# clase 34 de python del canal pildoras informaticas.