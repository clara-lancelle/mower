# -*- coding: UTF-8 -*-
class Mower:
    actual_pos_y = 0
    actual_pos_x = 0
    y_boundary = 0
    x_boundary = 0
    dir = ''
    cardinalities = ["N", "E", "S", "W"]
    error = ''

    def __init__(self, garden_boundaries, start):
        bndr = str(garden_boundaries)
        self.y_boundary = int(bndr[1])
        self.x_boundary = int(bndr[0])
        self.actual_pos_y = int(start[1])
        self.actual_pos_x = int(start[0])
        self.dir = start[3]
        if((self.actual_pos_x > self.x_boundary) or (self.actual_pos_y > self.y_boundary)):
            self.error = "La position de la tondeuse est en dehors des limites."
            print(self.error)
       
    def move_to_dir(self):
        if(self.dir == "N" and self.actual_pos_y != self.y_boundary):
            self.actual_pos_y += 1
        elif(self.dir == "W" and self.actual_pos_x != 0):
            self.actual_pos_x -= 1
        elif(self.dir == "S" and self.actual_pos_y != 0):
            self.actual_pos_y -= 1
        elif(self.dir == "E" and self.actual_pos_x != self.x_boundary):
            self.actual_pos_x += 1
        else:
            self.error = "Une erreur s'est produite."
           
    def change_dir(self, letter):
        if (self.dir in self.cardinalities):
            dir_in_card = self.cardinalities.index(self.dir)
            if(letter == "G"):
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
            self.error = "La direction renseignée est incorrecte."

    def mow(self, ins):
        for letter in ins:
            if(self.error == ""):
                if(letter == "A"):
                    self.move_to_dir() 
                elif(letter == "G" or letter == "D"):
                    self.change_dir(letter)
                else:
                    self.error = "Commande incorrecte."
                    print(self.error)
                    break
            else:
                self.error = "Impossible d'exécuter la commande."
                print(self.error)
                break
        print(str(self.actual_pos_x) + str(self.actual_pos_y) + self.dir)