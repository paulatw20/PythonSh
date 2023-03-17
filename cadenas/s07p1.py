class Ciudad():
    #Constructor
    def __init__(self, nombre, escan, sal, pais):
        self.Nombre = nombre
        self.Escandinava = escan
        self.Salario = sal
        self.Pais = pais
    #Metodos
    def muestra(self):
        print(self.Nombre + " " + str(self.Escandinava) + " " + str(self.Salario) + " " + self.Pais)
    def incrementoSueldo(self):
        self.Salario = self.Salario + self.Salario*0.05

    def normaliza(self):
        self.Nombre = self.Nombre.capitalize()
        self.Pais = self.Pais.capitalize()
        self.Salario = int(self.Salario)

#instancias
ciudades = [Ciudad("madrid", False, 1200.23, "españa"),
            Ciudad("estocolmo", True, 1800.23, "suecia"),
            Ciudad("Helsinki", True, 2100, "Finlandia"),
            Ciudad("Bruselas", False, 1400, "Belgica"),
            Ciudad("Paris", False, 1500, "Francia"),
            Ciudad("Lyon", False, 1400, "Francia"),
            Ciudad("Tampere", True, 2000, "Finlandia")]

for c in ciudades:
    c.normaliza()
    c.muestra()
print("\n")
