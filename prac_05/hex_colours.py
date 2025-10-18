"""
CP1404/CP5632 Practical
Hexadecimal colour names in a dictionary
"""
CODE_TO_COLOUR = {"asparagus": "#87a96b", "cerulean": "#007ba7", "chartreuse1": "#7fff00", "cornsilk1": "#fff8dc",
                "dogwood rose": "#d71868", "fuzzy wuzzy": "#87421f", "phthalo green": "#123524",
                  "quinacridone magenta": "#8e3a59", "zomp": "#39a78e", "puce": "#CC8899"}
for colour_code in CODE_TO_COLOUR:
    print(f"{colour_code:3} is {CODE_TO_COLOUR[colour_code]}")

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    print(f"colour_name, is {CODE_TO_COLOUR.get(colour_name)}")
    colour_code = input("Enter colour name: ").lower()
