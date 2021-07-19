
class Coche:
    def __init__(self, marca : str):
        self.marca = marca
        print(marca)
        
    def get_marca(self):
        print("La marca es"+" "+self.marca)

class CocheDB:
    def get_auto(self) -> Coche:
        pass

    def save_Coche(self, marca: Coche):
        pass

marca  = Coche('Chevrolet')
print(Coche.get_marca(marca))
