import codecs
import random
from operator import index
from typing import Optional, Any

from src.model.City import City
from src.model.Country import Country
import csv


class World:
    def __init__(self):
        self.countries: {str: Country} = {}

    def parse_data(self):
        with open('DataFiles/GEODATASOURCE-COUNTRY-BORDERS.CSV', 'r') as country_border_file:
            reader = csv.reader(country_border_file)

            for row in reader:
                # print(row)
                if row[0] not in self.countries.keys():
                    self.countries[row[0]] = Country(row[1], row[0])
                self.countries.get(row[0]).add_neighbour(row[2])

        with codecs.open('DataFiles/worldcities.csv', 'r', encoding='utf-8', errors='ignore') as world_cities_file:
            city_reader = csv.reader(world_cities_file)
            for row in city_reader:
                if city_reader.line_num == 1:
                    continue
                country_code = row[5]
                if country_code not in self.countries.keys():
                    country = self.country_from_name(row[4])
                    if country is None:
                        # print(row[4])
                        # print("MISSION FAILED")
                        # Gaza Strip, West Bank and Kosovo is not included in the other country data set,
                        # TODO: do I fix this?
                        pass
                else:
                    country = self.countries.get(country_code)
                if country is not None:
                    # print(f'name: {row[0]}, lat/long: {row[2], row[3]}, pop: {row[9]}')
                    city = City(row[0], row[2], row[3], row[9])
                    country.cities.append(city)

    def print_country_data(self, country: Country):
        print(f'Name: {country.name}')
        if country.neighbours != []:
            print(f'Neighbours ({len(country.neighbours)}):')
            neighbours = []
            for neighbour in country.neighbours:
                try:
                    neighbours.append(self.countries.get(neighbour).name)
                except AttributeError:
                    pass
            print(neighbours)
        print(f'Some major cities ({len(country.cities)}):')
        cities = []
        for i in range(min(5, len(country.cities))):
            city = country.cities[i]
            cities.append((city.name, str(round(city.population, -3))[:-3] + "k"))
        print(cities)

    def is_valid_input(self, user_input):
        if user_input in self.countries.keys():
            return True
        for code, country in self.countries:
            if country.name == user_input:
                return True
        return False

    def get_country(self, user_input) -> [Country]:
        if user_input in self.countries.keys():
            return [self.countries.get(user_input)]

        matching = []
        for code, country in self.countries.items():
            if user_input.lower() in country.name.lower():
                matching.append(country)

        return matching

    def get_specified_country(self, matching_countries) -> Optional[Country]:
        print("Did you mean...")
        for i, country in enumerate(matching_countries):
            print(f'{str(i + 1)}: {country.name}')
        index_selected = input("Select country by choosing number (or go back by pressing enter) ->")
        try:
            return matching_countries[int(index_selected) - 1]
        except (IndexError, TypeError, ValueError):
            return None

    def country_from_name(self, name):
        for code, country in self.countries.items():
            if name.lower() in country.name.lower():
                return country

        return None

    def get_random_country(self):
        country = self.country_from_name("Holy See")
        while len(country.cities) <= 1:
            country = random.choice(list(self.countries.values()))
        print("Random country: " + country.name)
        return country








