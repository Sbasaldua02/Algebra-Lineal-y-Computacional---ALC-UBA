######################## TESTS LABO 00 ALC ########################
# Un test por ejercicio, como pide el enunciado.
# Se apoya en las funciones definidas en librerias.py.

import numpy as np
from librerias import *


print()
print("=" * 58)
print("           INICIO TESTS LABO 00")
print("=" * 58)


### EJERCICIO 1 ###
assert esCuadrada(np.array([[1, 2], [3, 4]]))
assert esCuadrada(np.array([[7]]))
assert not esCuadrada(np.array([[1, 2], [3, 4], [5, 6]]))
assert not esCuadrada(np.array([1, 2, 3]))          # vector 1D
assert not esCuadrada(np.ones((2, 2, 2)))           # tensor 3D
print("Ej  1   esCuadrada.................. OK")


### EJERCICIO 2 ###
assert casi_iguales(triangSup(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])),
                    np.array([[0, 2, 3], [0, 0, 6], [0, 0, 0]]))
assert casi_iguales(triangSup(np.array([[1, 2, 3], [4, 5, 6]])),
                    np.array([[0, 2, 3], [0, 0, 6]]))
assert casi_iguales(triangSup(np.array([[1, 2], [3, 4], [5, 6]])),
                    np.array([[0, 2], [0, 0], [0, 0]]))
assert casi_iguales(triangSup(np.array([[7]])), np.array([[0]]))

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
assert casi_iguales(triangSup(triangSup(A)), triangSup(A))   # idempotente
print("Ej  2   triangSup................... OK")


### EJERCICIO 3 ###
assert casi_iguales(triangInf(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])),
                    np.array([[0, 0, 0], [4, 0, 0], [7, 8, 0]]))
assert casi_iguales(triangInf(np.array([[1, 2, 3], [4, 5, 6]])),
                    np.array([[0, 0, 0], [4, 0, 0]]))
assert casi_iguales(triangInf(np.array([[1, 2], [3, 4], [5, 6], [7, 8]])),
                    np.array([[0, 0], [3, 0], [5, 6], [7, 8]]))
assert casi_iguales(triangInf(np.array([[7]])), np.array([[0]]))
print("Ej  3   triangInf................... OK")


### EJERCICIO 4 ###
assert casi_iguales(diagonal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])),
                    np.array([[1, 0, 0], [0, 5, 0], [0, 0, 9]]))

# el test cruzado que amarra el bloque 2-3-4
for A in [np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
          np.array([[1, 2, 3], [4, 5, 6]]),
          np.array([[1, 2], [3, 4], [5, 6], [7, 8]]),
          np.array([[7]])]:
    assert casi_iguales(triangSup(A) + triangInf(A) + diagonal(A), A)
print("Ej  4   diagonal.................... OK")


### EJERCICIO 5 ###
assert traza(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) == 15
assert traza(np.arange(15).reshape(3, 5)) == 18          # ancha
assert traza(np.arange(15).reshape(5, 3)) == 12          # alta
assert traza(np.array([[7]])) == 7
assert traza(np.array([[-1, 2], [3, -4]])) == -5
assert abs(traza(np.array([[1.5, 0.0], [0.0, 2.5]])) - 4.0) < 1e-12
print("Ej  5   traza....................... OK")


### EJERCICIO 6 ###
assert casi_iguales(traspuesta(np.array([[1, 2, 3], [4, 5, 6]])),
                    np.array([[1, 4], [2, 5], [3, 6]]))
assert casi_iguales(traspuesta(np.array([[1, 2], [3, 4]])),
                    np.array([[1, 3], [2, 4]]))
assert casi_iguales(traspuesta(np.array([[7]])), np.array([[7]]))

A = np.array([[1, 2, 3], [4, 5, 6]])
assert casi_iguales(traspuesta(traspuesta(A)), A)        # involutiva
assert traza(A) == traza(traspuesta(A))                  # la traza no cambia
print("Ej  6   traspuesta.................. OK")


