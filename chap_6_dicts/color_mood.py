# Loop through a dictionary and print a message for each key/value pair.

color_mood = {
    'purple': 'mystical',
    'red': 'passionate',
    'blue': 'peaceful',
    'green': 'creative',
    'yellow': 'cheerful',
    'silver': 'refined',
    'gold': 'powerful',
    'rainbows': 'fearless',
}

for color, mood in color_mood.items():  #.items() grabs both key and value
    print(f"Wearing {color} says to others, 'I'm a {mood} person.'")