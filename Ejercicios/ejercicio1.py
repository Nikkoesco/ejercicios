numero1 = input("primer numero: ")
numero2 = input("segundo numero: ")
numero3 = input("tercero numero: ")

# Mayor
if numero1 >= numero2 and numero1 >= numero3:
   numero_mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
   numero_mayor = numero2
else: 
   numero_mayor = numero3
   
 # Menor
if numero1 <= numero2 and numero1 <= numero3:
   numero_menor = numero1
elif numero2 <= numero1 and numero2 <= numero3:
   numero_menor = numero2
else: 
   numero_menor = numero3
   
# Medio
if numero1 >= numero2 and numero1 <= numero3 or numero1 <= numero2 and numero1 >= numero3:
   numero_medio = numero1
elif numero2 >= numero1 and numero2 <= numero3 or numero1 <= numero2 and numero1 >= numero3:
   numero_medio = numero2
else: 
   numero_medio = numero3
   
   
   
print("El numero mayor es: ", numero_mayor)
print("El numero medio es: ", numero_medio)
print("El numero menor es: ", numero_menor)