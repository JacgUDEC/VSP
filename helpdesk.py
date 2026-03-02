class ticket:
    def __init__(self, asunto, prioridad):
        self.asunto=asunto
        self.prioridad=prioridad
        self.__estado="abierto"

    def verestado(self):
        return f"Estado: {self.__estado}"
    def cambiarestado(self, nuevo_estado):
        validados = ("Abierto", "En_tramite", "Cerrado")
        if nuevo_estado in validados:
            self.__estado = nuevo_estado
        else:
            return "Error estado no valido"
    def verificar(self):
        return "Resolución genérica del ticket"
    
class cambioTicket(ticket):
    def verificar(self):
        return "Revisar el ticket, validar ticket"

class estadoticket(ticket):
    def verificar(self):
        return "Revisar el estado del ticket"
    
class prioridadticket(ticket):
    def verificar(self):
        return "Revise la prioridad del ticket"
    
while True:
    print("--- HelpDesk ---")
    print("1. Crear ticket" \
    "2. Cambiar estado" \
    "3. Mostrar resumen" \
    "Salir")