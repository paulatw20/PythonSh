cadena = "saludos"
cadena1 = "Hola Mundo"
cadena2 = "Saludos Mundo"
cadena3 = "hola mundo"
cadena4 = " Madrid Olimpico "
cadena5 = "123"
# numero de caracteres
print(len(cadena5))
# acceso a los caracteres por posición (indexación) (base 0)
print(cadena1[0])  # H
# podemos aplicar indexacion y funciones sobre un texto literal
print("python"[-1] + " " + "python".upper())  # n python
print(cadena1[7:10].upper())  # NDO del 7 al 9 (no incluye el limite superior)
# utilizando negativos va del final hacia el principio
print(cadena2[-4:-2])  # un (no incluye el limite superior)
print(cadena1 == cadena3)  # False
print(cadena1 == cadena3.capitalize())  # False porque capitalize solo convierte
# a mayusculas la primera letra de la primera palabra “Hola mundo”
print(cadena3.title())  # title() capitaliza toda las palabras “Hola Mundo”
print(cadena1.upper() == cadena3.upper())  # True
# tambien tenemos lower()

#strip() Elimina espacios al principio y al final
print("Madrid Olimpico" == cadena4.strip())  # True
# tambien tenemos lstrip() y rstrip()
# podemos indicar que caracter (o conjunto de caracteres) se puede eliminar con strip()
# pero solo al principio y al final
print(cadena2.strip("do"))  # SaludosMun
# split() divide en subcadenas en funcion del delimitador que le indiquemos como parametro
print(cadena1.split(" "))  # ['Hola','Mundo'] lo devuelve como lista (list)
# indexamos (base 0)
print(cadena1.split(" ")[0])  # 'Hola'
# count() obtiene el numero de veces que esta contenido un caracter (o subcadena)
print(cadena1.count("o"))  # 2
print(cadena1.count("x"))  # 0
print(cadena1.count("la"))  # 1
print("ain" in "rain")

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)
# en Python no tenemos el tipo char, los textos de un carácter son considerados str
letra = "x"
print(type(letra))  # str
letras = ["a", "b", "c"]
print(type(letras[0])) # str
