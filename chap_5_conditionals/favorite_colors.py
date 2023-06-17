# Tell someone what kind of person they are, based on their favorite color.

soft_colors = [
    'baby blue',
    'rose',
    'butter yellow',
    'pearl'
]

jewel_tones = [
    'emerald',
    'ruby',
    'sapphire',
    'jet'
]

earth_tones = [
    'brown',
    'charcoal',
    'russet',
    'ocher'
]

bright_colors = [
    'chartreuse',
    'electric blue',
    'neon yellow',
    'hot pink'
]

favorite_color = 'brown'

if favorite_color in soft_colors:
    personality = 'gentle'
elif favorite_color in jewel_tones:
    personality = 'classy'
elif favorite_color in earth_tones:
    personality = 'easygoing'
elif favorite_color in bright_colors:
    personality = 'fun'
else:
    personality = 'friendly'
    
if personality[0] in ['a','e','i','o','u']:
    article = 'an'
else:
    article = 'a'

print(f'You have {article} {personality} personality.')