### EJERCICIO 7 ###
assert esSimetrica(np.array([[1, 7, 3], [7, 4, 5], [3, 5, 6]]))
assert not esSimetrica(np.array([[1, 2], [3, 4]]))
assert not esSimetrica(np.array([[1, 2, 3], [4, 5, 6]]))      # no cuadrada
assert esSimetrica(np.array([[7]]))

A = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
assert esSimetrica(A + traspuesta(A))                          # siempre simetrica
assert esSimetrica(np.array([[1.0, 0.1 + 0.2], [0.3, 1.0]]))   # ruido de float
print("Ej  7   esSimetrica................. OK")


### EJERCICIO 8 ###
assert casi_iguales(calcularAx(np.array([[1, 2], [3, 4]]), np.array([1, 1])),
                    np.array([3, 7]))
assert casi_iguales(calcularAx(np.arange(15).reshape(3, 5), np.array([1, 0, -1, 2, 1])),
                    np.array([8, 23, 38]))
assert casi_iguales(calcularAx(np.array([[1, 2, 3], [4, 5, 6]]), np.array([1, 2, 3])),
                    np.array([14, 32]))
assert casi_iguales(calcularAx(np.array([[7]]), np.array([3])), np.array([21]))

I = np.array([[1., 0, 0], [0, 1, 0], [0, 0, 1]])
x = np.array([5., -2, 7])
assert casi_iguales(calcularAx(I, x), x)                 # Ix = x
print("Ej  8   calcularAx.................. OK")


### EJERCICIO 9 ###
A = np.array([[1, 2], [3, 4]])
intercambiarFilas(A, 0, 1)
assert casi_iguales(A, np.array([[3, 4], [1, 2]]))       # in-place: mira A, no el return

B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
intercambiarFilas(B, 0, 2)
assert casi_iguales(B, np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3]]))

C = np.array([[1, 2, 3], [4, 5, 6]])                     # no cuadrada
intercambiarFilas(C, 0, 1)
assert casi_iguales(C, np.array([[4, 5, 6], [1, 2, 3]]))

D = np.array([[1, 2], [3, 4]])                           # i == j no cambia nada
intercambiarFilas(D, 1, 1)
assert casi_iguales(D, np.array([[1, 2], [3, 4]]))

E = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])          # dos veces vuelve al original
original = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
intercambiarFilas(E, 0, 2)
intercambiarFilas(E, 0, 2)
assert casi_iguales(E, original)

F = np.array([[1, 2], [3, 4]])                           # fuera de rango tiene que gritar
try:
    intercambiarFilas(F, 0, 5)
    assert False, "tendria que haber tirado IndexError"
except IndexError:
    pass
print("Ej  9   intercambiarFilas........... OK")


### EJERCICIO 10 ###
A = np.array([[1.0, 2.0], [3.0, 4.0]])
sumar_fila_multiplo(A, 0, 1, 0.5)
assert casi_iguales(A, np.array([[2.5, 4.0], [3.0, 4.0]]))

B = np.array([[1.0, 2.0], [3.0, 4.0]])                   # s = 0 no cambia nada
sumar_fila_multiplo(B, 0, 1, 0.0)
assert casi_iguales(B, np.array([[1.0, 2.0], [3.0, 4.0]]))

C = np.array([[2.0, 4.0], [1.0, 2.0]])                   # s negativo anula la fila
sumar_fila_multiplo(C, 0, 1, -2.0)
assert casi_iguales(C, np.array([[0.0, 0.0], [1.0, 2.0]]))

D = np.array([[1.0, 2.0], [3.0, 4.0]])                   # hacer y deshacer
sumar_fila_multiplo(D, 0, 1, 0.5)
sumar_fila_multiplo(D, 0, 1, -0.5)
assert casi_iguales(D, np.array([[1.0, 2.0], [3.0, 4.0]]))
print("Ej 10   sumar_fila_multiplo......... OK")


