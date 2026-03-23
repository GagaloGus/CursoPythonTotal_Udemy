class Abuelo:
    def hablar(self):
        print("alo")

class Padre(Abuelo):
    def reir(self):
        print("xdnt")

class Madre:
    def reir(self):
        print("xd")

class Hijo(Padre, Madre):
    pass

hijo = Hijo()

hijo.hablar() # Al tener dos herencias con la misma clase, elige la primera clase de la que hereda (Padre)
hijo.reir()
print(Hijo.__mro__)
print(Hijo.__bases__)