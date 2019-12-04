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
        self.types = json["types"]
        self.abilities = json["abilities"]
        self.moves = [(move['move'], move['version_group_details'][0]['level_learned_at'])
                      for move in json['moves']]

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Height: {self.height} decimetres\n" \
               f"Weight: {self.weight} hectograms\n" \
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


class Request:

    def __init__(self):
        self.pokedex_state = None
        self.input_name = None
        self.input_file = None
        self.expanded = None
        self.output = None

    def __str__(self):
        return f"Request: State: {self.pokedex_state}, Data: {self.input_name}" \
               f", {self.input_file} Input file: {self.expanded}, Output: {self.output}, "


def setup_request_commandline():

    parser = argparse.ArgumentParser()
    parser.add_argument("mode",
                        help="The mode in which you wish to open the pokedex"
                             "ex. 'pokemon' mode can only search pokemon")
    parser.add_argument("name",
                        help="File for bulk queries, name or id "
                             "for single queries")
    parser.add_argument("-e", "--expanded", action="store_true",
                        help="Optional flag to expand certain attributes"
                             "within the pokedex.")
    parser.add_argument("-o", "--output",
                        help="Optional flag, if provided, a filename must"
                             "also be provided. Query result will be printed"
                             "to this file"),
    args = parser.parse_args()
    request = Request()
    request.mode = args.mode
    if '.txt' in args.name:
        request.input_file = args.name
    else:
        request.input_name = args.name
    request.name = args.name
    request.expanded = args.expanded
    request.output = args.output
    return request


def main(request):
    if request.mode == 'pokemon':
        data = asyncio.run(get_pokemon_data(request.name))
        pokemon = Pokemon(data)
        print(pokemon)
    elif request.mode == 'ability':
        asyncio.run(get_ability_data(request.name))
        data = asyncio.run(get_ability_data(request.name))
        ability = Ability(data)
        print(ability)
    else:
        asyncio.run(get_move_data(request.name))
        data = asyncio.run(get_move_data(request.name))
        move = Move(data)
        print(move)


if __name__ == '__main__':
    main(setup_request_commandline())
'''    request = setup_request_commandline()
    main(request)'''