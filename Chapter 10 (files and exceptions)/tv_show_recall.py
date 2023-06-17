from pathlib import Path
import json

path = Path('tv_show.json')
contents = path.read_text()
fav_show = json.loads(contents)

print(f"I know your favorite TV show! It's {fav_show}.")