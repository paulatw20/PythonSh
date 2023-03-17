temperatura = 36.5
listaTemperaturas=[]

def funcion(ti):
    for x in range(ti+1, 43):
        listaTemperaturas.append(x - 0.5)
        listaTemperaturas.append(x)
    listaTemperaturas.insert(0, ti)
    return listaTemperaturas
def funcion4(listaTemperaturas):
    for x in listaTemperaturas:
            print(x)
    return 0

def function2(listaTemperaturas):
    x = 0
    while (x < len(listaTemperaturas)):
        if (listaTemperaturas[x] == temperatura):
            print("*" + str(listaTemperaturas[x]))
        else:
            print(str(listaTemperaturas[x]))
        x += 1

    return 0

def function3(listaTemperaturas, valor):
    x = 0
    while (x < len(listaTemperaturas)):
        if (listaTemperaturas[x] == valor):
            return True
        x += 1
    else:
        return False
    return 0
print("Funcion que genera la lista: ")
print(funcion(35))
print("Funcion for")
print(funcion4(listaTemperaturas))
print("funcion que enseña el asterisco: ")
function2(listaTemperaturas)
print("Funcion que saca True o False: ")
print(function3(listaTemperaturas,temperatura))