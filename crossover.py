import generateChromosomes
from random import randint
from typing import List, Optional, Callable, Tuple

# n
seleccion = [['5559626270', '5065695771', '57606549', '566364'], ['50627258', '5653664949', '5461636158', '56606354']]
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


print(seleccion)
print(generateChromosomes.funcionFitness(seleccion))
resultado = crossover(seleccion)
print(resultado)




