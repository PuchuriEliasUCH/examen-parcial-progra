productos = {1: 1900.00, 2: 2699.00, 3: 1990.00, 4: 3550.00, 5: 3999.00}

class Laptop:
    def __init__(self, marca, cantidad):
        self.marca = marca
        self.cantidad = cantidad

    def precio(self):
        return productos[self.marca]
    
    def subtotal(self):
        return self.precio() * self.cantidad
    
    def descuento(self):
        if 0 < self.cantidad <= 3:
            return self.subtotal() * 0.035
        elif 3 < self.cantidad <= 6:
            return self.subtotal() * 0.045
        elif 6 < self.cantidad <= 10:
            return self.subtotal() * 0.05
        elif 10 < self.cantidad:
            return self.subtotal() * 0.07
        else:
            return 0
        
    def importe(self):
        return self.subtotal() - self.descuento()
        
    def obsequio(self):
        return ('mouse' if self.importe() < 10000 else 'teclado')
    
    def imprimir(self):
        print(f"""
Importe de la compra: {self.subtotal()} 
Importe del descuento: {self.descuento()} 
Importe de la venta: {self.importe()} 
Obsequio: {self.obsequio()} 
""")
        
marca = int(input(f"""
Ingrese la laptop que llevará
1 - Lenovo i5
2 - Lenovo i7
3 - HP Ryzen 5
4 - Asus i7
5 - Asus Gamer
                  
"""))
cantidad = int(input("Ingrese la cantidad de productos: "))
o = Laptop(marca, cantidad)
o.imprimir()