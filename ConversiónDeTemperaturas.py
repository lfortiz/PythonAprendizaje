#
#Conversión de temperaturas
#LFOrtiz - Febrero 2019
#control de errores
#tomado del texto "Python for everybody"
#

#
# Declaración de variables
#

inp = 0 # temperatura a convertir
cel = 0 #temperatura en grados celsius
fahr = 0 # temperatura en grados Farenheit

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')