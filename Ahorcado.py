#JUEGO AHORCADO
import random
palabrasComunes = ["que","de","no","a","la","el","es","y","en","lo","un","por","me","una","te","los","se","con","para","mi","si","bien","pero","yo","eso","las","su","tu","del","al","como","le","esto","ya","todo","esta","vamos","muy","hay","ahora","algo","estoy","tengo","nos","nada","cuando","ha","este","puedo","quiero","soy","tiene","gracias","o","bueno","fue","ser","hacer","son","todos","era","eres","vez","tienes","creo","ella","he","ese","voy","puede","sabes","hola","sus","porque","dios","nunca","quieres","casa","favor","esa","dos","tan","señor","tiempo","verdad","estaba","mejor","va"]

palabraElegida = palabrasComunes[random.randrange(len(palabrasComunes))]
palabraArr = []

print("Adivina la palabra: ")

intentos = 5
acierto = 1

while len(palabraElegida) != len(palabraArr):
    palabraArr.append("_")
print (palabraArr)

letras = []
while("".join(palabraArr) != palabraElegida and intentos > 0):
    letra = (input("Introduce una letra: ") )
    for i in range(len(palabraElegida)):
        if(letra == palabraElegida[i]):
            palabraArr[i] = letra
            acierto = 2
        letras.append(letra)
        
    print (palabraArr)
    if acierto == 1:
        intentos -= 1
    acierto = 1
    print ("Te quedan " + str(intentos) + " intentos")
    
    
if intentos == 0:
    print ("Mala suerte :(, no acertaste, la palabra era: '" + palabraElegida + "'. Vuelve a intentarlo")
else:
    print("Correcto, tu palabra es: " + palabraElegida)
