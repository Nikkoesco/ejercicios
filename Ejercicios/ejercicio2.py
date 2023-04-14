#introducir parametros

par1 = input("Ingrese el primer parametro: ")
par2 = input("Ingrese el segundo parametro: ")
par3 = input("Ingrese el tercer parametro: ")
par4 = input("Ingrese el cuarto parametro: ")

#Función parametro igual a número  
    
def parametro(x):
 try:
     int(x)
     return True
 except ValueError:
     return False

if parametro (par1):
    print("Es un número")
else:
    print("No es número")   
if parametro (par2):
    print("Es un número")
else:
    print("No es número")
if parametro (par3):
    print("Es un número")
else:
    print("No es número")
if parametro (par4):
    print("Es un número")
else:
    print("No es número")
    
 #Funcion palindromo
    
def palindromo(param):
    param = param.lower()
    return param == param[::-1]  
 
if (palindromo(par1)) == True:
    print("El parametro uno es palindromo")
else:
    print("El parametro uno no es palindromo") 
if (palindromo(par2)) == True:
    print("El parametro dos es palindromo")
else:
    print("El parametro dos no es palindromo")
if (palindromo(par3)) == True:
    print("El parametro tres es palindromo")
else:
    print("El parametro tres no es palindromo")
if (palindromo(par4)) == True:
    print("El parametro cuatro es palindromo")
else:
    print("El parametro cuatro no es palindromo")               

#Ordenar parametros   
    orden = [par1, par2, par3, par4] 
    orden.sort()
    print ("los parametros ordenados: ", orden)   
  
    