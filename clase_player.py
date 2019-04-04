import turtle

class Player:
    def __init__(self, numero):
        self.__numero = numero
        self.__cuerpo = turtle.Turtle()
        
    def __str__(self):
        return "Player {}".format(self._numero)
    
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
    
