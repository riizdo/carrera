import turtle
import clase_player

class Circuito():
    
    
    def __init__(self, width = 900, height = 500):
        self.__corredor = []
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        
        self.player(len(self.__corredor), True)
        self.__corredor[0].nombre('pepe')
        self.__corredor[0].color('green')
        
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
            
    def player(self, numero, nuevo = False):
        if nuevo == False and numero < len(self.__corredor):
            return self.__corredor[numero]
        elif nuevo == True and numero == len(self.__corredor):
            self.__corredor.append(clase_player.Player(numero, 'pepe'))
            
    def cantidad(self):
        return len(self.__corredor)