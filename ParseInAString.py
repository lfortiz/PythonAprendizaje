#
# buscar parte de una cadena a partir de un caracter especificado
# @LFOrtiz - Febrero 2019
# Tomado de Python for Everybody
#

#Declaración de variables
data='From stephen.marquard@uc.ac.za Sat Jan 5 09:14:16 2008'
atpos = 0 #posición en número
sppos = 0 # posición de final
host = '' #cadena destino del trozo que buscamos
atpos = data.find('@') # caracter inicial @
sppos = data.find(' ',atpos)
host = data[atpos+1:sppos]
print(host)
