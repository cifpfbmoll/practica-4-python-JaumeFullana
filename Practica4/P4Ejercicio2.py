#Pida al usuario 5 números y diga si estos estaban en orden decreciente, 
#creciente o desordenados.
print ("Buenas, introduzca 5 numeros diferentes para que pueda ordenarlos:")

numero1=float(input("Primer numero"))
numero2=float(input("Segundo numero"))
numero3=float(input("Tercer numero"))
numero4=float(input("Cuarto numero"))
numero5=float(input("Quinto numero"))

if (numero1<numero2<numero3<numero4<numero5):
    print("Estan ordenados en orden creciente")
elif(numero1>numero2>numero3>numero4>numero5):
    print("Estan ordenados en orden decreciente")
else:
    print("Estan desordenados")