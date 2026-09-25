"""
Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns the species with the highest conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated with a species, including its name, habitat, and wild population. The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.

def most_endangered(species_list):
    pass
Example Usage:

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))
Example Output:

Vaquita

U
return the name of the species with the lowest population
output-> string
input-> dictionary
if more than one specie have the same population, return the one with the lowest index

P 
loop through the species_list and keep track of the lowest population and associated specie name

I


"""
def most_endangered_specie(species_list):
    min_population = float('inf')
    specie_name = ""
    for _, specie in enumerate(species_list):
        if specie['population'] < min_population:
            min_population = specie['population']
            specie_name = specie['name']
    return specie_name


species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Maine",
     "habitat": "Marine",
     "population": 10
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered_specie(species_list))


