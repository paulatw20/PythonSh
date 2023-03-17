class Ciudad():
    #Constructor
    def __init__(self, nombre, escan, sal, pais):
        self.Nombre = nombre
        self.Escandinava = escan
        self.Salario = sal
        self.Pais = pais
    #Metodo
    def muestra(self):
        print(self.Nombre + " " + str(self.Escandinava) + " " + str(self.Salario) +
              " " + self.Pais)
    def incrementoSueldo(self):
        self.Salario= self.Salario + self.Salario*0.05

class Ciudad2(Ciudad):
    #Muestra2
    def muestra(self):
        print(self.Nombre + "\n" + str(self.Escandinava) + "\n\t" +
              str(self.Salario[0]) + "\t" + str(self.Salario[1]) +
              "\n" + self.Pais + "\n")

ciudades = [Ciudad("Madrid", False, 1200, "España"),
            Ciudad("Estocolmo", True, 1800, "Suecia"),
            Ciudad("Helsinki", True, 2100, "Finlandia"),
            Ciudad("Bruselas", False, 1400, "Belgica"),
            Ciudad("Paris", False, 1500, "Francia"),
            Ciudad("Lyon", False, 1400, "Francia"),
            Ciudad("Tampere", True, 2000, "Finlandia")]

for c in ciudades:
    c.muestra()
print("\n")

#incremento sueldo sobre todas las ciudades
for c in ciudades:
    c.incrementoSueldo()
print("\n")

 #Visualizo la ciudad y su sueldo
print("Ciudades con incremento de Sueldo")
for c in ciudades:
    print(str(c.Nombre) +": " + str(c.Salario) + "\n")


ciudades2 = [Ciudad2("Madrid", False, [1200, 0.84], "España"),
             Ciudad2("Estocolmo", True, [1800, 0.91], "Suecia"),
             Ciudad2("Helsinki", True, [2100, 0.90], "Finlandia"),
             Ciudad2("Bruselas", False, [1400, 0, 88], "Belgica"),
             Ciudad2("Paris", False, [1500, 0.87], "Francia"),
             Ciudad2("Lyon", False, [1400, 0.87], "Francia"),
             Ciudad2("Tampere", True, [2000, 0.90], "Finlandia")]
print("Se muestran las ciudades 2:")
for c in ciudades2:
    c.muestra()