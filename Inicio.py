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
score = 0


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
    global snackeElements, snackeStack, snackeElementsAux, score
    lastKey = curses.KEY_ENTER
    score = 0
    snakeHead = [10,15]
    snackeElements.insert([10,5])
    snackeElements.insert([9,5])
    snackeElements.insert([8,5])
    snackF1 = [7,7]
    snackF2 = [15,30]

    # display Food1
    win.addch(snackF1[0], snackF1[1], '+')

        # display Food1
    win.addch(snackF2[0], snackF2[1], '*')

    lastButtonDireccion = 1
    button_direction = 1
    key = curses.KEY_RIGHT


    def collisionWithF1():
        global score
        snackF1 = [random.randint(1,h-2),random.randint(1,w-2)]
        score += 1
        return snackF1, score

    def collisionWithF2():
        global score
        snackF2 = [random.randint(1,h-2),random.randint(1,w-2)]
        score -= 1
        if score == -3:
            sc.addstr(14, 40, 'you lose')
            sc.refresh()
            time.sleep(2)
            sc.clear()
            menu()
        return snackF2, score

    def collisionWithSelf(snackeElements):
        snakeHead = list(snackeElements._primero.getElemento())
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
            lastKey = key
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
        elif key == ord ( '1' ):

            while snackeElements._primero is not None:
                snackeElementsAux.insert(snackeElements.getLastData())
            snackeElements = snackeElementsAux
            snackeElementsAux = Structures.ListDE()
            snakeHead = list(snackeElements._primero.getElemento())

            if button_direction == 1:
                button_direction = 0
            elif button_direction == 0:
                button_direction = 1
            elif button_direction == 3:
                button_direction = 2
            elif button_direction == 2:
                button_direction = 3

            if lastKey == curses.KEY_UP:
                key = curses.KEY_DOWN
            elif lastKey == curses.KEY_DOWN:
                key = curses.KEY_UP
            elif lastKey == curses.KEY_LEFT:
                key = curses.KEY_RIGHT
            elif lastKey == curses.KEY_RIGHT:
                key = curses.KEY_LEFT

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


        # Increase or Decrease Snake length on eating food
        if snakeHead == snackF1:
            snackF1, score = collisionWithF1()
            snackeElements.insertFirst(list(snakeHead))
            snackeStack.insert(snackF1)
            win.addch(snackF1[0], snackF1[1], '+')
        elif snakeHead == snackF2:
            snackF2, score = collisionWithF2()
            last = list(snackeElements.getLastData())
            win.addch(last[0], last[1], ' ')
            snackeElements.insertFirst(list(snakeHead))
            last = list(snackeElements.getLastData())
            win.addch(last[0], last[1], ' ')
            win.addch(snackF2[0], snackF2[1], '*')
        else:
            snackeElements.insertFirst(list(snakeHead))
            last = list(snackeElements.getLastData())
            win.addch(last[0], last[1], ' ')

        # show snake
        #print(snackeElements._primero.getElemento()[0], snackeElements._primero.getElemento()[1])
        win.addch(snackeElements._primero.getElemento()[0], snackeElements._primero.getElemento()[1], '#')

        # collision
        if collisionWithSelf(snackeElements) == 1:
            break
        elif snakeHead[0]>=h-1 or snakeHead[0]<=0 or snakeHead[1]>=w-1 or snakeHead[1]<=0 :
            if snakeHead[0]>=h-1:
                snakeHead[0] = 0
            elif snakeHead[0]<=0:
                snakeHead[0] = h-1
            elif snakeHead[1]>=w-1:
                snakeHead[1] = 0
            elif snakeHead[1]>=0:
                snakeHead[1] = w-1
            snackeElements.insertFirst(list(snakeHead))
            last = list(snackeElements.getLastData())
            win.addch(last[0], last[1], ' ')

    curses.endwin()

def menu():
    global userPlaying
    sc.border(1)
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
                sc.addstr(9, 40, nodoAuxiliar.getElemento() , curses.color_pair(1))
                sc.refresh()
                while 1:
                    n = sc.getch()
                    if n == ord ( 'w' ):
                        nodoAuxiliar = nodoAuxiliar._pAnt
                        sc.clear()
                        sc.addstr(9, 40, nodoAuxiliar.getElemento() , curses.color_pair(1))
                        sc.refresh()
                    elif n == ord ( 's' ):
                        nodoAuxiliar = nodoAuxiliar._pSig
                        sc.clear()
                        sc.addstr(9, 40, nodoAuxiliar.getElemento() , curses.color_pair(1))
                        sc.refresh()
                    elif n == ord ( '0' ):
                        userPlaying = nodoAuxiliar.getElemento
                        break
        elif c == ord ( '6' ):
            break
        #elif c == ord ( '\n' ) or c == ord ( '\r' ):
        #    print("enter capturado")

menu()
