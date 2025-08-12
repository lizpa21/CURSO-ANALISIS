"""#crear un programa que pida al usuario dos numeros, los multiplique y divida todo por el primer numero al cuadrado
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
resultado = (numero1 * numero2) / (numero1 ** 2)
print(f"El resultado de la operación es: {resultado} y su tipo de dato es: {type(resultado)}")
print("El tipo de dato del resultado es:", type(resultado))
#realizar un programa que calcule el indice corporal de una persona, el programa debe preguntar peso t=y altura, y mostrar el resultado
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
indice_corporal = round(peso / (altura ** 2),2)
print(f"El índice corporal es: {indice_corporal} y su tipo de dato es: {type(indice_corporal)}")
print("El tipo de dato del índice corporal es:", type(indice_corporal))"""
#una fabrica de camissetas y pantalones necesita calcular el peso total de camisetas y pantalones que enviara por la empresa de envios. 
# desarrollar unprogramaque pregunte el numero de camisas y pantalones y calcule el peso total del paquete

numero_camisas = int(input("Ingrese el número de camisas: "))
numero_pantalones = int(input("Ingrese el número de pantalones: "))
peso_camisa = 10  # Peso promedio de una camisa en gramos
peso_pantalon = 15  # Peso promedio de un pantalón en gramos
peso_total = (numero_camisas * peso_camisa) + (numero_pantalones * peso_pantalon)
print(f"El peso total del paquete es: {peso_total} kg y su tipo de dato es: {type(peso_total)}")
print("El tipo de dato del peso total es:", type(peso_total))