from pathlib import Path
import json

def get_stored_show(file):
    """Get the user's favorite TV show, if the info is available"""
    if file.exists():
        contents = Path(file).read_text()
        fav_show = json.loads(contents)
        return fav_show
    return None

def get_new_show(file):
    """Prompt for a new favorite show"""
    fav_show = input("What is your favorite TV show? ")
    contents = json.dumps(fav_show)
    file.write_text(contents)
    return fav_show

def state_fav_show():
    """Send a message about the user's favorite show"""
    path = Path('tv_show.json')
    fav_show = get_stored_show(path)
    
    if fav_show:
        print(f"I know your favorite show! It's {fav_show}.")
    else:
        fav_show = get_new_show(path)
        print("Now I know your favorite show!")


state_fav_show()
