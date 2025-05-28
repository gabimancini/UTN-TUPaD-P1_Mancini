# 1. Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Ingrese un número: "))
for i in range(1, n+1):
    print(f"El factorial de {i} es: {factorial(i)}")

# 2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
n = int(input("Ingrese la posición de la serie de Fibonacci que desea calcular: "))
for i in range(n):
    print(fibonacci(i), end=" ")
print()

# 3. Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)
    
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"El resultado de {base} elevado a la {exponente} es: {potencia(base, exponente)}")

# 4. Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n > 1:
        decimal_a_binario(n//2)
    print(n % 2, end="")  
n = int(input("Ingrese un número decimal: "))
decimal_a_binario(n)
print()

# 5. Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    if len(palabra) < 2:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1]) 
palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

# 6. Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
n = int(input("Ingrese un número: "))
print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")

# 7. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)
n = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print(f"El total de bloques que necesita para construir toda la pirámide es: {contar_bloques(n)}")

# 8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese un dígito: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}")
