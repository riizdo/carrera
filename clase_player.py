import turtle

class Player:
    def __init__(self, numero, nombre):
        self.__numero = numero
        self.__nombre = nombre
        self.__cuerpo = turtle.Turtle('turtle')
        
    def __str__(self):
        return "Player {}, corredor {}".format(self.__nombre, self.__numero)
    
    def __comp(self, valor):
        try:
            return int(valor)
        except:
            return None
        
    def forma(self, valor = None):
        if valor == None:
            return self.__cuerpo.shape()
        elif valor == 'arrow' or valor == 'turtle' or valor == 'circle' or valor == 'square' or valor == 'triangle' or valor == 'classic':
            self.__cuerpo.shape(valor)
    
    def numero(self, valor = None):
        valor = comp(valor)
        if valor == None:
            return self.__numero
        else:
            self.__numero = numero
        
    def nombre(self, nombre = None):
        if nombre == None:
            return self.__nombre
        else:
            self.__nombre = nombre
            
    def color(self, color = None):
        if color == None:
            return self.__cuerpo.color()
        else:
            self.__cuerpo.color(color)
            