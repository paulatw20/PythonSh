import datetime
from datetime import date

print('Conteste las siguientes cuestiones para saber si puede ser jugador de baloncesto')

nombre = input('Introduce tu nombre\n')
apellido = input('Introduce tu apellido\n')

date_entry = input('Introduce tu fecha de nacimiento en formato YYYY-MM-DD \n')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)

altura = input('Introduce tu altura en cm\n')
altura =int(altura)

temperatura = input('Introduce tu temperatura corporal en grados\n')
temperatura = temperatura.replace(",",".")
temperatura = float(temperatura)

if(altura<150):
    valeparabaloncesto = False
    print("No vales para baloncesto")
else:
    valeparabaloncesto = True
    print("Vales para baloncesto")

if(valeparabaloncesto == False):
    hoy = date.today()
    años = hoy.year - date1.year
    if(años < 17):print("Pero",nombre ,"aun hay esperanza, vuelve en unos años")



