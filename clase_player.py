import turtle

class Player(turtle.Turtle):
    
    def __init__(self, nombre):
        turtle.Turtle.__init__(self, 'turtle', 1000, True)
        self.__nombre = nombre
        
    def __str__(self):
        return "player {}". format(self.__nombre)
    
    def nombre(self, nombre = None):
        if nombre == None:
            return self.__nombre
        else:
            self.__nombre = nombre
            
    