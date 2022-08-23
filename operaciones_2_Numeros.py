'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Práctica 1 : Fundamentos y Sintaxis Del Lenguaje De Programación
Fecha: 26 De Agosto De 2022
'''

Num1=float(input("Captura Un Número: "))
Num2=float(input("Captura Otro Un Número: "))
while(Num2==0):
    print("No Se Puede Dividir Entre 0, Escribe Otro Número")
    Num2=float(input("Captura Un Número: "))
print(Num1,"+",Num2, "Es",Num1+Num2)
print(Num1,"-",Num2, "Es",Num1-Num2)
print(Num1,"*",Num2, "Es",Num1*Num2)
print(Num1,"/",Num2, "Es",Num1/Num2)
print(Num1,"%",Num2, "Es",Num1%Num2)