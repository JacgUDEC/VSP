class libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

bk1 = libro("Las medias", "Pedrito", 2008)
bk2 = libro("El arroz", "Pepe", 2015)

print(bk1.titulo)
print(bk2.titulo)