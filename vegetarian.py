import web_scraping
import random
import inflect
## Need to install inflect library using pip!!!

def turn_vegetarian(soup, steps, ingredients):
    # Define the lists of non-vegetarian ingredients
    lean_meats = ["Beef", "Lamb", "Veal", "Pork", "Kangaroo", "Sausages", "Bacon", "Ham", "Salami", "Chorizo", "Pepperoni", "Prosciutto", "Pancetta", "Bresaola", "Mortadella", "Capocollo", "Coppa", "Guanciale", "Lardo", "Lomo", "Nduja", "Soppressata", "Speck", "Cotechino", "Zampone", "Blood sausage", "Black pudding", "White pudding", "Haggis", "Liverwurst", "Head cheese", "Pate", "Rillettes", "Terrine", "Galantine", "Ballotine", "Mousse", "Foie gras", "Trotters", "Tripe", "Sweetbreads", "Kidneys", "Liver", "Heart", "Tongue", "Brain", "Cheek", "Tail", "Feet", "Ears", "Snout", "Intestines", "Lungs", "Spleen", "Pancreas", "Thymus", "Testicles", "Oxtail", "Bone marrow", "Bone broth", "Bone meal", "Bone ash", "Bone char", "Bone gelatin", "Bone glue", "Steak", "Roast", "Chop", "Cutlet", "Filet", "Tenderloin", "Sirloin", "Rump", "Round", "Chuck", "Brisket", "Flank", "Skirt", "Shank", "Hock", "Knuckle", "Neck", "Rib", "Loin", "Belly", "Bacon", "Ham", "Sausage", "Salami", "Pepperoni", "Prosciutto", "Pancetta", "Bresaola", "Mortadella", "Capocollo", "Coppa", "Guanciale", "Lardo", "Lomo", "Nduja", "Soppressata", "Speck", "Cotechino", "Zampone", "Blood sausage", "Black pudding", "White pudding", "Haggis", "Liverwurst", "Head cheese", "Pate", "Rillettes", "Terrine", "Galantine", "Ballotine", "Mousse", "Foie gras", "Trotters", "Tripe", "Sweetbreads", "Kidneys", "Liver", "Heart", "Tongue", "Brain", "Cheek", "Tail", "Feet", "Ears", "Snout", "Intestines", "Lungs", "Spleen", "Pancreas", "Thymus", "Testicles", "Oxtail", "Bone marrow", "Bone broth", "Bone meal", "Bone ash", "Bone char", "Bone gelatin", "Bone glue", "Steak", "Roast", "Chop", "Cutlet", "Filet", "Tenderloin", "Sirloin", "Rump", "Round", "Chuck", "Brisket", "Flank", "Skirt", "Shank", "Hock", "Knuckle", "Neck", "Rib", "Loin", "Belly", "Bacon", "Ham", "Sausage", "Salami", "Pepperoni", "Prosciutto", "Pancetta", "Bresaola", "Mortadella", "Capocollo", "Coppa", "Guanciale", "Lardo", "Lomo", "Nduja", "Soppressata", "Speck"]
    poultry = ["Chicken", "Turkey", "Duck", "Emu", "Goose", "Bush birds", "Quail", "Pheasant", "Partridge", "Grouse", "Guinea fowl", "Pigeon", "Squab", "Ostrich", "Rhea", "Cassowary", "Kiwi", "Egg", "Egg white", "Egg yolk", "Eggshell", "Egg membrane", "Egg albumen", "Egg vitellus", "Egg chalaza", "Egg germinal disc", "Egg air cell", "Egg sac", "Egg cord", "Egg tooth", "Egg beater", "Egg separator", "Egg poacher", "Egg boiler", "Egg cooker", "Egg timer", "Egg cup", "Egg carton", "Egg box", "Egg crate", "Egg tray", "Egg cart", "Egg basket", "Egg rack", "Egg holder", "Egg stand", "Egg case", "Egg carrier", "Egg caddy"]
    fish_and_seafood = ["Fish", "Prawns", "Crab", "Lobster", "Mussels", "Oysters", "Scallops", "Clams", "Squid", "Octopus", "Crayfish", "Yabbies", "Abalone", "Sea urchin", "Sea cucumber", "Sea snails", "Fish roe", "Fish maw", "Fish fin", "Fish head", "Fish tail", "Fish bone", "Fish skin", "Fish scales", "Fish liver", "Fish gills", "Fish swim bladder", "Fish stomach", "Fish intestines", "Fish blood", "Fish eggs", "Fish sperm", "Fish oil", "Fish sauce", "Fish paste", "Fish stock", "Fish floss", "Fish ball", "Fish cake", "Fish sausage", "Fish jerky", "Fish fillet", "Fish steak", "Fish cutlet", "Fish finger", "Fish stick", "Fish pie", "Fish soup", "Fish stew", "Fish curry", "Fish salad", "Fish sandwich", "Fish burger", "Fish taco", "Fish wrap", "Fish roll", "Fish sushi", "Fish sashimi", "Fish tempura", "Fish katsu", "Fish teriyaki", "Fish kabayaki", "Fish shioyaki", "Fish nitsuke", "Fish nimono", "Fish nabe", "Fish chowder", "Fish bisque", "Fish bouillabaisse", "Fish paella", "Fish risotto", "Fish pasta", "Fish pizza", "Fish lasagna", "Fish casserole", "Fish gratin", "Fish quiche", "Fish souffle", "Fish mousse", "Fish terrine", "Fish pate", "Fish rillettes", "Fish ceviche", "Fish carpaccio", "Fish tartare", "Fish crudo", "Fish poke", "Fish donburi", "Fish chirashi", "Fish bento", "Fish onigiri", "Fish okonomiyaki", "Fish takoyaki", "Fish dorayaki", "Fish taiyaki", "Fish manju", "Fish mochi", "Fish dango", "Fish daifuku", "Fish wagashi", "Fish yokan", "Fish dorayaki"]

    # Create an inflect engine
    p = inflect.engine()

    # Convert all items in the lists to lowercase
    lean_meats = [meat.lower() for meat in lean_meats]
    poultry = [item.lower() for item in poultry]
    fish_and_seafood = [item.lower() for item in fish_and_seafood]

    # Add plural forms to the lists
    lean_meats_with_plurals = lean_meats + [p.plural(meat) for meat in lean_meats]
    poultry_with_plurals = poultry + [p.plural(item) for item in poultry]
    fish_and_seafood_with_plurals = fish_and_seafood + [p.plural(item) for item in fish_and_seafood]


    # Define the lists of vegetarian substitutes
    lean_meat_substitutes = ["Tofu", "Tempeh", "Seitan", "Jackfruit", "Lentils", "Mushrooms"]
    poultry_substitutes = ["Tofu", "Tempeh", "Seitan", "Chickpeas", "Cauliflower", "Mushrooms"]
    fish_and_seafood_substitutes = ["Tofu", "Tempeh", "Seaweed", "Hearts of palm", "Artichokes", "Mushrooms"]

    # Define the lists of flavoring substitutes
    flavoring_substitutes = {
        "Bone broth": "Vegetable broth",
        "Fish sauce": "Soy sauce",
        "Fish stock": "Vegetable stock",
        "Chicken broth": "Vegetable broth",
        "Chicken stock": "Vegetable stock",
        "Beef broth": "Vegetable broth",
        "Beef stock": "Vegetable stock"
    }

    # Replace non-vegetarian ingredients with vegetarian substitutes
    for ingredient in ingredients:
        words = ingredient['name'].split()
        if any(word in lean_meats_with_plurals for word in words):
            ingredient['name'] = random.choice(lean_meat_substitutes) 
        elif any(word in poultry_with_plurals for word in words):
            ingredient['name'] = random.choice(poultry_substitutes)  
        elif any(word in fish_and_seafood_with_plurals for word in words):
            ingredient['name'] = random.choice(fish_and_seafood_substitutes)
        elif any(word in flavoring_substitutes for word in words):
            ingredient['name'] = flavoring_substitutes[ingredient['name']]
        

    #Replace ingredients in the steps
    for step in steps:
        for ingredient in ingredients:
            if ingredient['name'] in step['step']:
                step['step'] = step['step'].replace(ingredient['name'], ingredient['name'].lower())

    return steps, ingredients


#Example usage
soup, steps, ingredients = web_scraping.fetch_recipe("https://www.allrecipes.com/recipe/150306/the-best-chicken-fried-steak/")
steps, ingredients = turn_vegetarian(soup, steps, ingredients)

modified_steps = [step['step'] for step in steps if "studios" not in step['step'].lower()]
modified_steps_str = "\n".join(modified_steps)
modified_ingredients = [ingredient['name'] for ingredient in ingredients]
modified_ingredients_str = "\n".join(modified_ingredients)

# Write the string to the file
with open("veg.txt", "w") as f:
    f.write(modified_steps_str)
    f.write("\n\n")
    f.write(modified_ingredients_str)