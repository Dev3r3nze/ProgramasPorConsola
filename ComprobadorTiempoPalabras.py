import time

tm1 = time.perf_counter()

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
intentos = 0
letra1 = 0
letra2 = 0
letra3 = 0
letra4 = 0
letra5 = 0
letra6 = 0
pos = 0

#PALABRA A COMPROBAR
palabra = "zzzzzz"

palabraArr = list(palabra)

palabraAdivinada = ["a","a","a","a","a","a"]

#print(palabraAdivinada != palabraArr)
while palabraAdivinada != palabraArr:
#for i in range()
    if letra6 % 27 == 0 and letra6 != 0:
        letra5 += 1 
        if letra5 % 27 == 0 and letra5 != 0:     
            letra4 += 1
            if letra4 % 27 == 0 and letra4 != 0:
                letra3 += 1
                if letra3 % 27 == 0 and letra3 != 0:
                    letra2 += 1
                    if letra2 % 27 == 0 and letra2 != 0:
                        letra1 += 1
                        letra2 = 0
                        palabraAdivinada[0] = abecedario[letra1]
                    letra3 = 0
                    palabraAdivinada[1] = abecedario[letra2]
                letra4 = 0
                palabraAdivinada[2] = abecedario[letra3]
            palabraAdivinada[3] = abecedario[letra4]
            letra5=0
        palabraAdivinada[4] = abecedario[letra5]
        letra6=0
    palabraAdivinada[5] = abecedario[letra6]
    letra6+=1
    
    intentos+=1
   
print(palabraAdivinada)
print("Intentos:" , intentos)
tm2 = time.perf_counter()
print(f'Total time elapsed: {tm2-tm1:0.2f} seconds')
