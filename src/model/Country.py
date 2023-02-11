from src.model.City import City


class Country:
    def __init__(self, name, code):
        self.name: str = name
        self.code: str = code
        self.neighbours: [str] = []
        self.cities: [City] = []

    def add_neighbour(self, code):
        self.neighbours.append(code)
