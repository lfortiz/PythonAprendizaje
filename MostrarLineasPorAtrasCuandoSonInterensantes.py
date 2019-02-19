#
#Mostrar el final líneas de un fichero de texto que empiezan por From:
# cuando son interesantes, tienen algo que contar
#LFOrtiz - Febrero 2019
#tomado del texto "Python for everybody"
#

#
# Declaración de variables
#
count=0
nom_fich = 'mbox-short.txt'
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # Saltar línea "no interesante"
    if not line.startswith('From:'): # no empiezar por From:
        continue
    # Acciones para líneas interesantes
    print(line)
#el resultado es el ya visto, pero así se ve el uso de continue - for