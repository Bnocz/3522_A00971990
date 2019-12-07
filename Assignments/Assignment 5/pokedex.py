import argparse
import aiohttp
import asyncio


class ApiDataHandler:
    """
    Class to asynchronously collect data from pokeAPI. Has 3 methods to get pokemon,
    ability, or move data using asyncio
    """
    async def get_pokemon_data(id: str) -> dict:
        """
        gets pokemon data from pokeAPI, takes in a str as the ID to search
        the API.
        :return: JSON dict
        """
        url = "https://pokeapi.co/api/v2/pokemon/{}/"
        async with aiohttp.ClientSession() as session:
            target_url = url.format(id)
            response = await session.get(url=target_url)
            return await response.json()

    async def get_move_data(id: int) -> dict:
        """
        gets move data from pokeAPI, takes in a str as the ID to search
        the API.
        :return: JSON dict
        """
        url = "https://pokeapi.co/api/v2/move/{}/"
        async with aiohttp.ClientSession() as session:
            target_url = url.format(id)
            response = await session.get(url=target_url)
            return await response.json()

    async def get_ability_data(id: int) -> dict:
        """
        gets ability data from pokeAPI, takes in a str as the ID to search
        the API.
        :return: JSON dict
        """
        url = "https://pokeapi.co/api/v2/ability/{}/"
        async with aiohttp.ClientSession() as session:
            target_url = url.format(id)
            response = await session.get(url=target_url)
            return await response.json()

    async def get_pokemon_data_expanded(url: str) -> dict:
        """
        gets pokemon data from pokeAPI, takes in a str as the ID to search
        the API.
        :return: JSON dict
        """
        async with aiohttp.ClientSession() as session:
            target_url = url
            response = await session.get(url=target_url)
            return await response.json()


class FileHandler:
    """
    class to handle files. Currently only has a function
    to append to a user-given file with the output
    """

    def print_output_to_file(file_path, string):
        with open(file_path, "a") as file_to_write:
            file_to_write.write(string)


class Pokemon:
    """
    Adapter class for Pokemon data. Takes data from get_pokemon_data function and fills in
    attributes using the json dictionary provided.
    """
    def __init__(self, json):
        """
        initializes attributes from JSON dictionary provided by get_pokemon_data
        :param json: json Dictionary
        """
        self.json = json
        self.name = json["name"]
        self.id = json["id"]
        self.height = json["height"]
        self.weight = json["weight"]
        self.types = json["types"]
        self.abilities = json["abilities"]
        self.abilities_formatted = [f"Ability: {x['ability']['name']} URL: {x['ability']['url']}"
                                    for x in self.abilities]
        self.moves = [(move['move'], move['version_group_details'][0]['level_learned_at'])
                      for move in json['moves']]

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Height: {self.height} decimetres\n" \
               f"Weight: {self.weight} hectograms\n" \
               f"Types: {self.types}\n" \
               f"Abilities: {self.abilities_formatted}\n" \
               f"Moves: {self.moves}\n" \
               f"\n"


class Ability:
    """
    Adapter class for Ability data. Takes data from get_ability_data function and fills in
    attributes using the json dictionary provided.
    """
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
               f"Pokemon: {self.pokemon}\n" \
               f"\n"


class Move:
    """
    Adapter class for Move data. Takes data from get_move_data function and fills in
    attributes using the json dictionary provided.
    """
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
               f"Effect: {self.effect_short}\n" \
               f"\n"


class PokemonExpanded(Pokemon):
    """
    wrapper for Pokemon class that contains the expanded attributes when user enters
    --expanded or -e in argparse.
    """

    def __init__(self, json):
        super().__init__(json)
        self.stats = json['stats']
        self.formatted_stats = [f"{x['stat']['name']}: {x['base_stat']}" for x in self.stats]
       #self.abilities_effect = json['effect_entries']['effect']
        #self.abilities_effect_short = json['effect_entries']['short_effect']
        #self.abilities_generation = json['generation']
        #self.abilities_pokemon = json['pokemon']['pokemon']['name']

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Height: {self.height} decimetres\n" \
               f"Weight: {self.weight} hectograms\n" \
               f"Types: {self.types}\n" \
               f"Stats: {self.formatted_stats}\n" \
               '''f"Abilities: {self.abilities_formatted}" \
               f"Abilities Expanded: {self.abilities_effect}, {self.abilities_effect_short}. {self.abilities_generation}" \
               f"{self.abilities_pokemon}\n" \
               f"Moves: {self.moves}\n"'''


class Request:
    '''
    Class to store command line requests entered by user.
    Fills attributes through command line and passes request
    to main method.
    '''

    def __init__(self):
        self.pokedex_state = None
        self.input_name = None
        self.input_file = None
        self.expanded = None
        self.output = None

    def __str__(self):
        return f"Request: State: {self.pokedex_state}, Data: {self.input_name}" \
               f", {self.input_file} Input file: {self.expanded}, Output: {self.output}, "


class ArgParser:
    """
    Fills an object of type Request with command line
    arguments supplied by user. Has arguments to set
    mode of pokedex, and accept query input
    """
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
    """
    driver method for class. Takes a request object,
    and based on its attributes queries the pokedex for
    the requested data.
    :param request:
    :return:
    """
    if request.input_file is None:
        if request.mode == 'pokemon':
            data = asyncio.run(ApiDataHandler.get_pokemon_data(request.input_name))
            pokemon = Pokemon(data)
            if request.output is not None:
                FileHandler.print_output_to_file(request.output, pokemon.__str__())
            else:
                print(pokemon)
        elif request.mode == 'ability':
            asyncio.run(ApiDataHandler.get_ability_data(request.name))
            data = asyncio.run(ApiDataHandler.get_ability_data(request.name))
            ability = Ability(data)
            if request.output is not None:
                FileHandler.print_output_to_file(request.output, ability.__str__())
            else:
                print(ability)
        else:
            asyncio.run(ApiDataHandler.get_move_data(request.name))
            data = asyncio.run(ApiDataHandler.get_move_data(request.name))
            move = Move(data)
            if request.output is not None:
                FileHandler.print_output_to_file(request.output, move.__str__())
            else:
                print(move)
    else:
        if request.mode == 'pokemon':
            with open(request.input_file) as query_data:
                for line in query_data:
                    line_new = line.replace("\n", "")
                    data = asyncio.run(ApiDataHandler.get_pokemon_data(line_new))
                    if request.expanded is True:
                        pokemon = PokemonExpanded(data)
                        if request.output is not None:
                            FileHandler.print_output_to_file(request.output, pokemon.__str__())
                        else:
                            print(pokemon)
                    else:
                        pokemon = Pokemon(data)
                        if request.output:
                            FileHandler.print_output_to_file("output.txt", pokemon.__str__())
                        else:
                            print(pokemon)
        elif request.mode == 'ability':
            with open(request.input_file) as query_data:
                for line in query_data:
                    line_new = line.replace("\n", "")
                    data = asyncio.run(ApiDataHandler.get_ability_data(line_new))
                    ability = Ability(data)
                    if request.output is not None:
                        FileHandler.print_output_to_file(request.output, ability.__str__())
                    else:
                        print(ability)
        else:
            with open(request.input_file) as query_data:
                for line in query_data:
                    line_new = line.replace("\n", "")
                    data = asyncio.run(ApiDataHandler.get_move_data(line_new))
                    move = Move(data)
                    if request.output is not None:
                        FileHandler.print_output_to_file(request.output, move.__str__())
                    else:
                        print(move)


if __name__ == '__main__':
    main(ArgParser.setup_request_commandline())
