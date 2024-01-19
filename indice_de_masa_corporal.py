# El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

#  	edad < 45	edad ≥ 45
#   IMC < 22.0	bajo	medio
#   IMC ≥ 22.0	medio	alto
# El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.

# Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.
estatura = float(input("Ingrese su estatura (en metros): "))
peso = float(input("Ingrese su peso: "))
edad = int(input("Ingrese su edad: "))
imc = peso/estatura**2
if(0 <= edad < 45):
    if(imc < 22):
        print("El riesgo de que sufras enfermedades coronarias es bajo.")
    elif(imc >= 22):
        print("El riesgo de que sufras enfermedades coronarias es medio.")
elif(45 <= edad <= 150):
    if(imc < 22):
        print("El riesgo de que sufras enfermedades coronarias es medio.")
    elif(imc >= 22):
        print("El riesgo de que sufras enfermedades coronarias es alto.")
else:
    print("Ingrese una edad válida.")