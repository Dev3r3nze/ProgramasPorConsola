import random
mapa = [["[.]","[.]","[.]","[.]","[.]","[.]"],["[.]","[.]","[.]","[.]","[.]","[.]"],["[.]","[.]","[.]","[.]","[.]","[.]"],["[.]","[.]","[.]","[.]","[.]","[.]"],["[.]","[.]","[.]","[.]","[.]","[.]"],["[.]","[.]","[.]","[.]","[.]","[.]"]]

def printear():
    for i in range(len(mapa)): 
        print(mapa[i])
printear()
    
bombas=[]

for i in range(random.randrange(3,8)): 
    bombas.append(str(random.randrange(6)))
    bombas.append(str(random.randrange(6)))

for i in range(int(len(bombas))):
    if i % 2 == 0:
        bombas[i] = bombas[i] + "" + bombas[i+1]
    

for i in range(int(len(bombas))//2):
    bombas.pop(i+1)

#print(bombas)


def turno():
    global bombas 
    
    posX = input("Introduce la columna (1-6): ")
    posY = input("Introduce la fila (1-6): ")
    pos = [posX,posY]
    
    for i in range(len(bombas)):
        if "".join(bombas[i]) == "".join(pos):
            mapa[int(posY)-1][int(posX)-1] = "[x]"
            print("BUUM")
        
        else:
            mapa[int(posY)-1][int(posX)-1] = "[ ]"
    
    
    
    printear()
    
while True:
    turno()
