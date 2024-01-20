#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
try:
    n1 = float(input("Operando: "))
    op = input("Operador (+,-,*,/,**): ")
    n2 = float(input("Operando: "))
    if op == "+":
        s = n1 + n2
        print(s)
    elif op == "-":
        r = n1 - n2
        print(r)
    elif op == "*":
        m = n1 * n2
        print(m)
    elif op == "/" and n2!= 0:
        d = n1 / n2
        print(d)
    elif op == "**":
        m = n1 ** n2
        print(m)
    else:
        print("ERROR")
except ValueError:
    print("No es un número válido")