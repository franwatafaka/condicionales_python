# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados
numero_1 = 7
numero_2 = -2

# Verifique si el numero_1 es mayor a 5
if numero_1 > 5:
#   --> En caso afirmativo, verifique si el numero_2
#       es positivo
    if numero_2 > 0:
#       --> En caso afirmativo imprima en pantalla "Resp=1"
        print('Resp=1')
#       --> En caso negativo imprima en pantalla   "Resp=2"
    else:
        print('Resp=2')
#  --> En caso negativo (numero_1 no es mayor a 5)
else:
#      verifique si el numero_2 es mayor a 5
    if numero_2 > 5:
#       --> En caso afirmativo imprima en pantalla "Resp=3"
        print('Resp=3')
#       --> En caso negativo imprima en pantalla "Resp=4"
    else:
        print('Resp=4')

# Verifique la calificación de un estudiante según su
# puntaje en un examen
puntaje = 70

# Si el puntaje es mayor igual a 90 --> imprimir A
if puntaje >= 90:
    print('A')
# Si el puntaje es mayor igual a 80 --> imprimir B
elif puntaje >=80:
    print('B')
# Si el puntaje es mayor igual a 70 --> imprimir C
elif puntaje >=70:
    print('C')
# Si el puntaje es mayor igual a 60 --> imprimir D
elif puntaje >=60:
    print('D')
# Si el puntaje es menor a  60      --> imprimir F
else:
    print('F')

# Debe imprimir en pantalla la calificacion
# Utilizar "if" anidados
