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

p1 = Particula(1, 4, 5, 6, 7, 60, 255, 255, 0)
p2 = Particula(2, 3, 5, 8, 1, 20, 0, 255, 255)
p3 = Particula(3, 10, 7, 2, 8, 40, 255, 0, 255)

pc = ParticulaCompuesta()
pc.agregar_inicio(p1)
pc.agregar_final(p2)
pc.agregar_inicio(p3)
pc.mostrar()