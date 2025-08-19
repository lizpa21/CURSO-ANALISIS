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
        break"""


