"""

#ciclos.py  

# Ejercicio 1: Imprimir los números del 1 al 10 utilizando un bucle for.

for i in range(1, 11):
    print(i)
#imprimir los numeros pares del 10 al 1
for i in range(10,0,-1):
    if i % 2 != 0:
        print(i)   
#for con listas
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
#imprimir una lista de numeros del 1 al 10
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(numero)
    #declaramos una lista de letras de a hasta e
letras = ['a','b','c','d','e']
for letra in letras:
    print(letra)
#imprimir los numeros del 1 al 10 usando tuplas
numeros_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for numero in numeros_tupla:
    print(numero)
#declaramos una tupla del 1 al 10 
tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for numero in tupla_numeros:
    print(numero)
#imprimir una tupla de letras de a hasta e
tupla_letras = ('a', 'b', 'c', 'd', 'e')
for letra in tupla_letras:
    print(letra)
    #ciclo while imprimir los numeros del 1 al 10
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

#imprimir los numeros pares del 10 al 0 con ciclo while
contador = 10
while contador >= 1:
    if contador % 2 == 0:
        print(contador)
    contador -= 1      
#teniendo la sgte lista imprimir las edades mayores a 20
edades = [18, 22, 19, 25, 21, 17, 23, 20]
for edad in edades:
    if edad > 20:
        print(edad) 
#averiguar si en la sgte lista de edades hay personas con 18 años devolver mensaje si hay personas con 18 anos con for

edades = [18, 18, 32, 45, 23,18, 19, 20]
hay_personas_18 = False
for edad in edades:
    if edad == 18:
        hay_personas_18 = True
        cantidad_18 = edades.count(edad)
        print(f"Hay {cantidad_18} personas con 18 años.")
        break
if hay_personas_18:
    print("Hay personas con 18 años en la lista.")
else:
    print("No hay personas con 18 años en la lista.")
#RECORRER LA SGTE LISTA USANDO WHILE 
edades = [18, 18, 32, 45, 23,18, 19, 20]
i = 0
while i < len(edades):
    print(edades[i])
    i += 1     
#Escribir un programa de registro de usuaraios q cumpla los sgtes pasos:
# 1. Solicitar al usuario que ingrese su nombre de usuario y contraseña.el usuario digita el nombre y la contrasena y el sistema valida si existe
# si la contrasena existe debe sacar mensaje diciendo la contrasena existe y volver al 1
# si no existe guardar daros contrasena y sacar un mensaje diciendo contrasena guardada con existo y preguntar al usuario si desea guardar un usuario nuevo si la respuestaes si, volver al paso 1 si es no terminar el programa con el sgte mensaje gracias fin del programa
usuarios = {}
while True:
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    if contrasena in usuarios.values():
        print("La contraseña ya existe. Intente con otra.")
    else:
        usuarios[nombre_usuario] = contrasena
        print("Contraseña guardada con éxito.")
    
    guardar_nuevo = input("¿Desea guardar un usuario nuevo? (si/no): ").strip().lower()
    if guardar_nuevo != 'si':
        print("Gracias, fin del programa.")
        break
#Escribir un programa de registro de usuarios que siga o cumplacon los siguientes pasos

#1.El programa pide el nombre y la contraseña
#2.El usuario digita el nombre y la contraseña y el sistema valida si la contraseña ya existe
#3.Si la contraseña ya existe el programa debe sacar un mensaje diciendo "La contraseña ya existe" y volver al paso 1
#4.Si la contraseña no existe guardar los datos(contraseña) y sacar un mensaje diciendo "Contraseña guardada con éxito" y preguntar al usuario si desea guardar un usuario nuevo
#5.Si la respuesta es "si" volver al paso 1, si es "no" terminar el programa con el siguiente mensaje "Gracias, fin del programa"
# usar diccionario para los nombresde usuario
usuarios = {}
while True:     
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    if contrasena in usuarios.values():
        print("La contraseña ya existe. Intente con otra.")
    else:
        usuarios[nombre_usuario] = contrasena
        print("Contraseña guardada con éxito.")
    
    guardar_nuevo = input("¿Desea guardar un usuario nuevo? (si/no): ").strip().lower()
    if guardar_nuevo != 'si':
        print("Gracias, fin del programa.")
        break 
    #1.El programa pide el nombre y la contraseña
#2.El usuario digita el nombre y la contraseña y el sistema valida si la contraseña ya existe
#3.Si la contraseña ya existe el programa debe sacar un mensaje diciendo "La contraseña ya existe" y volver al paso 1
#4.Si la contraseña no existe guardar los datos(contraseña) y sacar un mensaje diciendo "Contraseña guardada con éxito" y preguntar al usuario si desea guardar un usuario nuevo
#5.Si la respuesta es "si" volver al paso 1, si es "no" terminar el programa con el siguiente mensaje "Gracias, fin del programa"

# usar diccionario para los nombresde usuario

usuarios = {}
while True:
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    if contrasena in usuarios.values():
        print("La contraseña ya existe. Intente con otra.")
    else:
        usuarios[nombre_usuario] = contrasena
        print("Contraseña guardada con éxito.")
    
    guardar_nuevo = input("¿Desea guardar un usuario nuevo? (si/no): ").strip().lower()
    if guardar_nuevo != 'si':
        print("Gracias, fin del programa.")
        break
#calcular el factorial de un numero usando ciclo while si la respuestas anterior es no terminar el programa y mostrar la lista de numeros factoriales calculados
factoriales = []
while True: 
    numero = int(input("Ingrese un número para calcular su factorial: "))
    factorial = 1
    i = 1
    while i <= numero:
        factorial *= i
        i += 1
    factoriales.append((numero, factorial))
    print(f"El factorial de {numero} es {factorial}.")
    
    continuar = input("¿Desea calcular otro factorial? (si/no): ").strip().lower()
    if continuar != 'si':
        print("Gracias, fin del programa.")
        break
    print("Números y sus factoriales calculados:", factoriales)

"""
#1. Escribe un programa que imprima los números del 1 al 10, uno por línea.
for i in range(1, 11):
    print(i)    
#2.Escribe un programa que pida al usuario números enteros uno por uno. El programa debe seguir pidiendo números y sumándolos hasta que el usuario escriba 0. Luego debe imprimir la suma total.
# Inicializamos la suma en 0
suma_total = 0
# Bucle para pedir números al usuario
while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break  # Salimos del bucle si el usuario ingresa 0
    suma_total += numero  # Sumamos el número ingresado a la suma total
# Imprimimos la suma total
print(f"La suma total es: {suma_total}")
#3.Pide al usuario un número entero y muestra su tabla de multiplicar del 1 al 10.
numero = int(input("Ingrese un número entero para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
# 4.El programa debe tener un número secreto. El usuario tiene que adivinarlo. Mientras no lo adivine, el programa debe seguir preguntando.
# Número secreto
numero_secreto = 7  # Puedes cambiar este número por cualquier otro
# Bucle para pedir al usuario que adivine el número
while True:
    intento = int(input("Adivina el número secreto (entre 1 y 10): "))
    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto.")
        break  # Salimos del bucle si el usuario adivina el número
    else:
        print("Número incorrecto. Intenta de nuevo.")   
#5.Escribe un programa que diga si un número entero es primo o no de un número entero positivo ingresado por el usuario.
numero = int(input("Ingrese un número entero positivo para verificar si es primo: "))
if numero > 1:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")
else:
    print("Por favor, ingrese un número entero positivo mayor que 1.")

