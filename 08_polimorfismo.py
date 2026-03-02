class animal:
    def sonidos(self):
        pass

class vaca(animal):
    def sonidos(self):
        print("muuuuuuuu")

class cerdo(animal):
    def sonidos(self):
        print("oinc")
    
class gallo(animal):
    def sonidos(self):
        print("Cacaraca")
    
animales=[vaca(),
          cerdo(),
          gallo()]

for animal in animales:
    animal.sonidos()