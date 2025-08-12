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
        print(edad) """
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