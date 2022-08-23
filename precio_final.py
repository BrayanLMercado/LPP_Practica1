'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Práctica 1 : Fundamentos y Sintaxis Del Lenguaje De Programación
Fecha: 26 De Agosto De 2022
'''

precio=float(input("Precio del Artículo: "))
while(precio<0):
    print("El Precio Del Artículo Debe Ser Positivo")
    precio=float(input("Precio del Artículo: "))
precioDesc=round(precio*0.7,2)
precioFinal=round(precioDesc*1.08,2)
print("Precio Con Descuento:",precioDesc)
print("Precio Final:",precioFinal)

