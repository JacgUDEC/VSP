class ticket:
    def __init__(self, asunto, prioridad):
        self.asunto=asunto
        self.prioridad=prioridad
        self.__estado="Abierto"
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

class Ticketsoftware(ticket):
    def verificar(self):
        return "Revisar software"
class Tickethardware(ticket):
    def verificar(self):
        return "Revisar hardware"
class Ticketred(ticket):
    def verificar(self):
        return "Revisar red"
class cambioTicket(ticket):
    def verificar(self):
        return "Revisar el ticket, validar ticket"
class estadoticket(ticket):
    def verificar(self):
        return "Revisar el estado del ticket"
class prioridadticket(ticket):
    def verificar(self):
        return "Revise la prioridad del ticket"
    
def mostrar_menu():
    print("--- HelpDesk ---")
    print("1. Crear ticket\n2. Cambiar estado\n3. Mostrar resumen\n4. Salir")
def menu_del_ticket():
    print("---Tipo de ticket")
    print("1. Software\n2. Hardware\n3. Red\n4. Salir")
    tipo=input("> ")
    asunto=input("Ingresa el asunto: ")
    prioridad=input("Ingresa la prioridad: ")

    if tipo == "1":
        return Ticketsoftware(asunto, prioridad)
    elif tipo=="2":
        return Tickethardware(asunto, prioridad)
    elif tipo=="3":
        return Ticketred(asunto, prioridad)
    else:
        print("Tipo de ticket no valido")
        return None

tickets=[]

while True:
    mostrar_menu()
    op=input("> ")
    if op=="1":
        menu_del_ticket()