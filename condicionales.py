""" condicionales en Python 
#asignar un valor a una variable y usar condicionales para imprimir un mensaje basado en el valor de la variable
x=6
#para comparar valores se usa el operador de igualdad '=='
if x == 5:
    print("x es igual a 5")
else:
    print("x no es igual a 5")

#condicionales con if/elif/else
x=11
if x == 10:
    print("x es igual a 10")
elif x==7:
    print("x es igual a 7")
elif x==5:
    print("x es igual a 5")
else:
    print("x no es igual a 10 ni a 7 ni a 5")
#condicionales con if/elif/else usando >= o >=
x = 13
if x >= 13:
    print("x es mayor que 13")
elif x >= 7:
    print("x es mayor o igual a 7")
elif x >= 3:
    print("x es mayor o igual a 3")
else:
    print("x es mayor o igual q ninguma de las anteriores")
#condicionales con if/elif/else usando operadores logicos
x = 15
if x > 10 and x < 20:
    print("x es mayor que 10 y menor que 20")
elif x < 10 or x > 20:
    print("x es menor que 10 o mayor que 20")
else:
    print("x no cumple ninguna de las condiciones anteriores")

z = 100
if z >= 7 and z <= 14:
    print("z está entre 7 y 14")
elif z > 14 and z <= 20:
    print("z es mayor que 14 y menor o igual a 20")
elif z > 20 and z <= 30:
    print("z es mayor que 20 y menor que 30")
else:
    print("z no cumple ninguna de las condiciones anteriores")
#condicionales anidados
x = 10
if x > 5:
    print("x es mayor que 5")
    if x < 15:
        print("x es menor que 15")
    else:
        print("x es mayor o igual a 15")
else:
    print("x es menor o igual a 5")
    if x < 0:
        print("x es negativo")
    else:
        print("x es positivo o cero")
#preguntar al usuario por el sexo: masculino o femenino, si es masculino preguntar por el numero de dedula y si es femenino preguntar por el numero de pasaporte
sexo = input("Ingrese su sexo (masculino/femenino): ").strip().lower()
if sexo == "masculino":
    cedula = input("Ingrese su número de cédula: ")
    print(f"Usted es masculino y su número de cédula es: {cedula}")
elif sexo == "femenino":
    pasaporte = input("Ingrese su número de pasaporte: ")
    print(f"Usted es femenino y su número de pasaporte es: {pasaporte}")
else:
    print("Sexo no reconocido. Por favor, ingrese 'masculino' o 'femenino'.")
#ingrese el sexo:Masculino(M) o Femenino(F), si es masculino preguntar por la edad, si la edad es igual a 20 imprimir la edad es igual a 20, si es femenino preguntar por su edad si la edad es igual a 21 imprimir la edad es igual a 21
sexo = input("Ingrese su sexo (Masculino(M) o Femenino(F)): ").strip().upper()
if sexo == "M":
    edad = int(input("Ingrese su edad: "))
    if edad == 20:
        print("La edad es igual a 20")
    else:
        print(f"La edad ingresada es {edad}, no es igual a 20.")
elif sexo == "F":
    edad = int(input("Ingrese su edad: "))
    if edad == 21:
        print("La edad es igual a 21")
    else:
        print(f"La edad ingresada es {edad}, no es igual a 21.")
else:
    print("Sexo no reconocido. Por favor, ingrese 'Masculino(M)' o 'Femenino(F)'.")
#calcular el peso ideal para hombres y mujeres, Realizar un programa que pregunte por el sexo (H/M), la altura en metros y el peso en kilogramos, y calcule el peso ideal según la fórmula:
#Para hombres: Peso ideal = (altura en cm - 100) * 0.9
#Para mujeres: Peso ideal = (altura en cm - 100) * 0.85
#El programa debe imprimir el peso ideal y si el peso actual está por debajo,
#por encima o es igual al peso ideal.           
sexo = input("Ingrese su sexo (H/M): ").strip().upper()
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))              
altura_cm = altura * 100
if sexo == "H":
    peso_ideal = (altura_cm - 100) * 0.9
    print(f"El peso ideal para hombres es: {peso_ideal:.2f} kg")
elif sexo == "M":
    peso_ideal = (altura_cm - 100) * 0.85
    print(f"El peso ideal para mujeres es: {peso_ideal:.2f} kg")
else:
    print("Sexo no reconocido. Por favor, ingrese 'H' para hombre o 'M' para mujer.")
    peso_ideal = None   
if peso_ideal is not None:
    if peso < peso_ideal:
        print("El peso actual está por debajo del peso ideal.")
    elif peso > peso_ideal:
        print("El peso actual está por encima del peso ideal.")
    else:
        print("El peso actual es igual al peso ideal.")
#fin del programa
#En estados unidos la mayoria de edad es 21 anos y en colombiaes 18 anos, hacer un programa que pregunte al usuario por su pais de residencia y su edad y de acuerdo a ello imprima si es menor o no de edad
pais = input("Ingrese su país de residencia (Estados Unidos/Colombia): ").strip().lower()
edad = int(input("Ingrese su edad: "))          
if pais == "estados unidos":
    if edad <= 21:
        print("Usted es menor de edad en Estados Unidos.")
    else:
        print("Usted es mayor de edad en Estados Unidos.")
elif pais == "colombia":
    if edad <= 18:
        print("Usted es menor de edad en Colombia.")
    else:
        print("Usted es mayor de edad en Colombia.")
else:
    print("País no reconocido. Por favor, ingrese 'Estados Unidos' o 'Colombia'.")56
#desarrollar un prgrama que pregunte al usuario por un numero entero e imprima si es par o impar
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")  
#desarrollar un programa que pregunte al usuario por un nickname y compare con una variable nickname previamente guardada si coincide  sacar mensaje diciendo nickname ya existe en caso contrario
#sacar mensaje diciendo nickname guardado exitosamente
nickname_guardado = "usuario123"
nickname_usuario = input("Ingrese su nickname: ").strip()
if nickname_usuario == nickname_guardado:
    print("Nickname ya existe.")
else:
    print("Nickname guardado exitosamente.")
    nickname_guardado = nickname_usuario
    
#desarrollar un programa que calcule el imc de un hombre o mujer, el programe debe preguntar por el peso, la altura y el sexo y debe  imprimir los sgtes resultados seegun corresponda bajo peso, normal, sobrepeso, obeso
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
sexo = input("Ingrese su sexo (H/M): ").strip().upper()
imc = peso / (altura ** 2)                      
if imc < 18.5:
    estado = "bajo peso"
elif 18.5 <= imc < 24.9:
    estado = "normal"
elif 25 <= imc < 29.9:
    estado = "sobrepeso"
else:
    estado = "obeso"    
print(f"Su IMC es: {imc:.2f}, lo que indica que tiene un estado de: {estado}.")
#en una tiend alos sgtes productos tienen descuento: camisetas tipo polo 15% de descuento si lleva mas de 5 precio unitario = 40000, jeans en tubo 10% si lleva mas de 3 precio unitario 100000, camisetas en v 4% si lleva mas de 10 precio unitario 60000, hacer un programa que pregunte por el producto y la cantidad y calcule el descuento y el precio final USAR
producto = input("Ingrese el producto (camiseta polo, jeans tubo, camiseta en V): ").strip().lower()
cantidad = int(input("Ingrese la cantidad: "))      
precio_unitario = 0
descuento = 0   
if producto == "camiseta polo":
    precio_unitario = 40000
    if cantidad > 5:
        descuento = 0.15 * precio_unitario * cantidad
elif producto == "jeans tubo":      
    precio_unitario = 100000
    if cantidad > 3:
        descuento = 0.10 * precio_unitario * cantidad
elif producto == "camiseta en v":
    precio_unitario = 60000
    if cantidad > 10:
        descuento = 0.04 * precio_unitario * cantidad
else:
    print("Producto no reconocido. Por favor, ingrese un producto válido.")
    descuento = 0       
precio_final = (precio_unitario * cantidad) - descuento
print(f"El precio final para {cantidad} {producto}(s) es: {precio_final:.2f} COP.")"""
#fin del programa"""
#en una tiend alos sgtes productos tienen descuento: camisetas tipo polo 15% de descuento si lleva mas de 5 precio unitario = 40000, jeans en tubo 10% si lleva mas de 3 precio unitario 100000, camisetas en v 4% si lleva mas de 10 precio unitario 60000, hacer un programa que pregunte por el producto y la cantidad y calcule el descuento y el precio final USAR
#USAR DICCIONARIO
productos = {
    "camiseta polo": {"precio": 40000, "descuento": 0.15, "cantidad_minima": 5},
    "jeans tubo": {"precio": 100000, "descuento": 0.10, "cantidad_minima": 3},
    "camiseta en v": {"precio": 60000, "descuento": 0.04, "cantidad_minima": 10}
}               
producto = input("Ingrese el producto (camiseta polo, jeans tubo, camiseta en V): ").strip().lower()
cantidad = int(input("Ingrese la cantidad: "))
if producto in productos:   
    precio_unitario = productos[producto]["precio"]
    descuento = 0
    if cantidad > productos[producto]["cantidad_minima"]:
        descuento = productos[producto]["descuento"] * precio_unitario * cantidad
    precio_final = (precio_unitario * cantidad) - descuento
    print(f"El precio final para {cantidad} {producto}(s) es: {precio_final:.2f} COP.")
else:
    print("Producto no reconocido. Por favor, ingrese un producto válido.")

