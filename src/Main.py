import math

from src.model.DisplayUtils import DisplayUtils
from src.model.GameState import Gamestate
from src.model.World import World

import pygame as p
from win32api import GetSystemMetrics

# GLOBALS
SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)
MAX_CITY_RADIUS = 50
MAX_FPS = 30


def main():
    world = World()
    world.parse_data()

    print("Which of the following things do you want to do? (Type the number and press enter)")
    print("1: Trivia game")
    print("2: Country search")
    user_choice = 0
    while user_choice == 0:
        try:
            user_choice = int(input("-> "))
        except (TypeError, ValueError, AttributeError):
            continue
        if user_choice >= 3:
            user_choice = 0

    if user_choice == 1:
        p.init()
        screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = p.time.Clock()

        gamestate = Gamestate(world)
        running = True
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.KEYDOWN:
                    if e.key == p.K_ESCAPE:
                        running = False
                    elif e.key == p.K_TAB:
                        gamestate.current_country = world.get_random_country()
                        # print("New country: " + gamestate.current_country.name)

            p.display.flip()
            screen.fill(p.Color("black"))
            gamestate.update(clock.get_rawtime())
            display(screen, gamestate)
            clock.tick(MAX_FPS)

    elif user_choice == 2:
        print("Type EXIT to exit")
        while True:
            user_input = input("Enter country code / name ->")
            if user_input == "EXIT":
                break
            matching_countries = world.get_country(user_input)
            if len(matching_countries) == 1:
                world.print_country_data(matching_countries[0])
            elif len(matching_countries) >= 1:
                country = world.get_specified_country(matching_countries)
                if country is not None:
                    world.print_country_data(country)
            else:
                print("Please enter a valid country code / name")


def display(screen, gamestate):
    if gamestate.current_country is not None:
        x, y, width, height, min_pop, max_pop = DisplayUtils.get_country_dimensions(gamestate.current_country)
        x -= width / 4
        y -= width / 4
        width *= 1.5
        height *= 1.5
        for city in gamestate.current_country.cities:
            city_x = int(((city.longitude - x) / width) * SCREEN_WIDTH)
            city_y = int(((abs(city.latitude - 90) - y) / height) * SCREEN_HEIGHT)
            radius = math.ceil((city.population / max_pop) * MAX_CITY_RADIUS)
            p.draw.circle(screen, p.Color("white"), (city_x, city_y), radius)


if __name__ == "__main__":
    main()

