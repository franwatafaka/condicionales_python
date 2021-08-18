# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print('{} es mayor que {}'. format(texto_1, texto_2))
else:
    print('{} es mayor que {}'. format(texto_2, texto_1))
# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print('{} posee mas cantidad de letras que {}'.format(texto_1, texto_2))
else:
    print('{} posee mas cantidad de letras que {}'.format(texto_2, texto_1))
# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
if texto_1[:1] > texto_2[:1]:
    print('la letra {} del texto_1 es mayor que {} del texto_2'.format(texto_1[:1], texto_2[:1]))
else:
    print('la letra {} del texto_2 es mayor que {} del texto_1'.format(texto_2[:1], texto_1[:1]))
copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
print('Verifique que copia_texto_1 es igual a texto_1')
if copia_texto_1 == texto_1:
    print('Son iguales')
else:
    print('No son iguales')
# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
print('Verifique que copia_texto_1 es distinta a texto_2')
if copia_texto_1 != texto_2:
    print('Son diferentes')
else:
    print('ambos textos son iguales')