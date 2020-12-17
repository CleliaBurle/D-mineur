import random
from classes.box import Box

class Game:
    '''
    Cette classe contient 3 attributs :
        - finish    : booleen indiquant si la partie est finie
        - level     : int indiquant le niveau du démineur (debutant, intermediaire, expert)
        - playground: tableau a 2 dimensions de cases ou se passe le jeu
    '''

    def __init__(self, level):
        self.finish = False
        self.level = level
        self.playground = create_playground(level)
        self.play()

    def dig(self, coord):
        x = coord[0]
        y = coord[1]
        sizex = len(self.playground[0])
        sizey = len(self.playground)
        if x >= 0 and x < sizex and y >= 0 and y < sizey:
            self.playground[y][x].set_showed(True)
            if self.playground[y][x].mined:
                print("You lose!")
                self.finish = True

    def play(self):
        while not self.finish:
            map = str()
            for j in range(len(self.playground)):
                line = str()
                for i in range(len(self.playground[0])):
                    if not self.playground[j][i].showed:
                        line = line + ". "
                    else:
                        line = line + str(self.playground[j][i].neighboor) + " "
                map = map + line + "\n"
            print(map)
            print()
            xstr = input("Select a box : x = ")
            ystr = input("Select a box : y = ")
            while xstr == "":
                xstr = input("Select a box : x = ")
            while ystr == "":
                ystr = input("Select a box : y = ")
            x = int(xstr)
            y = int(ystr)
            self.dig((x, y))
            win = True
            for i in range(len(self.playground)):
                for j in range(len(self.playground[0])):
                    if not self.playground[j][i].mined and not self.playground[j][i].showed:
                        win = False
            if win:
                print("You win!")
            self.finish = win or self.finish

        map = str()
        for j in range(len(self.playground)):
            line = str()
            for i in range(len(self.playground[0])):
                if not self.playground[j][i].showed:
                    line = line + "X "
                else:
                    line = line + str(self.playground[j][i].neighboor) + " "
            map = map + line + "\n"
        print(map)
        print("Thanks for playing!")


def create_playground(level):
    # Liste qui contiendra les coordonnées des cases minées
    coord_mines = []

    if level == -1:  # Niveau test           5x5         2 mines
        sizex = 5
        sizey = 5
        mines = 2
    elif level == 0:  # Niveau débutant       10x10       10 mines
        sizex = 10
        sizey = 10
        mines = 10

    elif level == 1:  # Niveau intermédiaire  16x16       40 mines
        sizex = 16
        sizey = 16
        mines = 40

    else:  # Niveau expert         16x30       99 mines
        sizex = 30
        sizey = 16
        mines = 99

    # Création d'un tableau de cases initialisées à 0 et False : playground[y][x]
    playground = [[Box(False, 0) for i in range(sizex)] for j in range(sizey)]
    # Détermination des cases minées
    for k in range(mines):
        x = random.randint(0, sizex - 1)
        y = random.randint(0, sizey - 1)
        while (x, y) in coord_mines:  # Si on répète deux fois la meme coordonnée
            x = random.randint(0, sizex - 1)  # On recrée un autre couple de coordonnées
            y = random.randint(0, sizey - 1)
        coord_mines.append((x, y))  # On ajoute les coordonnées à la liste
    # Placement des cases minées
    for coord in coord_mines:  # Pour chaque couple de coordonnées
        x = coord[0]  # On insère une case minée dans le playground
        y = coord[1]  # aux coordonnées données
        playground[y][x] = Box(True, 0)

    for j in range(len(playground)):
        for i in range(len(playground[0])):
            pmines = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x != i or y != j:
                        if x >= 0 and x < sizex and y >= 0 and y < sizey:
                            if playground[y][x].mined:
                                pmines += 1
            playground[j][i].set_neighboor(pmines)

    return playground
