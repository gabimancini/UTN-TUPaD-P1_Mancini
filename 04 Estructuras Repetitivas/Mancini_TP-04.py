# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

numeros = '' 
for i in range(101):
    numeros += str(i) + '\n'
print(numeros)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad
#  de dígitos que contiene.

num = input("Ingresa un número entero: ")
print("El número tiene", len(num), "dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos 
# entre dos valores dados por el usuario, excluyendo esos dos valores.

mun_min = input("Ingresa el primer número: ")
mun_max = input("Ingresa el segundo número: ")
suma = 0
for i in range(int(mun_min) + 1, int(mun_max)):
    suma += i
print("La suma de los números entre", mun_min, "y", mun_max, "es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
#  El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma = 0
num = int(input("Ingresa un número entero (0 para terminar): "))
while num != 0:
    suma += num
    num = int(input("Ingresa un número entero (0 para terminar): "))
print("La suma de los números ingresados es:", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, 
# el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num_random = random.randint(0,9)
num = int(input("Adivina el número (entre 0 y 9): "))
intentos = 0
while num_random != num:
    suma += 1
    num = int(input("Adivina el número (entre 0 y 9): "))
print("La suma de los números ingresados es:", suma)

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, 
# en orden decreciente.

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y
#  un número entero positivo indicado por el usuario.

num_user =  int(print("Ingresa un número entero positivo: "))
suma = 0
if num_user < 0:
    print("El número ingresado no es positivo.")
    num_user = int(input("Ingresa un número entero positivo: "))
else:
    for i in range(num_user + 1):
        suma += i
print("La suma de los números entre 0 y", num_user, "es:", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, 
# cuántos son negativos y cuántos son positivos. (Nota: para probar
#  el programa puedes usar una cantidad menor, pero debe estar preparado 
# para procesar 100 números con un solo cambio).

contador = 0
num_pares = 0
num_impares = 0
num_positivos = 0
num_negativos = 0
for i in range(100):
    num = int(input("Ingresa un número entero: "))
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
    if num > 0:
        num_positivos += 1
    elif num < 0:
        num_negativos += 1
    contador += 1
print("Cantidad de números pares:", num_pares)
print("Cantidad de números impares:", num_impares)
print("Cantidad de números positivos:", num_positivos)
print("Cantidad de números negativos:", num_negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y 
# luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor,
#  pero debe poder procesar 100 números cambiando solo un valor).

contador = 0
suma = 0
for i in range(100):
    num = int(input("Ingresa un número entero: "))
    suma += num
    contador += 1
media = suma / contador
print("La media de los números ingresados es:", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = input("Ingresa un número entero: ")
num_invertido = num[::-1]
print("El número invertido es:", num_invertido)
