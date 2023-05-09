import pygame
from configuracion import *
from dibujo import *
import random


class Juego:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.beeps = [Audio(BEEP1), Audio(BEEP2), Audio(BEEP3), Audio(BEEP4)]
        self.flash_colours = [BLANCO, BLANCO, BLANCO, BLANCO]
        self.colours = [CYANOSCURO, AZUL, MAGENTAOSCURO, VERDEOSCURO]
       
       

        self.buttons = [
            Boton(420, 150, CYANOSCURO),
            Boton(640, 150, AZUL),
            Boton(420, 370, MAGENTAOSCURO),
            Boton(640, 370, VERDEOSCURO),
        ]
        
        

    def Puntaje_Alto(self):
        with open("Puntaje_Alto.txt", "r") as file:
            score = file.read()
        return int(score)

    def Guardar_Puntos(self):
        with open("Puntaje_Alto.txt", "w") as file:
            if self.score > self.high_score:
                file.write(str(self.score))
            else:
                file.write(str(self.high_score))

    def nuevo(self):
        self.waiting_input = False
        self.pattern = []
        self.current_step = 0
        self.score = 0
        self.high_score = self.Puntaje_Alto()

    def inicio(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.clicked_button = None
            self.events()
            self.draw()
            self.update()

    def update(self):
        if not self.waiting_input:
            pygame.time.wait(1000)
            self.pattern.append(random.choice(self.colours))
            for button in self.pattern:
                self.animacion_del_boton(button)
                pygame.time.wait(200)
            self.waiting_input = True

        else:
            
            if self.clicked_button and self.clicked_button == self.pattern[self.current_step]:
                self.animacion_del_boton(self.clicked_button)
                self.current_step += 1

               
                if self.current_step == len(self.pattern):
                    self.score += 1
                    self.waiting_input = False
                    self.current_step = 0

            
            elif self.clicked_button and self.clicked_button != self.pattern[self.current_step]:
                self.animacion_perder()
                self.Guardar_Puntos()
                self.playing = False
        
    

    def animacion_del_boton(self, colour):
        for i in range(len(self.colours)):
            if self.colours[i] == colour:
                sound = self.beeps[i]
                flash_colour = self.flash_colours[i]
                button = self.buttons[i]

        original_surface = self.screen.copy()
        flash_surface = pygame.Surface((BUTTON_SIZE, BUTTON_SIZE))
        flash_surface = flash_surface.convert_alpha()
        r, g, b = flash_colour
        sound.play()
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            for alpha in range(start, end, ANIMATION_SPEED * step):
                self.screen.blit(original_surface, (0, 0))
                flash_surface.fill((r, g, b, alpha))
                self.screen.blit(flash_surface, (button.x, button.y))
                pygame.display.update()
                self.clock.tick(FPS)
        self.screen.blit(original_surface, (0, 0))

    def animacion_perder(self):
        original_surface = self.screen.copy()
        flash_surface = pygame.Surface((self.screen.get_size()))
        flash_surface = flash_surface.convert_alpha()
        for beep in self.beeps:
            beep.play()
        
        
        r, g, b = BLANCO
        for _ in range(3):
            for start, end, step in ((0, 255, 1), (255, 0, -1)):
                   
                for alpha in range(start, end, ANIMATION_SPEED * step):
                    self.screen.blit(original_surface, (0, 0))
                    flash_surface.fill((r, g, b, alpha))
                    self.screen.blit(flash_surface, (0, 0))
                    pygame.display.update()
                    self.clock.tick(FPS)
                    
    def draw(self):
       
        self.screen.fill(BGCOLOR)
        UIElement(476, 100, f"PUNTOS: {str(self.score)}").draw(self.screen)
        UIElement(650, 100, f"PUNTAJE MAS ALTO: {str(self.high_score)}").draw(self.screen)
        for button in self.buttons:
            button.draw(self.screen)        
        pygame.display.update()
        
         
    def events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.click(mouse_x, mouse_y):
                        self.clicked_button = button.colour
            
juego = Juego()

while True:
    juego.nuevo()
    juego.inicio()
    

