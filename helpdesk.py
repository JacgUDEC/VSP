class ticket:
    def __init__(self, asunto, prioridad):
        self.asunto = asunto
        self.prioridad = prioridad
        self.__estado = "Abierto"

    def verestado(self):
        return self.__estado

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


def mostrar_menu():
    print("\n--- HelpDesk ---")
    print("1. Crear ticket")
    print("2. Cambiar estado")
    print("3. Mostrar resumen")
    print("4. Salir")


def menu_del_ticket():
    print("\n--- Tipo de ticket ---")
    print("1. Software")
    print("2. Hardware")
    print("3. Red")

    tipo = input("> ")
    asunto = input("Ingresa el asunto: ")
    prioridad = input("Ingresa la prioridad: ")

    if tipo == "1":
        return Ticketsoftware(asunto, prioridad)
    elif tipo == "2":
        return Tickethardware(asunto, prioridad)
    elif tipo == "3":
        return Ticketred(asunto, prioridad)
    else:
        print("Tipo de ticket no valido")
        return None


tickets = []

while True:

    mostrar_menu()
    op = input("> ")

    if op == "1":

        t = menu_del_ticket()

        if t:
            tickets.append(t)
            print("Ticket creado correctamente")

    elif op == "2":

        if not tickets:
            print("No hay tickets registrados")
            continue

        print("\nLista de tickets")
        for i, t in enumerate(tickets):
            print(i + 1, "-", t.asunto, "| Estado:", t.verestado())

        num = int(input("Selecciona ticket: ")) - 1

        if 0 <= num < len(tickets):
            nuevo = input("Nuevo estado (Abierto / En_tramite / Cerrado): ")
            tickets[num].cambiarestado(nuevo)
            print("Estado actualizado")

    elif op == "3":

        if not tickets:
            print("No hay tickets registrados")
            continue

        print("\n--- Resumen de Tickets ---")

        for i, t in enumerate(tickets):
            print("\nTicket", i + 1)
            print("Asunto:", t.asunto)
            print("Prioridad:", t.prioridad)
            print("Estado:", t.verestado())
            print("Acción:", t.verificar())

    elif op == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida")