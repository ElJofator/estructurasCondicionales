#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.
dividendo = float(input("Dividendo: "))
divisor = float(input("Divisor: "))
residuo = dividendo%divisor
if(residuo == 0):
    print("\nLa división es exacta.")
else:
    print("\nLa división no es exacta.")
print(f"Cociente: {int(dividendo/divisor)}")
print(f"Resto: {int(residuo)}")