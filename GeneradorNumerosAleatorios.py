#
#Generador de números aleatorios entre 0 y 1
#LFOrtiz - Febrero 2019
#tomado del texto "Python for everybody"
#

#
# Declaración de variables
#
x=0
import random

print('Números aleatorios')
print('==================')
for i in range(10):
    x = random.random()
    print(x)