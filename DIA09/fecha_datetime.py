import datetime

mi_hora = datetime.time(15, 30, 45) # establecer una hora manual
mi_dia = datetime.date(2026, 5, 11) # establecer una fecha manual
mi_fecha = datetime.datetime(2037, 9, 11, 15, 30, 45) # fecha y hora manual
dia_hoy = datetime.date.today() # fecha de hoy

mi_dia.ctime() # devuelve la fecha y hora formateada y bonita

mi_fecha = mi_fecha.replace(month=3) # cambia algun dato de la fecha