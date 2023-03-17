def funcion(numero):
 return 100/numero
# con try podemos capturar excepciones
try:
 print(funcion(0))
 # print(funcion(1))
except KeyboardInterrupt as e: # se ejecuta si se da un tipo especifico de error
 print("interupccion de teclado " + str(e))
except ZeroDivisionError as e: # se ejecuta si se da un tipo especifico de error
 print("El numero NO puede ser 0 " + str(e))
except: # se ejecuta si hay algun otro error
 print("Error inesperado")
else: # se ejecuta si no hay errores
 print("El numero SI puede ser 1")
finally: # se ejecuta en cualquier caso
 print("esto se ejecuta en cualquier caso")
# con raise podemos forzar el lanzamiento de una excepcion aunque no se hubiera producido
numero_positivo = input("Introduce un numero positivo")
if int(numero_positivo) < 0:
 raise Exception("el numero debe ser positivo")
else:
 print("El numero es correcto")

def infinite_sequence():
    num = 35.0
    while True:
    #while num <= 42.0:
        yield num
        num += 0.5

temperaturas = []
try:
    for i in infinite_sequence():
        #print(i, end=" ")
        temperaturas.append(i)
        print("\n" + str(temperaturas))

except KeyboardInterrupt as e:
    print("Se acabo ")



class temperaturas():
    def __init__(self, temperatura):
        self.Temperatura = temperatura

    def añadir(self, temperaturaNueva):
        #if(temperaturaNueva > 42.0):
         #   raise Exception("temperatura elevada, no es valida")
        #else:
        self.Temperatura = self.Temperatura.append(temperaturaNueva)

    def imprimir(self):
        print(self.Temperatura)

listaTemps= temperaturas([36.5, 37.0])
listaTemps.añadir(input("Introduce una temperatura"))
listaTemps.imprimir()


class temperaturas():
    def __init__(self, temperatura):
        self.Temperatura = temperatura

    def añadir(self, temperaturaNueva):
        self.Temperatura = self.Temperatura.append(temperaturaNueva)

    def imprimir(self):
        print(self.Temperatura)


listaTemps = temperaturas([36.5, 37.0])
listaTemps.añadir(float(input("Introduce una temperatura \n")))
listaTemps.imprimir()