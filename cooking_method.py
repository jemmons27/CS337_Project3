import re
import web_scraping

"""-------------------------------------------Helper Functions-----------------------------------------------"""

def convert_to_minutes(match):
    total_minutes = 0
    ## necessary because initial regex doesn't really match that well
    if "minute" in match.group(0):
        min_pattern = r'(\d+)\s*minutes?'
        minutes = re.search(min_pattern, match.group(0)).group(1)
        total_minutes = minutes
    if "hours" in match.group(0):
        hour_pattern = r'(\d+)\s*hours?'
        hours = re.search(hour_pattern, match.group(0)).group(1)
        total_minutes += hours * 60
    return int(total_minutes)

def change_time(match, scale_factor):
    minutes = convert_to_minutes(match)
    new_minutes = int(minutes * scale_factor)
    new_hours = new_minutes // 60
    new_minutes = new_minutes % 60
    # print("hours/minutes", new_hours, new_minutes)
    if new_hours == 0:
        return f"{new_minutes} minutes"
    elif new_minutes == 0:
        return f"{new_hours} hours"
    else:
        return f"{new_hours} hours {new_minutes} minutes"

def change_cook_time(step, sf): #if sf is greater than 1, it increases, if less than 1, it decreases
    pattern = r"(\d+)\s*(?:to\s*(\d+)\s*)?hours?|\d+\s*(?:to\s*(\d+)\s*)?minutes?"
    # print(step, sf)
    
    # Find all matches
    matches = re.finditer(pattern, step)
    modified_step = step
    for match in matches:
        matched_string = match.group(0)  # Extract the entire matched string
        print(f"Matched string: {matched_string}")
        print(f"Groups: {match.groups()}")  # Print all captured groups

        new_time = change_time(match, sf)
        print(f"New time: {new_time}")
    
        # Modify the step
        modified_step = re.sub(re.escape(matched_string), new_time, modified_step, count=1)

    return modified_step

"""--------------------------------------Main Functionality--------------------------------------------------------"""

def replace_cooking_method(steps, old_method, new_method):
    """
    Replaces a given cooking method with a desired cooking method in the recipe steps.
    (Tries to) account for the difference in cooking time between fast and slow cooking methods. 

    Parameters:
    steps (list): List of steps in the recipe.
    old_method (str): The cooking method to be replaced.
    new_method (str): The new cooking method to replace the old one.

    Returns:
    list: Modified list of steps with the new cooking method.
    """
    fast_cooking_methods = ["boil", "fry", "grill", "roast", "saute", "sear", "simmer", "steam", "stir-fry", "pressure cook"]
    slow_cooking_methods = ["bake", "braise", "broil", "caramelize", "poach", "slow-cook", "smoke", "sous-vide", "stew"]

    modified_steps = []

    #dictionary of cooking methods to cooking tools
    cooking_tools = {
        "boil": "pot",
        "bake": "oven",
        "braise": "pan",
        "broil": "oven",
        "caramelize": "pan",
        "fry": "pan",
        "grill": "grill",
        "poach": "pot",
        "roast": "oven",
        "saute": "pan",
        "sear": "pan",
        "simmer": "pot",
        "slow-cook": "slow-cooker",
        "smoke": "smoker",
        "sous-vide": "sous-vide machine",
        "steam": "steamer",
        "stew": "pot",
        "stir-fry": "wok",
        "pressure cook": "pressure cooker"
    }

    old_method = old_method.lower()
    new_method = new_method.lower()

    steps = [step['step'] for step in steps]
    # print(steps)

    for step in steps:
        if re.search(rf'\b{old_method}\b', step, re.IGNORECASE):
            # Best case scenario: both methods are fast-cooking or both are slow-cooking: simple substitution
            if (old_method in fast_cooking_methods and new_method in fast_cooking_methods) or \
               (old_method in slow_cooking_methods and new_method in slow_cooking_methods):
                modified_step = re.sub(rf'\b{old_method}\b', new_method, step, flags=re.IGNORECASE)
            # If old method is fast cooking and new is slow ||| need to increase cook time
            elif old_method in fast_cooking_methods and new_method in slow_cooking_methods:
                sub = re.sub(rf'\b{old_method}\b', new_method, step, flags=re.IGNORECASE)
                if re.search(r"(?:(\d+)\s*hours?)?\s*(?:(\d+)\s*minutes?)?", step):
                    modified_step = change_cook_time(sub, 2)
            # If old method is slow cooking and new is fast ||| need to decrease cook time
            elif old_method in slow_cooking_methods and new_method in fast_cooking_methods:
                sub = re.sub(rf'\b{old_method}\b', new_method, step, flags=re.IGNORECASE)
                if re.search(r"(?:(\d+)\s*hours?)?\s*(?:(\d+)\s*minutes?)?", step):
                    modified_step = change_cook_time(sub, 0.5)

            #if cooking implement mentioned in same sentence
            if re.search(rf'\b{cooking_tools[old_method]}\b', step, re.IGNORECASE):
                modified_step = re.sub(rf'\b{cooking_tools[old_method]}\b', cooking_tools[new_method], modified_step, flags=re.IGNORECASE)
            #if the method is at the beginning of the sentence, capitalize the first letter of the step
            if modified_step[0].islower():
                modified_step = modified_step[0].upper() + modified_step[1:]
            
            modified_steps.append(modified_step)
        else:
            modified_steps.append(step)

    return [step for step in modified_steps if "studios" not in step.lower()]


