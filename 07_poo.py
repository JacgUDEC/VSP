class jugador:
    def __init__(self, name, gol, trofeos):
        self.name=name
        self.gol=gol
        self.trofeos=trofeos
    def mostrar_goles(self):
        print("nombre del jugador: ", self.name)
        print("numero de goles: ", self.gol)
        print("numero de trofeos: ", self.trofeos)

jugador1=jugador("Messi", 91, 46)
jugador1.mostrar_goles()

