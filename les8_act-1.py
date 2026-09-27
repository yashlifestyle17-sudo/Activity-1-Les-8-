pasta = ("Maggie Pasata", "Italian", 20 ,"Median")
biryani = ("Mutton Biryani", "Indian", 40, "Easy")

print("Recipe 1: ", pasta)
print("Name: ", pasta[0])
print("Cuisine: ", pasta[1])
print("Difficulty: ", pasta[-1])

all_recipe = (pasta, biryani)
print("\nFirst recipe name: ", all_recipe[0][0])
print("Second Recipe time", all_recipe[1][2], "min")
print("Pasta Details:", pasta[1:3])

print("\nPasta Recipe details: ")
for detail in pasta:
    print(" -", detail)

pasta_ingredients = {"tomato", "garlic", "oil", "chilli", "pasta", "garlic"}
biryani_ingredients = {"rice", "mutton", "garlic", "onion", "tomato", "spices/masala"}
print("\nPasta ingredients:", pasta_ingredients)
print("Briyani ingredients:", biryani_ingredients)
print("Total pasta ingredients", len(pasta_ingredients))

#variables for comparing
all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_ingredients = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll ingredients:", all_ingredients)
print("Common ingredients:", common)
print("Only in Pasta:", only_pasta)
print("Not shared:", unique_ingredients)

