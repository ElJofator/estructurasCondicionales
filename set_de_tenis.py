# El joven periodista Solarrabietas debe relatar un partido de tenis, pero no conoce las reglas del deporte. En particular, no ha logrado aprender cómo saber si un set ya terminó, y quién lo ganó.

# Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, pero además debe haber ganado por lo menos dos juegos más que su rival. Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, el set se define en un último juego, en cuyo caso el resultado final es 7-6.

# Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

# si A ganó el set, o
# si B ganó el set, o
# si el set todavía no termina, o
# si el resultado es inválido (por ejemplo, 8-6 o 7-3).
# Desarrolle un programa que solucione el problema de Solarrabietas:
import math

ja = int(input("Juegos ganados por A: "))
jb = int(input("Juegos ganados por B: "))
if((0 <= ja <= 7) and (0 <= jb <= 7)):
    if(ja <= 5 and jb <= 5):
        print("Aún no termina")
    elif(ja == 7 or jb == 7):
        if(ja == 7 and 5 <= jb <= 6):
            print("Ganó A")
        elif(jb == 7 and 5 <= ja <= 6):
            print("Ganó B")
        else:
            print("Inválido")
    elif(ja == 6 or jb == 6):
        if(abs(ja - jb) >= 2):
            if(ja > jb):
                print("Ganó A")
            else:
                print("Ganó B")
        elif(abs(ja - jb) == 1):
            print("Aún no termina")
        else:
            print("Inválido")
else:
    print("Inválido")