import turtle
import clase_player

class Circuito():
    
    
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        corredores = []
        self.new_player(len(corredores))
        
        self.__screen = turtle.Screen()
        
    def __str__(self):
        return 'pantalla del circuito'
    
    def __comp(self, valor):
        try:
            return int(valor)
        except:
            return None
    
    def width(self, width = None):
        width = self.__comp(width)
        if width == None:
            return self.__width
        else:
            self.__width = width
            
    def height(self, height = None):
        height = self.__comp(height)
        if height == None:
            return self.__height
        else:
            self.__height = height
            
    def new_player(self, valor):
        player = clase_player.Player(valor)