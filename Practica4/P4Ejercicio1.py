#Pida al usuario 5 números y diga cuál es el mayor y cuál el menor.
print ("Buenas, introduzca cinco numeros diferentes, uno por uno, para que asi\
pueda indicarle cual es el mayor y cual el menor:")

numero1=float(input("Primer numero"))
numero2=float(input("Segundo numero"))
numero3=float(input("Tercer numero"))
numero4=float(input("Cuarto numero"))
numero5=float(input("Quinto numero"))

if(numero1>numero2 and numero1>numero3 and numero1>numero4 and numero1>numero5):
    print("El primer numero(",numero1,")es el mayor")
elif(numero2>numero1 and numero2>numero3 and numero2>numero4 and numero2>numero5):
    print("El segundo numero(",numero2,")es el mayor")
elif(numero3>numero1 and numero3>numero2 and numero3>numero4 and numero3>numero5):
    print("El tercer numero(",numero3,")es el mayor")
elif(numero4>numero1 and numero4>numero2 and numero4>numero3 and numero4>numero5):
    print("El cuarto numero(",numero4,")es el mayor")
elif(numero5>numero1 and numero5>numero2 and numero5>numero3 and numero5>numero4):
    print("El quinto numero(",numero5,")es el mayor")  
else:
    print ("ERROR: hay dos numeros mayores iguales")

if(numero1<numero2 and numero1<numero3 and numero1<numero4 and numero1<numero5):
    print("El primer numero(",numero1,") es el menor")
elif(numero2<numero1 and numero2<numero3 and numero2<numero4 and numero2<numero5):
    print("El segundo numero(",numero2,") es el menor")
elif(numero3<numero1 and numero3<numero2 and numero3<numero4 and numero3<numero5):
    print("El tercer numero(",numero3,") es el menor")
elif(numero4<numero1 and numero4<numero2 and numero4<numero3 and numero4<numero5):
    print("El cuarto numero(",numero4,") es el menor")
elif(numero5<numero1 and numero5<numero2 and numero5<numero3 and numero5<numero4):
    print("El quinto numero(",numero5,") es el menor")
else:
    print ("ERROR: hay dos numeros menores iguales")