

if __name__ == "__main__":


    pokemon_types = {
        # Key    :  Value 
        'Pikachu': 'electric',
        'Bulbasaur': 'grass',
        'Charmander': 'fire'
    }

    # print(pokemon_types)

    # pokemon_types_pair = (
    #     ('Pikachu', 'electric'),
    #     ('Bulbasaur', 'grass'),
    #     ('Charmander', 'fire'),
    # )

    # pokemon_types_from_tuple = dict(pokemon_types_pair)
    # print(pokemon_types_from_tuple)

    # print('Mew' in pokemon_types)

    # print(pokemon_types.get('Pikachu', 'Unknown'))

    pokemon_types['Mew'] = 'psychic'
    # pokemon_types['Squirtel'] = 'water'
    # print(pokemon_types)

    # del pokemon_types['Squirtel']
    # print(pokemon_types)

    pokemon_types['Squirtle'] = 'water'
    # print(pokemon_types)

    # for key, value in pokemon_types.items():
    #     print(f'Pokemon {key} is of type {value}')


    pokedex = {
        25 : {
            'name': 'Pikachu',
            'type': 'electric'
        },
        1 : {
            'name': 'Bulbasaur',
            'type': 'grass'
        },
        4 : {
            'name': 'Charmander',
            'type': 'fire'
        }
    }

    print(pokedex)
    print(pokedex[25]['name'])
