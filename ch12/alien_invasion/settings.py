class Settings:
    """ Esta clase almacena todas las configuraciones """

    def __init__(self):
        # Configuraciones de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuracion de la nave
        self.ship_speed = 1.5

        # Configuración de balas
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3