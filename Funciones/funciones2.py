finEntrada = False
nombres = []

def licitacion(*nombres, equipo):
    print("equipo " + equipo + " :")
    if(len(*nombres)==0):
        print("sin Jugadores")
    else:
        for c in nombres:
            print("\t" + str(c))

while(finEntrada == False):
    print("Escriba 0 si ya no desea incorporar mas jugadores")
    if(input()=='0'):
        finEntrada =True
        break
    print("introduzca un miembro y pulse enter")
    nombres.append(input())




licitacion(nombres, equipo="buff")
