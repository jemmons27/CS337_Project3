
import web_scraping
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import unicodedata

def swap_cuisine():

    ingredient_mapping = {
    # Dairy Products
    "Milk": "Soy milk",
    "Cheese": "Silken tofu",
    "Butter": "Sesame oil",
    "Cream": "Coconut milk",
    "Yogurt": "Fermented tofu",
    "Sour cream": "Rice vinegar",
    "Whipped cream": "Sweetened tofu pudding",
    "Cream cheese": "Sweet bean paste",
    "Ice cream": "Frozen mung bean dessert",
    "Custard": "Egg tart filling",
    
    # Herbs and Spices
    "Parsley": "Cilantro",
    "Thyme": "Scallions",
    "Basil": "Thai basil",
    "Rosemary": "Star anise",
    "Oregano": "Five-spice powder",
    "Dill": "Chinese celery",
    "Chives": "Garlic chives",
    "Tarragon": "Ginger",
    "Sage": "Cinnamon stick",
    "Bay leaves": "Dried tangerine peel",
    "Nutmeg": "Five-spice powder",
    "Cinnamon": "Cassia bark",
    "Vanilla": "Rock sugar",
    "Allspice": "Sichuan peppercorns",
    "Cloves": "Star anise",
    "Paprika": "Dried chili flakes",
    "Cumin powder": "Ground white pepper",
    "Caraway seeds": "Fennel seeds",
    "Coriander leaves": "Cilantro",
    "Saffron": "Turmeric powder",
    
    # Oils and Fats
    "Olive oil": "Peanut oil",
    "Canola oil": "Soybean oil",
    "Avocado oil": "Corn oil",
    "Butter": "Lard",
    "Margarine": "Soybean oil",
    "Lard": "Rendered pork fat",
    "Vegetable shortening": "Coconut oil",
    "Ghee": "Sesame oil",
    "Coconut oil": "Peanut oil",
    "Sunflower oil": "Rice bran oil",
    
    # Vegetables
    "Avocado": "Mashed edamame",
    "Zucchini": "Winter melon",
    "Asparagus": "Bamboo shoots",
    "Brussels sprouts": "Baby bok choy",
    "Kale": "Gai lan",
    "Turnips": "Daikon radish",
    "Rutabaga": "Lotus root",
    "Artichokes": "Lotus stem",
    "Beets": "Red dates",
    "Rhubarb": "Chinese hawthorn",
    "Sweet corn": "Baby corn",
    "Parsnips": "Burdock root",
    "Celery root": "Chinese celery",
    "Bell peppers": "Red chili peppers",
    "Iceberg lettuce": "Napa cabbage",
    "Radishes": "Pickled mustard greens",
    "Endive": "Chinese lettuce (shengcai)",
    "Fennel bulb": "Garlic chives",
    "Squash": "Kabocha squash",
    "Leeks": "Garlic chives",
    
    # Meats and Seafood
    "Turkey": "Duck",
    "Goose": "Duck",
    "Rabbit": "Frog legs",
    "Lamb chops": "Mutton or goat meat",
    "Venison": "Beef strips",
    "Bacon": "Crispy pork belly",
    "Ham": "Chinese cured ham",
    "Pork belly": "Braised pork belly ",
    "Scallops": "Dried scallops",
    "Oysters": "Dried oysters",
    
    # Fruits
    "Strawberries": "Goji berries",
    "Cherries": "Chinese hawthorn",
    "Peaches": "Lychee",
    "Apricots": "Dried apricots",
    "Grapes": "Longan fruit",
    "Figs": "Dried figs",
    "Dates": "Red dates",
    "Pomegranate": "Fresh lychee",
    "Cranberries": "Dried hawthorn slices",
    "Raisins": "Dried longan",
    "Currants": "Dried goji berries",
    "Blackberries": "Mulberries",
    "Raspberries": "Fresh hawthorn",
    "Cantaloupe": "Hami melon",
    "Honeydew": "Winter melon",
    "Watermelon": "Hami melon",
    "Papaya": "Asian pear",
    "Kiwi": "Starfruit",
    "Pineapple": "Chinese preserved pineapple",
    
    # Grains and Seeds
    "Quinoa": "Millet",
    "Couscous": "Broken rice",
    "Polenta": "Cornmeal porridge",
    "Oats": "Rice congee",
    "Barley": "Job's tears (coix seeds)",
    "Bulgar wheat": "Steamed glutinous rice",
    "Rye": "Buckwheat noodles",
    "Spelt": "Wheat starch",
    "Flaxseeds": "Sesame seeds",
    "Chia seeds": "Basil seeds",
    
    # Miscellaneous
    "Peanut butter": "Sesame paste",
    "Mayonnaise": "Soybean paste",
    "Ketchup": "Sweet and sour sauce",
    "Mustard": "Chinese hot mustard",
    "Worcestershire sauce": "Soy sauce and sugar mix",
    "Pickles": "Pickled mustard greens",
    "Capers": "Pickled radish",
    "Anchovies": "Fermented fish paste",
    "Horseradish": "Wasabi",
    "Balsamic vinegar": "Black rice vinegar"
}


    substitutions = {}

    soup, steps, ingredients = web_scraping.fetch_recipe("https://www.allrecipes.com/recipe/16354/easy-meatloaf/")
    threshold=80
    f = open("cuisine.txt", "w")
    for ingredient in ingredients:
        # Find the best match from the dictionary keys
        match, score = process.extractOne(ingredient['name'], ingredient_mapping.keys(), scorer=fuzz.partial_ratio)
        if score >= threshold:  # Only consider it a match if the similarity score meets the threshold
            substitutions[ingredient['name']] = ingredient_mapping[match]
            ingredient['name'] = ingredient_mapping[match]
        quantity = unicodedata.normalize('NFKD', ingredient['quantity']).encode('ascii', 'ignore').decode('utf-8')

        f.write(ingredient['quantity'] + " " + ingredient['unit'] + " " + ingredient['name'] + "\n")
    

    for step in steps:
        for ingredient in substitutions.keys():
            if ingredient in step['step']:
                step['step'] = step['step'].replace(ingredient, substitutions[ingredient]) 
        f.write(step['step'] + "\n")

swap_cuisine()
            




