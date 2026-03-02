#Jhonatan Chitiva

class Vehiculo: 
    def __init__(self, marca, modelo, linea, velocidad):
        self.marca=marca
        self.modelo=modelo
        self.linea=linea
        self.velocidad=velocidad #Velocidad MAX
        self.velocidadi=0 #Velocidad inicial
    def mostrarinf(self):
        pass
    def aceleracion(self):
        if self.velocidadi < self.velocidad: #Acelerar
            self.velocidadi += 10
        elif self.velocidadi > self.velocidad: #Si se exede la velocidad se controla para que el limite sea la maxima
            self.velocidadi = self.velocidad

class Carro(Vehiculo):
    def mostrarinf(self):
        print(f"(Auto) Marca: {self.marca}, Modelo: {self.modelo}, Linea: {self.linea}.")

class Moto(Vehiculo):
    def mostrarinf(self):
        print(f"(Moto) Marca: {self.marca}, Modelo: {self.modelo}, Linea: {self.linea}.")


v1=Carro("BMW", 2024, "M4 Competition", 290)
v2=Carro("Toyota", 2023, "Corolla GR (Sport)", 230)
v3=Carro("Tesla", 2024, "Model 3 Performance", 261)
v4=Moto("Yamaha", 2024, "YZF-R1", 299)
v5=Moto("BMW", 2024, "S 1000 RR", 303)

Vehiculos=[v1,
           v2,
           v3,
           v4,
           v5]

for Vehiculo in Vehiculos:
    Vehiculo.mostrarinf()