"""
As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, represented by the string observed_species. Each character in observed_species denotes a species observed in the region.

Your task is to determine how many instances of the observed species are also considered endangered.

Note: Species are case-sensitive, so "a" is considered a different species from "A".

Write a function to count the number of endangered species observed.

def count_endangered_species(endangered_species, observed_species):
    pass
Example Usage:

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  
Example Output:

3 # `a` and `A` are endangered species. `a` appears once, and `A` twice.
0

U
Your task is to determine how many instances of the observed species are also considered endangered.


P
Use a nested loop 
Using a counter for observed species and loop through endangered species checking if the specie is present in the counter and adding the count


I
"""
def count_endangered_species(endangered_species, observed_species):
    from collections import Counter
    count = 0
    specie_frequency = Counter(observed_species)
    for char in set(endangered_species):
        count += specie_frequency[char]
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2)) 