class usurio:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        self.__estado="Activo"
    def mostrarinfo(self):
        return f"El estado del usuario {self.nombre} ({self.edad} años) es: {self.estado}"
    def cambiarestado(self):
        if self.__estado == "Activo":
            self.__estado = "Inactivo"
        elif self.__estado == "Inactivo":
            self.__estado = "Activo"

while True:
    print("---")