numero1 = int(input("primer numero: "))
numero2 = int(input("segundo numero: "))
numero3 = int(input("tercer numero: "))
numero4 = int(input("cuarto numero: "))

#sumar numeros impares y pares

numeros =[numero1, numero2, numero3, numero4]
cont_pares = 0
pares = 0
cont_impares = 0
impares = 0

for x in numeros:

    if x % 2 == 0:
        pares = pares + x
        cont_pares = cont_pares + 1
    else:
        impares = impares + x 
        cont_impares = cont_impares + 1
        
#promedio pares e impares
        
if cont_pares > 0:
        promedio_pares = pares / cont_pares
else:
        promedio_pares = 0

if cont_impares > 0:
          promedio_impares = impares / cont_impares
        
else:
          promedio_impares = 0

print ("la suma de pares es: ", pares)
print ("la suma de impares es: ", impares)
print ("El promedio de los pares es: ", promedio_pares)
print ("El promedio de los impares es: ", promedio_impares)
        
#Promedio mayor

if promedio_pares > promedio_impares:
    print ("El promedio de pares es mayor que el de impares")
   
elif promedio_impares > promedio_pares:
    print ("El promedio de impares es mayor que el de pares")  

else:
    print ("El promedio de los numeros es igual")    
                  

