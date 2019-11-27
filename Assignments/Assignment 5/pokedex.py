import argparse

import aiohttp
import asyncio


async def get_pokemon_data(id: str) -> dict:
    url = "https://pokeapi.co/api/v2/pokemon/{}/"
    async with aiohttp.ClientSession() as session:
        target_url = url.format(id)
        response = await session.get(url=target_url)
        return await response.json()

async def get_move_data(id: int) -> dict:
    url = "https://pokeapi.co/api/v2/move/{}/"
    async with aiohttp.ClientSession() as session:
        target_url = url.format(id)
        response = await session.get(url=target_url)
        return await response.json()

async def get_ability_data(id: int) -> dict:
    url = "https://pokeapi.co/api/v2/ability/{}/"
    async with aiohttp.ClientSession() as session:
        target_url = url.format(id)
        response = await session.get(url=target_url)
        return await response.json()


class Pokemon:

    def __init__(self, json):
        self.json = json
        self.name = json["name"]
        self.id = json["id"]
        self.height = json["height"]
        self.weight = json["weight"]
        self.stats = json["stats"]
        self.types = json["types"]
        self.abilities = json["abilities"]
        self.moves = json["moves"]

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Height: {self.height} decimetres\n" \
               f"Weight: {self.weight} hectograms\n" \
               f"Stats: {self.stats}\n" \
               f"Types: {self.types}\n" \
               f"Abilities: {self.abilities}\n" \
               f"Moves: {self.moves}\n"


class Ability:

    def __init__(self, json):
        self.json = json
        self.name = json["name"]
        self.id = json["id"]
        self.generation = json["generation"]["name"]
        self.effect = json["effect_entries"][0]["effect"]
        self.effect_short = json["effect_entries"][0]["short_effect"]
        self.pokemon = json["pokemon"]

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation Introduced: {self.generation}\n" \
               f"effect: {self.effect}\n" \
               f"effect(short): {self.effect_short}\n" \
               f"Pokemon: {self.pokemon}\n"


class Move:
    def __init__(self, json):
        self.json = json
        self.name = json["name"]
        self.id = json["id"]
        self.generation = json["generation"]['name']
        self.accuracy = json["accuracy"]
        self.pp = json['pp']
        self.power = json['power']
        self.type = json['type']
        self.damage_class = json['damage_class']
        self.effect_short = json['effect_entries'][0]['short_effect']

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation Introduced: {self.generation}\n" \
               f"Accuracy: {self.accuracy}\n" \
               f"PP: {self.pp}\n" \
               f"Power: {self.power}\n" \
               f"Type: {self.type}\n" \
               f"Physical/Special: {self.damage_class}\n" \
               f"Effect: {self.effect_short}"


def setup_request_commandline():
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("pokemon", "ability", "move",
                        help="The mode in which you wish to open the pokedex"
                             "ex. 'pokemon' mode can only search pokemon")
    parser.add_argument("filename.txt", "name or id",
                        help="File for bulk queries, name or id "
                             "for single queries")
    parser.add_argument("-e", "--expanded",
                        help="Optional flag to expand certain attributes"
                             "within the pokedex.")
    parser.add_argument('-o "filename.txt"', '--output "filename.txt',
                        help="Optional flag, if provided, a filename must"
                             "also be provided. Query result will be printed"
                             "to this file"),
'''    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()'''


if __name__ == '__main__':
    data = asyncio.run(get_move_data(5))
    move = Move(data)
    print(move)