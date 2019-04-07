import turtle
import clase_player
import random

class Circuito():
    
    
    def __init__(self, width = 900, height = 500):
        self.__corredor = []
        self.__width = width
        self.__height = height
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.setworldcoordinates(0, height, width, 0)
        
        self.player(True)
        
    def __str__(self):
        return 'pantalla del circuito'

    def player(self, nuevo = False): 
        if nuevo == False:
            return self.__corredor
        elif nuevo == True:
            indice = len(self.__corredor)
            nombre = self.__screen.textinput('Nombre', 'Introduzca el nombre')
            color = self.__screen.textinput('color', 'Introduzca el color')
            self.__corredor.append(clase_player.Player(nombre))
            self.__corredor[indice].penup()
            self.__corredor[indice].color(color)
            self.__corredor[indice].forward(5)
            self.__corredor[indice].left(90)
            self.__corredor[indice].forward(30)
            
            for indice in range(len(self.__corredor)):
                self.__corredor[indice].forward(30)
            
    def ejecucion(self):
        iniciando = True
        while iniciando:
            instruccion = self.__screen.textinput('Instruccion', 'player: añade un player\ninicio: inicia la carrera')
            if instruccion == 'player':
                self.player(True)
            elif instruccion == 'inicio':
                iniciando = False
                
        for indice in range(len(self.__corredor)):
            self.__corredor[indice].left(270)
                    
        juego = True                        
        while juego:
            finish = self.__width - 30
            for indice in range(len(self.__corredor)):
                avance = random.randint(1, 6)
                self.__corredor[indice].forward(avance)
                
                if self.__corredor[indice].position()[0] >= finish:
                    juego = False
                    self.__corredor[indice].left(90)
                    self.__corredor[indice].sety(self.__height / 2)
                    self.__corredor[indice].left(90)
                    self.__corredor[indice].setx(self.__width / 2)
                    self.__corredor[indice].write(self.__corredor[indice].position()[0])
                
                
if __name__ == '__main__':
    circuito = Circuito()
    circuito.ejecucion()