# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os
import requests
import json


# Load the downloaded data
def load_csv():
    # loads csv data, function can be used in other places
    pokemon = pd.read_csv('backend/data/pokemon_all.csv')
    return pokemon


def create_json():
    # Create a json file with pokeapi data
    url = 'https://pokeapi.co/api/v2/pokemon/'
    pokeapi_data = {}
    for i in range(1, 1026):
        data = requests.get(url + str(i))
        if i == 0:
            pokeapi_keys = set(data.json().keys())
        if data.status_code == 200:
            pokeapi_data[i] = data.json()
        else:
            print('Error: ', data.status_code)
    return pokeapi_keys, pokeapi_data


# Run main function to obtain pokeapi data of all pokemon on your local machine
if __name__ == '__main__':
    pokeapi_data = create_json()
    with open('data/pokeapi_data.json', 'w') as json_file:
        json.dump(pokeapi_data, json_file, indent=4)
