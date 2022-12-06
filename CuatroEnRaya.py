mapa = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]

def printear():
    for i in range(len(mapa)):
        print(mapa[i])
        
printear()
ganado1 = 0
ganado2 = 0

def turno(player):
    global ganado1
    global ganado2
    
    if player == 1:
        pos = int(input("Plyer X: "))-1
        if mapa[(len(mapa))-1][pos] == " ":
            mapa[(len(mapa))-1][pos] = "x"
        elif mapa[(len(mapa))-2][pos] == " ":
            mapa[(len(mapa))-2][pos] = "x"
        elif mapa[(len(mapa))-3][pos] == " ":
            mapa[(len(mapa))-3][pos] = "x"
        elif mapa[(len(mapa))-4][pos] == " ":
            mapa[(len(mapa))-4][pos] = "x"
        elif mapa[(len(mapa))-5][pos] == " ":
            mapa[(len(mapa))-5][pos] = "x"
    elif player == 2:
        pos = int(input("Plyer O: "))-1
        if mapa[(len(mapa))-1][pos] == " ":
            mapa[(len(mapa))-1][pos] = "o"
        elif mapa[(len(mapa))-2][pos] == " ":
            mapa[(len(mapa))-2][pos] = "o"
        elif mapa[(len(mapa))-3][pos] == " ":
            mapa[(len(mapa))-3][pos] = "o"
        elif mapa[(len(mapa))-4][pos] == " ":
            mapa[(len(mapa))-4][pos] = "o"
        elif mapa[(len(mapa))-5][pos] == " ":
            mapa[(len(mapa))-5][pos] = "o"
    
    
    for i in range(len(mapa)):
        for j in range(len(mapa[i])-3):
            #caso linea
            if(mapa[i][j] == mapa[i][j+1] and mapa[i][j] == mapa[i][j+2] and mapa[i][j] == mapa[i][j+3] and mapa[i][j] == "x"):
                ganado1 = 1
    
    for i in range(2):
        for j in range(len(mapa[i])-3):
            #caso escalera derecha
            if(mapa[i][j] == mapa[i+1][j+1] and mapa[i][j] == mapa[i+2][j+2] and mapa[i][j] == mapa[i+3][j+3]  and mapa[i][j] == "x"):
                    ganado1 = 1   
                 
    for i in range(2):
        for j in range(len(mapa[i])):   
            #print(str(i) + " - " + str(j))
            #caso hacia abajo
            if(mapa[i][j] == mapa[i+1][j] and mapa[i][j] == mapa[i+2][j] and mapa[i][j] == mapa[i+3][j]  and mapa[i][j] == "x"):
                    ganado1 = 1
    for i in range(len(mapa)-3):
        for j in range(len(mapa[i])):
            #caso escalera invertida
            if(mapa[i+3][j] == mapa[i-1][j-1] and mapa[i+3][j] == mapa[i-2][j-2] and mapa[i+3][j] == mapa[i-3][j-3] and mapa[i+3][j] == "x"):
                    ganado1 = 1  
                    
    for i in range(len(mapa)):
        for j in range(len(mapa[i])-3):
            #caso linea
            if(mapa[i][j] == mapa[i][j+1] and mapa[i][j] == mapa[i][j+2] and mapa[i][j] == mapa[i][j+3] and mapa[i][j] == "o"):
                ganado2 = 1
    
    for i in range(2):
        for j in range(len(mapa[i])-3):
            #caso escalera derecha
            if(mapa[i][j] == mapa[i+1][j+1] and mapa[i][j] == mapa[i+2][j+2] and mapa[i][j] == mapa[i+3][j+3]  and mapa[i][j] == "o"):
                    ganado2 = 1   
                 
    for i in range(2):
        for j in range(len(mapa[i])):   
            #print(str(i) + " - " + str(j))
            #caso hacia abajo
            if(mapa[i][j] == mapa[i+1][j] and mapa[i][j] == mapa[i+2][j] and mapa[i][j] == mapa[i+3][j]  and mapa[i][j] == "o"):
                    ganado2 = 1
    for i in range(len(mapa)-4):
        for j in range(len(mapa[i])):
            #caso escalera invertida
            if(mapa[i+3][j] == mapa[i-1][j-1] and mapa[i+3][j] == mapa[i-2][j-2] and mapa[i+3][j] == mapa[i-3][j-3] and mapa[i+3][j] == "o"):
                    ganado2 = 1   
           
while ganado1 == 0:
    turno(1)
    printear()
    
    if ganado1 == 0:
        turno(2)
        printear()

if ganado1 == 1:
    print("Ganador: X")
else:
    print ("Ganador: O")
