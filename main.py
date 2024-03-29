#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 30 8 * * * /home/edson/Projetos/WRFOutputReader/job.sh > /home/edson/Projetos/WRFOutputReader/job.log 2>&1
import generateGraphs as gg
from settings import settings
import fileManager as fm

location = settings['settings']['location']['output']
variables = settings['main']['variables']
grades = settings['main']['grades']
# /*
#   Para cada variável definada no script.json
#   serão gerados seus respectivos mapas
# */

#fm.deleteSavePath(location)

print("The current grades are:")
for grade in grades:
    print("--> " + grade)
print("The active variables are:")
for variable in variables:
    print("--> " + variable)
    
for grade in grades:
    for variable in variables:
        gg.generateGraphs(grade, variable)
