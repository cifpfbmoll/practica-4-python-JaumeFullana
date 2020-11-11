#Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y 
#pida los datos según que caso y muestre el resultado.
print("Buenas! bienvenidos a la calculadora de areas de triangulos y\
 cuadrados!")

poligono=input("Si quieres calcular el area de un triangulo ponga: triangulo \n\
Si quieres calcular el area de un cuadrado ponga: cuadrado \n")

if(poligono=="triangulo"):
    
    print("Vale, vamos a calcular el area de un triangulo!")
    
    base_triangulo=float(input("cuantos cm mide la base del triangulo?"))
    altura_triangulo=float(input("cuantos cm mide la altura del triangulo?"))
    
    area_triangulo=(base_triangulo*altura_triangulo)/2
    
    print("El area del triangulo es", area_triangulo)
    
elif(poligono=="cuadrado"):
    
    print("Vale, vamos a calcular el area de un cuadrado!")
    
    lado_cuadrado=float(input("cuantos cms mide uno de los lados del \
cuadrado?"))
    
    area_cuadrado=(lado_cuadrado**2)
    
    print("El area del cuadrado es", area_cuadrado)
    
else:
    
    print("ERROR: porfavor introduzca triangulo o cuadrado")