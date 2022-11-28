#JUEGO TRES EN RAYA
row1 = [".",".","."]
row2 = [".",".","."]
row3 = [".",".","."]
print (row1)
print (row2)
print (row3)

def turno1():
    jugador1 = int(input("Jugador 1, intorduce la posición libre en la que quieres poner (1-9 de arriba a la izquierda a la derecha):"))
    if jugador1 <= 0 or jugador1 > 9:
         jugador1 = int(input("Jugador 1, elige del 1 al 9 de arriba a la izquierda a la derecha:"))
    if jugador1<=3:
        if row1[jugador1-1] == ".": 
            row1[jugador1-1] = "O"
        else:
            turno1()
    if jugador1<=6 and jugador1>3:
        if row2[jugador1-4] == ".": 
            row2[jugador1-4] = "O"
        else:
            turno1()
    if jugador1<=9 and jugador1>6:
        if row3[jugador1-7] == ".": 
            row3[jugador1-7] = "O"
        else:
           turno1()
    
def turno2():
    jugador2 = int(input("Jugador 2, intorduce la posición libre en la que quieres poner (1-9 de arriba a la izquierda a la derecha):"))
    if jugador2 <= 0 or jugador2 > 9:
         jugador2 = int(input("Jugador 2, elige del 1 al 9 de arriba a la izquierda a la derecha:"))
    if jugador2<=3:
        if row1[jugador2-1] == ".": 
            row1[jugador2-1] = "X"
        else:
            turno2()
    if jugador2<=6 and jugador2>3:
        if row2[jugador2-4] == ".": 
            row2[jugador2-4] = "X"
        else:
            turno2()
    if jugador2<=9 and jugador2>6:
        if row3[jugador2-7] == ".": 
            row3[jugador2-7] = "X"
        else:
            turno2()
    
turno1()
print (row1)
print (row2)
print (row3)
turno2()
print (row1)
print (row2)
print (row3)

while (row1[0] != row1[1] and row1[1] != row1[2]) or (row2[0] != row2[1] and row2[1] != row2[2] ) or (row3[0] != row3[1] and row3[1] != row3[2] ) or (row1[0] != row2[0] and row2[0] != row3[0]) or (row1[1] != row2[1] and row2[1] != row2[1]) or (row1[2] != row2[2] and row2[2] != row3[2]) or (row1[0] != row2[1] and row2[1] != row3[2]) or (row1[2] != row2[1] and row2[1] != row3[0]):
    turno1()
    print (row1)
    print (row2)
    print (row3)
    if (row1[0] == row1[1] and row1[1] == row1[2] and row1[0] != ".") or (row2[0] == row2[1] and row2[1] == row2[2] and row2[0] != ".") or (row3[0] == row3[1] and row3[1] == row3[2] and row3[0] != ".") or (row1[0] == row2[0] and row2[0] == row3[0]and row1[0] != ".") or (row1[1] == row2[1] and row2[1] == row2[1]and row2[1] != ".") or (row1[2] == row2[2] and row2[2] == row3[2]and row3[2] != ".") or (row1[0] == row2[1] and row2[1] == row3[2]and row1[0] != ".") or (row1[2] == row2[1] and row2[1] == row3[0] and row1[2] != "."):
        print ("Gana el jugador 1")
        break
    turno2()
    print (row1)
    print (row2)
    print (row3)
    if (row1[0] == row1[1] and row1[1] == row1[2] and row1[0] != ".") or (row2[0] == row2[1] and row2[1] == row2[2] and row2[0] != ".") or (row3[0] == row3[1] and row3[1] == row3[2] and row3[0] != ".") or (row1[0] == row2[0] and row2[0] == row3[0] and row1[0] != ".") or (row1[1] == row2[1] and row2[1] == row2[1] and row2[1] != ".") or (row1[2] == row2[2] and row2[2] == row3[2] and row3[2] != ".") or (row1[0] == row2[1] and row2[1] == row3[2] and row1[0] != ".") or (row1[2] == row2[1] and row2[1] == row3[0] and row1[2] != "."):
            print ("Gana el jugador 2")
            break
