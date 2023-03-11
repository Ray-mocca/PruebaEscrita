# Desarrollo un algoritmo con las estructuras vistas que pregunte al usuario los números ganadores del lotto de ese día
# los almacene en una lista y los muestre en la consola ordenados de menor a mayor y separados por comas.

#Pedir los numeros ganadores
numeros_ganadores = input("Ingrese los números ganadores separados por comas: ")

#convertir los numeros a una lista
lista_numeros = numeros_ganadores.split(",")

#Convertirlos a numeros enteros
lista_numeros = [int(numero) for numero in lista_numeros]

#Ordenar los numeros de menor a mayor
lista_numeros.sort()

#imprimir los numeros ordenados

print("Los numeros ganadores del lotto son: ")
for numero in lista_numeros:
    print(numero)
