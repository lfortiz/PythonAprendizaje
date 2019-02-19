#
#Gestón de errores al ir a abrir un fichero
#LFOrtiz - Febrero 2019
#tomado del texto "Python for everybody"
#

#
# Declaración de variables
#
count=0
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
        print('File cannot be opened:', fname)
        exit()

for line in fhand:
    if line.startswith('From:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)