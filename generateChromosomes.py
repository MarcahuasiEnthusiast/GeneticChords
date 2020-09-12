import random as r

#Funcionar para concatenar numeros
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

# Generacion de poblacion
tamanhoPoblacion = 100
data = []
dataList = []

for l in range(tamanhoPoblacion):
    data = []
    for i in range(0, 4, 1):
        chord = ''
        for j in range(0, r.randint(3,3), 1):
            x = r.randint(48,72)
            if j == 0:
                x = str(x)
                chord += x
            else:
                x = str(x)
                chord += x
                numConcat(chord, x)
        data.append(chord)
        print()
    dataList.append(data)

for l in range(len(dataList)):
    print("DNA ", l, ":", dataList[l])

print("ADN progresiones de acordes: \n ")
print(dataList)

'''
Funcion Fitness
'''

dictIntervalos = {
    '0' : 1.4,
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
    x = (abs(a - b)) % 12
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

    if ((a == 3 and b == 4) or (a == 3 and c == 4) or (b == 3 and a == 4) or (b == 3 and c == 4) or (c == 3 and a == 4) or (c == 3 and b == 4)):
        return -1
    if ((a == 8 and b == 9) or (a == 8 and c == 9) or (b == 8 and a == 9) or (b == 8 and c == 9) or (c == 8 and a == 9) or (c == 8 and b == 9)):
        return -1
    else:
        return 1


print("\n")
progresionTest = ['535762', '555962', '525760', '555760', '535760', '555962', '55596064', '54576064']
print("Test: ", progresionTest)

fitnessValuesList = []
intervalsList = []
for i in range(len(progresionTest)):
    fitnessValue = 100
    P = None
    root = numConcat(progresionTest[i][0], progresionTest[i][1])
    intervals = []
    print("Acorde:",progresionTest[i])
    for j in range(0, len(progresionTest[i]), 2):
        if (j==0):
            print("nota Raiz:", root)
        else:
            a = progresionTest[i][j]
            b = progresionTest[i][j + 1]
            x = numConcat(a, b)
            intervals.append(checkInterval(root, x))
            fitnessValue *= getPofInterval(root, x)
            print("nota",j//2+1,":",x,",", "P =", getPofInterval(root,x), ",", checkInterval(root,x), ",", "valor Fitness: ", fitnessValue)
        if (j==len(progresionTest[i])-2):
            desastreTonal = checkThirdsAndSixths(progresionTest, i)
            if (desastreTonal == -1):
                print("desastre tonal", desastreTonal)
                fitnessValue *= 0.1
            if (desastreTonal == 1):
                pass
    intervalsList.append(intervals)
    fitnessValuesList.append(fitnessValue)
    print("\n")


print("Intervalos: ")
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