### EJERCICIO 11 ###
assert esDiagonalmenteDominante(np.array([[5, 1, 1], [1, 6, 2], [0, 1, 4]]))
assert not esDiagonalmenteDominante(np.array([[4, -1, 2], [1, 5, -2], [2, 1, 3]]))  # empata
assert not esDiagonalmenteDominante(np.array([[1, 2], [3, 1]]))
assert esDiagonalmenteDominante(np.array([[-5, 1], [1, -5]]))     # diagonal negativa
assert esDiagonalmenteDominante(np.array([[7]]))                  # 1x1: 7 > 0
assert not esDiagonalmenteDominante(np.array([[0]]))              # 1x1: 0 > 0 es falso
assert esDiagonalmenteDominante(np.array([[3.0, 0.0], [0.0, -2.5]]))
assert not esDiagonalmenteDominante(np.array([[2, 1, 1], [0, 5, 0], [0, 0, 3]]))
print("Ej 11   esDiagonalmenteDominante.... OK")


### EJERCICIO 12 ###
assert casi_iguales(matrizCirculante(np.array([1, 2, 3])),
                    np.array([[1., 2, 3], [3, 1, 2], [2, 3, 1]]))
assert casi_iguales(matrizCirculante(np.array([5])), np.array([[5.]]))
assert casi_iguales(matrizCirculante(np.array([1.5, -2.0, 0.0])),
                    np.array([[1.5, -2, 0], [0, 1.5, -2], [-2, 0, 1.5]]))

v = np.array([7, 3, 9, 1, 4])
C = matrizCirculante(v)
assert casi_iguales(C[0], v)                     # la primera fila es v
for i in range(5):
    assert C[i, i] == v[0]                       # la diagonal es toda v[0]
print("Ej 12   matrizCirculante............ OK")


### EJERCICIO 13 ###
assert casi_iguales(matrizVandermonde(np.array([2, 3, 5])),
                    np.array([[1., 1, 1], [2, 3, 5], [4, 9, 25]]))
assert casi_iguales(matrizVandermonde(np.array([1, 2])), np.array([[1., 1], [1, 2]]))
assert casi_iguales(matrizVandermonde(np.array([7])), np.array([[1.]]))
assert casi_iguales(matrizVandermonde(np.array([0.5, 2.0])),
                    np.array([[1., 1], [0.5, 2]]))

v = np.array([3, -1, 4, 2])
V = matrizVandermonde(v)
assert casi_iguales(V[0], np.array([1., 1, 1, 1]))   # fila 0: todo unos
assert casi_iguales(V[1], v)                          # fila 1: el vector tal cual
print("Ej 13   matrizVandermonde........... OK")


### EJERCICIO 14 ###
phi = 1.618033988749895
assert abs(numeroAureo(1) - 1.0) < 1e-12         # F2/F1
assert abs(numeroAureo(2) - 2.0) < 1e-12         # F3/F2
assert abs(numeroAureo(3) - 1.5) < 1e-12         # F4/F3
assert abs(numeroAureo(40) - phi) < 1e-10        # ya convergio

anterior = abs(numeroAureo(10) - phi)            # el error se achica en cada paso
for k in range(11, 25):
    actual = abs(numeroAureo(k) - phi)
    assert actual < anterior
    anterior = actual
print("Ej 14   numeroAureo................. OK")


### EJERCICIO 15 ###
assert lista_fibonacci(3) == [0, 1, 1, 2, 3]
assert lista_fibonacci(5) == [0, 1, 1, 2, 3, 5, 8, 13, 21]

assert casi_iguales(matrizFiboncacci(1), np.array([[0.]]))
assert casi_iguales(matrizFiboncacci(3), np.array([[0., 1, 1], [1, 1, 2], [1, 2, 3]]))
assert casi_iguales(matrizFiboncacci(4),
                    np.array([[0., 1, 1, 2], [1, 1, 2, 3], [1, 2, 3, 5], [2, 3, 5, 8]]))

