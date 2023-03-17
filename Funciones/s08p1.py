# Funcion uno lambda y normal
def funcion1():
 print("saludos desde una funcion")

funcion1l = lambda :print("Saludos desde una funcion lambda")

funcion1()
funcion1l()

# Funcion dos lambda y normal
def funcion2(a,b):
 print(a + " desde " + b)
funcion2l = lambda x , y : print(str(x).upper() + " desde " + str(y).upper())
funcion2("saludos","Python")
funcion2l("Saludos","lambda")

# Funcion tres lambda y normal
def funcion3():
 return 1000

funcion3l = lambda x:print( x)

print(funcion3())
print("lambda:")
funcion3l(2000)

# Funcion cuatro lambda y normal
def funcion4(x,y,z):
 return x+y+z

funcion4l= lambda x, y, z: print(x + y + z)

print(funcion4(5,3,4))
print("lambda:")
funcion4l(10,1,2)



# Funcion 5 lambda y normal
def funcion5(r,s):
 print("Esto es por la sentencia print " + str(15 % 3))
 return r % s

funcion5l = lambda x, y: print(str(x % y))

print(funcion5(10,3))
print("lambda:")
funcion5l(15,5)
