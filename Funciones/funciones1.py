# funcion sin parametros y sin valor de retorno
def funcion1():
 print("saludos desde una funcion")
funcion1() # llamada a la funcion
# funcion con parametros y sin valor de retorno
def funcion2(a,b):
 print(a + " desde " + b)
funcion2("saludos","Python")
# funcion sin parametros y con valor de retorno
def funcion3():
 return 1000
funcion3() # no hace nada
print(funcion3()) # muestra 1000 (el valor retornado por la funcion)
# funcion con parametros y con valor de retorno
def funcion4(x,y,z):
 return x+y+z
print(funcion4(5,3,4))
print("\n")
# igual que la anterior pero ademas conteniendo sentencias
def funcion5(r,s):
 print("Esto es por la sentencia print " + str(15 % 3))
 return r % s
funcion5(10,3) # no muestra el valor de retorno pero ejecuta la sentencia
print("\n")
print(funcion5(10,3)) # ademas de ejecutar la sentencia muestra valor de retorno
print("\n")
resultado5 = funcion5(10,4)
# cuando almacenamos el resultado de una funcion ejecuta la sentencia