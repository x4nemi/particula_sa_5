from particula import Particula

class ParticulaCompuesta:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

p = Particula(1, 4, 5, 6, 7, 8, 9, 9)
p1 = Particula(2, 3, 5, 8, 1, 20, 65, 87, 98)
print(p)
pc = ParticulaCompuesta()
pc.agregar_final(p1)
pc.agregar_inicio(p)
pc.agregar_inicio(p1)
pc.mostrar()