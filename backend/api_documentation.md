# Pokemon API Documentation

This document provides documentation for the Pokemon API, which allows users to retrieve information about Pokemon and calculate odds of battles between them.

## Endpoints

### Get Pokemon by ID

**URL:** `/pokemon/id/<int:pokemon_id>`
**Method:** `GET`

**Description:** Retrieves information about a Pokemon based on its Pokedex number.

**Parameters:**
- `pokemon_id` (integer): The Pokedex number of the Pokemon.

**Response:**
- Success (200 OK):
  - Body: Name of the Pokemon.
- Error (404 Not Found):
  - Body: "Pokemon not found".

### Get Pokemon by Name

**URL:** `/pokemon/name/<string:pokemon_name>`
**Method:** `GET`

**Description:** Retrieves the Pokedex number of a Pokemon based on its name.

**Parameters:**
- `pokemon_name` (string): The name of the Pokemon.

**Response:**
- Success (200 OK):
  - Body: Pokedex number of the Pokemon.
- Error (404 Not Found):
  - Body: "Pokemon not found".

### Get Pokemon Info by ID

**URL:** `/pokemon/info/<int:pokemon_id>`
**Method:** `GET`

**Description:** Retrieves detailed information about a Pokemon based on its Pokedex number.

**Parameters:**
- `pokemon_id` (integer): The Pokedex number of the Pokemon.

**Response:**
- Success (200 OK):
  - Body: JSON object containing various attributes of the Pokemon, such as name, types, stats, etc.
- Error (404 Not Found):
  - Body: "Pokemon not found".

### Get Pokemon Characteristic by ID

**URL:** `/pokemon/characteristic/<int:pokemon_id>/<string:characteristic>`
**Method:** `GET`

**Description:** Retrieves a specific characteristic of a Pokemon based on its Pokedex number.

**Parameters:**
- `pokemon_id` (integer): The Pokedex number of the Pokemon.
- `characteristic` (string): The characteristic to retrieve (e.g., "attack", "defense", "hp").

**Response:**
- Success (200 OK):
  - Body: Value of the specified characteristic for the Pokemon.
- Error (404 Not Found):
  - Body: "Pokemon not found".

### Get Pokemon by Classification

**URL:** `/pokemon/classification/<string:classification>`
**Method:** `GET`

**Description:** Retrieves a list of Pokemon with a specific classification.

**Parameters:**
- `classification` (string): The classification of Pokemon to retrieve.

**Response:**
- Success (200 OK):
  - Body: List of names of Pokemon belonging to the specified classification.
- Error (404 Not Found):
  - Body: "Pokemon not found".

### Get Pokemon Sorted by Column

**URL:** `/pokemon/sort_by/<string:column>`
**Method:** `GET`

**Description:** Retrieves Pokemon sorted by a specific column.

**Parameters:**
- `column` (string): The column by which to sort the Pokemon (e.g., "attack", "defense", "hp").

**Response:**
- Success (200 OK):
  - Body: List of Pokemon sorted by the specified column.
- Error (404 Not Found):
  - Body: "Pokemon not found".
- Error (400 Bad Request):
  - Body: "Column not allowed".

### Get Legendary Pokemon

**URL:** `/pokemon/legendary`
**Method:** `GET`

**Description:** Retrieves a list of legendary Pokemon.

**Response:**
- Success (200 OK):
  - Body: List of names of legendary Pokemon.
- Error (404 Not Found):
  - Body: "Pokemon not found".

### Get Odds of Battle

**URL:** `/odds`
**Method:** `GET`

**Description:** Calculates the odds of winning between two Pokemon in a battle.

**Parameters:**
- `pokemon1` (integer): Pokedex number of the first Pokemon.
- `pokemon2` (integer): Pokedex number of the second Pokemon.

**Query Parameters:**
- `pokemon1` (integer): Pokedex number of the first Pokemon.
- `pokemon2` (integer): Pokedex number of the second Pokemon.
- `level1` (integer): Level number of the first Pokemon.
- `level2` (integer): Level number of the second Pokemon. 

**Response:**
- Success (200 OK):
  - Body: JSON object containing odds of winning, winner's name, and battle statistics.
- Error (404 Not Found):
  - Body: "Pokemon not found".

### Compare Teams

**URL:** `/compare`
**Method:** `GET`

**Description:** Compares the odds of winning between two teams of Pokemon in a battle.

**Query Parameters:**
- `pokemon1` (integer): Pokedex number of the first Pokemon in Team 1.
- `pokemon2` (integer): Pokedex number of the second Pokemon in Team 1.
- ...
- `pokemon12` (integer): Pokedex number of the sixth Pokemon in Team 2.
- `level1` (integer): Level of the first Pokemon in Team 1. 
- `level2` (integer): Level of the second Pokemon in Team 1. 
- ...
- `level12` (integer): Level of the sixty Pokemon in Team 2. 

**Response:**
- Success (200 OK):
  - Body: JSON object containing average odds of winning, details of both teams, and battle statistics.
- Error (404 Not Found):
  - Body: "Pokemon not found".

#### Example:

**Request:**
GET /compare?pokemon1=1&pokemon2=2&pokemon3=3&pokemon4=4&pokemon5=5&pokemon6=6&pokemon7=7&pokemon8=8&pokemon9=9&pokemon10=10&pokemon11=11&pokemon12=12

**Response (200 OK):**
```json
{
  "odds": 0.743591928374092,
  "team1": [
    {"name": "Bulbasaur", "type1": "Grass", "type2": "Poison", ...},
    {"name": "Ivysaur", "type1": "Grass", "type2": "Poison", ...},
    ...
  ],
  "team2": [
    {"name": "Charmander", "type1": "Fire", "type2": None, ...},
    {"name": "Charmeleon", "type1": "Fire", "type2": None, ...},
    ...
  ]
}
