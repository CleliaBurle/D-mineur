import random, sys
from tkinter import *
import tkinter


# Create the grid
def grid(nb_col, nb_lines, dim, origin):
    x1 = origin
    y1 = origin
    # grid width
    y2 = y1 + (dim * nb_lines)
    # grid height
    x2 = x1 + (dim * nb_col)
    column = 0
    while column <= nb_col:
        column += 1
        canvas.create_line(x1, y1, x1, y2, width=2, fill="black")
        x1 += dim
    x1 = origin
    line = 0
    while line <= nb_lines:
        line += 1
        canvas.create_line(x1, y1, x2, y1, width=2, fill="black")
        y1 += dim

# Initialize the game
def game_init():
    global nb_hidden_mines, nb_seen_mines, play
    play = True
    nb_seen_mines = 0
    canvas.delete(ALL)
    nb_hidden_mines = nb_mines
    show_counter()
    y = 0
    while y < nb_lig:
        x = 1
        y += 1
        while x <= nb_col:
            tab_m[x, y] = 0
            tab_j[x, y] = ""

            canvas.create_rectangle((x - 1) * dim + gap, (y - 1) * dim + gap,
                                    x * dim + gap, y * dim + gap, width=0, fill="grey")
            x += 1

            grid(nb_col, nb_lig, dim, gap)
            nb_neighboring_mines = 0

            while nb_neighboring_mines < nb_mines:
                col = random.randint(1, nb_col)
                line = random.randint(1, nb_lig)
                nb_neighboring_mines += 1

    i = 0
    while i < nb_mines:
        tab_m[random.randint(1, nb_col), random.randint(1, nb_lig)] = 9
        i += 1

# Initialize the level
def level_init():
    global nb_col, nb_lig, nb_mines
    level = choix.get()
    if level == 1:
        nb_col, nb_lig, nb_mines, cases = 10, 10, 12, (10 * 10)
    if level == 2:
        nb_col, nb_lig, nb_mines, cases = 15, 15, 30, (15 * 15)
    if level == 3:
        nb_col, nb_lig, nb_mines, cases = 20, 20, 50, (20 * 20)
    canvas.configure(width=(nb_col * dim) + gap, height=(nb_lig * dim) + gap)
    game_init()


def show_counter():
    mines_count.configure(text=str(nb_hidden_mines))


def show_nb_mines(nb_neighboring_mines, col, lines):
    global nb_hidden_mines, nb_seen_mines
    if tab_j[col, lines] == "":
        nb_seen_mines += 1
    if tab_j[col, lines] == "d":
        nb_hidden_mines += 1
        nb_seen_mines -= 1
        show_counter()
        tab_j[col, lines] = nb_neighboring_mines
        canvas.create_rectangle((col - 1) * dim + gap + 3, (lines - 1) * dim + gap + 3, col * dim + gap - 3,
                                lines * dim + gap - 3, width=0, fill="ivory")
        color = ['blue', 'orange', 'red', 'green', 'cyan', 'skyblue', 'pink']
        canvas.create_text(col * dim - dim // 2 + gap, lines * dim - dim // 2 + gap, text=str(nb_neighboring_mines),
                           fill=color[nb_neighboring_mines - 1], font='Arial 22')

# Get nb mines
def nb_mines_adj(col, line):
    if col > 1:
        min_col = col - 1
    else:
        min_col = 1
    if col < nb_col:
        max_col = col + 1
    else:
        max_col = col
    if line > 1:
        min_lig = line - 1
    else:
        min_lig = 1
    if line < nb_lig:
        max_lig = line + 1
    else:
        max_lig = line

    txtinfo = ""
    nb_mines = 0
    index_line = min_lig

    while index_line <= max_lig:
        index_col = min_col

        while index_col <= max_col:
            if tab_m[index_col, index_line] == 9:
                nb_mines += 1

            index_col = index_col + 1
        index_line = index_line + 1
    return nb_mines

