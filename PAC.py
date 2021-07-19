class Discount:
    # obtencion variables
    def __init__(self, customer, price):
      self.customer = customer
      self.price = price
    #Descuento 
    def get_discount(self):
      return self.price * 0.2

class VIPDiscount(Discount):
    #obtencion variables 
    def get_discount(self):
      #descuento sobre funcion
      return super().get_discount() * 2