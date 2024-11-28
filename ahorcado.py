import random

grupo_palabras = ["perro", "gato", "elefante", "leon", "computadora", "laptop", "reloj", "microondas", "manzana", "banana", "pera", "naranja", "amor", "libertad", "victoria", "tristeza"]
palabra = random.choice(grupo_palabras)
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