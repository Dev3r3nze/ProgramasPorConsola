import time

tm1 = time.perf_counter()

vivo = True
turnos = 0

mapa = [["|////////////////////|"],
["|...........//   //..|"],
["|..........//   //...|"],
["|.........//   //....|"],
["|........//   //.....|"],
["|.......//   //......|"],
["|.......\   \......|"],
["|........\   \.....|"],
["|.........\   \....|"],
["|..........\ o \...|"],
["|...........\   \..|"],
["|\\\\\\\\\\\\\\\\\\\\|"]]

def Printear():
    for i in range(len(mapa)):
        print(mapa[i])

def Turno():
    global vivo
    global turnos
    turnos += 1
    direction = int(input("Indique izquierda (4) o derecha (6):"))
    nuevaLinea = ["|............//   //.|"]
    mapa.insert(1,nuevaLinea)
    posBola = str(mapa[10]).find("o")
    
    if(str(mapa[10]).find("//")!=-1):
        posBarraInicio = str(mapa[9]).find(".//")+2
        posBarraFinal = str(mapa[9]).find("//.")-2
    else:
        posBarraInicio = str(mapa[9]).find(".\\")+2
        posBarraFinal = str(mapa[9]).find("\\.")-2
    
    #print((posBola-1) > posBarraInicio)
    
    if direction == 4 and (posBola-1) > posBarraInicio:
        #seguir
        linea = list(str(mapa[9]))
        
        linea[posBola-1] = "o"
        linea[posBola] = " "
        mapa[9] = ("").join(linea)
        
    if direction == 6 and (posBola) < posBarraFinal:
        #seguir
        linea = list(str(mapa[9]))
        linea[posBola+1] = "o"
        linea[posBola] = " "
        mapa[9] = ("").join(linea)
        
    mapa[10] = str(mapa[10]).replace("o", " ")
    mapa.pop(11)
    Printear()
    #print("posBola: ",posBola, " posInicio: ",posBarraInicio, " posFinal: ", posBarraFinal)
    posBola = str(mapa[9]).find("o")
    #print(posBola )
    if (posBola) <= posBarraInicio or (posBola) >= posBarraFinal:
        print("Te estrellaste")
        vivo = False
    
Printear()

while(vivo):
    #print(vivo)
    Turno()

tm2 = time.perf_counter()
print(f'Tiempo: {tm2-tm1:0.2f} segundos')
print("Has avanzado: ", turnos)
print(f'Velocidad: {turnos/(tm2-tm1):0.2f}')
