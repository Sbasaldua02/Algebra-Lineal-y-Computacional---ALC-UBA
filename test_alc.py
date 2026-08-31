# -*- coding: utf-8 -*-
# Corre TODOS los tests de los enunciados contra alc.py de una sola vez.
# Si algo falla, dice cual es y sigue con el resto.

import numpy as np
import alc

fallas = []

def probar(nombre, f):
    try:
        f()
        print("  OK    " + nombre)
    except AssertionError:
        print("  FALLA " + nombre)
        fallas.append(nombre)
    except Exception as e:
        print("  ERROR " + nombre + "  ->  " + type(e).__name__ + ": " + str(e)[:70])
        fallas.append(nombre)


def sonIguales(x, y, atol=1e-08):
    return np.allclose(alc.error(x, y), 0, atol=atol)


print()
print("========== LABO 1  -  Numeros de maquina ==========")

probar("error 1/5", lambda: (
    None if not sonIguales(1, 1.1) else 1/0))
probar("error 2/5", lambda: (
    None if sonIguales(1, 1 + np.finfo('float64').eps) else 1/0))
probar("error 3/5", lambda: (
    None if not sonIguales(1, 1 + np.finfo('float32').eps) else 1/0))
probar("error 4/5", lambda: (
    None if not sonIguales(np.float16(1), np.float16(1) + np.finfo('float32').eps) else 1/0))
probar("error 5/5", lambda: (
    None if sonIguales(np.float16(1), np.float16(1) + np.finfo('float16').eps, atol=1e-3) else 1/0))

probar("error_relativo 1/4", lambda: (
    None if np.allclose(alc.error_relativo(1, 1.1), 0.1) else 1/0))
probar("error_relativo 2/4", lambda: (
    None if np.allclose(alc.error_relativo(2, 1), 0.5) else 1/0))
probar("error_relativo 3/4", lambda: (
    None if np.allclose(alc.error_relativo(-1, -1), 0) else 1/0))
probar("error_relativo 4/4", lambda: (
    None if np.allclose(alc.error_relativo(1, -1), 2) else 1/0))

probar("matricesIguales 1/3", lambda: (
    None if alc.matricesIguales(np.diag([1, 1]), np.eye(2)) else 1/0))
probar("matricesIguales 2/3", lambda: (
    None if alc.matricesIguales(
        np.linalg.inv(np.array([[1, 2], [3, 4]])) @ np.array([[1, 2], [3, 4]]),
        np.eye(2)) else 1/0))
probar("matricesIguales 3/3", lambda: (
    None if not alc.matricesIguales(
        np.array([[1, 2], [3, 4]]).T, np.array([[1, 2], [3, 4]])) else 1/0))


print()
print("========== LABO 2  -  Transformaciones lineales ==========")

probar("rota 1/3", lambda: (
    None if np.allclose(alc.rota(0), np.eye(2)) else 1/0))
probar("rota 2/3", lambda: (
    None if np.allclose(alc.rota(np.pi/2), np.array([[0, -1], [1, 0]])) else 1/0))
probar("rota 3/3", lambda: (
    None if np.allclose(alc.rota(np.pi), np.array([[-1, 0], [0, -1]])) else 1/0))

probar("escala 1/3", lambda: (
    None if np.allclose(alc.escala([2, 3]), np.array([[2, 0], [0, 3]])) else 1/0))
probar("escala 2/3", lambda: (
    None if np.allclose(alc.escala([1, 1, 1]), np.eye(3)) else 1/0))
probar("escala 3/3", lambda: (
    None if np.allclose(alc.escala([0.5, 0.25]), np.array([[0.5, 0], [0, 0.25]])) else 1/0))

probar("rota_y_escala 1/3", lambda: (
    None if np.allclose(alc.rota_y_escala(0, [2, 3]), np.array([[2, 0], [0, 3]])) else 1/0))
probar("rota_y_escala 2/3", lambda: (
    None if np.allclose(alc.rota_y_escala(np.pi/2, [1, 1]), np.array([[0, -1], [1, 0]])) else 1/0))
probar("rota_y_escala 3/3", lambda: (
    None if np.allclose(alc.rota_y_escala(np.pi, [2, 2]), np.array([[-2, 0], [0, -2]])) else 1/0))

probar("afin 1/3", lambda: (
    None if np.allclose(alc.afin(0, [1, 1], [1, 2]),
                        np.array([[1, 0, 1], [0, 1, 2], [0, 0, 1]])) else 1/0))
probar("afin 2/3", lambda: (
    None if np.allclose(alc.afin(np.pi/2, [1, 1], [0, 0]),
                        np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])) else 1/0))
probar("afin 3/3", lambda: (
    None if np.allclose(alc.afin(0, [2, 3], [1, 1]),
                        np.array([[2, 0, 1], [0, 3, 1], [0, 0, 1]])) else 1/0))

probar("trans_afin 1/3", lambda: (
    None if np.allclose(alc.trans_afin(np.array([1, 0]), np.pi/2, [1, 1], [0, 0]),
                        np.array([0, 1])) else 1/0))
probar("trans_afin 2/3", lambda: (
    None if np.allclose(alc.trans_afin(np.array([1, 1]), 0, [2, 3], [0, 0]),
                        np.array([2, 3])) else 1/0))
probar("trans_afin 3/3", lambda: (
    None if np.allclose(alc.trans_afin(np.array([1, 0]), np.pi/2, [3, 2], [4, 5]),
                        np.array([4, 7])) else 1/0))


print()
print("==========================================================")
if fallas:
    print("  FALLARON " + str(len(fallas)) + " de 27:")
    for f in fallas:
        print("     - " + f)
else:
    print("  LOS 27 TESTS PASAN  -  listo para subir al servidor")
print("==========================================================")
print()
