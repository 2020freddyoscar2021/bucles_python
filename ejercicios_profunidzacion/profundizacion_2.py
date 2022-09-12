# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

from ast import Break
from turtle import goto, st


numero_1 = int(input('Ingrese el primer número de la secuencia\n'))
numero_2 = int(input('Ingrese el segundo número de la secuencia\n')) 

simbolo_ejecutar = str(input('Ingrese el simbolo de comendo ejecutar: \n- Suma (+)\n- Resta (-)\n- Multiplicación (*)\n- División (/)\n- Exponente/Potencia (**)\n- Salir poner (FIN) --> Ingrese simbolo: ' ))

while True:
    if simbolo_ejecutar == '+':
        suma = numero_1 + numero_2
        print('La suma es: ',suma)
        break
    elif simbolo_ejecutar == '-':
        resta = numero_1 - numero_2
        print('La resta es: ',resta)
        break
    elif simbolo_ejecutar == '*':
        multiplica = numero_1 * numero_2
        print('La multiplicacion es: ',multiplica)    
        break
    elif simbolo_ejecutar == '/':
        divide = numero_1 / numero_2
        print('La division es: ',divide)
        break
    elif simbolo_ejecutar == '**':
        potencia = numero_1 ** numero_2
        print('La potencia es: ',potencia)
        break
    elif simbolo_ejecutar == 'FIN':
        break
    else:
        print('Error no ingreso valores indicados vuelva ingresar: ')
        break

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
