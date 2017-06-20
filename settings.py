"""

Creates a dict where you have key and value from your script.json

"""

import json

# Load the configuration settings

with open('/home/edson/Projetos/WRFOutputReader/script.json') as data:
    settings = json.load(data)

