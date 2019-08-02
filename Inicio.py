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
menu()
#sc.refresh()

#sc.getkey()

"""
# Initial Snake and Apple position
snake_head = [10,15]
snake_position = [[15,10],[14,10],[13,10]]
apple_position = [20,20]
score = 0

# display apple
win.addch(apple_position[0], apple_position[1], curses.ACS_DIAMOND)

prev_button_direction = 1
button_direction = 1
key = curses.KEY_RIGHT

def collision_with_apple(score):
    apple_position = [random.randint(1,h-2),random.randint(1,w-2)]
    score += 1
    return apple_position, score

def collision_with_boundaries(snake_head):
    if snake_head[0]>=h-1 or snake_head[0]<=0 or snake_head[1]>=w-1 or snake_head[1]<=0 :
        return 1
    else:
        return 0

def collision_with_self(snake_position):
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        return 1
    else:
        return 0

a = []
while True:
    win.border(0)
    win.timeout(100)

    next_key = win.getch()

    if next_key == -1:
        key = key
    else:
        key = next_key

    # 0-Left, 1-Right, 3-Up, 2-Down
    if key == curses.KEY_LEFT and prev_button_direction != 1:
        button_direction = 0
    elif key == curses.KEY_RIGHT and prev_button_direction != 0:
        button_direction = 1
    elif key == curses.KEY_UP and prev_button_direction != 2:
        button_direction = 3
    elif key == curses.KEY_DOWN and prev_button_direction != 3:
        button_direction = 2
    else:
        pass

    prev_button_direction = button_direction

    # Change the head position based on the button direction
    if button_direction == 1:
        snake_head[1] += 1
    elif button_direction == 0:
        snake_head[1] -= 1
    elif button_direction == 2:
        snake_head[0] += 1
    elif button_direction == 3:
        snake_head[0] -= 1

    # Increase Snake length on eating apple
    if snake_head == apple_position:
        apple_position, score = collision_with_apple(score)
        snake_position.insert(0, list(snake_head))
        a.append(apple_position)
        win.addch(apple_position[0], apple_position[1], curses.ACS_DIAMOND)

    else:
        snake_position.insert(0, list(snake_head))
        last = snake_position.pop()
        win.addch(last[0], last[1], ' ')

    # display snake
    win.addch(snake_position[0][0], snake_position[0][1], '#')

    # On collision kill the snake
    if collision_with_boundaries(snake_head) == 1 or collision_with_self(snake_position) == 1:
        break


sc.addstr(10, 30, 'Your Score is:  '+str(score))
sc.refresh()
"""
#time.sleep(2)
curses.endwin()
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

dE = ListDE()
dE.insert(24)
dE.insert(30)
dE.insert(254)
dE.insert(284)
dE.print()
dE.delete()
dE.print()
