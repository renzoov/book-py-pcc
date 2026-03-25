class Settings:
    """ Esta clase almacena todas las configuraciones """

    def __init__(self):
        # Configuraciones de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuracion de la nave
        self.ship_limit = 3

        # Configuración de balas
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configuración de aliens
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_Settings()

    def initialize_dynamic_Settings(self):
        self.ship_speed = 5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
