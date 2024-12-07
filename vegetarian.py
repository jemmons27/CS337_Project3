''' Soup = Beautiful Soup object from the html
    Steps = list of steps in the recipe
    Ingredients = list of ingredients in the recipe
    Returns a tuple containing the modified steps and ingredients
'''
import random

def turn_vegetarian(soup, steps, ingredients):
    # Define the lists of non-vegetarian ingredients
    lean_meats = ["Beef", "Lamb", "Veal", "Pork", "Kangaroo", "Sausages", "Bacon", "Ham", "Salami", "Chorizo", "Pepperoni", "Prosciutto", "Pancetta", "Bresaola", "Mortadella", "Capocollo", "Coppa", "Guanciale", "Lardo", "Lomo", "Nduja", "Soppressata", "Speck", "Cotechino", "Zampone", "Blood sausage", "Black pudding", "White pudding", "Haggis", "Liverwurst", "Head cheese", "Pate", "Rillettes", "Terrine", "Galantine", "Ballotine", "Mousse", "Foie gras", "Trotters", "Tripe", "Sweetbreads", "Kidneys", "Liver", "Heart", "Tongue", "Brain", "Cheek", "Tail", "Feet", "Ears", "Snout", "Intestines", "Lungs", "Spleen", "Pancreas", "Thymus", "Testicles", "Oxtail", "Bone marrow", "Bone broth", "Bone meal", "Bone ash", "Bone char", "Bone gelatin", "Bone glue"]
    poultry = ["Chicken", "Turkey", "Duck", "Emu", "Goose", "Bush birds", "Quail", "Pheasant", "Partridge", "Grouse", "Guinea fowl", "Pigeon", "Squab", "Ostrich", "Rhea", "Cassowary", "Kiwi", "Egg", "Egg white", "Egg yolk", "Eggshell", "Egg membrane", "Egg albumen", "Egg vitellus", "Egg chalaza", "Egg germinal disc", "Egg air cell", "Egg sac", "Egg cord", "Egg tooth", "Egg beater", "Egg separator", "Egg poacher", "Egg boiler", "Egg cooker", "Egg timer", "Egg cup", "Egg carton", "Egg box", "Egg crate", "Egg tray", "Egg cart", "Egg basket", "Egg rack", "Egg holder", "Egg stand", "Egg case", "Egg carrier", "Egg caddy"]
    fish_and_seafood = ["Fish", "Prawns", "Crab", "Lobster", "Mussels", "Oysters", "Scallops", "Clams", "Squid", "Octopus", "Crayfish", "Yabbies", "Abalone", "Sea urchin", "Sea cucumber", "Sea snails", "Fish roe", "Fish maw", "Fish fin", "Fish head", "Fish tail", "Fish bone", "Fish skin", "Fish scales", "Fish liver", "Fish gills", "Fish swim bladder", "Fish stomach", "Fish intestines", "Fish blood", "Fish eggs", "Fish sperm", "Fish oil", "Fish sauce", "Fish paste", "Fish stock", "Fish floss", "Fish ball", "Fish cake", "Fish sausage", "Fish jerky", "Fish fillet", "Fish steak", "Fish cutlet", "Fish finger", "Fish stick", "Fish pie", "Fish soup", "Fish stew", "Fish curry", "Fish salad", "Fish sandwich", "Fish burger", "Fish taco", "Fish wrap", "Fish roll", "Fish sushi", "Fish sashimi", "Fish tempura", "Fish katsu", "Fish teriyaki", "Fish kabayaki", "Fish shioyaki", "Fish nitsuke", "Fish nimono", "Fish nabe", "Fish chowder", "Fish bisque", "Fish bouillabaisse", "Fish paella", "Fish risotto", "Fish pasta", "Fish pizza", "Fish lasagna", "Fish casserole", "Fish gratin", "Fish quiche", "Fish souffle", "Fish mousse", "Fish terrine", "Fish pate", "Fish rillettes", "Fish ceviche", "Fish carpaccio", "Fish tartare", "Fish crudo", "Fish poke", "Fish donburi", "Fish chirashi", "Fish bento", "Fish onigiri", "Fish okonomiyaki", "Fish takoyaki", "Fish dorayaki", "Fish taiyaki", "Fish manju", "Fish mochi", "Fish dango", "Fish daifuku", "Fish wagashi", "Fish yokan", "Fish dorayaki"]

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
        if ingredient['name'] in lean_meats:
            ingredient['name'] = random.choice(lean_meat_substitutes) 
        elif ingredient['name'] in poultry:
            ingredient['name'] = random.choice(poultry_substitutes)  
        elif ingredient['name'] in fish_and_seafood:
            ingredient['name'] = random.choice(fish_and_seafood_substitutes)
        elif ingredient['name'] in flavoring_substitutes:
            ingredient['name'] = flavoring_substitutes[ingredient['name']]

    return steps, ingredients