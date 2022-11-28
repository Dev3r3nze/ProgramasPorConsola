#ADIVINA EL NUMERO RANDOM
import random 
n2 = float(random.randrange(10))
n1 = float(input("Adivina el número (1-10): ") )

while n1 != n2:
  n1 = float(input("No, Introduce otro número: ") )

print("acertado")
