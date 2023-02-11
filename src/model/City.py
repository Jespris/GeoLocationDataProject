

class City:
    def __init__(self, name, latitude, longitude, population):
        self.name: str = name
        self.latitude: float = float(latitude)
        self.longitude: float = float(longitude)
        self.population: int = 0 if population == '' else int(float(population))

