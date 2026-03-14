class Miembro:
    def __init__(self, nombre, edad, estado): #Cada miembro tiene nombre, edad, estado (Activo o Inactivo)
        self.nombre=nombre
        self.edad=edad
        self.estado=estado
    def mostrarinfo(self): #Mostar el nombre, edad y estado de los Miembros
        return f"El estado del usuario {self.nombre} ({self.edad} años) es: {self.estado}"
    def cambiaractivo(self): #Activar la membresia a un miembro
        if self.estado == "Inactivo":
            estadon="Activo"
            self.estado=estadon
            print("\nEstado cambiado correctamente ☑️")
        else:
            print(f"\n☑️  El miembro {self.nombre}, ya esta activo")
    def cambiarinactivo(self): #Desactivar membresia a un mienbro
        if self.estado == "Activo":
            estadon="Inactivo"
            self.estado=estadon
            print("\nEstado cambiado correctamente ☑️")
        else:
            print(f"\n☑️  El miembro {self.nombre}, ya esta Inactivo")
    def verificarentrada(self): #Verificar si la membresia de un miembro esta activa, si es asi dejar al miembro entrar al gimnacio
        if self.estado=="Activo":
            print("\nHa entrado satisfactoriamente ☑️")
        else: 
            print("\nEl usuario tiene inactiva la membresia ❗")

usuarios=[] #Lista de los miembros

def menu(): #El menu principal del programa
    print("\n💪--Gimnasio--💪\n")
    print("1. Registar miembros\n2. Ingresar al gimnasio\n3. Cambiar estados\n4. Mostrar usuarios registrados\n5. Salir\n")

def crear(): #Creacion de un nuevo miembro
    nombre=input("\nNombre: ")
    edad=input("Edad: ")
    estado="Activo"
    print("\nUsuario creado ☑️")
    return Miembro(nombre, edad, estado)

def menucrear(): #El menu de confirmacion si se quiere crear un nuevo miembro
    while True:
        print("\n✍️ --Creacion de Miembros--✍️\n")
        print("1. Registrar\n2. Salir\n")
        try:
            opcc=int(input("> "))
            if opcc==1:
                m=crear()
                usuarios.append(m)
            elif opcc==2:
                break
            else:
                print("\nOpcion no valida ❗")
        except:
            print("\nOpcion no valida ❗")


while True: #bucle principal del programa
    menu()

    opc=(input("> "))
    if opc == "1": #Si se deasea crear nuevo miembro
        menucrear()
    elif opc =="2": #El miembro quiere entrar al gimnacio
        if not usuarios:
            print("\nNo hay usuarios registrados 🚫")
        else:
            while True:
                print("\n📋--Seleccione su nombre--📋\n")
                for i, m in enumerate(usuarios):
                    print(f"{i+1}. {m.nombre} {m.edad} años")
                try:
                    index=int(input("\n> "))-1
                    usuarios[index].verificarentrada()
                    break
                except:
                    print("\nMiembro no valido ❗")
    elif opc =="3": #Cambiar el estado de la membresia de un miembro seleccionado
        if not usuarios:
            print("\nNo hay usuarios registrados 🚫")
        else:
            while True:
                print("\n📋--Seleccione el usuario--📋\n")
                for i, m in enumerate(usuarios):
                    print(f"{i+1}. {m.nombre} | Membresia: {m.estado}")
                try:
                    index=int(input("\n> "))-1
                    print("\nQue desea hacer ❓\n")
                    opcca=int(input("1. Cambiar a activo\n2. Cambiar a inactivo\n\n> "))
                    if opcca == 1:
                        usuarios[index].cambiaractivo()
                        break
                    elif opcca == 2:
                        usuarios[index].cambiarinactivo()
                        break
                    else:
                        print("Opcion no valida ❗")
                except:
                        print("\nOpcion no valido ❗")
    elif opc == "4": #Ver la lista de los miembros resgistrados con sus datos
        if not usuarios:
            print("\nNo hay usuarios registrados 🚫")
        else:
            print("\n📋--Miembros registrados--📋\n")
            for i, m in enumerate(usuarios):
                print(f"{i+1}. {m.mostrarinfo()}")
            print("\nPresione Enter para continuar ➡️")
            input("...")
    else:
        print("\nOpcion no valida ❗")