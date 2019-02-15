#
# Buscar el valor máximo y mínimo de una lista
# @LFOrtiz - Febrero 2019
# Tomado de Python for Everybody
#

#Declaración de variables
lista=[3,41,12,9,74,15]
largest=None
smallest=None
print("Antes:", largest)

#Cálculo del máximo
for itervar in lista:
    if largest is None or itervar > largest:
        largest = itervar
    print('Loop: ',itervar,largest)
print('Mayor:',largest)

#Cálculo del mínimo
print("Antes:", smallest)
for itervar in lista:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop: ',itervar,smallest)
print('Menor: ',smallest)