F = matrizFiboncacci(5)
assert esSimetrica(F)                            # porque i+j = j+i
print("Ej 15   matrizFiboncacci............ OK")


### EJERCICIO 16 ###
assert casi_iguales(matrizHilbert(1), np.array([[1.0]]))
assert casi_iguales(matrizHilbert(2), np.array([[1, 1 / 2], [1 / 2, 1 / 3]]))
assert casi_iguales(matrizHilbert(3), np.array([[1, 1 / 2, 1 / 3],
                                                [1 / 2, 1 / 3, 1 / 4],
                                                [1 / 3, 1 / 4, 1 / 5]]))

H = matrizHilbert(5)
assert esSimetrica(H)
assert abs(H[0, 0] - 1.0) < 1e-12                # la esquina siempre vale 1
for i in range(5):
    for j in range(5):
        assert abs(H[i, j] * (i + j + 1) - 1.0) < 1e-12   # verifica la definicion
print("Ej 16   matrizHilbert............... OK")


### EJERCICIO 17 ###
assert casi_iguales(valores_polinomios_100_puntos(np.array([3., 0, 1]), 3),
                    np.array([4., 3., 4.]))
assert casi_iguales(valores_polinomios_100_puntos(np.array([0., 1]), 2),
                    np.array([-1., 1.]))

p5 = rellenar([-1., 1, -1, 1, -1, 1], 100)       # x^5 - x^4 + x^3 - x^2 + x - 1
p2 = rellenar([3., 0, 1], 100)                    # x^2 + 3
p10 = rellenar([-2.] + [0.] * 9 + [1.], 100)      # x^10 - 2

v5 = valores_polinomios_100_puntos(p5, 100)
v2 = valores_polinomios_100_puntos(p2, 100)
v10 = valores_polinomios_100_puntos(p10, 100)

assert len(v5) == 100 and len(v2) == 100 and len(v10) == 100
assert abs(v5[0] - (-6.0)) < 1e-9 and abs(v5[-1] - 0.0) < 1e-9
assert abs(v2[0] - 4.0) < 1e-9 and abs(v2[-1] - 4.0) < 1e-9
assert abs(v10[0] - (-1.0)) < 1e-9 and abs(v10[-1] - (-1.0)) < 1e-9

for c, v in ((p5, v5), (p2, v2), (p10, v10)):     # contra evaluacion directa
    for k in range(100):
        t = -1.0 + 2.0 * k / 99.0
        assert abs(v[k] - evaluar_directo(c, t)) < 1e-9
print("Ej 17   valores_polinomios.......... OK")


### EJERCICIO 18 ###
A = np.array([[1., 2, 3], [4, 5, 6], [7, 8, 10]])
R = escalonar_filas(A)
assert es_escalonada(R)
assert abs(R[0, 0]) == 7.0                       # eligio el mayor en modulo

assert es_escalonada(escalonar_filas(np.array([[0., 1], [0, 2]])))       # columna nula
assert es_escalonada(escalonar_filas(np.array([[0., 0], [0, 0]])))       # matriz nula
assert es_escalonada(escalonar_filas(np.array([[5., 3, 11], [15, 9, 33], [20, 12, 44]])))
assert es_escalonada(escalonar_filas(np.array([[1., 2], [3, 4], [5, 6], [7, 8]])))

for _ in range(200):                             # 200 matrices al azar
    M = np.random.randn(5, 5) * 10
    assert es_escalonada(escalonar_filas(M))

eps = 1e-18                                      # estabilidad numerica
E = escalonar_filas(np.array([[eps, 1.0], [1.0, 1.0]]))
assert abs(E[0, 0] - 1.0) < 1e-12                # no uso el pivote diminuto
assert abs(E[1, 1] - 1.0) < 1e-9
print("Ej 18   escalonar_filas (pivoteo)... OK")


print("=" * 58)
print("           FIN TESTS LABO 00   -   18/18 OK")
print("=" * 58)
print()
