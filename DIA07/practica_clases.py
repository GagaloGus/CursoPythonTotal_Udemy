class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal hace un ruido")

class Pajaro(Animal):
    alas = True
    gordito = True
    
    def __init__(self, edad, color, especie):
        super().__init__(edad, color)
        self.especie = especie

    def __str__(self) -> str:
        return f"Soy un pajaro {self.especie} {self.color} de {self.edad} años"
    
    def hablar(self):
        print(f"pio pio mamaguebo, soy {self.color}")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")

    def pintar_negro(self):
        self.color = "negro"

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.gordito = False
    
    @staticmethod
    def clase_padre():
        print(Pajaro.__bases__)
        

mi_pajaro = Pajaro(3, "amarillo", "tucan")
print(mi_pajaro)
mi_pajaro.volar(2)
mi_pajaro.hablar()
mi_pajaro.pintar_negro()
mi_pajaro.hablar()

del mi_pajaro

Pajaro.poner_huevos(3)
Pajaro.clase_padre()