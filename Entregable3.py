diccionario = {
 "Nombre":"Paula",
 "Apellido":"Echavarria",
 "FechaNacimiento": "04/01/2000",
 "Altura": 158,
 "Temperatura":36
}
#Reasignacion de variables por defecto a personalizadas
diccionario["Nombre"] = input('Introduce tu nombre\n')
diccionario["Apellido"] = input('Introduce tu apellido\n')
diccionario["FechaNacimiento"]  = input('Introduce tu fecha de nacimiento en formato YYYY-MM-DD \n')
diccionario["Altura"] = int(input('Introduce tu altura en centimetros\n'))
diccionario["Temperatura"] = int(input('Introduce tu temperatura media\n'))

#impresion de tuplas [Clave, Valor]

for pareja in diccionario.items():
 print(pareja)

temperatura = float(diccionario["Temperatura"])
temperatura +=0.5
diccionario["Temperatura"] = temperatura
print("\n Tu temperatura ha aumentado 0.5, los nuevos datos son los siguientes\n")
for pareja in diccionario.items():
 print(pareja)


