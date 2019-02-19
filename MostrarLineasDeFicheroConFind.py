#
#Mostrar el final líneas de un fichero de texto que empiezan por From:, usando el método Find
#LFOrtiz - Febrero 2019
#tomado del texto "Python for everybody"
#

#
# Declaración de variables
#
count=0
nom_fich = 'mbox-short.txt'

fhand = open(nom_fich)
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
       print('dentro')

        print(line)
        continue # excluir ese dominio
    #print(line)