COLOUR_TO_CODE = {"absolute zero": "#0048ba", "apricot": "#fbceb1", "aqua": "#00ffff", "candy pink": "#e4717a",
                  "chestnut": "#954535", "Frostbite": "#e936a7", "harvest gold": "#da9100", "jungle green": "#29ab87",
                  "maroon": "#b03060", "vanilla": "#f3e5ab"}

user_colour = input("Enter Colour Name: ").lower()
while user_colour != "":
    if user_colour in COLOUR_TO_CODE:
        print(f"{user_colour.capitalize()} has code: {COLOUR_TO_CODE[user_colour]}")
    else:
        print("Invalid Name")
    user_colour = input("Enter Colour Name: ").lower()
