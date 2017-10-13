import os 
os.system("cls")
print("*************************************")
print("PROGRAMADOR: Rodrigo Mazariegos")
print("FECHA: 05/10/2017")
print("DESCRIPCION: Ejercicio 6 laboratorio #3")
print("*************************************")

def EsPrimo(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
        return True
    print (EsPrimo(3))
    
           
num=int(input("Ingrese el numero:"))
EsPrimo(num)

