"EJERCICIO 1: Pide el nombre al usuario y salúdalo."

nombre = input("¿Cuál es tu nombre?: ")
if nombre.strip() == "":
    print("Error: nombre vacío")
else:
    print(f'Hola "{nombre}"')
