from datetime import date
 
hoy = date.today()
 
pagos = 7
nuevo_mes = hoy.month + pagos
nuevo_year = hoy.year
nuevo_dia = hoy.day
 
if nuevo_mes > 12:
    nuevo_mes = nuevo_mes % 12
    nuevo_year += 1
 
if nuevo_mes == 2 and hoy.day > 28: nuevo_dia = 28
if hoy.day > 30 and nuevo_mes in (4, 6, 11): nuevo_dia = 30
 
hoy = hoy.replace(nuevo_year, nuevo_mes, nuevo_dia)
 
print hoy
