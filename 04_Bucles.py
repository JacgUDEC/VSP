# while True:
#     print("Hola, estas en el programa!")
#     respuesta = input("¿Quieres salir? (s/n): ")
#     if respuesta == "s":
#         print("¡Adiós!")
#         break

frutas={"manzana":500,
        "banana":300,
        "naranja":400, 
        "pera":250
        }
for fruta, precio in frutas.items():
    print(f"{fruta}: {precio} pesos")