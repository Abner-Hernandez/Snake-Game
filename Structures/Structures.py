import subprocess
class Nodo():
    def __init__(self,elemento):
        self._elemento = elemento
        self._pSig = None
        self._pAnt = None

    def getElemento(self):
        return self._elemento

    def setElemento(self, data, num):
        if num == 0:
            self._elemento[0] = data
        elif num == 1:
            self._elemento[1] = data

class List():
    def __init__(self):
        self._primero = None
        self._ultimo = None

    def insert(self,elemento):
        print("Implement Insert Method")

    def delete(self):
        print("Implement delete Method")

    def graphList(self):
        print("Implement graph Method")

    def guardarArchivo(self,cadena, name):
        file = open(name+".dot", "w")
        file.write(cadena)
        file.close()
        subprocess.run("dot -Tpng "+name+".dot -o "+name+".png", shell=True)
        subprocess.run(name +".png", shell=True)

class ListDE(List):
    def insert(self,elemento):
        nuevo = Nodo(elemento)
        if self._primero is None:
            self._primero = self._ultimo = nuevo
        elif self._primero == self._ultimo:
            self._primero._pSig = nuevo
            self._ultimo = nuevo
            self._ultimo._pAnt = self._primero
        else:
            self._ultimo._pSig = nuevo
            nuevo._pAnt = self._ultimo
            self._ultimo = nuevo

    def insertFirst(self, elemento):
        if self._primero is not None:
            nuevo = Nodo(elemento)
            nuevo._pSig = self._primero
            self._primero._pAnt = nuevo
            self._primero = nuevo
        else:
            nuevo = Nodo(elemento)
            self._primero = self._ultimo = nuevo
        
    def delete(self):
        nodoAux = self._primero
        while nodoAux is not None:
            print(nodoAux.getElemento())
            nodoAux = nodoAux._pSig
        if self._primero is not None and self._primero != self._ultimo:
            nodoAux = self._ultimo
            self._ultimo = nodoAux._pAnt
            self._ultimo._pSig = None
            nodoAux._pAnt = None
            del nodoAux
        elif self._primero == self._ultimo and self._primero is not None:
            self._primero = None
            self._ultimo = None
            #print ("El ultimo elemento de la lista ha sido eliminado")

    def getLastData(self):
        if self._primero is not None:
            if self._primero is not None and self._primero != self._ultimo:
                nodoAux = self._ultimo
                self._ultimo = nodoAux._pAnt
                self._ultimo._pSig = None
                nodoAux._pAnt = None
                dataReturn = nodoAux.getElemento()
                del nodoAux
                return dataReturn
            elif self._primero == self._ultimo and self._primero is not None:
                dataReturn = self._primero.getElemento()
                self._primero = None
                self._ultimo = None
                #print ("El ultimo elemento de la lista ha sido eliminado")
                return  dataReturn
            
    def buscar(self, elemento):
        nodoAux = self._primero._pSig
        while nodoAux is not None:
            if nodoAux.getElemento() == elemento:
                return True
            nodoAux = nodoAux._pSig
        return False

    def graphList(self):
        cont = 0
        txtArchivo ="";
        txtArchivo += "digraph Mass{\n";
        txtArchivo += "subgraph cluster_0{\n";
        txtArchivo += "SnakPositions[label = \"SNAKE REPORT\" color = blue style= filled fontcolor = white shape = box];\n";
        nodoAux = self._primero

        while nodoAux is not None:
            txtArchivo += "node[shape = record label= "
            txtArchivo += "\""
            txtArchivo += "<A0> |"
            txtArchivo += "(" + str(nodoAux.getElemento()[1]) + "," + str(nodoAux.getElemento()[0]) + ")" +" \n"
            txtArchivo += "| <A1>"
            txtArchivo += "\""
            txtArchivo += "]"+ "nodo" + str(cont) +";\n"
            cont += 1
            nodoAux = nodoAux._pSig

        nodoAux = self._primero
        cont = 0
        txtArchivo +=  "nodo" + str(cont) + ":A1" +" -> "+ "nodo" + str(cont+1) + ":A0" + "\n"
        nodoAux = nodoAux._pSig
        while nodoAux is not None:
            cont +=1
            txtArchivo += "nodo" + str(cont) + ":A0" +" -> "+ "nodo" + str(cont-1) + ":A1" +"\n"
            if nodoAux != self._ultimo:
                txtArchivo += "nodo" + str(cont) + ":A1" +" -> "+ "nodo" + str(cont+1) + ":A0" + "\n"
            nodoAux = nodoAux._pSig

        txtArchivo += "color = blue \n}"

        txtArchivo += "\n} "
        self.guardarArchivo(txtArchivo, "listDE")

