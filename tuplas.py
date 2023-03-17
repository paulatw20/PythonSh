# se utilizan paréntesis ( )
tupla = ("saludos", "desde", 2030)
print(tupla)  # ('saludos', 'desde', 2030)
print(type(tupla))  # <class 'tuple'>
print(tupla[2])  # es indexable
# recorremos la tupla
for a in tupla:
    print(str(a))

# comprobar si un elemento esta en una tupla
resultado = 2030 in tupla
print(resultado)  # True
# count() e index()
print(str(tupla.count("saludos")) + " " + str(tupla.index("saludos")))
# otra forma sintáctica = "tuple packing"
tuplaotra = "saludos", "desde", 2040
print(tuplaotra)
print(type(tuplaotra))
# para crear una tupla de 1 solo elemento hay que indicar la coma
# si no lo cogería como una sola variable (texto, número, etc)
tuplaotra2 = ("saludos",)
# sin embargo, para las listas sí que lo coge como lista de ambas formas
# ["saludos",] ["saludos"]