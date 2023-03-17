# La Herencia es una relación de ‘Generalizacion’
# puesto que la clase padre es un ‘caso general’ de la clase hija
# clase padre (superclase)
class Vehiculo:
    def __init__(self, color, precio, pais):
        self.Color = color
        self.Precio = precio
        self.Pais = pais


# clase hija (subclase)
class Coche(Vehiculo):
    def __init__(self, color, precio, pais, n_ruedas, n_puertas):
        super().__init__(color, precio, pais)
        self.N_puertas = n_puertas
        self.N_ruedas = n_ruedas

    def indicador(self):
        print("es un coche")

    def indicador2(self):
        print("es un coche 2")


# al instanciar un bmw, no hace falta que metas un coche ya creado porque la clase coche no tiene constructor
class Bmw(Coche):
    def __init__(self, color, precio, pais, n_ruedas, n_puertas, modelo):
        super().__init__(color, precio, pais, n_ruedas, n_puertas)
        self.Modelobmw = modelo



# al tener el mismo nombre sobreescribe el de la clase padre (Coche)


class Persona():
    def __init__(self, nombre, apellido):
        self.Nombre = nombre
        self.Apellido = apellido

    def muestro(self):
        print(self)


class clienteBMW(Persona, Coche):
    def __init__(self, nombre, apellido, color, precio, pais, n_ruedas, n_puertas, modelo):
        Persona.__init__(self, nombre, apellido)
        Bmw.__init__(self, color, precio, pais, n_ruedas, n_puertas, modelo)



    def muestro(self):
        Persona.muestro(self)
        Bmw.muestro(self)


# en Python No tenemos sobrecarga de método
# podemos hacer algo parecido a la sobrecarga mediante parámetros opcionales

cocheconcreto = Bmw("rojo", 40000, "lituania", 4, 3, 320)
persona1 = Persona("pepito", "grillo")

cocheconcreto.indicador()  # ejecuta el de la clase hija
cocheconcreto.indicador2()
print("Numero de Ruedas: " + str(cocheconcreto.N_ruedas) +
      " Color: " + str(cocheconcreto.Color) +
      " Precio: " + str(cocheconcreto.Precio) +
      " Numero de Puertas: " + str(cocheconcreto.N_puertas) +
      " Modelo Bmw: " + str(cocheconcreto.Modelobmw))
print(" ")
# para comprobar si una clase deriva de otra
print(issubclass(Coche, Vehiculo))  # True clase Coche es subclase de clase Vehiculo
print(issubclass(Vehiculo, Coche))  # False
print(issubclass(Bmw, Vehiculo))  # True clase Coche tambien deriva de clase Vehiculo
print(issubclass(Coche, Coche))  # True una clase tambien es subclase de si misma
print(issubclass(Bmw, (Vehiculo, Coche)))  # True
# en el segundo parámetro podemos meter una tupla de clases en lugar de una sola clase
print(" ")
# para comprobar si un objeto es una instancia de una clase
print(isinstance(cocheconcreto, Bmw))  # True
# tambien se considera instancia de las clases de las que deriva su propia clase
print(isinstance(cocheconcreto, Coche))  # True
print(isinstance(cocheconcreto, Vehiculo))  # True
print(isinstance(cocheconcreto, (Vehiculo, Coche)))  # True
# en el segundo parámetro podemos meter una tupla de clases en lugar de una sola clase
