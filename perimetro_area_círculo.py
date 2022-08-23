'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Práctica 1 : Fundamentos y Sintaxis Del Lenguaje De Programación
Fecha: 26 De Agosto De 2022
'''
import math

radio=float(input("Radio Del Círculo: "))
while(radio<0):
    print("Captura Un Radio con Valor Positivo")
    radio=float(input("Radio Del Círculo: "))
perimetro=round(math.pi*radio*2,5)
area=round(math.pi*radio**2,5)
print("El Perimetro Del Circulo Con Radio ",radio, "Es",perimetro, "u")
print("El Area Del Circulo Con Radio ",radio, "Es",area, "u^2")