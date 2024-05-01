import os
import urllib.request


def download_sprites():
    directory = "sprites/"
    base_url = "https://www.serebii.net/pokemon/art/"
    num_pokemon = 1025
    try:
        os.mkdir(directory)
    except Exception:
        pass
    for i in range(1, num_pokemon + 1):
        cur_pokemon_file = str(i) + ".png"
        if i < 10:
            cur_pokemon_file = "00" + cur_pokemon_file
        elif i < 100:
            cur_pokemon_file = "0" + cur_pokemon_file
        url = base_url + cur_pokemon_file
        file_name = directory + cur_pokemon_file
        urllib.request.urlretrieve(url, file_name)


if __name__ == "__main__":
    download_sprites()
