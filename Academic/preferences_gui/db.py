# Aaron Sage Field
# Preferences GUI
# April 22nd, 2025
# Database Layer

DATA = 'preferences.txt'

def read():
    # name = '' and language, autosave = DEFAULT
    defaults = {
        'name': '',
        'language': 'English',
        'autosave': '5'
                }
    preferences = defaults.copy()
    try:
        with open(DATA, 'r') as file:
            for line in file:
                if '|' in line:
                    key, value = line.strip().split('|', 1)
                    preferences[key] = value
    except FileNotFoundError:
        with open(DATA, 'w'):
            pass
    return preferences

def save(preferences):
    with open(DATA, 'w') as file:
        file.write(f"name|{preferences['name']}\n")
        file.write(f"language|{preferences['language']}\n")
        file.write(f"autosave|{preferences['autosave']}\n")
    
