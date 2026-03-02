print("Lista de estudiantes\n")

print("1. Juan")
print("2. Alejandra")
print("3. María\n")

estudiantes=["Juan", "Alejandra", "María"]
notas={"Juan": 4.5, "Alejandra": 3.8, "María": 4.2}
x=int(input("Ingrese el número de estudiante (1-3): "))
x-=1
if x == 0:
    print(f"la nota de {estudiantes[0]} es {notas['Juan']}")
elif x == 1:
    print(f"la nota de {estudiantes[1]} es {notas['Alejandra']}")
elif x == 2:
    print(f"la nota de {estudiantes[2]} es {notas['María']}")
else:
    print("Número de estudiante no válido")