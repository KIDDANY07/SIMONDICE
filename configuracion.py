import pygame
from pygame import mixer
mixer.init()
#Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRISOSCURO = (40, 40, 40)
GRISCLARO = (100, 100, 100)
VERDE = (0, 255, 0)
VERDEOSCURO = (0, 215, 0)
AZUL = (219, 127, 26)
AZULOSCURO = (0, 0, 155)
CYAN = (0, 215, 215)
CYANOSCURO = (0, 215, 215)
MAGENTA = (255, 0, 255)
MAGENTAOSCURO = (215, 0, 215)
BGCOLOR = GRISOSCURO

# CONFIG DEL JUEGO
WIDTH = 1300
HEIGHT = 700
FPS = 60
TITLE = "Simon Dice"
BUTTON_SIZE = 200
ANIMATION_SPEED = 20
BEEP1 = 1250
BEEP2 = 1700
BEEP3 = 1120
BEEP4 = 930