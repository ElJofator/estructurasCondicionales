# Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.

# Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

#   si acaso el triángulo es inválido; y
#   si no lo es, qué tipo de triángulo es.
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
if((a + b) > c and (a + c) > b and (b + c) > a):
    if(a == b == c):
        print("El triángulo es equilátero.")
    elif(a == b or a == c or b == c):
        print("El triángulo es isoceles.")
    else:
        print("El triángulo es escaleno.")
else:
    print("No es un triángulo válido.")