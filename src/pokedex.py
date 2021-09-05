#!/usr/bin/env python3
import os
import json
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
searchError = {
                "error" : "Sorry didn't understand you. Please Enter a <b>valid</b> pokemon name or <b>ID (upto 890)</b> to get info"
            }

# Open the existing JSON file for loading into a variable
with open(os.path.dirname(os.path.realpath(__file__))+'/Utils/pokemon.min.json') as jsondata:
    pokemons = json.load(jsondata)

# Get params in a list
def getList(list):
    elements_str = ""
    if len(list) > 0:
        for element in list:
            elements_str += element.capitalize() + " "
    else: 
        elements_str = list[0].capitalize()
    return elements_str

# Format the json result of the pokemon search
def format_result(pokemon):
    output = {
        "name"      : pokemon["name"], 
        "number"    : pokemon["number"],
        "type"      : getList(pokemon["type"]),
        "weight"    : str(pokemon["weight"]),
        "height"    : str(pokemon["height"]), 
        "abilities" : getList(pokemon["abilities"]),
        "weakness"  : getList(pokemon["weakness"]),
        "image"     : pokemon["ThumbnailImage"]
    }
    return output

# get a Pokemon by Id number
def getPokemonById(id_name):
    logger.info("Searching Pokemon by ID with value " + id_name)
    pokemon = list(filter(lambda x:x["id"]==int(id_name),pokemons))
    pokemon = pokemon[0]
    output = format_result(pokemon)
    return output

# get a Pokemon by Name
def getPokemonByName(id_name):
    logger.info("Searching Pokemon by Name with value " + id_name)
    results = []
    for pokemon in pokemons:
        if  id_name.lower() in pokemon["slug"]:
            results.append(format_result(pokemon))
    if len(results) == 0:
        results = searchError
    return results
    
# main function
def pokedex(id_name):
    output = ""
    if id_name.isnumeric():
        if int(id_name) in range(1,890):
            output = getPokemonById(id_name)
        else:
            output = searchError
    elif id_name.isalpha():
        output = getPokemonByName(id_name)

    return output