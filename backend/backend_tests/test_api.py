from backend import api


def test_get_pokemon_by_id():
    assert api.get_pokemon_by_id(1) == 'Bulbasaur'
    assert api.get_pokemon_by_id(-1)[0] == 'Pokemon not found'


def test_get_pokemon_by_name():
    assert api.get_pokemon_by_name('Bulbasaur') == '1'
    assert api.get_pokemon_by_name('Not a Pokemon')[0] == 'Pokemon not found'


def test_get_pokemon_info_by_id():
    assert api.get_pokemon_info_by_id(1)['name'] == 'Bulbasaur'
    assert api.get_pokemon_info_by_id(-1)[0] == 'Pokemon not found'


def test_get_pokemon_characteristic_by_id():
    assert api.get_pokemon_characteristic_by_id(1, 'height_m') \
        == "0.7"
    assert api.get_pokemon_characteristic_by_id(-1, 'abilities')[0] \
        == 'Pokemon not found'


def test_get_pokemon_by_classification():
    assert api.get_pokemon_by_classification('Seed Pokémon') \
        == ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Mega Venusaur', 'Sunkern']
    assert api.get_pokemon_by_classification('Not a classification')[0] \
        == 'Pokemon not found'


def test_get_pokemon_sorted_by_column():
    assert api.get_pokemon_sorted_by_column('attack')[1] == ['Mega Heracross', 185]
    assert api.get_pokemon_sorted_by_column('Not a column')[0] \
        == 'Column not allowed'


def test_get_legendary_pokemon():
    assert api.get_legendary_pokemon()[0] == 'Mewtwo'