# # Example usage 1
# soup, steps, ingredients = web_scraping.fetch_recipe("https://www.allrecipes.com/recipe/150306/the-best-chicken-fried-steak/")

# original_steps = [step['step'] for step in steps  if "studios" not in step['step'].lower()]
# original_steps_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(original_steps))

# modified_steps = replace_cooking_method(steps, "fry", "bake")
# modified_steps_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(modified_steps))

# # Write the string to the file
# with open("cm.txt", "w") as f:
#     f.write("-------------- Example Usage 1 --------------\n\n")
#     f.write("ORIGINAL STEPS:\n")
#     f.write(original_steps_str)
#     f.write("\n\n")
#     f.write("MODIFIED STEPS:\n")
#     f.write(modified_steps_str)

# # Example usage 2
# soup, steps, ingredients = web_scraping.fetch_recipe("https://www.allrecipes.com/recipe/240559/traditional-gyros/")

# original_steps = [step['step'] for step in steps  if "studios" not in step['step'].lower()]
# original_steps_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(original_steps))

# modified_steps = replace_cooking_method(steps, "bake", "roast")
# modified_steps_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(modified_steps))

# # Write the string to the file
# with open("cm.txt", "w") as f:
#     f.write("\n\n\n-------------- Example Usage 2 --------------\n\n")
#     f.write("ORIGINAL STEPS:\n")
#     f.write(original_steps_str)
#     f.write("\n\n")
#     f.write("MODIFIED STEPS:\n")
#     f.write(modified_steps_str)

# Example usage 3  

soup, steps, ingredients = web_scraping.fetch_recipe("https://www.allrecipes.com/recipe/16354/easy-meatloaf/")

original_steps = [step['step'] for step in steps  if "studios" not in step['step'].lower()]
original_steps_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(original_steps))

modified_steps = replace_cooking_method(steps, "bake", "steam")
modified_steps_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(modified_steps))

# Write the string to the file
with open("cm.txt", "w", encoding='utf-8') as f:
    f.write("\n\n\n-------------- Example Usage 3 --------------\n\n")
    f.write("ORIGINAL STEPS:\n")
    f.write(original_steps_str)
    f.write("\n\n")
    f.write("MODIFIED STEPS:\n")
    f.write(modified_steps_str)




# Example usage
# steps = [
#     "Preheat the oven to 350 degrees.",
#     "Grill the chicken for 1 hour and 15 minutes.",
#     "Bake the vegetables for 20 minutes."
# ]
# old_method = "Grill"
# new_method = "Roast"

# modified_steps = replace_cooking_method(steps, old_method, new_method)
# print(modified_steps)