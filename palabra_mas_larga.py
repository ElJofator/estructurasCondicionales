p1 = input("Palabra 1: ")
p2 = input("Palabra 2: ")
if(len(p1) > len(p2)):
    print(f"La palabra {p1} tiene {len(p1) - len(p2)} letras más que {p2}")
elif(len(p1) < len(p2)):
    print(f"La palabra {p2} tiene {len(p2) - len(p1)} letras más que {p1}")
else:
    print("Las dos palabras tienen el mismo largo")