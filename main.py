# from tkinter import *
from classes.game import Game
import random

#
# windows = Tk()
# windows.geometry('800x800')
# label = Label(windows, text="Démineur")
#
#
# #.pack() affiche le label dans la fenêtre
# label.pack()
#
# #boucle Tkinter qui lance la fenêtre
# windows.mainloop()





def main():
    level = input("choose the level : -1 to 1 : ")
    while level == "" :
        level = input("choose the level : -1 to 1")
    Game(level)

    # dd = Demineur(0)
    # di = Demineur(1)
    # de = Demineur(2)
    # print()
    # print("Demineur test : ")
    # print("    finish : " + str(dt.finish))
    # print("    level : " + str(dt.level))
    # case = dt.playground[0][0]
    # print("    1ère case : mined : " + str(case.mined))
    # print("    1ère case : flagged : " + str(case.flagged))
    # print("    1ère case : showed : " + str(case.showed))
    # print("    1ère case : neighboor : " + str(case.neighboor))
    # print()
    # print("Demineur intermediaire : ")
    # print("    finish : " + str(di.finish))
    # print("    level : " + str(di.level))
    # case = di.playground[0][0]
    # print("    1ère case : mined : " + str(case.mined))
    # print("    1ère case : flagged : " + str(case.flagged))
    # print("    1ère case : showed : " + str(case.showed))
    # print("    1ère case : neighboor : " + str(case.neighboor))
    # print()
    # print("Demineur expert : ")
    # print("    finish : " + str(de.finish))
    # print("    level : " + str(de.level))
    # case = de.playground[0][0]
    # print("    1ère case : mined : " + str(case.mined))
    # print("    1ère case : flagged : " + str(case.flagged))
    # print("    1ère case : showed : " + str(case.showed))
    # print("    1ère case : neighboor : " + str(case.neighboor))
    # print()
    # print("Demineur test : ")
    # for j in range(len(dt.playground)):
    #     line = str()
    #     for i in range(len(dt.playground[0])):
    #         line = line + " " + str(dt.playground[j][i].mined)
    #     print(line)
    # print()
    # for j in range(len(dt.playground)):
    #     line = str()
    #     for i in range(len(dt.playground[0])):
    #         if not dt.playground[j][i].mined:
    #             line = line + " " + str(dt.playground[j][i].neighboor)
    #         else:
    #             line = line + " *"
    #     print(line)


if __name__ == "__main__":
    main()
