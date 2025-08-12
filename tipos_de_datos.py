"""
#tipos de datos numericos
#int, float, complex
#int: enteros
numero_entero = 10
print("Número entero:", numero_entero)

x=5
resultado = x * 2
print("Resultado de x * 2:", resultado)
#imprimir tipos de datos
print("Tipo de dato de numero_entero:", type(resultado))

#float: decimales

y=3.4

resultado_float = y *2
print("Resultado de y * 2:", resultado_float)
#imprimir tipos de datos
print("Tipo de dato de resultado_float:", type(resultado_float))


#complex: numeros complejos
z = 2 + 3j
t= 5 
resultado_complex = z +t
print("Resultado de z * t:", resultado_complex)
#imprimir tipos de datos
print("Tipo de dato de resultado_complex:", type(resultado_complex))

#tipos de datos cadena
#str: cadenas de texto
cadena_texto = "Hola, Python!"
print("Cadena de texto:", cadena_texto)
#imprimir tipos de datos
print("Tipo de dato de cadena_texto:", type(cadena_texto))
#tipos de datos cadena de texto con concatenación
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print("Nombre completo:", nombre_completo)
#imprimir tipos de datos
print("Tipo de dato de nombre_completo:", type(nombre_completo))  
#hacer un programa q pregunte por la edad y imprima uds tiene esa edad
edad = input("¿Cuál es tu edad? ")
print("Usted tiene", edad, "años.")    
#hacer un programa que pregunte un numero e imprima el numero que usted ingreso es el numero
numero_ingresado = input("Ingrese un número: ")
print("El número que usted ingresó es:", numero_ingresado)   
#hacer un programa que pregunte por un numero e imprima el resultado por 2
numero = input("Ingrese un número para multiplicar por 2: ")
resultado_multiplicacion = int(numero) * 2
print("El resultado de multiplicar", numero, "por 2 es:", resultado_multiplicacion)  
#comentario en bloque

hacer un programa que pregunte por un numero n, e imprima el resultado en la sgte operacion
resultado = n + 1/ 2
  
numero_n = input("Ingrese un número n: ")
resultado_operacion = (int(numero_n) + 1 )/ 2
print("El resultado de la operación n + 1/2 es:", resultado_operacion)
#hacer un programa que pregunte por un numero n, e imprima el resultado en la sgte operacion resultado =(n +1)/2 + n*(3+1)/2
numero_n = input("Ingrese un número n: ")
resultado_operacion = (int(numero_n) + 1 )/ 2 + (int(numero_n) * (3 + 1) )/ 2
print("El resultado de la operación (n + 1)/2 + n*(3 + 1)/2 es:", resultado_operacion)

#tipos de datos listas
lista_numeros = [1, 2, 3, 4, 5]
print("Lista de números:", lista_numeros)
#imprimir tipos de datos
print("Tipo de dato de lista_numeros:", type(lista_numeros))
#lista de cadena de texto
lista_cadenas = ["Python", "Java", "C++"]
print("Lista de cadenas:", lista_cadenas)
#imprimir tipos de datos
print("Tipo de dato de lista_cadenas:", type(lista_cadenas))
#tipos de datos tuplas
tupla_numeros = (10, 20, 30)
print("Tupla de números:", tupla_numeros)
#imprimir tipos de datos
print("Tipo de dato de tupla_numeros:", type(tupla_numeros))
#tupla de cadena de texto
tupla_cadenas = ("Rojo", "Verde", "Azul")
print("Tupla de cadenas:", tupla_cadenas)
#imprimir tipos de datos
print("Tipo de dato de tupla_cadenas:", type(tupla_cadenas)) 
   #tipo de dato rango
rango_numeros = range(1, 10)
print("Rango de números:", list(rango_numeros))
#imprimir tipos de datos
print("Tipo de dato de rango_numeros:", type(rango_numeros))
#generamos un rango con limite inferior 1 y superior 9
rango_numeros = range(1, 10)
print("Rango de números:", list(rango_numeros))
#imprimir tipos de datos
print("Tipo de dato de rango_numeros:", type(rango_numeros))
#generar rango sin limite inferior y limite superior 10
rango_numeros = range(10)
print("Rango de números:", list(rango_numeros))
#imprimir tipos de datos
print("Tipo de dato de rango_numeros:", type(rango_numeros))
#generamos un rango con limite inferior 5 y limite superior 15 con saltos de dos en dos
rango_numeros = range(5, 15, 2)
print("Rango de números con saltos de 2:", list(rango_numeros))
#imprimir tipos de datos
print("Tipo de dato de rango_numeros:", type(rango_numeros))    
#imprimir el rango con numeros pares limite inferior 0 y limite superior 10
rango_pares = range(0, 10, 2)
print("Rango de números pares:", list(rango_pares))
#imprimir tipos de datos
print("Tipo de dato de rango_pares:", type(rango_pares))
#imprimir el rango con numeros impares limite inferior 0 y limite superior 10


rango_impares = range(1, 10, 2)
print("Rango de números impares:", list(rango_impares))
#imprimir tipos de datos
print("Tipo de dato de rango_impares:", type(rango_impares))    
#hallar el area de unt riangulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo = (base * altura) / 2
print("El área del triángulo es:", area_triangulo)


#tipos de datos conjuntos set no pueden llevar duplicados y no se pueden ordenar
conjunto_alumnos = set(["Juan", "María", "Pedro"])
conjunto_alumnosb = set(["Ana", "María", "Pedro"])
#union de conjuntos
conjunto_union = conjunto_alumnos.union(conjunto_alumnosb)
print("Conjunto de alumnos:", conjunto_alumnos)
print("Conjunto de alumnosb:", conjunto_alumnosb)
print("Conjunto de alumnos después de la unión:", conjunto_union)
#imprimir tipos de datos
print("Tipo de dato de conjunto_union:", type(conjunto_union))
#intersección de conjuntos
conjunto_interseccion = conjunto_alumnos.intersection(conjunto_alumnosb)
print("Conjunto de alumnos después de la intersección:", conjunto_interseccion)
#imprimir tipos de datos
print("Tipo de dato de conjunto_interseccion:", type(conjunto_interseccion))   
#tipos de datos con frozenset
#conjunto inmutable frozenset nos epuede modificar
conjunto_inmutable = frozenset(["Python", "Java", "C++"])
print("Conjunto inmutable:", conjunto_inmutable)
#imprimir tipos de datos
print("Tipo de dato de conjunto_inmutable:", type(conjunto_inmutable))  
#tipos de datos diccionarios


diccionario_alumnos = {
      "nombre": 'Carlos',
      "apellido": 'Aguilera'
}
print("Diccionario de alumnos:", diccionario_alumnos)
#imprimir tipos de datos
print("Tipo de dato de diccionario_alumnos:", type(diccionario_alumnos))
#diccionario mixto
diccionario_mixto = {
      "nombre": 'Ana',
      "edad": 25,
      "activo": True
}
print("Diccionario mixto:", diccionario_mixto)
#imprimir tipos de datos
print("Tipo de dato de diccionario_mixto:", type(diccionario_mixto))
#tipos de datos booleanos
x = True
print(type(x))
y = False
print(type(y))
#tipos de datos bytes
byte_data = b"Hola, Python!"
print("Datos en bytes:", byte_data)
#imprimir tipos de datos
print("Tipo de dato de byte_data:", type(byte_data))"""
#tipos de datos bytearray
bytearray_data = bytearray(b"Hola, Python!")
print("Datos en bytearray:", bytearray_data)
#imprimir tipos de datos
print("Tipo de dato de bytearray_data:", type(bytearray_data))

