#Pida al usuario tres números y un cuarto número, y compruebe si este último es 
#divisor de los tres números primeros.
print ("Buenas, inserte tres numeros enteros diferentes:")
numero1=int(input("Primer numero"))
numero2=int(input("Segundo numero"))
numero3=int(input("Tercer numero"))

print ("Ahora inserte un cuarto numero entero y comprobaremos si este es \
divisor de los tres primeros")

divisor=float(input("Cuarto numero"))

if(numero1%divisor==0):
    print("El cuarto numero es divisor del primero")
else:
    print("El cuarto numero no es divisor del primero")
    
if(numero2%divisor==0):
    print("El cuarto numero es divisor del segundo")
else:
    print("El cuarto numero no es divisor del segundo")
    
if(numero3%divisor==0):
    print("El cuarto numero es divisor del tercro")
else:
    print("El cuarto numero no es divisor del tercero")
    