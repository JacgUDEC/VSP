nota1 = float(input("ingrese la nota numero 1: "))
nota2 = float(input("ingrese la nota numero 2: "))

if nota1 > nota2:
    print(f"la nota numero 1 ({nota1}) es mayor que la nota numero 2 ({nota2})")
elif nota2 > nota1:
    print(f"la nota numero 2 ({nota2}) es mayor que la nota numero 1 ({nota1})")
else:
    print(f"la nota numero 1 ({nota1}) es igual a la nota numero 2 ({nota2})")