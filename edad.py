#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:
from time import localtime

print("Ingrese su fecha de nacimiento.")
try:
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    tiempo = localtime()
    dia_actual = tiempo.tm_mday
    mes_actual = tiempo.tm_mon
    año_actual = tiempo.tm_year
    edad = año_actual - año
    if(mes_actual - mes <= 0 and dia_actual - dia < 0):
        edad -= 1
    print(f"Usted tiene {edad} años")
except ValueError:
    print("No es un número válido")