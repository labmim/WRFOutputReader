"""

Creates a dict where you have key and value from your script.json

"""

import json

with open('script.json') as data:
    settings = json.load(data)
    

    
