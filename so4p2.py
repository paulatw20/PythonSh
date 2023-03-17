temperatura = 36.5
listaTemperaturas=[]

for x in range(36, 43):
    listaTemperaturas.append(x-0.5)
    listaTemperaturas.append(x)
listaTemperaturas.insert(0,35.0)

for x in listaTemperaturas:
    if(x == temperatura):
       print(str(temperatura) + "*")
    else:
        print(x)

x=0
while(x < len(listaTemperaturas)):
    if(listaTemperaturas[x] == temperatura):
       print("Valor encontrado: \n" + str(listaTemperaturas[x]))
       break
    x+=1
else: print("no se ha encontrado")



