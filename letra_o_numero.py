#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.
digitos = ["0","1","2","3","4","5","6","7","8","9"]
minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
caracter = input("Ingrese caracter: ")
bandera = True
for i in range(len(minusculas)):
    if(i < 10):
        if(caracter == digitos[i]):
            print("Es número.")
            bandera = False
            break
    if(caracter == minusculas[i]):
        print("Es letra minuscula.")
        bandera = False
        break
    if(caracter == mayusculas[i]):
        print("Es letra mayuscula.")
        bandera = False
        break
if(bandera):
   print("No es letra ni número.")