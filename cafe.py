class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self):
        self.items = []  

    def agregar(self, producto, cantidad):
        self.items.append([producto, cantidad])

    def total(self):
        suma = 0
        for prod, cant in self.items:
            suma += prod.precio * cant
        return suma

    def mostrar(self):
        print("Pedido:")
        for prod, cant in self.items:
            print(f"  {cant} x {prod.nombre} = ${prod.precio * cant}")
        print(f"Total a pagar: ${self.total()}")

class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.pedido = None

    def tomar_pedido(self):
        self.pedido = Pedido()
        print(f"Mesa {self.numero} lista para pedido")

cafe = Producto("Café", 4000)
arepa = Producto("Arepa", 6000)

mesa_3 = Mesa(3)
mesa_3.tomar_pedido()

mesa_3.pedido.agregar(cafe, 2)
mesa_3.pedido.agregar(arepa, 1)

mesa_3.pedido.mostrar()