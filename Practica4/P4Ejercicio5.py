#Pida al usuario un importe en euros y diga si el cajero automático le 	puede 
#dar dicho importe utilizando el mismo billete y el más grande 	
#(recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5 	€). 	
#Por ejemplo: 25 euros → “el cajero te devuelve 5 billetes de 5 euros”	
#20 euros → “el cajero te devuelve 1 billete de 20 euros”	
#130 euros → “el cajero te devuelve 13 billetes de 10 euros”

importe=int(input("Diga el importe en euros que quiera sacar y el programa le \n\
dira cuantos billetes le va a dar y de que cantidad. Recuerdo \n\
que solo disponemos de billetes. \n"))

if(importe%5==0 or importe%10==0):
    if(importe%500==0):
        billetes=(importe)/500
        print ("El cajero te devuelve", int(billetes),"de 500")
    elif(importe%200==0):
        billetes=(importe)/200
        print ("El cajero te devuelve", int(billetes),"de 200")
    elif(importe%100==0):
        billetes=(importe)/100
        print ("El cajero te devuelve", int(billetes),"de 100")
    elif(importe%50==0):
        billetes=(importe)/50
        print ("El cajero te devuelve", int(billetes),"de 50")
    elif(importe%20==0):
        billetes=(importe)/20
        print ("El cajero te devuelve", int(billetes),"de 20")
    elif(importe%10==0):
        billetes=(importe)/10
        print ("El cajero te devuelve", int(billetes),"de 10")
    elif(importe%5==0):
        billetes=(importe)/5
        print ("El cajero te devuelve", int(billetes),"de 5")
        
else:
    print ("ERROR: no podemos darle ese importe, solo disponemos de billetes")