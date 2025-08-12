"""#hallar el area de unt riangulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo = (base * altura) / 2

#imprimir el resultado usando el fstring
print(f"El área del triángulo es: {area_triangulo} y su tipo de dato es: {type(area_triangulo)}")
print   ("El tipo de dato del área del triángulo es:", type(area_triangulo))
#redondear el área del triángulo a dos decimales
area_triangulo_redondeado = round(area_triangulo, 2)
print(f"El área del triángulo redondeada a dos decimales es: {area_triangulo_redondeado} y su tipo de dato es: {type(area_triangulo_redondeado)}")
print("El tipo de dato del área del triángulo redondeada es:", type(area_triangulo_redondeado))
#la edad de juan  mas la edad de pedro es igual a 60, pedro tiene el doble de la de juan, q edad tienen ambos
edad_juan = float(input("Ingrese la edad de Juan: "))
edad_pedro = 2 * edad_juan
edad_juan + edad_pedro == 60
edad_total = edad_juan + edad_pedro
print(f"La edad de Juan es: {edad_juan} y la de Pedro es: {edad_pedro}")
print(f"La edad total de Juan y Pedro es: {edad_total} y su tipo de dato es: {type(edad_total)}")
print("El tipo de dato de la edad total es:", type(edad_total))

#desarrollar un programe=a que pregunte al usuario por el radio de un círculo y la altura de un cilindro, y calcule el area del cilindro.
import math
radio = float(input("Ingrese el radio del círculo: "))
altura = float(input("Ingrese la altura del cilindro: "))
area_cilindro = round(2 * math.pi * radio * (radio + altura),2)
print(f"El área del cilindro es: {area_cilindro} y su tipo de dato es: {type(area_cilindro)}")
print("El tipo de dato del área del cilindro es:", type(area_cilindro))
#desarrollar un programa que imprima una lista de los numeros pares del uno al 10 
numeros_pares = [num for num in range(1, 11) if num % 2 == 0]
print("Lista de números pares del 1 al 10:", numeros_pares) 
#imprimir tipos de datos
print("Tipo de dato de numeros_pares:", type(numeros_pares))"""
#desarrollar un programa que imprima una lista de los numeros pares del 10 al 20
numeros_pares_10_20 = [num for num in range(10, 21) if num % 2 == 0]
numeros_pares_10_20_2 = range(10, 21,2)
print("Lista de números pares del 10 al 20:", numeros_pares_10_20)
print("Lista de números pares del 10 al 20 forma 2:", numeros_pares_10_20_2)
#imprimir tipos de datos
print("Tipo de dato de numeros_pares_10_20:", type(numeros_pares_10_20))