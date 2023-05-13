import pygame

pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAGENT = (154, 13, 105)


font = pygame.font.Font(None, 30)
text = font.render("SINGLE LINKED LIST", True, MAGENT)

#Definir dimensiones de la pantalla
size = (900, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Mi juego')

#Iterar hasta que el usuario haga click sobre el botÃ³n
done = False

#Se usa para establecer cuan rapido se actualiza la pantalla
clock = pygame.time.Clock()
#--------------Bucle principal del programa--------------
while not done:
    #--Bucle Principal de Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Si el usuario hizo click sobre salir
            done = True  #Marcamos como hecho y salimos de este bucle
    #La logica del juego debe ir aqui
    #El codigo de dibujo deberia ir aqui
    #Primero, limpia la pantalla con planco. No vayas a poner otros comandos de dibujo encima de esto, de otra forma seran borrados por este comando:
    screen.fill(WHITE)
    screen.blit(text, (90,170))
    #---Avanzamos y actualizamos la pantalla con lo que hemos dibujado---
    pygame.display.flip()
    #---Limitamos a 60 fotogramas por segundos---
    clock.tick(30)