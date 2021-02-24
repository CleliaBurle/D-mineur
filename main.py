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
    root = tkinter.Tk()
    canvas = Canvas(root, width=10, height=10, bg="black")
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

