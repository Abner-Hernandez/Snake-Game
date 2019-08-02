#---------------------------------------------------------Lists
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
            self._ultimo._pSig = nuevo
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

class Stack(List):
    def insert(self,elemento):
        nuevo = Nodo(elemento)
        if self._primero == None:
            self._primero = self._ultimo = nuevo
        elif self._primero == self._ultimo:
            self._ultimo = nuevo
            self._ultimo._pSig = self._primero
        else:
            self._ultimo._pSig = nuevo
            self._ultimo = nuevo

    def delete(self):
        if self._primero != None and self._primero != self._ultimo:
            nodoAux = self._ultimo
            self._ultimo = self._ultimo._pSig
            nodoAux._pSig = None
            del nodoAux
        elif self._primero == self._ultimo:
            self._primero = None
            self._ultimo = None
            print ("El ultimo elemento de la lista ha sido eliminado")



#---------------------------------------------------------------- Game
import random
import curses
import time

#screen
sc = curses.initscr()
h, w = sc.getmaxyx()
win = curses.newwin(h, w, 0, 0)

win.keypad(1)
curses.curs_set(0)

curses.start_color()
curses . init_pair ( 1,curses.COLOR_GREEN , curses.COLOR_BLACK)

def menu():
    sc.addstr(2, 55, "Menu", curses.color_pair(1))
    sc.addstr(5, 40, "1.Play (Jugar)", curses.color_pair(1))
    sc.addstr(8, 40, "2.Scoreboard (Puntuaciones)", curses.color_pair(1))
    sc.addstr(11, 40, "3.User selection (Usuarios)", curses.color_pair(1))
    sc.addstr(14, 40, "4.Reports (reportes)", curses.color_pair(1))
    sc.addstr(17, 40, "5.Bulk loading (carga masiva)", curses.color_pair(1))

    c = sc.getch()
    if c == ord ( '1' ):
        sc.addstr(19, 40, "5.Bulk loading (carga2 masiva)", curses.color_pair(1))
        sc.refresh()
        time.sleep(10)
    elif c == curses . KEY_ENTER :
        sc.addstr(19, 40, "5.Bulk loading (carga2 masiva)", curses.color_pair(1))
        time.sleep(10)

dE = ListDE()
dE.insert(24)
dE.insert(30)
dE.insert(254)
dE.insert(284)
dE.print()
dE.delete()
dE.print()
