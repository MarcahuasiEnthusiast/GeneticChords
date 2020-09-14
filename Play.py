
import rtmidi
import random as r
from random import randint
import time

#MIDI
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print(available_ports, "\n")

# Attempt to open the port
if available_ports:
    midiout.open_port(1)
else:
    midiout.open_virtual_port("My virtual output")


#Funcion para concatenar numeros
def numConcat(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    num1 += num2
    return int(num1)

#   36 = C1
#   48 = C2
#   60 = C3
#   72 = C4
#   84 = C5

# AUDIO:
#ADN = [['606266', '59626760', '60536055', '5156685551','51626457', '56586559', '53656358', '5965696363']]
#chordProgression = ['58556550', '595966', '5360604968', '5061696163', '5564626471', '4864676448', '6056675151', '56556561']

def stopSendingMIDI():
    pass
def playADN(data):


    for k in range(len(data)):
        print("Iteracion: ", k+1)
        for i in range (len(data[k])):
            #note on
            try:
                a = numConcat(data[k][i][0], data[k][i][1])
                b = numConcat(data[k][i][2], data[k][i][3])
                c = numConcat(data[k][i][4], data[k][i][5])
                d = numConcat(data[k][i][6], data[k][i][7])
                print(a, b, c, d)
            except:
                print(a, b, c)
                pass
            try:
                midiout.send_message([0x90, a, 127])
                midiout.send_message([0x90, b, 127])
                midiout.send_message([0x90, c, 127])
                midiout.send_message([0x90, d, 127])
            except:
                pass
            time.sleep(2.0)
            #note off
            try:
                a = (0x80, a, 0)
                b = (0x80, b, 0)
                c = (0x80, c, 0)
                d = (0x80, d, 0)
            except:
                pass
            try:
                midiout.send_message(a)
                midiout.send_message(b)
                midiout.send_message(c)
                midiout.send_message(d)
            except:
                pass

    #del midiout

def playChordProgression(data, midiout, n):

    for j in range(n):
        for i in range(len(data)):
            # note on
            try:
                a = numConcat(data[i][0], data[i][1])
                b = numConcat(data[i][2], data[i][3])
                c = numConcat(data[i][4], data[i][5])
                d = numConcat(data[i][6], data[i][7])
                print(a, b, c, d)
            except:
                print(a, b, c)
                pass
            try:
                midiout.send_message([0x90, a, 127])
                midiout.send_message([0x90, b, 127])
                midiout.send_message([0x90, c, 127])
                midiout.send_message([0x90, d, 127])
            except:
                pass
            time.sleep(2.0)
            # note off
            try:
                a = (0x80, a, 0)
                b = (0x80, b, 0)
                c = (0x80, c, 0)
                d = (0x80, d, 0)
            except:
                pass
            try:
                midiout.send_message(a)
                midiout.send_message(b)
                midiout.send_message(c)
                midiout.send_message(d)
            except:
                pass
    del midiout

'''
Generar Poblacion
'''
def generarADN(n):
    # Generacion de poblacion
    tamanhoPoblacion = n
    data = []
    dataList = []

    for l in range(tamanhoPoblacion):
        data = []
        for i in range(0, 4, 1):
            chord = ''
            for j in range(0, r.randint(3,4), 1):

                if j == 0:
                    x = r.randint(48, 60)
                    x = str(x)
                    chord += x
                if j == 1:
                    x = r.randint(53, 65)
                    x = str(x)
                    chord += x
                if j == 2:
                    x = r.randint(60, 72)
                    x = str(x)
                    chord += x
                if j == 3:
                    x = r.randint(48, 65)
                    x = str(x)
                    chord += x
                    numConcat(chord, x)
                if j == 4:
                    x = r.randint(48, 72)
                    x = str(x)
                    chord += x
                    numConcat(chord, x)
            data.append(chord)
        dataList.append(data)

    #for l in range(len(dataList)):
    #    print("DNA ", l, ":", dataList[l])
    #print("\n")
    #print("ADN progresiones de acordes:")
    #print(dataList)
    return dataList

def printADN(dataList):
    for l in range(len(dataList)):
        print("DNA ", l, ":", dataList[l])
    print()
    print("ADN progresiones de acordes:")
    print(dataList)

'''
Funcion Fitness
'''

dictIntervalos = {
    '0' : 1.0,
    '1' : 0.1,
    '2' : 0.5,
    '3' : 1.25,
    '4' : 1.25,
    '5' : 0.75,
    '6' : 0.2,
    '7' : 1.5,
    '8' : 1.25,
    '9' : 1.25,
    '10': 1.0,
    '11': 0.8
}

def checkInterval(a, b):   # Retorna el intervalo generado entre dos notas
    x = (abs(a - b)) % 12 # 0=12
    interval = None
    if (x == 0): interval = "Unisono"
    if (x == 1): interval = "Segunda Menor"
    if (x == 2): interval = "Segunda Mayor"
    if (x == 3): interval = "Tercera Menor"
    if (x == 4): interval = "Tercera Mayor"
    if (x == 5): interval = "Cuarta Justa"
    if (x == 6): interval = "Quinta Disminuida"
    if (x == 7): interval = "Quinta Justa"
    if (x == 8): interval = "Sexta Menor"
    if (x == 9): interval = "Sexta Mayor"
    if (x == 10): interval = "Septima Menor"
    if (x == 11): interval = "Septima Mayor"

    return x, interval

def checkIntervalNumber(a, b):   # Retorna el intervalo generado entre dos notas
    x = (abs(a - b)) % 12
    return x

def getPofInterval(a,b):    #Retorna el valor P entre dos notas (intervalo)
    x = (abs(a - b)) % 12
    x = str(x)
    return dictIntervalos[x]

def checkThirdsAndSixths(progresionTest, i):
    root = numConcat(progresionTest[i][0], progresionTest[i][1])
    a = None
    b = None
    c = None
    for it in range(0, len(progresionTest[i]), 2):
        if it == 2:
            n1 = progresionTest[i][it]
            n2 = progresionTest[i][it + 1]
            x = numConcat(n1, n2)
            a = checkIntervalNumber(root, x)
        if it == 4:
            n1 = progresionTest[i][it]
            n2 = progresionTest[i][it + 1]
            x = numConcat(n1, n2)
            b = checkIntervalNumber(root, x)
        if it == 6:
            n1 = progresionTest[i][it]
            n2 = progresionTest[i][it + 1]
            x = numConcat(n1, n2)
            c = checkIntervalNumber(root, x)
    #print(a)
    #print(b)
    #print(c)

    #No se permiten:
    # 3M + 3m
    if ((a == 3 and b == 4) or (a == 3 and c == 4) or (b == 3 and a == 4) or (b == 3 and c == 4) or (c == 3 and a == 4) or (c == 3 and b == 4)):
        return -1
    # 6M + 6m
    if ((a == 8 and b == 9) or (a == 8 and c == 9) or (b == 8 and a == 9) or (b == 8 and c == 9) or (c == 8 and a == 9) or (c == 8 and b == 9)):
        return -1
    # 3M + 6m
    if ((a == 4 and b == 8) or (a == 4 and c == 8) or (b == 4 and a == 4) or (b == 4 and c == 8) or (c == 4 and a == 8) or (c == 4 and b == 8)):
        return -1
    # 3m + 6M
    if ((a == 3 and b == 9) or (a == 3 and c == 9) or (b == 3 and a == 9) or (b == 3 and c == 9) or (c == 3 and a == 9) or (c == 3 and b == 9)):
        return -1
    else:
        return 1

def checkHalfTonesDistances(progresionTest, i):
    root = numConcat(progresionTest[i][0], progresionTest[i][1])
    a = 0
    b = 0
    c = 0
    for it in range(0, len(progresionTest[i]), 2):
        if it == 2:
            n1 = progresionTest[i][it]
            n2 = progresionTest[i][it + 1]
            a = numConcat(n1, n2)
        if it == 4:
            n1 = progresionTest[i][it]
            n2 = progresionTest[i][it + 1]
            b = numConcat(n1, n2)
        if it == 6:
            n1 = progresionTest[i][it]
            n2 = progresionTest[i][it + 1]
            c = numConcat(n1, n2)

    if ((root == a - 1) or (root == b - 1) or (root == c - 1) or
        (a == root - 1) or (root == b - 1) or (a == c - 1) or
        (b == root - 1) or (b == a - 1) or (b == c - 1) or
        (c == root - 1) or (c == a - 1) or (c == b -1)):
        return -1
    else:
        return 1

# Funcion fitness: Imprime caracteristica del cromosoma y retorna valor fitness de este
def funcionFitnessPRINT(progresion):
    print("Progresion: ", progresion, "\n")
    fitnessValuesList = []
    intervalsList = []
    for i in range(len(progresion)):
        fitnessValue = 100
        root = numConcat(progresion[i][0], progresion[i][1])
        intervals = []
        print("Acorde:",progresion[i])
        for j in range(0, len(progresion[i]), 2):
            if (j==0):
                print("nota Raiz:", root)
            else:
                a = progresion[i][j]
                b = progresion[i][j + 1]
                x = numConcat(a, b)
                intervals.append(checkInterval(root, x))
                fitnessValue *= getPofInterval(root, x)
                print("nota",j//2+1,":",x,",", "P =", getPofInterval(root,x), ",", checkInterval(root,x), ",", "valor Fitness: ", fitnessValue)
            if (j==len(progresion[i])-2):
                desastreTonal = checkThirdsAndSixths(progresion, i)
                mediostonos = checkHalfTonesDistances(progresion,i)
                if (desastreTonal == -1):
                    print("desastre tonal...", desastreTonal)
                    fitnessValue *= 0.1
                if (mediostonos == -1):
                    print("medios tonos...", desastreTonal)
                    fitnessValue *= 0.1
                else:
                    pass
        intervalsList.append(intervals)
        fitnessValuesList.append(fitnessValue)
        print("\n")

    print("Intervalos encontrados en relación a la nota raiz de cada acorde de la progresión: ", "\n")
    for i in range(len(intervalsList)):
        print("Intervalos acorde ", i+1, ":", intervalsList[i])
    print("\n")

    print("lista de fitness value por acorde: ", fitnessValuesList)
    fitnessTotal = 0
    for i in range(0, len(fitnessValuesList)):
        fitnessTotal += fitnessValuesList[i]
    fitnessTotal = (fitnessTotal/len(fitnessValuesList))

    print("Fitness total: ",fitnessTotal)
    print("\n")

def funcionFitness(progresion):
    fitnessValuesList = []
    intervalsList = []
    for i in range(len(progresion)):
        fitnessValue = 100
        root = numConcat(progresion[i][0], progresion[i][1])
        intervals = []
        for j in range(0, len(progresion[i]), 2):
            if (j==0):
                pass
            else:
                a = progresion[i][j]
                b = progresion[i][j + 1]
                x = numConcat(a, b)
                intervals.append(checkInterval(root, x))
                fitnessValue *= getPofInterval(root, x)
            if (j==len(progresion[i])-2):
                desastreTonal = checkThirdsAndSixths(progresion, i)
                mediostonos = checkHalfTonesDistances(progresion, i)
                if (desastreTonal == -1):
                    fitnessValue *= 0.1
                if (mediostonos == -1):
                    fitnessValue *= -0.1
                else:
                    pass
        intervalsList.append(intervals)
        fitnessValuesList.append(fitnessValue)
    fitnessTotal = 0
    for i in range(0, len(fitnessValuesList)):
        fitnessTotal += fitnessValuesList[i]
    fitnessTotal = (fitnessTotal/len(fitnessValuesList))
    #print(fitnessTotal)
    return fitnessTotal

# Test
#ADN = generarADN(10)
#printADN(ADN)
# Notas se generan entre 48 y 72
#Testeando cromosoma individual
#print("\n")
#progresion = ['535762', '555962', '525760', '555760', '535760', '555962', '55596064', '54576064']
#funcionFitnessPRINT(['606367', '576065', '596267', '57606467'])

#for i in range(len(ADN)):
#    print(ADN[i])
#    print(funcionFitness(ADN[i]))

def seleccion(n):
    cromosomasSeleccionados = []
    seleccion = []
    while (len(cromosomasSeleccionados) < n):
        ADN = generarADN(1)
        #printADN(ADN)
        for i in range(len(ADN)):
            print(funcionFitness(ADN[i]))
            if (funcionFitness(ADN[i]) >= 185):
                cromosomasSeleccionados.append(ADN[i])
    print()
    for i in range(len(cromosomasSeleccionados)):
        print("Cromosoma Seleccionado:", i+1, ":", cromosomasSeleccionados[i])
        funcionFitnessPRINT(cromosomasSeleccionados[i])
        seleccion.append(cromosomasSeleccionados[i])

    return seleccion

def crossover(seleccion):
    #if len(a) != len(b):
    #    raise ValueError("Genomes a and b must be of same length")

    result = []
    for i in range(0, len(seleccion[0])):
        #print("len",len(seleccion[0][i]))
        if (len(seleccion[0][i]) <= len(seleccion[1][i])):
            p = randint(0, len(seleccion[0][i]))
        if (len(seleccion[1][i]) <= len(seleccion[0][i])):
            p = randint(0, len(seleccion[1][i]))
        length = len(seleccion[0])
        #print(seleccion[0][i][0:p] + seleccion[1][i][p:])
        #result.append((seleccion[0][i][0:p] + seleccion[1][i][p:], seleccion[1][i][0:p] + seleccion[0][i][p:]))
        result.append(seleccion[0][i][0:p] + seleccion[1][i][p:])
    return result

def init():
    n = input('Elegir número de cromosomas modelo (1 < n)')
    n = int(n)


    cromosomasSeleccionados = seleccion(n)
    print("\n")
    print("cromosomas seleccionados", cromosomasSeleccionados, "\n")
    print("Valor Fitness 1: ", funcionFitness(cromosomasSeleccionados[0]))
    print("Valor Fitness 2: ", funcionFitness(cromosomasSeleccionados[1]))
    print("Promedio Valor Fitness: ", (funcionFitness(cromosomasSeleccionados[0])+funcionFitness(cromosomasSeleccionados[1]))/2, "\n")
    print("\n")
    cruzamientoInit = ["60", "61", "61", "61"]  # bajo fitness inicial
    cruzamiento = cruzar(cromosomasSeleccionados, cruzamientoInit)
    #return cromosomasSeleccionados

#time.sleep(1.0)
global cont
def cruzar(cromosomasSeleccionados, cruzamientoInit):
    global cont
    cont = 0
    cruzamiento = cruzamientoInit
    stopSendingMIDI()#STOP MIDI



    while(funcionFitness(cruzamiento) <= (funcionFitness(cromosomasSeleccionados[0])+funcionFitness(cromosomasSeleccionados[1]))/2):
        cruzamiento = crossover(cromosomasSeleccionados)
        print("Valor Fitness del cruzamiento", cont+1, ":", funcionFitness(cruzamiento))
        cont = cont + 1
    print("cromosomas seleccionados", cromosomasSeleccionados, "\n")



    for i in range(len(cromosomasSeleccionados)):
        print("Valor Fitness del Cromosoma seleccionado", i+1, funcionFitness(cromosomasSeleccionados[i]))
    print("Promedio Valor Fitness: ",
          (funcionFitness(cromosomasSeleccionados[0]) + funcionFitness(cromosomasSeleccionados[1])) / 2, "\n")
    print("Luego de", cont, "cruzamientos entre los cromosomas seleccionados, obtenemos la siguiente progresion:")
    print(cruzamiento)
    print("cuyo valor fitness es:", funcionFitness(cruzamiento), "\n")

    playChordProgression(cruzamiento, midiout, 1)

    answer = input(
        "Menu: \n 'n' = volver a cruzar cromosomas \n 'y' = Resultado: escuchar la progresion 8 veces \n 'g' = Generar nueva seleccion")
    print('%s \n' % (answer))

    if (answer == 'y'):
        print("RESULTADO FINAL:", cruzamiento)
        playChordProgression(cruzamiento, midiout, 4)
        return cruzamiento
    if (answer == 'n'):
        cruzamiento = cruzar(cromosomasSeleccionados, cruzamientoInit)
    if (answer == 'g'):
        init()

cromosomasSeleccionados = init()

print()












#playADN(ADN)
#playChordProgression(chordProgression)

