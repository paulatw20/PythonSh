from excepciones import exceptions as misExcep
#Clases
class temperaturas():
    def __init__(self):
        self.Temp = []
    def añadir (self, newTemp):
        self.Temp.append(newTemp)
    def imprimirTemp(self):
        for i in self.Temp:
            print(i)

#Programa
i=0;
temperaturasL = temperaturas()
while(i<5):
    try:
        newTemp = float(input("introduce tu temperatura"))
        if(newTemp > 42.0):
            raise misExcep.TempeInvalid
        else:
            temperaturasL.añadir(newTemp)
            print("añado la temperatura")
            print("hola")

    except misExcep.TempeInvalid:
        print("ha ocurrido la excepcion de temperatura invalida")
    i += 1

temperaturasL.imprimirTemp()