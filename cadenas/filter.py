temperaturas = [35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0]
def exactas(x):
    if(x/(round(x))==1):return True
    else: return False

valoresCero = filter(exactas, temperaturas)

for x in valoresCero:
    print(x)
