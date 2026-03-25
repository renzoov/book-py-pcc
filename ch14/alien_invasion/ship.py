import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ Clase que administra la nave """

    def __init__(self, ai_game):
        """ Inicializa la nave y configura su posición inicial """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen del barco y obtén su rectángulo.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nueva nave en la parte inferior central de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Almacene un flotador que indique la posición horizontal exacta del barco
        self.x = float(self.rect.x)

        # Bandera de movimiento; comienza con un barco que no se mueve.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Actualiza la posición de la nave basado en la bandera de movimiento. """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Actualiza el objeto rectangulo de self.x
        self.rect.x = self.x

    def blitme(self):
        """ Dibuja la nave en su ubicación actual """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)