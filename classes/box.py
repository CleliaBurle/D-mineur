class Box:
    '''
    Cette classe contient 4 attributs :
        - mined     : booléen indiquant si la case contient une mine ou non
        - flagged   : booléen indiquant si la case est flaggée ou non
        - showed    : booléen indiquand si la case est dévoilée ou non
        - neighboor : int donnant le nombre de mines voisines à la case courante
    '''

    def __init__(self, mined, neighboor):
        self.mined = mined
        self.flagged = False
        self.showed = False
        if mined:
            self.neighboor = 0
        else:
            self.neighboor = neighboor

    def set_neighboor(self, neighboor):
        self.neighboor = neighboor

    def set_showed(self, showed):
        self.showed = showed
