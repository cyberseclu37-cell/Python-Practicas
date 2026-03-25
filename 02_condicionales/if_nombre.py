nombre = input("¿Cuál es tu nombre?: ")

if nombre.strip() == "":
    print("Error: no ingresaste nombre")
else:
    print(f'Hola "{nombre}"')
