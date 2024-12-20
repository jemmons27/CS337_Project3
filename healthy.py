
import web_scraping
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def turn_healthy(url):

    healthy_substitutions = {
    "beef": 
        "lentils",       
    "pork": 
        "jackfruit (pulled pork)", 
    "lamb": 
        "mushrooms", 
    "mutton": 
        "seitan", 
    "goat":
        "cauliflower (roasts or curries)",
    "sugar": 
        "honey",
    "butter": 
        "olive oil",
    "white flour": 
        "whole wheat flour",
    "flour": 
        "whole wheat flour",
    "pasta": 
        "zucchini noodles (zoodles) or spaghetti squash",
    }

    substitutions = {}

    soup, steps, ingredients = web_scraping.fetch_recipe(url)
    threshold=80
    f = open("healthy.txt", "w", encoding='utf-8')
    for ingredient in ingredients:
        # Find the best match from the dictionary keys
        match, score = process.extractOne(ingredient['name'], healthy_substitutions.keys(), scorer=fuzz.partial_ratio)
        if score >= threshold:  # Only consider it a match if the similarity score meets the threshold
            substitutions[ingredient['name']] = healthy_substitutions[match]
            ingredient['name'] = healthy_substitutions[match]
        f.write(ingredient['quantity'] + " " + ingredient['unit'] + " " + ingredient['name'] + "\n")

    for step in steps:
        for ingredient in substitutions.keys():           
            if ingredient in step['step']:
                step['step'] = step['step'].replace(ingredient, substitutions[ingredient]) 
        for ingredient in healthy_substitutions.keys():
            if ingredient in step['step']:
                step['step'] = step['step'].replace(ingredient, healthy_substitutions[ingredient]) 
        f.write(step['step'] + "\n")

    f.write("Substitutions: \n")
    for item, value in substitutions.items():
        f.write(item + " substituted with " + value + "\n")

turn_healthy("https://www.allrecipes.com/recipe/240559/traditional-gyros/")
#https://www.allrecipes.com/recipe/16354/easy-meatloaf/
#https://www.allrecipes.com/recipe/150306/the-best-chicken-fried-steak/
            




