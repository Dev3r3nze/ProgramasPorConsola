#JUEGO PIEDRA, PAPEL O TIJERAS
print("Jugador 1, elige:")
jugador1 = float(input("Piedra(7), Papel (4) o Tijera(1): ")) 
print("Jugador 2, elige:")
jugador2 = float(input("Piedra(9), Papel (6) o Tijera(3): ")) 

if jugador1 == 7 and jugador2 == 9:
    print("Empate")
if jugador1 == 7 and jugador2 == 6:
    print("Gana el jugador 1")
if jugador1 == 7 and jugador2 == 3:
    print("Gana el jugador 2")
if jugador1 == 4 and jugador2 == 9:
    print("Gana el jugador 2")
if jugador1 == 4 and jugador2 == 6:
    print("Empate")
if jugador1 == 4 and jugador2 == 3:
    print("Gana el jugador 1")
if jugador1 == 1 and jugador2 == 9:
    print("Gana el jugador 2")
if jugador1 == 1 and jugador2 == 6:
    print("Gana el jugador 1")
if jugador1 == 1 and jugador2 == 3:
    print("Empate")
