from Structures import Structures

#---------------------------------------------------------------- File
import tkinter as tk
from tkinter import filedialog

def selectFile(file_path):
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
scoreBoard = Structures.Queue()
users = Structures.ListCDE()
pause = False
nextlvl = False
score = 0

#screen
sc = curses.initscr()
curses.curs_set(0)

curses.start_color()
curses . init_pair ( 1,curses.COLOR_GREEN , curses.COLOR_BLACK)

curses.noecho()
h, w = sc.getmaxyx()
axuH = h
auxW = w
win = curses.newwin(h, w, 0, 0)
win.keypad(1)

def cleanScreen():
    sc.clear()
    sc.refresh()

def defaultVars():
    global  snackeStack, snackeElements, snackeElementsAux, pause, score
    snackeElements = Structures.ListDE()
    snackeElementsAux = Structures.ListDE()
    snackeStack = Structures.Stack()
    pause = False
    score = 0

def calcRandFood():
    rand = random.randint(0,100)
    if rand > 20:
        return 1    #good food
    else:
        return 0    #bad food

def play(velocidad, h, w):
    global snackeElements, snackeStack, snackeElementsAux, score, pause, sc, scoreBoard, nextlvl
    sc.clear()
    sc.refresh()
    win = curses.newwin(h, w, 0, 0)
    win.keypad(1)

    #Initial Positions Snake
    snakeHead = [5,15]
    snackeElements.insert([5,3])
    snackeElements.insert([4,3])
    snackeElements.insert([3,3])

    snakeFood = [random.randint(1,h-2),random.randint(1,w-2)]
    tipeFood = calcRandFood()

    # display Food
    if tipeFood == 1:
        win.addch(snakeFood[0], snakeFood[1], '+')
    else:
        win.addch(snakeFood[0], snakeFood[1], '*')

    lastButtonDireccion = 1
    button_direction = 1
    key = curses.KEY_RIGHT
    lastKey = curses.KEY_ENTER

    def collisionWithSelf(snackeElements):
        snakeHead = list(snackeElements._primero.getElemento())
        if snackeElements.buscar(snakeHead):
            return 1
        else:
            return 0

    while True:
        win.border(0)
        win.timeout(velocidad)

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
        elif key == ord ( 'p' ):
            pause = True
            ah = h
            aw = w
            menu()
            h = ah
            w = aw
            win = curses.newwin(h, w, 0, 0)
            win.keypad(1)
            win.border(0)

            # display Food
            if tipeFood == 1:
                win.addch(snakeFood[0], snakeFood[1], '+')
            else:
                win.addch(snakeFood[0], snakeFood[1], '*')

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
        if snakeHead == snakeFood:
            if tipeFood == 1:
                score += 1
                snackeElements.insertFirst(list(snakeHead))
                snackeStack.insert(snakeFood)
            elif tipeFood == 0:
                score -= 1
                last = list(snackeElements.getLastData())
                win.addch(last[0], last[1], ' ')
                snackeElements.insertFirst(list(snakeHead))
                last = list(snackeElements.getLastData())
                win.addch(last[0], last[1], ' ')
                snackeStack.delete()
            if score == -3:
                sc.addstr(14, 40, 'you lose')
                sc.refresh()
                time.sleep(2)
                sc.clear()
                score = 0
                menu()

            snakeFood = [random.randint(1,h-2),random.randint(1,w-2)]
            tipeFood = calcRandFood()

            # display Food
            if tipeFood == 1:
                win.addch(snakeFood[0], snakeFood[1], '+')
            else:
                win.addch(snakeFood[0], snakeFood[1], '*')

        else:
            snackeElements.insertFirst(list(snakeHead))
            last = list(snackeElements.getLastData())
            win.addch(last[0], last[1], ' ')

        # show snake
        win.addch(snackeElements._primero.getElemento()[0], snackeElements._primero.getElemento()[1], '#')

        if score == 15 and nextlvl is False:
            nextlvl = True
            w = int(w*0.7)
            h = int(h*0.7)
            snackeElements = Structures.ListDE()
            play(35, h, w)

        # collision
        if collisionWithSelf(snackeElements) == 1:
            scoreBoard.insert([userPlaying, score])
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

    snackeElements.graphList()
    snackeStack.graphList()
    menu()


