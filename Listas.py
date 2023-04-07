import colorama
from colorama import Style
from colorama import Fore
print(Fore.CYAN+ Style.DIM+'''
List:
    Una lista es un tipo de estructura de datos en python y la creamos mediante Corchetes.
    una lista esta compuestas de elementos.
    el primer elemento de la lista es 0
    el segundo elemento de la lista es 1
    el indice de la lista es el numero de posicion donde se encuentra cada elemento.
    ejemplo:
        myList=[1, 2, 3, 4]

'''+ Style.RESET_ALL)
# crear una lista en pyhton
newList = []

def crearLista():
    myList=""
    while myList != "myList":
        myList = input(Fore.GREEN+Style.BRIGHT+"Insertar el nombre de myList a continuacion: "+Style.RESET_ALL)
    print("la variable myList se ha creado")
def insertarList(newElemento):
    global newList
    print('''
    con el metodo myList.append() agregamos un elemento al final de la lista
    
    Insertar un elemento a una lista: 
    ''')
    newList.append(newElemento)
    print(newList)
print("Creamos una lista en python llamada myList entre corchetes")
print("ejemplo: myList = [numeros, cadenas, o listas]")

crearLista()
elemento=input()
insertarList(elemento)

# exec("%s = %l" % (newLista,[1]))
# print(type(a))
# print(newLista, eval(newLista), type(eval(newLista)))
 # esta es una lista que contiene 4 elementos
print(" ")
print("imprimimos un elemento de la lista a traves de un indice")
# print(mylist[2])
print(" ")
print(" ")
print(" Metodos de una Lista")
print('''       myList.append() = add an elements at the end of the list
                myList.insert() = adds an element at the specified position.
                myList.index()  = returns the index of the first occurrence of specified value
                myList.remove() = removes the first item with the specified value
                myList.pop()    = removes the element using index it's value.
                myList.clear()  = removes all the elements from the list
                myList.copy()   = returns a copy of de list.
                myList.count()  = Returns the numbers of times an elements appears in the list
                myList.sort()   = Sorts the list.
                myList.extend() = add the element of a list, to the end of the current list
                myList.reverse()= reverses the order of the list.
                ''')
print("el elemento impreso en la lista es el tercer elemento. ya que el primero tiene indice 0")
print("Agregamos Un elemento al final de la lista  ")
print("mylist.append(8)")
# mylist.append(8)
print("Insertamos un elemento en la segunda posicion ")
print(" mylist.insert(2,9)")
# mylist.insert(2,9)
print(" ")
print(" ")
print(" Indice de Una Lista")
print("     myList.index(Nombre_del_elemento_de_la_lista)")
print("     Esta Funcion nos devuelve el numero del indice del elemento de una lista")
print("         Imprimimos una lista y SABER el numero de indice del elemento")
print("         Creamos una variable para guardar el numero y luego lo imprimimos")
# print(mylist)

# indice=mylist.index(2)
# print(indice)
print(" ")
print(" *********************************************")
print(" Eliminar Elemento")
print("     myList.remove(8)")
print("     Esta Funcion Elimina un elemento de la lista, para ello indicamos el nombre del elemento")
print("     mas no el indice del elemnto")
# print(mylist)
# mylist.remove(8)
# print(mylist)
print(" ")
print(" *********************************************")
print(" ")
print(" Eliminar el Ultimo Elemento")
print("     myList.pop()")
print("     Esta funcion Elimina el ultimo elemento")
# mylist.pop()
print(" ")
print(" *********************************************")
print(" ")

