function insertPokemonInList(pokemon) {
    let dropdowns = document.getElementsByClassName('pokemon-dropdown'); // Get all dropdowns to fill with pokemon
    let newOption = document.createElement("option");
    newOption.textContent = pokemon.name;
    newOption.value = pokemon.num;
    for (let i = 0; i < dropdowns.length; ++i) {
        let dropdown = dropdowns[i];
        dropdown.append(newOption.cloneNode(true));
    }
}

var CSV_URL = 'https://raw.githubusercontent.com/Bezbakri/extras/main/pokemon.csv'; // Shenanigans to read the csv without issues with CORS


$.get(CSV_URL, function (data) {
    let lines = data.split("\n");
    // Skip first row since it contains the CSV header
    lines.shift();

    /*
    Transform each line into an object {num: xx, name: xx}
    */
    let pokemons = lines.map(function (line) {
      let fields = line.split(",");
      return {
        num: fields[0], 
        name: fields[1]
      };
    });

    // Then append every pokemon to our list
    for (let i = 0; i < pokemons.length - 1; ++i) {
      insertPokemonInList(pokemons[i]);
    }

});

$(document).ready(function () {
    $("#pokemon-teams").on("submit", function(event) {
        event.preventDefault();

        let formValues = $(this).serialize();
        let url = "http://localhost/backend/api.py";
        let dummy_url = "https://httpbin.org/post"        // To see if everything else works
        $.ajax({
          type: "POST",
          url: url,         
          data: formValues,
          dataType: "json",
          success: function (response) {
            console.log(formValues);
          }, 
          error : function(response) {
              alert("Please select all values");
          }
        });
    });
});

function getImageUrl(value){
    let url;
    if (value == "null") {
        url = "images/null.png";
    } else {
        url = "../sprites/" + value + ".png";
    }
    return url;
}