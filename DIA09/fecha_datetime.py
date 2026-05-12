import datetime

mi_hora = datetime.time(15, 30, 45) # establecer una hora manual
mi_dia = datetime.date(2026, 5, 11) # establecer una fecha manual
mi_fecha = datetime.datetime(2037, 9, 11, 15, 30, 45) # fecha y hora manual
dia_hoy = datetime.datetime.today() # fecha y hora de hoy

mi_dia.ctime() # devuelve la fecha y hora formateada y bonita

mi_fecha = mi_fecha.replace(month=3) # cambia algun dato de la fecha

fecha_creacion = datetime.datetime(2026, 1, 1, 8, 30)
fecha_eliminacion = datetime.datetime(2026, 1, 3, 20, 46)
tiempo_vida = fecha_eliminacion - fecha_creacion
print(tiempo_vida.seconds) # devuelve el tiempo entre las dos fechas, seconds devuele el tiempo en segundos