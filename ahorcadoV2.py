import random

categorias_palabras = {
    "animales": ["perro", "gato", "elefante", "leon"],
    "maquinas": ["computadora", "laptop", "reloj", "microondas"],
    "frutas": ["manzana", "banana", "pera", "naranja"],
    "conceptos": ["amor", "libertad", "victoria", "tristeza"]
}

print("Lista de categorias: ")
for category in categorias_palabras.keys():
    print(f"- {category}")

categoria_elegida = input("Elige una categoria: ").lower()

while categoria_elegida not in categorias_palabras:
    categoria_elegida = input("Categoria invalida. Intenta de nuevo: ").lower()

palabra = random.choice(categorias_palabras[categoria_elegida])
palabra_elegida = ["_"] * len(palabra)


intentos = 10

while intentos > 0:
   
    print('\nPalabra actual: ' + ' '.join(palabra_elegida))

    letra = input('Elige una letra: ').lower()
   
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_elegida[i] = letra
        print('Bien hecho!')
    else:
        intentos -= 1
        print(f'Incorrecto, te quedan {intentos} intentos!')

    if '_' not in palabra_elegida:
        print('\nEnhorabuena! La palabra es: ' + palabra)
        break

if intentos == 0:
    print('\nTe quedaste sin intentos, La palabra correcta era: ' + palabra)