class ListCDE(List):
    def insert(self,elemento):
        nuevo = Nodo(elemento)
        if self._primero is None:
            self._primero = self._ultimo = nuevo
            self._ultimo._pSig = self._primero
            self._ultimo._pAnt = self._primero
            self._primero._pSig = self._ultimo
            self._primero._pAnt = self._ultimo
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
        if self._primero is not None and self._primero != self._ultimo:
            nodoAux = self._ultimo
            self._ultimo = nodoAux._pAnt
            self._ultimo._pSig = self._primero
            self._primero._pAnt = self._ultimo
            nodoAux._pAnt = None
            nodoAux._pSig = None
            del nodoAux
        elif self._primero == self._ultimo and self._primero is not None:
            self._primero = None
            self._ultimo = None
            #print ("El ultimo elemento de la lista ha sido eliminado")

    def graphList(self):
        cont = 0
        txtArchivo ="";
        txtArchivo += "digraph Mass{\n";
        txtArchivo += "subgraph cluster_0{\n";
        txtArchivo += "SnakPositions[label = \"SNAKE REPORT\" color = blue style= filled fontcolor = white shape = box];\n";
        nodoAux = self._primero
        while nodoAux is not None:
            txtArchivo += "node[shape = record label= "
            txtArchivo += "\""
            txtArchivo +=  str(nodoAux.getElemento())
            txtArchivo += "\""
            txtArchivo += "]"+ "nodo" + str(cont) +";\n"
            if nodoAux == self._ultimo:
                break
            cont += 1
            nodoAux = nodoAux._pSig


        nodoAux = self._primero
        txtArchivo += "nodo" + str(0) +" -> "+ "nodo" + str(1) + "\n"
        cont = 1
        nodoAux = nodoAux._pSig
        while nodoAux != self._ultimo:
            txtArchivo += "nodo" + str(cont) +" -> "+ "nodo" + str(cont-1) +"\n"
            txtArchivo += "nodo" + str(cont) +" -> "+ "nodo" + str(cont+1) + "\n"
            cont +=1
            nodoAux = nodoAux._pSig

        txtArchivo += "nodo" + str(0) +" -> "+ "nodo" + str(cont) +"\n"
        txtArchivo += "nodo" + str(cont) +" -> "+ "nodo" + str(cont-1) +"\n"
        txtArchivo += "nodo" + str(cont) +" -> "+ "nodo" + str(0) + "\n"

        txtArchivo += "color = blue \n}"

        txtArchivo += "\n} "
        self.guardarArchivo(txtArchivo, "listUsers")

class Queue(List):
    cont = 0
    def insert(self,elemento):
        self.cont +=1
        nuevo = Nodo(elemento)
        if self._primero is None:
            self._primero = self._ultimo = nuevo
        elif self._primero == self._ultimo:
            self._primero._pAnt = nuevo
            self._ultimo = nuevo
            self._ultimo._pSig = self._primero
        else:
            self._ultimo._pSig = nuevo
            nuevo._pAnt = self._ultimo
            self._ultimo = nuevo

    def delete(self):
        self.cont -=1
        if self._primero is not None and self._primero != self._ultimo:
            nodoAux = self._primero._pAnt
            nodoAuxE = self._primero
            nodoAux._pSig = None
            self._primero._pAnt = None
            self._primero = nodoAux
            del nodoAuxE
        elif self._primero == self._ultimo and self._primero is not None:
            self._primero = None
            self._ultimo = None
            #print ("El ultimo elemento de la lista ha sido eliminado")

    def print(self):
        nodoAux = self._ultimo
        while(nodoAux != self._primero):
            print (nodoAux.getElemento() , "-> " , end="")
            nodoAux = nodoAux._pSig
        print (nodoAux.getElemento())

    def graphList(self):
        txtArchivo ="";
        txtArchivo += "digraph Mass{\n";
        txtArchivo += "subgraph cluster_0{\n";
        txtArchivo += "SnakPositions[label = \"SCORE REPORT\" color = blue style= filled fontcolor = white shape = box];\n";
        nodoAux = self._ultimo

        txtArchivo += "node[shape = record label= "
        txtArchivo += "\""
        txtArchivo += "(" + str(nodoAux.getElemento()[0])  + "," + str(nodoAux.getElemento()[1]) + ")"
        print(nodoAux.getElemento()[0] )
        nodoAux = nodoAux._pSig
        while nodoAux is not None:
            txtArchivo += " | (" + str(nodoAux.getElemento()[0])  + "," + str(nodoAux.getElemento()[1]) + ")"
            nodoAux = nodoAux._pSig

        txtArchivo += "\""
        txtArchivo += "] nodo \n"
        txtArchivo += "color = blue \n}"

        txtArchivo += "\n} "
        self.guardarArchivo(txtArchivo, "snacks")

class Stack(List):
    def insert(self,elemento):
        nuevo = Nodo(elemento)
        if self._primero is None:
            self._primero = self._ultimo = nuevo
        elif self._primero == self._ultimo:
            self._ultimo = nuevo
            self._ultimo._pSig = self._primero
        else:
            nuevo._pSig = self._ultimo
            self._ultimo = nuevo

    def delete(self):
        if self._primero is not None and self._primero != self._ultimo:
            nodoAux = self._ultimo
            self._ultimo = self._ultimo._pSig
            del nodoAux
        elif self._primero == self._ultimo and self._primero is not None:
            self._primero = None
            self._ultimo = None
            #print ("El ultimo elemento de la lista ha sido eliminado")

    def print(self):
        nodoAux = self._ultimo
        while(nodoAux != self._primero):
            print (nodoAux.getElemento() , "-> " , end="")
            nodoAux = nodoAux._pSig
        print (nodoAux.getElemento())

    def graphList(self):
        txtArchivo ="";
        txtArchivo += "digraph Mass{\n";
        txtArchivo += "subgraph cluster_0{\n";
        txtArchivo += "SnakPositions[label = \"SCORE REPORT\" color = blue style= filled fontcolor = white shape = box];\n";
        nodoAux = self._ultimo

        txtArchivo += "node[shape = record label= "
        txtArchivo += "\""

        txtArchivo += "(" + str(nodoAux.getElemento()[1]) + "," + str(nodoAux.getElemento()[0]) + ")"
        nodoAux = nodoAux._pSig

        while nodoAux is not None:
            txtArchivo += " | (" + str(nodoAux.getElemento()[1]) + "," + str(nodoAux.getElemento()[0]) + ")"
            nodoAux = nodoAux._pSig

        txtArchivo += "\""
        txtArchivo += "] nodo \n"

        txtArchivo += "color = blue \n}"

        txtArchivo += "\n} "
        self.guardarArchivo(txtArchivo, "score")
