# -*- coding: utf-8 -*-

from jugador import *
from moderador import *


if __name__ == "__main__":
    comptador1 = 0
    comptador2 = 0
    comptador_intern = 0

    jugador1 = Jugador("Pere")
    jugador2 = Jugador("Anna")
    jutge = Moderador()

    while comptador1 < 3 and comptador2 < 3 and comptador_intern < 10:
        ma_j1 = jugador1.jugar_una_ma()
        ma_j2 = jugador2.jugar_una_ma()
        ma_guanyadora = jutge.modera(ma_j1, ma_j2)
        if ma_guanyadora == ma_j1:
            comptador1 += 1
            print jugador1.get_nom() + " té avantatge, " + ma_j1 + " guanya a " + ma_j2
        elif ma_guanyadora == ma_j2:
            comptador2 += 1
            print jugador2.get_nom() + " té avantatge, " + ma_j2 + " guanya a " + ma_j1
        else:
<<<<<<< HEAD
=======
            print "Es produeix empat"
>>>>>>> 4b5688233b0798d244955a8a062bf3a9be75936f
        comptador_intern += 1
    if comptador1 > comptador2:
        print jugador1.get_nom() + " ha guanyat"
    elif comptador2 > comptador1:
        print jugador2.get_nom() + " ha guanyat"
    else:
        print "Els dos jugadors han empatat"
