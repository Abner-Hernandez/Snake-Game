"""
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

#---------------------------------------------------------------- Implementation
"""
from Structures import Structures
users = Structures.ListCDE()

#---------------------------------------------------------------- File
import tkinter as tk
from tkinter import filedialog

def selectFile():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    archivo = open(file_path, "r")
    lines = archivo.readlines()
    try:
        for user in lines:
            users.insert(user)
        archivo.close()
    except:
        print ("Error")

#---------------------------------------------------------------- Game
import curses
import time
import random

#-----------vars
userPlaying = None
snackeElements = Structures.ListDE()
snackeElementsAux = Structures.ListDE()
snackeStack = Structures.Stack()

#screen
sc = curses.initscr()
h, w = sc.getmaxyx()
win = curses.newwin(h, w, 0, 0)

win.keypad(1)
curses.curs_set(0)

curses.start_color()
curses . init_pair ( 1,curses.COLOR_GREEN , curses.COLOR_BLACK)
curses.noecho()

def cleanScreen():
    sc.clear()
    sc.refresh()

def play():
    global snackeElements, snackeStack, snackeElementsAux
    score = 0
    snakeHead = [10,15]
    snackeElements.insert([10,5])
    snackeElements.insert([9,5])
    snackeElements.insert([8,5])
    snackF1 = [7,7]

    # display Food1
    win.addch(snackF1[0], snackF1[1], '+')

    lastButtonDireccion = 1
    button_direction = 1
    key = curses.KEY_RIGHT


    def collisionWithF1():
        global score
        snackF1 = [random.randint(1,h-2),random.randint(1,w-2)]
        score += 1
        return snackF1, score

    def collision_with_boundaries(snakeHead):
        if snakeHead._primero.getElemento()[0]>=h-1 or snakeHead._primero.getElemento()[0]<=0 or snakeHead._primero.getElemento()[1]>=w-1 or snakeHead._primero.getElemento()[1]<=0 :
            return 1
        else:
            return 0

    def collisionWithSelf(snackeElements):
        snakeHead = snackeElements._primero.getElemento()
        if snackeElements.buscar(snakeHead):
            return 1
        else:
            return 0

    while True:
        win.border(0)
        win.timeout(100)

        nextKey = win.getch()

        if nextKey == -1:
            key = key
        else:
            key = nextKey

        # 0-Left, 1-Right, 3-Up, 2-Down
        if key == curses.KEY_LEFT and lastButtonDireccion != 1:
            button_direction = 0
        elif key == curses.KEY_RIGHT and lastButtonDireccion != 0:
            button_direction = 1
        elif key == curses.KEY_UP and lastButtonDireccion != 2:
            button_direction = 3
        elif key == curses.KEY_DOWN and lastButtonDireccion != 3:
            button_direction = 2
        elif key == curses.KEY_ENTER:
            if lastButtonDireccion == 1:
                lastButtonDireccion = 0
            elif lastButtonDireccion == 0:
                lastButtonDireccion = 1
            elif lastButtonDireccion == 3:
                lastButtonDireccion = 2
            elif lastButtonDireccion == 2:
                lastButtonDireccion = 3

            if key == curses.KEY_LEFT and lastButtonDireccion != 1:
                button_direction = 0
            elif key == curses.KEY_RIGHT and lastButtonDireccion != 0:
                button_direction = 1
            elif key == curses.KEY_UP and lastButtonDireccion != 2:
                button_direction = 3
            elif key == curses.KEY_DOWN and lastButtonDireccion != 3:
                button_direction = 2

            while snackeElements._primero is not None:
                snackeElementsAux.insert(snackeElements.getLastData())
            snackeElements = snackeElementsAux
            snackeElementsAux = Structures.ListDE()
        else:
            pass

        lastButtonDireccion = button_direction

        # Change the head position based on the button direction
        if button_direction == 1:
            snakeHead[1] += 1
        elif button_direction == 0:
            snakeHead[1] -= 1
        elif button_direction == 2:
            snakeHead[0] += 1
        elif button_direction == 3:
            snakeHead[0] -= 1

    #continuar aqui leido pero sino volver a leer


        # Increase Snake length on eating apple
        if snakeHead == snackF1:
            snackF1, score = collisionWithF1()
            snackeElements.insertFirst(list(snakeHead))
            snackeStack.insert(snackF1)
            win.addch(snackF1[0], snackF1[1], '+')

        else:
            snackeElements.insertFirst(list(snakeHead))
            last = list(snackeElements.getLastData())
            win.addch(last[0], last[1], '+')

        # display snake
        win.addch(snackeElements._primero.getElemento()[0], snackeElements._primero.getElemento()[1], '#')

        # On collision kill the snake
        if collision_with_boundaries(snakeHead) == 1 or collisionWithSelf(snackeElements) == 1:
            break


    sc.addstr(10, 30, 'Your Score is:  '+str(score))
    sc.refresh()

    time.sleep(2)
    curses.endwin()

