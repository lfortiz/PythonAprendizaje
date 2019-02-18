#
#Mostrar sólo líneas de un fichero de texto que empiezan por From:
#LFOrtiz - Febrero 2019
#tomado del texto "Python for everybody"
#

#
# Declaración de variables
#
count=0
nom_fich = 'mbox-short.txt'
fhand = open(nom_fich)
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)