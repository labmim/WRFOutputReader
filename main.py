import generateGraphs as gg
from settings import settings

variables = settings['main']['variables']

# /*
#   Para cada variável definada no script.json
#   serão gerados seus respectivos mapas
# */

for variable in variables:
    gg.generateGraphs(variable)
