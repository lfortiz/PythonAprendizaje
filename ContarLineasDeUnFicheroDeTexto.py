#
#Contar líneas de un fichero de texto
#LFOrtiz - Febrero 2019
#tomado del texto "Python for everybody"
#

#
# Declaración de variables
#
count=0
nom_fich = 'ContarLetras.py'

fhand = open(nom_fich)
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)