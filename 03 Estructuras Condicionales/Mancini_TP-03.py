# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Ingresa tu edad: "))
# Verifico si la edad es mayor a 18
if edad > 18:
    # Si la edad es mayor a 18, imprimo "Es mayor de edad"
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.
nota = int(input("Ingresa tu nota: "))
# Verifico si la nota es mayor o igual a 6
if nota >= 6:
    # Si la nota es mayor o igual a 6, imprimo "Aprobado"
    print("Aprobado")
    # Si la nota es menor a 6, imprimo "Desaprobado"
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par".
# Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.
num = int(input("Ingresa un número par: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años
edad = int(input("Ingresa tu edad: "))
# Verifico a qué categoría pertenece
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos 
# que tiene un iterable tal como una lista o un string.
password = int(input("Ingresa una contraseña entre 8 y 14 caracteres: "))
# Verifico si la contraseña tiene entre 8 y 14 caracteres
if len(password) >= 14 and len(password) <= 8:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros
# aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros aleatorios de la siguiente forma:
#import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)
# Calculo la moda, mediana y media
print(f"La moda es: {mode(numeros_aleatorios)}")
print(f"La mediana es: {median(numeros_aleatorios)}")
print(f"La media es: {mean(numeros_aleatorios)}")
# Comparo para determinar si hay sesgo
if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Sesgo positivo")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Sesgo negativo")
else:
    print("Sin sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
fras = input("Ingrese una frase :")
# Verifico si el último caracter es una vocal
if fras[-1] in "aeiou":
    print(f"{fras}!")
else:
    print(fras)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingresa tu nombre: ")
# Pido al usuario que ingrese un número
num = int(input("Ingresa 1 si querés tu nombre en mayúscula, 2 si lo querés en minúscula o 3 si querés capitalizada: "))
# Transformo el nombre según la opción seleccionada
if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
else:
    print(nombre.title())

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = float(input("Ingresa la magnitud del terremoto: "))
# Clasifico la magnitud del terremoto
if magnitud < 3:
    print("Muy leve")
    # Si la magnitud es menor a 3, imprimo "Muy leve"
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
    # Si la magnitud es mayor o igual a 3 y menor a 4, imprimo "Leve"
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    # Si la magnitud es mayor o igual a 4 y menor a 5, imprimo "Moderado"
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Periodo del año                                                Estación en el hemisferio norte    Estación en el hemisferio sur
# Desde el 21 de diciembre hasta el 20 de marzo (incluidos)      Invierno                            Verano
# Desde el 21 de marzo hasta el 20 de junio(incluidos)           Primavera                           Otoño
# Desde el 21 de junio hasta el 20 deseptiembre (incluidos)      Verano                              Invierno
# Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) Otoño                               Primavera
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# Pido al usuario en qué hemisferio se encuentra
hemisferio = input("En qué hemisferio se encuentra (N/S): ")
# Pido al usuario el mes y el día
mes = input("Ingresa el mes: ")
dia = int(input("Ingresa el día: "))
# Verifico en qué estación del año se encuentra
# Utilizo el operador "or" para evaluar si el mes es diciembre y el día es mayor o igual a 21
if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")
        # Si el mes es diciembre y el día es mayor o igual a 21, imprimo "Invierno"
elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
    # Si el mes es marzo y el día es mayor o igual a 21, imprimo "Primavera"
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")
elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
    if hemisferio == "N":
        print("Verano")
    else:
        print("Invierno")
else:
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera") 