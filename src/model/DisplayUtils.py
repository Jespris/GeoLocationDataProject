from src.model.City import City
from src.model.Country import Country


class DisplayUtils:
    @staticmethod
    def get_country_dimensions(country):
        left_most: City = country.cities[0]
        up_most: City = country.cities[0]
        down_most: City = country.cities[0]
        right_most: City = country.cities[0]
        smallest: City = country.cities[-1]
        largest: City = country.cities[0]
        for city in country.cities:
            if city.longitude < left_most.longitude:
                left_most = city
            elif city.longitude > right_most.longitude:
                right_most = city
            if city.latitude > up_most.latitude:
                up_most = city
            elif city.latitude < down_most.latitude:
                down_most = city
            if city.population > largest.population:
                largest = city
            elif city.population < smallest.population:
                smallest = city
        return left_most.longitude, \
            abs(up_most.latitude - 90), \
            (right_most.longitude - left_most.longitude), \
            (up_most.latitude - down_most.latitude), \
            smallest.population, \
            largest.population
