#
#Contar líneas de un fichero de texto que empiezen por algo
#LFOrtiz - Febrero 2019
#tomado del texto "Python for everybody"
#

#
# Declaración de variables
#
count=0
fname = ''

#recoger nombre del fichero
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('From:'):
        count = count + 1
print('There were', count, 'from lines in', fname)