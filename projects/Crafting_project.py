import sys
import inflect
def main():
    print(craft_req(input("The item you want to craft: "), ))

def check_dictionary(search):
    try:
        search_option = search.strip().lower() # only if the programmer decides to change the initial input to an int type
    except AttributeError:
        sys.exit(AttributeError("First input has to be a string"))
    items = {"cap": "🧢", "sword":"⚔", "tent":"🏕️", "bomb":"💣", "bow":"🏹", "shield":"🛡️", "wand":"🪄","cake":"🎂"}
    if search_option in items:
        return items[search_option]
    else:
        raise IndexError("No object by that name")

def amount(search, amt_input):
    item = check_dictionary(search)
    if not amt_input:
        try:
            amt = int(input("How many of that item?"))
        except ValueError:
            sys.exit(ValueError("Put in a number for the second input"))
        return (item,amt)
    else:
        amt = int(amt_input)
        return (item,amt)
def craft_req(search, amt_input = ""):
    p = inflect.engine()
    searching = amount(search,amt_input)
    item = searching[0]
    if not amt_input:
        amt = searching[1]
    else:
        amt = int(amt_input)
    requirements_dict = {
        "🧢": {"cloth": 5, "needle": 1, "spool": 1},
        "⚔": {"iron": 6, "wood": 3, "hammer": 1},
        "💣": {"gunpowder": 6, "clay": 8, "rope": 1},
        "🏹": {"string": 10, "wood": 5, "rope": 3},
        "🏕️": {"hide": 30, "wood": 20, "rope": 20, "cloth": 25},
        "🛡️": {"leather": 10, "wood": 10, "iron": 15},
        "🪄": {"birch wood": 3, "fairy wings": 7, "witches wart": 7},
        "🎂": {"egg": 6, "sugar": 12, "milk bucket": 1, "flour": 15}
    }

    material_requirements = requirements_dict[item] # material_requirement is the item picture
    converted_dict = {}
    for material in material_requirements:
        converted_dict[material]= material_requirements[material] * amt
    def f_conversion(d):
        result = [ ]
        for item in d:
            result.append(f"{d[item]} {item}")
        result = p.join(result)
        return result

    result = f"You need {f_conversion(converted_dict)} to make {amt} {item}"
    if amt > 1:
        result += "'s"
    return result





if __name__ == "__main__":
    main()
