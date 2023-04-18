class Mower:
    #actual position of the mower on x
    actual_pos_y: int = 0
    #actual position of the mower on x
    actual_pos_x: int = 0 
    #x limit
    y_boundary: int = 0
    #y limit
    x_boundary: int = 0
    #direction
    dir: str = ''
    cardinalities = ['N', 'E', 'S', 'W']
    error: str = ''

    #at the call of the mower, give garden boundaries and start position of the mower
    def __init__(self, garden_boundaries: int, start: str):
        bndr = str(garden_boundaries)
        self.y_boundary = int(bndr[1])
        self.x_boundary = int(bndr[0])
        self.actual_pos_y = int(start[1])
        self.actual_pos_x = int(start[0])
        self.dir = start[3]
        if((self.actual_pos_x > self.x_boundary) or (self.actual_pos_y > self.y_boundary)):
            self.error = 'La position de la tondeuse est en dehors des limites.'
            print(self.error)
       
    # move the mower in the requested direction but only if it don't exceed the limit   
    def move_to_dir(self):
        if(self.dir == 'N' and self.actual_pos_y != self.y_boundary):
            self.actual_pos_y += 1
        elif(self.dir == 'W' and self.actual_pos_x != 0):
            self.actual_pos_x -= 1
        elif(self.dir == 'S' and self.actual_pos_y != 0):
            self.actual_pos_y -= 1
        elif(self.dir == 'E' and self.actual_pos_x != self.x_boundary):
            self.actual_pos_x += 1
        else:
            self.error = 'Une erreur s\'est produite.'

    #change the direction of the mower, for left we have to browse the array of cardinalities
    # for right to left and vice verso for the right instruction
    def change_dir(self, letter):
        if (self.dir in self.cardinalities):
            dir_in_card = self.cardinalities.index(self.dir)
            if(letter == 'G'):
                if(dir_in_card != 0):
                    dir_in_card -= 1
                    self.dir = self.cardinalities[dir_in_card]
                else:
                    self.dir = self.cardinalities[3]
            else:
                if(dir_in_card != 3):
                    dir_in_card += 1
                    self.dir = self.cardinalities[dir_in_card]
                else:
                    self.dir = self.cardinalities[0]
        else:
            self.error = 'La direction renseignée est incorrecte.'

    # reads the given instructions and call functions to execute them if they're valid,
    # else, a message is displayed
    def mow(self, ins: str):
        for letter in ins:
            if(self.error == ''):
                if(letter == 'A'):
                    self.move_to_dir() 
                elif(letter == 'G' or letter == 'D'):
                    self.change_dir(letter)
                else:
                    print(letter)
                    self.error = 'Commande incorrecte.'
                    print(self.error)
                    break
            else:
                self.error = 'Impossible d\'exécuter la commande.'
                print(self.error)
                break
        print(f'{self.actual_pos_x}{ self.actual_pos_y}{self.dir}')
