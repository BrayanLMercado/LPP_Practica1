'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Práctica 1 : Fundamentos y Sintaxis Del Lenguaje De Programación
Fecha: 26 De Agosto De 2022
'''

Pesos=float(input("Cantidad De Pesos: "))
ED=float(input("Equivalencia Dolar a Pesos: ")) # Equivalencia Dolar
EE= float(input("Equivalencia Euro a Pesos: ")) #Equivalencia Euro
print('')
while(Pesos<0 or ED<0 or EE<0):
    print("Captura Unicamente Valores Positivos")
    Pesos=float(input("Cantidad De Pesos: "))
    ED=float(input("Equivalencia Dolar a Pesos: "))
    EE= float(input("Equivalencia Euro a Pesos: ")) 
    print("")
print(Pesos,"Pesos Equivale a",round(Pesos/ED,2), "Dolares")
print(Pesos,"Pesos Equivale a",round(Pesos/EE,2), "Euros")