# Show empty case
def show_zero_case(col, line):
    global nb_hidden_mines, nb_seen_mines
    if tab_j[col, line] != 0:
        if tab_j[col, line] == "d":

            nb_hidden_mines += 1
            nb_seen_mines -= 1
            canvas.create_text(col * dim - dim // 2 + gap, line * dim - dim // 2 + gap, text="", fill='black',
                               font='Arial 20')
            tab_j[col, line] = 0
            nb_seen_mines = nb_seen_mines + 1
            if col > 1:
                nb_neighboring_mines = nb_mines_adj(col - 1, line)
                if nb_neighboring_mines == 0:
                    show_zero_case(col - 1, line)
                else:
                    show_nb_mines(nb_neighboring_mines, col - 1, line)
            if col < nb_col:
                nb_neighboring_mines = nb_mines_adj(col + 1, line)
                if nb_neighboring_mines == 0:
                    show_zero_case(col + 1, line)
                else:
                    show_nb_mines(nb_neighboring_mines, col + 1, line)
            if line > 1:
                nb_neighboring_mines = nb_mines_adj(col, line - 1)
                if nb_neighboring_mines == 0:
                    show_zero_case(col, line - 1)
                else:
                    show_nb_mines(nb_neighboring_mines, col, line - 1)
            if line < nb_lig:
                nb_neighboring_mines = nb_mines_adj(col, line + 1)
                if nb_neighboring_mines == 0:
                    show_zero_case(col, line + 1)
                else:
                    show_nb_mines(nb_neighboring_mines, col, line + 1)
                if col > 1 and line > 1:
                    nb_neighboring_mines = nb_mines_adj(col - 1, line - 1)
                    if nb_neighboring_mines == 0:
                        show_zero_case(col - 1, line - 1)
                    else:
                        show_nb_mines(nb_neighboring_mines, col - 1, line - 1)
                if col > 1 and line < nb_lig:
                    nb_neighboring_mines = nb_mines_adj(col - 1, line + 1)
                    if nb_neighboring_mines == 0:
                        show_zero_case(col - 1, line + 1)
                    else:
                        show_nb_mines(nb_neighboring_mines, col - 1, line + 1)
                if col < nb_col and line > 1:
                    nb_neighboring_mines = nb_mines_adj(col + 1, line - 1)
                    if nb_neighboring_mines == 0:
                        show_zero_case(col + 1, line - 1)
                    else:
                        show_nb_mines(nb_neighboring_mines, col + 1, line - 1)
                if col < nb_col and line < nb_lig:
                    nb_neighboring_mines = nb_mines_adj(col + 1, line + 1)
                    if nb_neighboring_mines == 0:
                        show_zero_case(col + 1, line + 1)
                    else:
                        show_nb_mines(nb_neighboring_mines, col + 1, line + 1)
                show_counter()
        else:
            canvas.create_rectangle((col - 1) * dim + gap + 3, (line - 1) * dim + gap + 3,
                                    col * dim + gap - 3, line * dim + gap - 3,
                                    width=6, fill="white")
            show_counter()

# Display lose
def lose(n_col, n_line):
    global play
    play = False
    nline = 0
    canvas.create_image(n_col, n_line, image=im_mine)
    canvas.create_text((nb_col / 2) * dim - 15 + gap, (nb_lig / 2) * dim - 5 + gap, text='Lose !', fill='black',
                       font='Arial 50')

# Display win
def win():
    canvas.create_text((nb_col / 2) * dim - 15 + gap, (nb_lig / 2) * dim - 5 + gap, text='Well done !', fill='black',
                       font='Arial 50', bg="white")
    fen.update_idletasks()

# Manage the left click
def left_click(event):
    global nb_seen_mines
    if play:
        n_col = (event.x - gap) // dim + 1
        n_line = (event.y - gap) // dim + 1
        if (tab_j[n_col, n_line] == ""):
            if n_col >= 1 and n_col <= nb_col and n_line >= 1 and n_line <= nb_lig:
                if (tab_m[n_col, n_line] == 9):
                    lose(n_col, n_line)
                else:
                    nb_neighboring_mines = nb_mines_adj(n_col, n_line)
                    if nb_neighboring_mines >= 1:
                        canvas.create_rectangle((n_col - 1) * dim + gap + 3, (n_line - 1) * dim + gap + 3,
                                                n_col * dim + gap - 3, n_line * dim + gap - 3,
                                                width=6, fill="blue")
                        tab_j[n_col, n_line] = "n"
                        show_nb_mines(nb_neighboring_mines, n_col, n_line)

                        show_counter()

                    else:
                        show_zero_case(n_col, n_line)

            if (nb_hidden_mines == 0):
                win()

