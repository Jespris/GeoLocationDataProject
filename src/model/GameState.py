from src.model.Country import Country


DELAY = 1000


class Gamestate:
    def __init__(self, world):
        self.world = world
        self.current_country: Country = None
        self.player_score: int = 0
        self.player_guess: str = ""
        self.completed_countries: [Country] = []
        self.delay_left: int = 10

    def update(self, delta_time):
        if self.current_country is None:
            self.delay_left -= delta_time
            print(self.delay_left)
            if self.delay_left <= 0:
                self.delay_left = DELAY
                self.current_country = self.world.get_random_country()
                # print(self.current_country.name)
