
class Coche:

    #Obtencion variables
    def __init__(self, marca : str):
        self.marca = marca
        print(marca)
    # obtencion marca
    def get_marca(self):
        print("La marca es"+" "+self.marca)

#Escritura en base de datos 
class CocheDB:
    
    def get_auto(self) -> Coche:
        pass

    def save_Coche(self, marca: Coche):
        pass

marca  = Coche('Chevrolet')
print(Coche.get_marca(marca))
