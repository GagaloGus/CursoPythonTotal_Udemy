# clase persona, con nombre y apellidos
# clase cliente que herede de persona, atributos: numero_cuenta y balance / metodos: str, depositar, retitar
# codigo para depositar reitrar o salir
# a prueba de errores

from random import *
import os

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def __str__(self) -> str:
        return f"Soy {self.nombre_completo()}"

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta:int, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = f"{numero_cuenta:04d}"
        self.balance = round(balance, 2)
    
    def __str__(self) -> str:
        return f"{super().__str__()}, tengo {self.balance}€ en mi cuenta '{self.numero_cuenta}'"

    def depositar(self, dinero):
        self.balance += dinero

    def retirar(self, dinero):
        retiro = min(self.balance, dinero)
        self.balance = retiro
    
def crear_cliente() -> Cliente:
    nombre = input("Dime tu nombre: ")
    apellido = input("Dime tu apellido: ")
    return Cliente(nombre, apellido, randint(0, 9999), uniform(50, 3000))

def inicio():
    os.system("cls")
    cliente = crear_cliente()
    opciones = ["Ver informacion", "Depositar", "Retirar", "Finalizar gestion"]
    while True:
        os.system("cls")
        print(f"Bienvenido a la gestion bancaria, {cliente.nombre}\nElige la gestion que quieres hacer")
        for i, value in enumerate(opciones):
            print(f"  [{i+1}] -> {value}")
        
        op = int(input(" -> "))
        match op:
            case 1:
                print(cliente)
            case 2:
                deposito = float(input("Cuanto dinero quieres depositar: "))
                cliente.depositar(deposito)
                print(f"Transaccion completada con exito! Depositaste {deposito}€")
            case 3:
                balance_pasado = cliente.balance
                retiro = float(input("Cuanto dinero quieres retirar: "))
                cliente.retirar(retiro)
                print(f"Transaccion completada con exito! Retiraste {min(balance_pasado, retiro)}€")
            case 4:
                print("Gracias por usar esta aplicacion!")
                break
        input("Presiona enter para continuar...")
            
inicio()