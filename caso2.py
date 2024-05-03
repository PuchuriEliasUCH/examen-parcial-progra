class Figura:
    def __init__(self, vertices):
        self.vertices = vertices

    def reporte(self):
        print(f"Esta es una figura de {self.vertices} vertices\n")

class Circulo(Figura):
    def __init__(self, vertices, radio):
        super().__init__(vertices)
        self.__radio = radio

    def set_radio(self, radio):
        self.__radio == radio

    def area(self):
        return 2*3.14*pow(self.__radio, 2)

    def perimetro(self):
        return 2*3.14*self.__radio
     
    def reporte(self):
        print(f"Soy un círculo de área {self.area()},\nperímetro {self.perimetro()}\ny tengo {self.vertices} vertices\n")

class Rectangulo(Figura):
    def __init__(self, vertices, largo, ancho):
        super().__init__(vertices)
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)

     
    def reporte(self):
        print(f"Soy un rectangulo de área {self.area()},\nperímetro {self.perimetro()}\ny tengo {self.vertices} vertices\n")


class Triangulo(Figura):
    def __init__(self, vertices, base, altura, lado1, lado2):
        super().__init__(vertices)
        self.altura = altura
        self.base = base
        self.lado1 = lado1
        self.lado2 = lado2
    
    def area(self):
        return self.base * self.altura / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.base

     
    def reporte(self):
        print(f"Soy un triangulo de área {self.area()},\nperímetro {self.perimetro()}\ny tengo {self.vertices} vertices\n")


oCir = Circulo(
    0, 
    float(input("Ingrese el valor del radio del circulo: "))
)
oCir.reporte()

oRec = Rectangulo(
    4,
    float(input("Ingrese el valor del largo del rectángulo: ")), 
    float(input("Ingrese el valor del ancho: "))
)
oRec.reporte()

oTri = Triangulo(
    3, 
    float(input("Ingrese el valor de la base del triángulo: ")), 
    float(input("Ingrese el valor de la altura: ")),
    float(input("Ingrese el valor del primer lado: ")),
    float(input("Ingrese el valor del segundo lado: "))
    )
oTri.reporte()
