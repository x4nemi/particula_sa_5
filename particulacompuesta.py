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

p = Particula(111, 4, 5, 6, 7, 8, 9, 9, 10.8)
print(p)
pc = ParticulaCompuesta()
pc.agregar_final(p)
pc.agregar_inicio(p)
pc.mostrar()