# Manage the right click
def right_click(event):
    global nb_hidden_mines, nb_seen_mines
    if play:
        nCol = (event.x - gap) // dim + 1
        nLig = (event.y - gap) // dim + 1
        if tab_j[nCol, nLig] != "n":
            if tab_j[nCol, nLig] == "":
                canvas.create_text(nCol * dim - dim // 2 + gap, nLig * dim - dim // 2 + gap, text="F", fill='black',
                                   font='Arial 20')
                tab_j[nCol, nLig] = "d"
                if tab_m[nCol, nLig] == 9:
                    nb_seen_mines += 1
                    nb_hidden_mines -= 1

            elif tab_j[nCol, nLig] == "d":
                canvas.create_rectangle((nCol - 1) * dim + gap + 3, (nLig - 1) * dim + gap + 3, nCol * dim + gap - 3,
                                        nLig * dim + gap - 3, width=0, fill="blue")
                canvas.create_text(nCol * dim - dim // 2 + gap, nLig * dim - dim // 2 + gap, text="?", fill='black',
                                   font='Arial 20')
                tab_j[nCol, nLig] = "?"
                if tab_m[nCol, nLig] == 9:
                    nb_seen_mines -= 1
                    nb_hidden_mines += 1
            elif tab_j[nCol, nLig] == "?":
                canvas.create_rectangle((nCol - 1) * dim + gap + 3, (nLig - 1) * dim + gap + 3,
                                        nCol * dim + gap - 3, nLig * dim + gap - 3,
                                        width=0, fill="grey")
                tab_j[nCol, nLig] = ""

            show_counter()
            if ((nb_col * nb_lig) == nb_seen_mines and nb_hidden_mines == 0):
                win()


fen = Tk()
fen.title("Démineur")
fen.resizable(width=False, height=False)

nb_col, nb_lig, nb_mines, cases = 0, 0, 0, 0
dim, gap, nb_seen_mines = 30, 3, 0

im_mine = PhotoImage(file="./utils/mine.png")
im_erreur = PhotoImage(file="./utils/croix.png")
im_flag = PhotoImage(file="./utils/drapeau.png")
tab_m = {}
tab_j = {}

canvas = Canvas(fen, width=(nb_col * dim) + gap, height=(nb_lig * dim) + gap, bg="grey")
canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-3>", right_click)
canvas.pack(side=RIGHT)

f2 = Frame(fen)

choix = IntVar()
choix.set(1)

case1 = Radiobutton(f2)
case1.configure(text='Beginner', command=level_init, variable=choix, value=1)
case1.pack(anchor=NW, padx=30)

case2 = Radiobutton(f2)
case2.configure(text='Advanced', padx=3, command=level_init, variable=choix, value=2)
case2.pack(anchor=NW, padx=30)

case3 = Radiobutton(f2)
case3.configure(text='Expert', padx=3, command=level_init, variable=choix, value=3)
case3.pack(anchor=NW, padx=30)
f2.pack()

f3 = Frame(fen)

text_mines = Label(f3, text="Mines restantes :")
mines_count = Label(f3, text="100")
text_mines.grid(row=4, column=1, sticky='NW')
mines_count.grid(row=4, column=2, sticky='NE')

f3.pack()

f1 = Frame(fen)
btn1 = Button(f1, width=14, text="Nouvelle partie", font="Arial 10", command=level_init)
btn1.pack(side=BOTTOM, padx=5, pady=5)
f1.pack(side=BOTTOM)

f4 = Frame(fen)

f4.pack(side=BOTTOM)
