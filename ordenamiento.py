#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:

try:
    n = int(input("Ingrese la cantidad de números: "))
    lista = []
    for i in range(n):
        lista.append(float(input(f"Ingrese el número {i+1}: ")))
    lista.sort()
    print(lista)
except ValueError:
    print("No es un número válido")