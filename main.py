# #Conceptos Principales de Python.
# #Propiedad de la clase
# #Metodos, o funciones de la clase.
#
# # Crear una Clase:
#       En la siguiente clase que crearemos  vamos a declarar propiedades fijas.
class Carro():
#   Propiedad de la clase
#   creamos cuatro propiedades de la clase carro.
    LargoChasis=250
    Ruedas=4
    AmchoChasis=40
    enmarcha=False
#
#     #Metodos, o funciones de la clase.
    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if(self.enmarcha):
            return "El carro se encuentra en marcha"
        else:
            return "El coche esta detenido."

    def parar(self):
        self.enmarcha=False

#Creamos Un objeto de la clase Carro, a esto se le llama "Instancia"
# Instancia: es cear un objeto de una clase definida.
carro1=Carro()

# en la siguiente codigo, accedemos al valor de la propiedad LargoChasis
print("El largo del coche es: ", carro1.LargoChasis)

# en el siguiente codigo aacedemos a la propiedad AmchoChasis
print("eL COCHE TIENE", carro1.AmchoChasis, "de ancho")

# en el siguiente codigo accedemos a una funcion de la clase llamada metodo.
# metodo: es una funcion definida en una clase.
print(carro1.estado())