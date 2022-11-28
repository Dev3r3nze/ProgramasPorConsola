#MAPA
row1 = ["..","..","..","..","..",".."]
row2 = ["..","..","..","..","..",".."]
row3 = ["..","..","..","..","..",".."]
row4 = ["..","..","{}","..","..",".."]
row5 = ["..","..","..","..","..",".."]
row6 = ["..","..","..","..","..",".."]

mapa = [row1,row2,row3,row4,row5,row6]

def printear():
    for i in range(len(mapa)):
        print(mapa[i])
    
printear()

#VARIALBES
pos = 21
actualRow = 0
perder = False
ganar = []

#TURNO
def turno():
    global pos
    global actualRow
    global perder
    
	direccion = 0
    
    while direccion != 2 and direccion != 4 and direccion != 6 and direccion != 8:
        direccion = float(input("Mover arriba (8), derecha(6), abajo(2), izquierda(4): "))
    
    #SACAR ROW
    if pos <= 6:
        actualRow = 0
    
    if pos <= 12 and pos > 6:
        actualRow = 1
    
    if pos <= 18 and pos > 12:
        actualRow = 2
    
    if pos <= 24 and pos > 18:
        actualRow = 3
    
    if pos <= 30 and pos > 24:
        actualRow = 4
    
    if pos <= 36 and pos > 30:
        actualRow = 5
        
    
    #MOVER ARRIBA
    if direccion == 8 and mapa[actualRow-1][pos-6*actualRow-1] == ".." and actualRow != 0:
        mapa[actualRow][pos-6*actualRow-1] = "[]"
        mapa[actualRow-1][pos-6*actualRow-1] = "{}"
        pos -= 6
        
    elif direccion == 8 and(mapa[actualRow-1][pos-6*actualRow-1] == "[]"):
        print("Perdiste")
        perder = True
    elif  direccion == 8: 
        direccion = float(input("No disponible, Mover arriba (8), derecha(6), abajo(2), izquierda(4): "))
        
    
    #MOVER DERECHA
    if pos-6*actualRow != 6 and direccion == 6 and mapa[actualRow][pos-6*actualRow] == "..":
        mapa[actualRow][pos-6*actualRow-1] = "[]"
        mapa[actualRow][pos-6*actualRow] = "{}"
        pos += 1
        
    elif pos-6*actualRow != 7 and direccion == 6 and mapa[actualRow][pos-6*actualRow+1] == "[]":
         print("Perdiste")
         perder = True
    elif  direccion == 6: 
        direccion = float(input("No disponible, Mover arriba (8), derecha(6), abajo(2), izquierda(4): "))  
        
        
    #MOVER ABAJO
    if actualRow != 5 and direccion == 2 and mapa[actualRow+1][pos-6*actualRow-1] == "..":
        mapa[actualRow][pos-6*actualRow-1] = "[]"
        mapa[actualRow+1][pos-6*actualRow-1] = "{}"
        pos += 6
        
    elif actualRow != 5 and direccion == 2 and mapa[actualRow+1][pos-6*actualRow-1] == "[]":
        print("Perdiste")
        perder = True
        
        
    elif  direccion == 2: 
        direccion = float(input("No disponible, Mover arriba (8), derecha(6), abajo(2), izquierda(4): "))
        
        
    #MOVER IZQUIERDA
    if direccion == 4 and mapa[actualRow][pos-6*actualRow-2] == ".." and actualRow != 5:
        mapa[actualRow][pos-6*actualRow-1] = "[]"
        mapa[actualRow][pos-6*actualRow-2] = "{}"
        pos -= 1
    elif direccion == 4 and mapa[actualRow][pos-6*actualRow-2] == "..":
        print("Perdiste")
        perder = True
    elif  direccion == 4: 
        direccion = float(input("No disponible, Mover arriba (8), derecha(6), abajo(2), izquierda(4): "))
    
    #VUELVA A SACAR LA ROW
    if pos <= 6:
        actualRow = 0
    
    if pos <= 12 and pos > 6:
        actualRow = 1
    
    if pos <= 18 and pos > 12:
        actualRow = 2
    
    if pos <= 24 and pos > 18:
        actualRow = 3
    
    if pos <= 30 and pos > 24:
        actualRow = 4
    
    if pos <= 36 and pos > 30:
        actualRow = 5
      
    if not perder:
        printear()

#PRIMER TURNO
turno()

#COMPRUEBA SI HAS GANADO
for i in range(len(mapa)):
    if mapa[i].count("..") == 0:
        ganar.append(True)
    else:
        ganar.append(False)

#SI HAY ESPACIO, NO HAS GANADO Y NO HAS PERDIDO, SIGUIENTE TURNO
while (mapa[actualRow-1][pos-6*actualRow-1] == "..") or(mapa[actualRow][pos-6*actualRow-1] == ".." ) or (mapa[actualRow][pos-6*actualRow-1] == "..") or (mapa[actualRow][pos-6*actualRow-2] == "..") and not perder and ganar.count(False) >= 1:
    turno()
