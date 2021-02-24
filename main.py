import random, sys
from tkinter import *
import tkinter
def grid(nb_col, nb_lines, dim, origin):
    x1=origin
    y1=origin
    #grid width
    y2 = y1 + (dim*nb_lines)
    #grid height
    x2 = x1 + (dim*nb_col)
    column = 0

    while column <= nb_col:
        column += 1
        canvas.create_line(x1,y1,x1,y2,width=2,fill="black")
        x1 += dim
    x1= origin
    line=0
    while line <= nb_lines:
        line += 1
        canvas.create_line(x1,y1,x2,y1,width=2,fill="black")
        y1 += dim


def game_init():
    global nb_hidden_mines, nb_seen_mines, play
    play = True
    nb_seen_mines = 0
    canvas.delete(ALL)
    nb_hidden_mines = nb_mines
    show_counter()
    y = 0
    while y < nb_lines:
        x = 1
        y += 1
        while x <= nb_col:
            tab_m[x, y] = 0
            tab_j[x,y]= ""
            canvas.create_rectangle((x-1)*dim+gap,(y-1)*dim+gap,
                                    x*dim+gap,y*dim+gap,width=0, fill="grey")
            x += 1
            grid(nb_col, nb_lines, dim, gap)
            nb_neighboring_mines = 0
            while nb_neighboring_mines < nb_mines:
                col = random.randint(1, nb_col)
                line = random.randint(1, nb_lines)
                if tab_m[col, line] != 9:
                    tab_m[col, line] = 9
                    nb_neighboring_mines += 1


def level_init():
    global nb_col, nb_lines, nb_mines
    level = choix.get()
    if level == 1:
        nb_col, nb_lig, nb_mines = 10, 10, 12# niveau avancé el
    if level == 2:
        nb_col, nb_lig, nb_mines = 15, 15, 30# niveau expert
    else:
        nb_col, nb_lig, nb_mines = 20, 20, 50#
    canvas.configure(width=(nb_col*dim)+gap, height=(nb_lig*dim)+gap)
    game_init()

def show_counter():
    mine_count.configure(text=str(nb_hidden_mines))
    mine_count.configure(text=str((nb_col*nb_lines)-nb_seen_mines))


def show_nb_mines(nb_neighboring_mines, col, lines):
    global nb_hidden_mines, nb_seen_mines
    if tab_j[col, lines] == "":
        nb_seen_mines = nb_seen_mines + 1
        if tab_j[col, lines] == "d":
            nb_hidden_mines = nb_hidden_mines + 1
            nb_seen_mines = nb_seen_mines - 1
            show_counter()
            tab_j[col, lines] = nb_neighboring_mines
            canvas.create_rectangle((col-1)*dim+gap+3, (lines-1)*dim+gap+3, col*dim+gap-3,
                                    lines*dim+gap-3, width=0, fill="ivory")
            color = ['blue', 'orange', 'red', 'green', 'cyan', 'skyblue', 'pink']
            canvas.create_text(col*dim-dim//2+gap, lines*dim-dim//2+gap, text=str(nb_neighboring_mines),
                               fill=color[nb_neighboring_mines-1], font='Arial 22')


fen = Tk()
fen.title("Démineur")
fen.resizable(width=False, height=False)

nb_col, nb_lines, nb_mines = 0, 0, 0
dim, gap, nb_seen_mines = 30, 3, 0

tab_m = {}
tab_j = {}

root = tkinter.Tk()
canvas = Canvas(root, width=10, height=10, bg="black")

choix = IntVar()
choix.set(1)

f3 = Frame(fen)

mine_count = Label(f3, text="100")
mine_count.grid(row=4, column=2, sticky='NE')