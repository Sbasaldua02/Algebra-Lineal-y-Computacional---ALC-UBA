# -*- coding: utf-8 -*-
import numpy as np
###### LABO 1 Numeros de Maquina ######
def error(x,y):
 return abs(float(x)-float(y))


def error_relativo(x,y):
 return abs(float(x)-float(y))/abs(float(x))

def matricesIguales(A,B):
    if np.shape(A) != np.shape(B):
        return False
    C = np.isclose(A, B, 1e-6)
    for x in np.reshape(C, -1):
        if not x:
            return False
    return True

###### LABO 2 Transformaciones Lineales ######
def rota(theta):
    return np.array([[np.cos(theta),-np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])

def escala(s):
    n = len(s)
    res = np.zeros((n,n))
    for i in range(n):
        res[i,i] = s[i]
    return res

def rota_y_escala (theta , s):
    return  escala(s) @ rota(theta)

def afin(theta ,s ,b):
    M = np.zeros((3,3))
    M[0:2, 0:2] = rota_y_escala(theta, s)
    M[0, 2] = b[0]
    M[1, 2] = b[1]
    M[2, 2] = 1
    return M
 
def trans_afin(v,theta ,s ,b):
    w = np.array([v[0], v[1], 1])      
    r = afin(theta, s, b) @ w          
    return np.array([r[0], r[1]])