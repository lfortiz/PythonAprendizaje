#
#Calcula la media de una lista de números
#LFOrtiz - Febrero 2019
#tomado del texto "Python for everybody"
#

## Versión por teclado

#
# Declaración de variables
#
total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)

# versión de lista

numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)