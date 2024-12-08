import re

def convert_to_minutes(match):
    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    total_minutes = hours * 60 + minutes
    return total_minutes

def change_time(match, scale_factor):
    minutes = convert_to_minutes(match)
    new_minutes = int(minutes * scale_factor)
    new_hours = new_minutes // 60
    new_minutes = new_minutes % 60
    if new_hours == 0:
        return f"{new_minutes} minutes"
    elif new_minutes == 0:
        return f"{new_hours} hours"
    else:
        return f"{new_hours} hours {new_minutes} minutes"

def change_cook_time(step, sf): #if sf is greater than 1, it increases, if less than 1, it decreases
    pattern = r"(?:(\d+)\s*hours?)?\s*(?:(\d+)\s*minutes?)?"
    modified_step = re.sub(pattern, lambda match: change_time(match, sf), step).strip()
    return modified_step

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

    old_method = old_method.lower()
    new_method = new_method.lower()

    for step in steps:
        if re.search(rf'\b{old_method}\b', step, re.IGNORECASE):
            # Best case scenario: both methods are fast-cooking or both are slow-cooking: simple substitution
            if (old_method in fast_cooking_methods and new_method in fast_cooking_methods) or \
               (old_method in slow_cooking_methods and new_method in slow_cooking_methods):
                modified_step = re.sub(rf'\b{old_method}\b', new_method, step, flags=re.IGNORECASE)
            # If old method is fast cooking and new is slow ||| need to increase cook time
            elif old_method in fast_cooking_methods and new_method in slow_cooking_methods:
                modified_step = change_cook_time(re.sub(rf'\b{old_method}\b', new_method, step, flags=re.IGNORECASE), 2)
            # If old method is slow cooking and new is fast ||| need to decrease cook time
            elif old_method in slow_cooking_methods and new_method in fast_cooking_methods:
                modified_step = change_cook_time(re.sub(rf'\b{old_method}\b', new_method, step, flags=re.IGNORECASE), 0.5)
            #if the method is at the beginning of the sentence, capitalize the first letter of the step
            if modified_step[0].islower():
                modified_step = modified_step[0].upper() + modified_step[1:]
            modified_steps.append(modified_step)
        else:
            modified_steps.append(step)

    return modified_steps

# Example usage
steps = [
    "Preheat the oven to 350 degrees.",
    "Grill the chicken for 1 hour and 15 minutes.",
    "Bake the vegetables for 20 minutes."
]
old_method = "Grill"
new_method = "Roast"

modified_steps = replace_cooking_method(steps, old_method, new_method)
print(modified_steps)