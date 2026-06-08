# Parse file with normalized names, remove "NAME" labels, and deduplicate effects per reagent

def clean_effects(filename):
    effects = {}

    with open(filename, 'r') as file:
        current_reagent = None
        for line in file:
            if "NAME" in line:  # Identify reagent line
                current_reagent = line.strip()[:-5]  # Remove trailing " NAME" suffix
                effects[current_reagent] = []  # Initialize list for current reagent's effects
            else:
                effect = line.strip()
                if not effect:
                    continue
                if effect not in effects[current_reagent]:  # Prevent duplicate effects
                    effects[current_reagent].append(effect)
    return effects

reagents = clean_effects('data/02_renamed.txt')


with open('data/03_cleaned_(final).txt', 'w') as file:
    for reagent, effect_list in reagents.items():
        file.write(reagent + "\n")
        for effect in effect_list:
            file.write(f"    {effect}\n")
        file.write("\n")  # Separate reagent blocks with new line