print("Hello, World!")
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")
print(f"Hola, {nombre}! Tienes {edad} años.")

if int(edad) < 18:
    print("Eres menor de edad.")