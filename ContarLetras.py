#
# Contar letras en un string
# @LFOrtiz - Febrero 2019
# Tomado de Python for Everybody
#

#Declaración de variables
word = 'tengo un perro que se llama pispotero'
letra_a_buscar = 'p'
count = 0
for letter in word:
    if letter == letra_a_buscar:
        count = count + 1
print('Hay ',count,' letras ',letra_a_buscar)
