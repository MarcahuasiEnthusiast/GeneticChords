import generateChromosomes
from random import randint
from typing import List, Optional, Callable, Tuple

chordProgression1 = ['5461706161', '51546156', '4861726065', '5854656567']
chordProgression2 = ['55586062', '576065', '5057695458', '515866']

print("Chromosoma 1:")
print(chordProgression1)
print("Chromosoma 2:")
print(chordProgression2)

chordProgression1 = str(chordProgression1)
chordProgression2 = str(chordProgression2)

# n
seleccion = [['5765626564', '5057695458', '5565634866', '53636163'], ['53616150', '5158704848', '4961715556', '5057615766']]
#seleccion.append(chordProgression1)
#seleccion.append(chordProgression2)

#for i in range(len(2)):

def crossover(seleccion):
    #if len(a) != len(b):
    #    raise ValueError("Genomes a and b must be of same length")





    result = []
    for i in range(0, len(seleccion[0])):
        p = randint(1, 6)
        length = len(seleccion[0])
        #print(seleccion[0][i][0:p] + seleccion[1][i][p:])
        #result.append((seleccion[0][i][0:p] + seleccion[1][i][p:], seleccion[1][i][0:p] + seleccion[0][i][p:]))
        result.append(seleccion[0][i][0:p] + seleccion[1][i][p:])
    return result

resultado = crossover(seleccion)
print(resultado)




