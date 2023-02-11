from src.model.World import World


def main():
    world = World()
    world.parse_data()

    while True:
        user_input = input("Enter country code / name ->")
        matching_countries = world.get_country(user_input)
        if len(matching_countries) == 1:
            world.print_country_data(matching_countries[0])
        elif len(matching_countries) >= 1:
            country = world.get_specified_country(matching_countries)
            if country is not None:
                world.print_country_data(country)
        else:
            print("Please enter a valid country code / name")


if __name__ == "__main__":
    main()

