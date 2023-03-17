# los diccionarios son colecciones basadas en parejas clave:valor
# al igual que las listas, los diccionarios son mutables (crecen dinamicamente)
# pero no se accede a los elementos por indice sino por clave
# si repetimos clave no da error pero sobreescribe el elemento anterior
# por ejemplo si en este caso añadimos un elemento “Lyon”:”Portugal” la longitud
# seguiría siendo 6 (es como si eliminamos “Lyon”:”Francia”
diccionario = {
    "Madrid": "España",
    "Jaén": "España",
    "Paris": "Francia",
    "Berlin": "Alemania",
    "Munich": "Alemania",
    "Lyon": "Francia"
}

print(diccionario)
# {'Madrid': 'España', 'Jaén': 'España', 'Lyon': 'Francia', 'Berlin': 'Alemania', 'Munich':'Alemania'}
print(type(diccionario))  # <class 'dict'>
print(len(diccionario))  # 6
# a diferencia de las listas no se accede a los elementos por índice sino por clave
# esto da error: print(diccionario[0])
print(diccionario["Munich"])  # Alemania
# otra forma equivalente
print(diccionario.get("Munich"))  # Alemania
# hay un segundo parámetro opcional que permite devolver un valor por defecto si no lo encuentra
print(diccionario.get("Savona","UE")) # UE
for x in diccionario.keys():  # puedo omitir keys() y tambien funciona
    print(x + " " + diccionario[x])
print(diccionario.keys())  # es de la clase <class 'dict_keys'>
print(diccionario.values())  # es de la clase <class 'dict_values'>
# no son indexables pero los podemos convertir a listas
print(list(diccionario.keys())[0], list(diccionario.values())[0])  # Madrid España
# podemos añadir y modificar elementos
diccionario["Berlin"] = "Republica Federal Alemania"
diccionario["Valencia"] = "España"
# tambien lo podriamos hacer con update()
diccionario.update({"Valencia": "Spain"})
# con pop() eliminamos elementos por clave
diccionario.pop("Lyon")
# con popitem() eliminaria el ultimo que haya entrado
# ítems() devuelve el conjunto de parejas
# es de la clase <class 'dict_items'> y cada pareja es una tupla
for pareja in diccionario.items():
    print(pareja)
# ('Madrid', 'España')
# ('Jaén', 'España') etc
print(list(diccionario.items()))
# esto devolveria una lista formada por tuplas de 2 elementos
# podemos recorrer los valores de esta forma
for c, v in diccionario.items():
    print(c + "----" + v)
# con fromkeys() obtenemos otro diccionario con las claves seleccionadas
# y con el value que establezcamos (también se puede insertart una lista en lugar de tupla)
diccionario_nuevo = diccionario.fromkeys(("Madrid", "Paris", "Berlin"), "UE")
# el value se lo asigna a todas las keys
for y in diccionario_nuevo:
    print(y, diccionario_nuevo[y].keys())

    # tambien tambien tenemos clear() como en las listas