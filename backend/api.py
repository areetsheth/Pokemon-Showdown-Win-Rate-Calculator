# import pandas as pd
from flask import Flask, request, jsonify
# from flask import request, jsonify
import os
if os.getenv('LOCAL_ENV'):
    import collect_data
else:
    import backend.collect_data as collect_data
import numpy as np
from scipy.stats import norm

app = Flask(__name__)

data = collect_data.load_csv()


@app.route('/pokemon/id/<int:pokemon_id>', methods=['GET'])
def get_pokemon_by_id(pokemon_id):
    pokemon = data[data['pokedex_number'] == pokemon_id]
    if pokemon.empty:
        return 'Pokemon not found', 404
    return pokemon['name'].values[0]


@app.route('/pokemon/name/<string:pokemon_name>', methods=['GET'])
def get_pokemon_by_name(pokemon_name):
    pokemon = data[data['name'] == pokemon_name]
    if pokemon.empty:
        return 'Pokemon not found', 404
    return str(pokemon['pokedex_number'].values[0])


@app.route('/pokemon/info/<int:pokemon_id>', methods=['GET'])
def get_pokemon_info_by_id(pokemon_id):
    pokemon = data[data['pokedex_number'] == pokemon_id]
    if pokemon.empty:
        return 'Pokemon not found', 404
    return pokemon.to_dict(orient='records')[0]


@app.route('/pokemon/characteristic/<int:pokemon_id>/<string:characteristic>',
           methods=['GET'])
def get_pokemon_characteristic_by_id(pokemon_id, characteristic):
    pokemon = data[data['pokedex_number'] == pokemon_id]
    if pokemon.empty:
        return 'Pokemon not found', 404
    return str(pokemon[characteristic].values[0])


@app.route('/pokemon/classification/<string:classification>', methods=['GET'])
def get_pokemon_by_classification(classification):
    pokemon = data[data['classification'] == classification]
    if pokemon.empty:
        return 'Pokemon not found', 404
    return pokemon['name'].values.tolist()


@app.route('/pokemon/sort_by/<string:column>', methods=['GET'])
def get_pokemon_sorted_by_column(column):
    allowable = ["attack", "defense", "hp", "sp_attack", "sp_defense",
                 "speed", "height_m", "weight_kg"]
    if column in allowable:
        temp = data.sort_values(by=column, ascending=False)
        if temp.empty:
            return 'Pokemon not found', 404
        return temp.loc[:, ['name', column]].values.tolist()
    else:
        return 'Column not allowed', 400


@app.route('/pokemon/legendary', methods=['GET'])
def get_legendary_pokemon():
    pokemon = data[data['status'] == 'Legendary']
    if pokemon.empty:
        return 'Pokemon not found', 404
    return pokemon['name'].values.tolist()


@app.route('/odds', methods=['GET'])
def get_odds(pokemon_id_1=0, pokemon_id_2=0, p1_level=0, p2_level=0):
    if 'pokemon1' in request.args and 'pokemon2' in request.args and 'level1' in request.args and 'level2' in request.args:
        pokemon_id_1 = int(request.args.get('pokemon1'))
        pokemon_id_2 = int(request.args.get('pokemon2'))
        p1_level = int(request.args.get('level1'))
        p2_level = int(request.args.get('level2'))
    pokemon_1 = data[data['pokedex_number'] == pokemon_id_1]
    pokemon_2 = data[data['pokedex_number'] == pokemon_id_2]
    if pokemon_1.empty or pokemon_2.empty:
        return 'Pokemon not found', 404
    info1 = get_pokemon_info_by_id(pokemon_id_1)
    info2 = get_pokemon_info_by_id(pokemon_id_2)

    p1_attack = info1['attack']
    p2_attack = info2['attack']

    p1_multiplier = 1
    p2_multiplier = 1
    p1_type1 = info1['type1'].lower()
    p2_multiplier *= info2['against_'+p1_type1]
    if not isinstance(info1['type2'], float):
        p1_type2 = info1['type2'].lower()
        p2_multiplier *= info2['against_'+p1_type2]
    p2_type1 = info2['type1'].lower()
    p1_multiplier *= info1['against_'+p2_type1]
    if not isinstance(info2['type2'], float):
        p2_type2 = info2['type2'].lower()
        p1_multiplier *= info1['against_'+p2_type2]

    p1_defense = info1['defense']
    p2_defense = info2['defense']
    p1_speed = info1['speed']
    p2_speed = info2['speed']
    p1_hp = info1['hp']
    p2_hp = info2['hp']
    p1_weight = info1['weight_kg']
    p2_weight = info2['weight_kg']

    p1_damage = ((((2 * p1_level) / 5 + 2) * p1_attack / p2_multiplier / p1_defense) / 50 + 2) * 1.5 * p1_multiplier * np.random.unifortm(0.85, 1)
    p2_damage = ((((2 * p2_level) / 5 + 2) * p2_attack / p1_multiplier / p2_defense) / 50 + 2) * 1.5 * p2_multiplier * np.random.uniform(0.85, 1)

    p1 = p1_damage 
    p2 = p2_damage 

    p1_sd = 0.2 * np.sqrt(p1_defense**2 + p1_speed**2 + p1_hp**2 + p1_weight**2)
    p2_sd = 0.2 * np.sqrt(p2_defense**2 + p2_speed**2 + p2_hp**2 + p2_weight**2)
    sd_comb = np.sqrt(p1_sd**2 + p2_sd**2)
    if p1 > p2:
        mean_diff = p1 - p2
        dist = norm(loc=mean_diff, scale=sd_comb)
        odds = 1 - dist.cdf(0)
        return jsonify({'odds': odds, 'Winner': info1['name'] + " beats " + info2['name'], 'p1': p1, 'p2': p2})
    elif p1 < p2:
        mean_diff = p2 - p1
        dist = norm(loc=mean_diff, scale=sd_comb)
        odds = dist.cdf(0)
        return jsonify({'odds': odds, 'Winner': info1['name'] + " loses to " + info2['name'], 'p1': p1, 'p2': p2})
    else:
        return jsonify({'odds': 0.5, 'Winner': info1['name'] + " ties " + info2['name']})


@app.route('/compare', methods=['GET'])
def compare_teams(pokemon1=1, pokemon2=2, pokemon3=3, pokemon4=4, pokemon5=5, pokemon6=6, pokemon7=7, pokemon8=8, pokemon9=9, pokemon10=10, pokemon11=11, pokemon12=12, level1=50, level2=50, level3=50, level4=50, level5=50, level6=50, level7=50, level8=50, level9=50, level10=50, level11=50, level12=50):
    # there are 12 query parameters, 6 for each team
    # the query parameters are pokemon1, pokemon2, ..., pokemon12
    total = 0.0
    for i in range(1, 7):
        for j in range(7, 13):
            response = get_odds(int(request.args.get(f'pokemon{i}')), int(request.args.get(f'pokemon{j}')), int(request.args.get(f'level{i}')), int(request.args.get(f'level{j}')))
            data = response.json
            total += data['odds']

    team_1_pokedex = [int(request.args.get(f'pokemon{i}')) for i in range(1, 7)]
    team_2_pokedex = [int(request.args.get(f'pokemon{j}')) for j in range(7, 13)]
    team_1 = [get_pokemon_by_id(pokemon_id) for pokemon_id in team_1_pokedex]
    team_2 = [get_pokemon_by_id(pokemon_id) for pokemon_id in team_2_pokedex]

    return jsonify({'odds': total/36, 'team1': team_1, 'team2': team_2})


if __name__ == '__main__':
    app.run(debug=True)