def mesageScreen(mensaje):
    sc.clear()
    sc.addstr(12, 40, mensaje , curses.color_pair(1))
    sc.refresh()
    time.sleep(3)
    cleanScreen()

def subMenuReport():
    global  win
    win = curses.newwin(h, w, 0, 0)
    win.keypad(1)
    sc.clear()
    sc.border(0)
    sc.addstr(2, 55, "REPORTS (REPORTES)", curses.color_pair(1))
    sc.addstr(4, 40, "1.SNAKE REPORT", curses.color_pair(1))
    sc.addstr(5, 40, "2.SCORE REPORT", curses.color_pair(1))
    sc.addstr(6, 40, "3.SCOREBOARD REPORT", curses.color_pair(1))
    sc.addstr(7, 40, "4.USERS REPORT", curses.color_pair(1))
    sc.addstr(8, 40, "5.RETURN", curses.color_pair(1))
    while 1:
        d = sc.getch()
        if d == ord ( '1' ):
            if snackeElementsAux._primero is not None:
                snackeElements.graphList()
            else:
                mesageScreen('No hay ninguna posición del Snake')
                subMenuReport()
        elif d == ord ( '2' ):
            if snackeStack._primero is not None:
                snackeStack.graphList()
            else:
                mesageScreen('No hay bocadillos guardados')
                subMenuReport()
        elif d == ord ( '3' ):
            if scoreBoard._primero is not None:
                scoreBoard.graphList()
            else:
                mesageScreen('No hay Scores de Jugadores')
                subMenuReport()
        elif d == ord ( '4' ):
            if users._primero is not None:
                users.graphList()
            else:
                mesageScreen('No hay Jugadores')
                subMenuReport()
        elif d == ord ( '5' ):
            menu()

def menu():
    global h, w, userPlaying, pause
    sc.clear()
    h, w = sc.getmaxyx()
    win = curses.newwin(h, w, 0, 0)
    win.keypad(1)

    sc.border(0)
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
            if pause is True:
                pause = False
                return
            elif userPlaying is not None:
                defaultVars()
                play(95, h, w)
            else:
                sc.clear()
                sc.addstr(4, 40, "Ingrese el nombre del jugador ", curses.color_pair(1))
                sc.refresh()
                curses.echo()
                s = sc.getstr(6,40, 15)
                curses.noecho()
                userPlaying = s
                users.insert(s)
                defaultVars()
                play(95, h, w)
                #newUser = input()
        elif c == ord ( '2' ):
            if scoreBoard._primero is not None:
                sc.clear()
                sc.border(0)
                nodoAux = scoreBoard._primero
                cont = 4
                sc.addstr(cont, 40, "Name", curses.color_pair(1))
                sc.addstr(cont, 75, "Score", curses.color_pair(1))

                while nodoAux is not None:
                    cont += 1
                    sc.addstr(cont, 40, nodoAux.getElemento()[0] , curses.color_pair(1))
                    sc.addstr(cont, 75, nodoAux.getElemento()[1], curses.color_pair(1))
                    nodoAux = nodoAux._pAnt
        elif c == ord ( '3' ):
            if users._primero is None:
                mesageScreen('No Hay ningun usuario Guardado')
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
                    elif n == ord ( 'a' ):
                        userPlaying = nodoAuxiliar.getElemento
                        menu()
        elif c == ord ( '4' ):
            subMenuReport()
        elif c == ord ( '5' ):
            try:
                sc.clear()
                sc.addstr(4, 40, "Ingrese el path de los usuarios ", curses.color_pair(1))
                sc.refresh()
                curses.echo()
                s = sc.getstr(6,40, 100)
                curses.noecho()
                selectFile(s)
            except:
                sc.clear()
                sc.addstr(12, 40, "Un error a ocurrido ", curses.color_pair(1))
                sc.refresh()
                time.sleep(3)
            menu()
        elif c == ord ( '6' ):
            curses.endwin()
            return

menu()
