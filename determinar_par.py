#Escriba un programa que determine si el número entero ingresado por el usuario es par o no.

try:
    n1 = int(input("Ingresa un número: "))
    if(n1%2 == 0):
        print("Su número es par")
    else:
        print("Su número es impar")
except ValueError:
    print("No es un número válido")