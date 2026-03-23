# vendedores reciben comisiones del 13%
# programa que pregunte el nombre y cuando han vendido
# programa responde ocn el nombre y cuanto han ganado por las comisiones

nombre = input("Ingrese su nombre: ")
ventas = float(input("Ingrese el ingreso de ventas totales: "))
comision = round(ventas * 13/100, 2)
print(f"Hola {nombre}, has ganado {comision}€ de comision")