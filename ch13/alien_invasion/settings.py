class Settings:
    """ Esta clase almacena todas las configuraciones """

    def __init__(self):
        # Configuraciones de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuracion de la nave
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Configuración de balas
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configuración de aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1