def menu():
    global userPlaying
    sc.addstr(2, 55, "Menu", curses.color_pair(1))
    sc.addstr(4, 40, "1.Play (Jugar)", curses.color_pair(1))
    sc.addstr(5, 40, "2.Scoreboard (Puntuaciones)", curses.color_pair(1))
    sc.addstr(6, 40, "3.User selection (Usuarios)", curses.color_pair(1))
    sc.addstr(7, 40, "4.Reports (reportes)", curses.color_pair(1))
    sc.addstr(8, 40, "5.Bulk loading (carga masiva)", curses.color_pair(1))
    sc.addstr(9, 40, "6.Exit", curses.color_pair(1))

    while 1:
        c = sc.getch()
        if c == ord ( '1' ):
            if userPlaying is not None:
                play()
            else:
                sc.clear()
                sc.addstr(4, 40, "Ingrese el nombre del jugador ", curses.color_pair(1))
                sc.refresh()
                curses.echo()
                s = sc.getstr(6,40, 15)
                curses.noecho()
                userPlaying = s
                users.insert(s)
                play()
                #newUser = input()
        if c == ord ( '5' ):
            selectFile()
            #sc.refresh()
        elif c == ord ( '3' ):
            if users._primero is None:
                sc.clear()
                sc.addstr(12, 40, 'No Hay ningun usuario Guardado' , curses.color_pair(1))
                sc.refresh()
                time.sleep(3)
                cleanScreen()
                menu()
            else:
                nodoAuxiliar = users._primero
                sc.clear()
                while 1:
                    n = win.getch()
                    if n == curses.KEY_UP:
                        nodoAuxiliar = nodoAuxiliar._pAnt
                        sc.clear()
                        sc.addstr(9, 40, nodoAuxiliar.getElemento() , curses.color_pair(1))
                        sc.refresh()
                    elif n == curses.KEY_DOWN:
                        nodoAuxiliar = nodoAuxiliar._pSig
                        sc.clear()
                        sc.addstr(9, 40, nodoAuxiliar.getElemento() , curses.color_pair(1))
                        sc.refresh()
                    elif n == ord ( '0' ):
                        userPlaying = nodoAuxiliar.getElemento
                        break
        elif c == ord ( '6' ):
            break
        elif c == curses . KEY_ENTER :
            sc.addstr(19, 40, "5.Bulk loading (carga2 masiva)", curses.color_pair(1))
            time.sleep(10)
menu()



#sc.refresh()

#sc.getkey()


#print(a)
#print(w,h)




"""
def ini(stdscr):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    begin_x = 20 ; begin_y = 7
    height = 5 ; width = 40
    win = curses . newwin ( height , width , begin_y , begin_x )
    stdscr.getkey()

def endApp(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

from curses import wrapper

wrapper(ini)

def main(stdscr):
    # Clear screen
    stdscr.clear()

    stdscr.refresh()
    stdscr.getkey()

from curses import wrapper
wrapper(main)
"""

dE = Structures.ListDE()
dE.insert(24)
dE.insert(30)
dE.insert(254)
dE.insert(284)
dE.print()
dE.delete()
dE.print()
