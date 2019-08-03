class Nodo():
    def __init__(self,elemento):
        self._elemento = elemento
        self._pSig = None
        self._pAnt = None

    def getElemento(self):
        return self._elemento

class List():
    def __init__(self):
        self._primero = None
        self._ultimo = None

    def insert(self,elemento):
        print("insert")

    def delete(self):
        print("delete")

class ListDE(List):
    def insert(self,elemento):
        nuevo = Nodo(elemento)
        if self._primero == None:
            self._primero = self._ultimo = nuevo
        elif self._primero == self._ultimo:
            self._primero._pSig = nuevo
            self._ultimo = nuevo
            self._ultimo._pAnt = self._primero
        else:
            self._ultimo._pSig = nuevo
            nuevo._pAnt = self._ultimo
            self._ultimo = nuevo

    def delete(self):
        if self._primero != None and self._primero != self._ultimo:
            nodoAux = self._ultimo
            self._ultimo = nodoAux._pAnt
            self._ultimo._pSig = None
            nodoAux._pAnt = None
            del nodoAux
        elif self._primero == self._ultimo:
            self._primero = None
            self._ultimo = None
            print ("El ultimo elemento de la lista ha sido eliminado")

    def print(self):
        nodoAux = self._primero
        while(nodoAux != self._ultimo):
            print (nodoAux.getElemento() , "-> " , end="")
            nodoAux = nodoAux._pSig
        print (nodoAux.getElemento())

class ListCDE(List):
    def insert(self,elemento):
        nuevo = Nodo(elemento)
        if self._primero == None:
            self._primero = self._ultimo = nuevo
        elif self._primero == self._ultimo:
            self._primero._pSig = nuevo
            self._ultimo._pAnt = nuevo
            self._ultimo = nuevo
            self._ultimo._pAnt = self._primero
            self._ultimo._pSig = self._primero
        else:
            self._ultimo._pSig = nuevo
            self._primero._pAnt = nuevo
            nuevo._pAnt = self._ultimo
            nuevo._pSig = self._primero
            self._ultimo = nuevo

    def delete(self):
        if self._primero != None and self._primero != self._ultimo:
            nodoAux = self._ultimo
            self._ultimo = nodoAux._pAnt
            self._ultimo._pSig = self._primero
            self._primero._pAnt = self._ultimo
            nodoAux._pAnt = None
            nodoAux._pSig = None
            del nodoAux
        elif self._primero == self._ultimo:
            self._primero = None
            self._ultimo = None
            print ("El ultimo elemento de la lista ha sido eliminado")

    def print(self):
        nodoAux = self._primero
        while(nodoAux != self._ultimo):
            print (nodoAux.getElemento() , "-> " , end="")
            nodoAux = nodoAux._pSig
        print (nodoAux.getElemento())

class Queue(List):
    def insert(self,elemento):
        nuevo = Nodo(elemento)
        if self._primero == None:
            self._primero = self._ultimo = nuevo
        elif self._primero == self._ultimo:
            self._ultimo = nuevo
            self._ultimo._pSig = self._primero
        else:
            nuevo._pSig = self._ultimo
            self._ultimo = nuevo

    def delete(self):
        if self._primero != None and self._primero != self._ultimo:
            nodoAux = self._ultimo
            while nodoAux._pSig != self._primero:
                nodoAux = nodoAux._pSig
            nodoAux2 = self._primero
            self._primero = nodoAux
            self._primero._pSig = None
            del nodoAux2
        elif self._primero == self._ultimo:
            self._primero = None
            self._ultimo = None
            print ("El ultimo elemento de la lista ha sido eliminado")

    def print(self):
        nodoAux = self._ultimo
        while(nodoAux != self._primero):
            print (nodoAux.getElemento() , "-> " , end="")
            nodoAux = nodoAux._pSig
        print (nodoAux.getElemento())

class Stack(List):
    def insert(self,elemento):
        nuevo = Nodo(elemento)
        if self._primero == None:
            self._primero = self._ultimo = nuevo
        elif self._primero == self._ultimo:
            self._ultimo = nuevo
            self._ultimo._pSig = self._primero
        else:
            nuevo._pSig = self._ultimo
            self._ultimo = nuevo

    def delete(self):
        if self._primero != None and self._primero != self._ultimo:
            nodoAux = self._ultimo
            self._ultimo = self._ultimo._pSig
            del nodoAux
        elif self._primero == self._ultimo:
            self._primero = None
            self._ultimo = None
            print ("El ultimo elemento de la lista ha sido eliminado")

    def print(self):
        nodoAux = self._ultimo
        while(nodoAux != self._primero):
            print (nodoAux.getElemento() , "-> " , end="")
            nodoAux = nodoAux._pSig
        print (nodoAux.getElemento())

listDobleE = ListDE()
listDobleE.insert([1,2])
listDobleE.insert([1,2])
listDobleE.insert([21,2])
listDobleE.insert([31,2])

listDobleE.print()
listDobleE.delete()
listDobleE.print()

pila = Stack()
pila.insert([1,2])
pila.insert([3,2])
pila.insert([21,2])
pila.insert([31,2])

pila.print()
pila.delete()
pila.print()


cola = Queue()
cola.insert([1,2])
cola.insert([3,2])
cola.insert([21,2])
cola.insert([31,2])

cola.print()
cola.delete()
cola.print()
cola.delete()
cola.print()
