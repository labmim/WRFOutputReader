import generateGraphs as gg
from settings import settings

variables = settings['main']['variables']
grades = settings['main']['grades']
# /*
#   Para cada variável definada no script.json
#   serão gerados seus respectivos mapas
# */

print("The current grades are:")
for grade in grades:
    print("--> " + grade)
print("The active variables are:")
for variable in variables:
    print("--> " + variable)
    
for grade in grades:
    for variable in variables:
        gg.generateGraphs(grade, variable)
