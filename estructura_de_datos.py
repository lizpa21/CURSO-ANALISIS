#definimos una lista de numeros del 1 al 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#recorremos con un ciclo for
for numero in numeros:
    print(numero)
    #accedemos a un valor de la lista
print(numeros[1])  # Imprime el primer elemento de la lista
#agregamos un nuevo valor a la lista
numeros.append(11)
#imprimimos la lista actualizada
print(numeros)
#eliminamos un valor de la lista
del numeros[10]
print(numeros)  # Imprime la lista sin el último elemento
#borrar por valor
numeros.remove(8)
print(numeros)  # Imprime la lista sin el valor 8
#ordenar listas
lista =[1,0,4,5,3,2]
#ordenamos lista ascendente
lista.sort()
print(lista)  # Imprime la lista ordenada ascendentemente
#diccionarios
diccionario = {
    "Daniel": 20,
    "Ana": 22,
    "Luis": 19,
    "Maria": 21
}
#recorremos el diccionario
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
#agregamos un nuevo elemento al diccionario
diccionario["Pedro"] = 23
#imprimimos el diccionario actualizado
print(diccionario)
#eliminamos un elemento del diccionario
del diccionario["Ana"]
#imprimimos el diccionario sin Ana
print(diccionario)  # Imprime el diccionario sin Ana
#ordenar diccionario por clave
diccionario_ordenado = dict(sorted(diccionario.items()))
print(diccionario_ordenado)  # Imprime el diccionario ordenado por clave
#diccionario por valor
diccionario_ordenado_valor = dict(sorted(diccionario.items(), key=lambda item: item[1]))
print(diccionario_ordenado_valor)  # Imprime el diccionario ordenado por valor
#diccionario por valor ascendente   
diccionario_ordenado_valor_asc = dict(sorted(diccionario.items(), key=lambda item: item[1], reverse=True))
print(diccionario_ordenado_valor_asc)  # Imprime el diccionario ordenado por valor ascendente
#tuplas dias de la semana
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
#recorremos la tupla
for dia in dias_semana:
    print(dia)
#accedemos a un valor de la tupla
print(dias_semana[0])  # Imprime el primer elemento de la tupla
#convertir tupla a lista
lista_dias = list(dias_semana)
print(lista_dias)  # Imprime la lista convertida
#crear una f