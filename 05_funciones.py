exit = False

print("\nCalculadora\n")

while not exit:
    print("\n1. Sumar\n2. Restar\n3. Multipicar\n4. Dividir\n5. Salir\n")

    seleccion = int(input("> "))

    while True:
        if seleccion < 6 and seleccion > 0:
            break
        else:
            print("!!Respuesta no valida!!")
            seleccion = int(input("> "))

    if seleccion == 1:
        a=float(input("\nNumero a: "))
        b=float(input("Numero b: "))

        def suma(a,b):
            return(a+b)
            
        print(f"\nRespuesta: {suma(a,b)}")
    elif seleccion == 2:
        a=float(input("\nNumero a: "))
        b=float(input("Numero b: "))

        def resta(a,b):
            return(a-b)
            
        print(f"\nRespuesta: {resta(a,b)}")
    elif seleccion == 3:
        a=float(input("\nNumero a: "))
        b=float(input("Numero b: "))

        def Mult(a,b):
            return(a*b)
            
        print(f"\nRespuesta: {Mult(a,b)}")
    elif seleccion == 4:
        a=float(input("\nNumero a: "))
        b=float(input("Numero b: "))

        def Div(a,b):
            return(a/b)
            
        print(f"\nRespuesta: {Div(a,b)}")
    elif seleccion == 5:
        exit = True
        
        