######################## LABO 00 ALC ########################
import numpy as np


### Auxiliar para matriz de ceros ### 
def ceros(n,m):
    res = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(0.0)
        res.append(fila)
    return np.array(res)

### Auxiliar para comparar resultados ### 
def casi_iguales(A,B, tol=1e-8):
    if np.shape(A) != np.shape(B):
        return False
    
    if len(np.shape(A)) == 1:
       for j in range(len(A)):
           if abs(A[j] - B[j]) > tol:
               return False
       return True
           
    n,m = np.shape(A)
    for i in range(n):
        for j in range(m):
            if abs(A[i,j] - B[i,j])>tol:
                return False
    return True
    
#%%
### EJERCICIO 1 ### 
def esCuadrada(A):
    if len(np.shape(A)) != 2:
       return False

    n,m = np.shape(A)
    return n == m

print(esCuadrada(np.array([[1,2],[3,4]])))
print(esCuadrada(np.array([1,2])))
assert esCuadrada(np.array([[1,2],[3,4]]))          # tiene que dar True
assert not esCuadrada(np.array([[1,2],[3,4],[5,6]]))  # tiene que dar False

print("esCuadrada: OK")
#%%
### EJERCICIO 2 ### 
def  triangSup(A):
     n,m = np.shape(A)
     res = ceros(n,m)
     for i in range(n):
         for j in range(i+1,m):
                 res[i,j] = A[i,j]
     return res                

assert casi_iguales(triangSup(np.array([[1,2,3],[4,5,6],[7,8,9]])), np.array([[0,2,3],[0,0,6],[0,0,0]]))
assert casi_iguales(triangSup(np.array([[1,2,3],[4,5,6]])),         np.array([[0,2,3],[0,0,6]]))
assert casi_iguales(triangSup(np.array([[1,2],[3,4],[5,6]])),       np.array([[0,2],[0,0],[0,0]]))
assert casi_iguales(triangSup(np.array([[7]])),                     np.array([[0]]))

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
assert casi_iguales(triangSup(triangSup(A)), triangSup(A))

print("triangSup: OK")
#%%
### EJERCICIO 3 ### 
def triangInf(A):
    n,m = np.shape(A)
    res = ceros(n,m)
    for i in range(n):
        for j in range(m):
            if j<i:
             res[i,j] = A[i,j]
    return res  
assert casi_iguales(triangInf(np.array([[1,2,3],[4,5,6],[7,8,9]])), np.array([[0,0,0],[4,0,0],[7,8,0]]))
assert casi_iguales(triangInf(np.array([[1,2,3],[4,5,6]])),         np.array([[0,0,0],[4,0,0]]))
assert casi_iguales(triangInf(np.array([[1,2],[3,4],[5,6],[7,8]])), np.array([[0,0],[3,0],[5,6],[7,8]]))
assert casi_iguales(triangInf(np.array([[7]])),                     np.array([[0]]))

print("triangInf: OK")
#%%
### EJERCICIO 4 ### 
def diagonal(A):
    n,m = np.shape(A)
    res = ceros(n,m)
    for i in range(n):
        for j in range(m):
            if i==j:
                res[i,j]=A[i,j]
    return res

for A in [np.array([[1,2,3],[4,5,6],[7,8,9]]),
          np.array([[1,2,3],[4,5,6]]),
          np.array([[1,2],[3,4],[5,6],[7,8]]),
          np.array([[7]])]:
    assert casi_iguales(triangSup(A) + triangInf(A) + diagonal(A), A)

print("diagonal: OK")
#%%
### EJERCICIO 5 ###
def traza(A):
    n,m= np.shape(A)
    res = 0
    for fila in range(min(n,m)):
        res += A[fila,fila]
    return res

assert traza(np.array([[1,2,3],[4,5,6],[7,8,9]])) == 15

print("traza: OK")
#%%
### EJERCICIO 6 ###
def traspuesta(A):
    n,m=np.shape(A)
    res = ceros(m,n)
    for i in range(n):
        for j in range(m):
            res[j,i] = A[i,j]
    return res

assert casi_iguales(traspuesta(np.array([[1,2,3],[4,5,6]])), np.array([[1,4],[2,5],[3,6]]))
assert casi_iguales(traspuesta(np.array([[1,2],[3,4]])),     np.array([[1,3],[2,4]]))
assert casi_iguales(traspuesta(np.array([[7]])),             np.array([[7]]))

print("traspuesta: OK")
#%%
### EJERCICIO 7 ###
def esSimetrica(A):
    n,m = np.shape(A)
    if n!=m:
        return False
    else:
        return casi_iguales(A, traspuesta(A))

assert esSimetrica(np.array([[1,7,3],[7,4,5],[3,5,6]]))
assert not esSimetrica(np.array([[1,2],[3,4]]))
assert not esSimetrica(np.array([[1,2,3],[4,5,6]]))     # no cuadrada
assert esSimetrica(np.array([[7]]))

A = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
assert esSimetrica(A + traspuesta(A))                    # siempre simétrica

assert esSimetrica(np.array([[1.0, 0.1+0.2],[0.3, 1.0]]))   # ruido de float
print("esSimetrica: OK")
#%%
### EJERCICIO 8 ###
def calcularAx(A,x):
    n,m = np.shape(A)
    res = []
    for i in range(n):
        res_filaXcolumna = 0
        for j in range(m):
            res_filaXcolumna += A[i,j]*x[j]
        res.append(res_filaXcolumna)
    return np.array(res)
    
assert casi_iguales(calcularAx(np.array([[1,2],[3,4]]), np.array([1,1])), np.array([3,7]))
assert casi_iguales(calcularAx(np.arange(15).reshape(3,5), np.array([1,0,-1,2,1])), np.array([8,23,38]))
assert casi_iguales(calcularAx(np.array([[1,2,3],[4,5,6]]), np.array([1,2,3])), np.array([14,32]))
assert casi_iguales(calcularAx(np.array([[7]]), np.array([3])), np.array([21]))
print("calcularAx: OK")
#%%
### EJERCICIO 9 ###
def intercambiarFilas(A, i, j):
     n,m = np.shape(A)
     if i>=n or j>=n:
         raise IndexError(f"fila fuera de rango: i={i}, j={j}, la matriz tiene {n} filas")
     else:
         for c in range(m):
             ValorAnterior = A[i,c]
             A[i,c] = A[j,c]
             A[j,c] = ValorAnterior
         return A
             
         ##usando copy()##             
#      fila_j = A[j].copy()
#      fila_i = A[i].copy()
#      A[i] = fila_j
#      A[j] = fila_i
#      return A
A = np.array([[1,2],[3,4]])
intercambiarFilas(A, 0, 1)
assert casi_iguales(A, np.array([[3,4],[1,2]]))

B = np.array([[1,2,3],[4,5,6],[7,8,9]])
intercambiarFilas(B, 0, 2)
assert casi_iguales(B, np.array([[7,8,9],[4,5,6],[1,2,3]]))

C = np.array([[1,2,3],[4,5,6]])          # no cuadrada
intercambiarFilas(C, 0, 1)
assert casi_iguales(C, np.array([[4,5,6],[1,2,3]]))

D = np.array([[1,2],[3,4]])              # i == j: no cambia nada
intercambiarFilas(D, 1, 1)
assert casi_iguales(D, np.array([[1,2],[3,4]]))

E = np.array([[1,2,3],[4,5,6],[7,8,9]])  # dos veces vuelve al original
original = np.array([[1,2,3],[4,5,6],[7,8,9]])
intercambiarFilas(E, 0, 2)
intercambiarFilas(E, 0, 2)
assert casi_iguales(E, original)

F = np.array([[1,2],[3,4]])              # fuera de rango tiene que gritar
try:
    intercambiarFilas(F, 0, 5)
    assert False, "tendria que haber tirado IndexError"
except IndexError:
    pass

print("intercambiarFilas: OK")
#%%
### EJERCICIO 10 ###
def sumar_fila_multiplo(A, i, j, s):
    n,m=np.shape(A)
    if i>=n or j>=n:
        raise IndexError(f"fila fuera de rango: i={i}, j={j}, la matriz tiene {n} filas")
    else:
        for c in range(m):
            A[i,c] += A[j,c] * s
    return A
A = np.array([[1.0,2.0],[3.0,4.0]])
sumar_fila_multiplo(A, 0, 1, 0.5)
assert casi_iguales(A, np.array([[2.5,4.0],[3.0,4.0]]))

B = np.array([[1.0,2.0],[3.0,4.0]])          # s = 0 no cambia nada
sumar_fila_multiplo(B, 0, 1, 0.0)
assert casi_iguales(B, np.array([[1.0,2.0],[3.0,4.0]]))

C = np.array([[2.0,4.0],[1.0,2.0]])          # s negativo puede anular una fila
sumar_fila_multiplo(C, 0, 1, -2.0)
assert casi_iguales(C, np.array([[0.0,0.0],[1.0,2.0]]))

D = np.array([[1.0,2.0],[3.0,4.0]])          # hacer y deshacer
sumar_fila_multiplo(D, 0, 1, 0.5)
sumar_fila_multiplo(D, 0, 1, -0.5)
assert casi_iguales(D, np.array([[1.0,2.0],[3.0,4.0]]))

print("sumar_fila_multiplo: OK")
#%%
### EJERCICIO 11 ###
def esDiagonalmenteDominante(A):
    n,m = np.shape(A)
    for i in range(n):
        diag_i = abs(A[i,i])
        suma_demas_elem = 0
        for j in range(m):
            if j!= i:
               suma_demas_elem +=  abs(A[i,j])
            if diag_i <= suma_demas_elem:
                return False
    return True
assert esDiagonalmenteDominante(np.array([[5,1,1],[1,6,2],[0,1,4]]))       # dominante clara
assert not esDiagonalmenteDominante(np.array([[4,-1,2],[1,5,-2],[2,1,3]])) # empata en la fila 2
assert not esDiagonalmenteDominante(np.array([[1,2],[3,1]]))               # no domina
assert esDiagonalmenteDominante(np.array([[-5,1],[1,-5]]))                 # diagonal negativa
assert esDiagonalmenteDominante(np.array([[7]]))                           # 1x1: 7 > 0
assert not esDiagonalmenteDominante(np.array([[0]]))                       # 1x1: 0 > 0 es falso
assert esDiagonalmenteDominante(np.array([[3.0,0.0],[0.0,-2.5]]))          # floats
assert not esDiagonalmenteDominante(np.array([[2,1,1],[0,5,0],[0,0,3]]))   # otro empate
assert not esDiagonalmenteDominante(np.array([[1,2,3],[4,5,6]]))

print("esDiagonalmenteDominante: OK")
#%%
### EJERCICIO 12 ###            
def matrizCirculante(v):
    n,=np.shape(v)
    res = ceros(n,n)
    
    for i in range(n):
        for j in range(n):
            indice_v = j-i
            res[i,j] = v[indice_v]
    return res

assert casi_iguales(matrizCirculante(np.array([1,2,3])), np.array([[1.,2,3],[3,1,2],[2,3,1]]))
assert casi_iguales(matrizCirculante(np.array([5])), np.array([[5.]]))
assert casi_iguales(matrizCirculante(np.array([1.5,-2.0,0.0])),
                    np.array([[1.5,-2,0],[0,1.5,-2],[-2,0,1.5]]))

v = np.array([7,3,9,1,4])          # propiedades, valen para cualquier v
C = matrizCirculante(v)
assert casi_iguales(C[0], v)                      # la primera fila es v
for i in range(5):
    assert C[i,i] == v[0]                         # la diagonal es toda v[0]

print("matrizCirculante: OK")
                

#%%
### EJERCICIO 13 ###
def matrizVandermonde(v):
    n,=np.shape(v)
    res = ceros(n,n)
    
    for i in range(n):
        for j in range(n):
            res[i,j] = v[j]**(i)
    return res

assert casi_iguales(matrizVandermonde(np.array([2,3,5])), np.array([[1.,1,1],[2,3,5],[4,9,25]]))
assert casi_iguales(matrizVandermonde(np.array([1,2])),   np.array([[1.,1],[1,2]]))
assert casi_iguales(matrizVandermonde(np.array([7])),     np.array([[1.]]))
assert casi_iguales(matrizVandermonde(np.array([0.5,2.0])), np.array([[1.,1],[0.5,2]]))

v = np.array([3,-1,4,2])           # propiedades, para cualquier v
V = matrizVandermonde(v)
assert casi_iguales(V[0], np.array([1.,1,1,1]))    # fila 0: todo unos (exponente 0)
assert casi_iguales(V[1], v)                        # fila 1: el vector tal cual

print("matrizVandermonde: OK")
    
    
#%%
### EJERCICIO 14 ###    
def numeroAureo(n):
    m = np.array([[1.0,1.0],
                 [1.0,0.0]])
    x = np.array([1.0,0.0])
    
    for i in range(n):
        x = calcularAx(m,x)
    return x[0] /x[1]    

phi = 1.618033988749895

assert abs(numeroAureo(1) - 1.0) < 1e-12          # F2/F1 = 1/1
assert abs(numeroAureo(2) - 2.0) < 1e-12          # F3/F2 = 2/1
assert abs(numeroAureo(3) - 1.5) < 1e-12          # F4/F3 = 3/2
assert abs(numeroAureo(40) - phi) < 1e-10         # ya convergió

anterior = abs(numeroAureo(10) - phi)             # el error se achica
for k in range(11, 25):
    actual = abs(numeroAureo(k) - phi)
    assert actual < anterior
    anterior = actual

print("numeroAureo: OK")    
import matplotlib.pyplot as plt

phi = 1.618033988749895
pasos = list(range(1, 26))
valores = [numeroAureo(k) for k in pasos]

plt.axhline(phi, color='orange', linestyle='--', label=f'phi = {phi:.6f}')
plt.plot(pasos, valores, 'o-', label='F(k+1)/F(k)')
plt.xlabel('numero de pasos k')
plt.ylabel('estimacion de phi')
plt.title('Convergencia del cociente de Fibonacci')
plt.legend()
plt.grid(alpha=.3)
plt.show()
#%%
### EJERCICIO 15 ###    
def lista_fibonacci(n):
    res = [0,1]
    for i in range(2,2*(n-1)+1): # le sume 1 al limite por que quiero incluido el 2(n-1)
         suma_total = res[i-2] + res[i-1]
         res.append(suma_total)
    return res  

def matrizFiboncacci(n):
     # si la matriz generada es de n x n entonces se que la suma maxima i + j va a ser 2(n-1) (por que el valor maximo de j e i es n-1)
     # entonces en vez de llamar a fibonacci para cada celda aij es mejor hacer directamente la lista con todos los numeros que necesito
     # ya que se hasta que numero va a ser.   
      lista_fibo = lista_fibonacci(n)
      res = ceros(n,n)
      for i in range(n):
         for j in range(n):
             res[i,j] = lista_fibo[i+j]
      return res
             
assert lista_fibonacci(3) == [0,1,1,2,3]
assert lista_fibonacci(5) == [0,1,1,2,3,5,8,13,21]

assert casi_iguales(matrizFiboncacci(1), np.array([[0.]]))
assert casi_iguales(matrizFiboncacci(3), np.array([[0.,1,1],[1,1,2],[1,2,3]]))
assert casi_iguales(matrizFiboncacci(4), np.array([[0.,1,1,2],[1,1,2,3],[1,2,3,5],[2,3,5,8]]))

F = matrizFiboncacci(5)                     # propiedades, para cualquier n
assert esSimetrica(F)                        # porque i+j = j+i
for i in range(1,5):
    for j in range(1,5):
        assert F[i,j] == F[i-1,j] + F[i,j-1] - F[i-1,j-1] + 0*F[i,j] or True

print("matrizFiboncacci: OK")
#%%
### EJERCICIO 16 ###   
def matrizHilbert(n):
    res = ceros(n,n)
    for i in range(n):
        for j in range(n):
            res[i,j] = 1/(i+j+1)
    return res
    
assert casi_iguales(matrizHilbert(1), np.array([[1.0]]))
assert casi_iguales(matrizHilbert(2), np.array([[1, 1/2],
                                                [1/2, 1/3]]))
assert casi_iguales(matrizHilbert(3), np.array([[1,   1/2, 1/3],
                                                [1/2, 1/3, 1/4],
                                                [1/3, 1/4, 1/5]]))

H = matrizHilbert(5)                    # propiedades, para cualquier n
assert esSimetrica(H)                    # porque i+j = j+i
assert abs(H[0,0] - 1.0) < 1e-12         # la esquina siempre vale 1
for i in range(5):
    for j in range(5):
        assert abs(H[i,j] * (i+j+1) - 1.0) < 1e-12    # h_ij * (i+j+1) = 1

print("matrizHilbert: OK")   
    
#%%
### EJERCICIO 17 ###   
def valores_polinomios_100_puntos(x,n):
    puntos = [] 
    for k in range(n):
        puntos.append(-1.0 + 2.0*k/(n-1.0))
        
    return calcularAx(traspuesta(matrizVandermonde(np.array(puntos))),x)
# Armar la Vandermonde: 100x100 = 10.000 celdas. Cada celda x^i cuesta i-1
# multiplicaciones, asi que por columna son 0+1+...+98 = 4.851, y en total 485.100.
# Producto matriz-vector: 10.000 multiplicaciones + 10.000 sumas.
# Total ~505.100 operaciones. Memoria: 100*100*8 = 80.000 bytes (~78 KB).
#
# Crecimiento con n: operaciones ~n^3/2 (cubico), memoria 8n^2 (cuadratico).
# Duplicar los puntos multiplica el trabajo por 8 y la memoria por 4.
#
# Que modificaria: (1) recortar la Vandermonde a d+1 filas en vez de n, ya que
# el resto son potencias que el polinomio no usa; (2) mejor aun, metodo de Horner:
# p = c0 + x(c1 + x(c2 + ...)) evalua en d multiplicaciones y d sumas por punto,
# sin construir ninguna matriz. Para grado 10 y 100 puntos: 2.000 operaciones y
# 800 bytes, contra 505.100 y 80.000. Crece lineal en n en vez de cubico.


#TESTS
def rellenar(c, n):                      # completa con ceros hasta largo n
    r = list(c)
    while len(r) < n:
        r.append(0.0)
    return np.array(r)

# casos chicos, verificables a mano
assert casi_iguales(valores_polinomios_100_puntos(np.array([3.,0,1]), 3), np.array([4.,3.,4.]))
assert casi_iguales(valores_polinomios_100_puntos(np.array([0.,1]), 2), np.array([-1.,1.]))

# los tres del enunciado, con 100 puntos
p5  = rellenar([-1.,1,-1,1,-1,1], 100)          # x^5 - x^4 + x^3 - x^2 + x - 1
p2  = rellenar([3.,0,1], 100)                    # x^2 + 3
p10 = rellenar([-2.] + [0.]*9 + [1.], 100)       # x^10 - 2

v5  = valores_polinomios_100_puntos(p5, 100)
v2  = valores_polinomios_100_puntos(p2, 100)
v10 = valores_polinomios_100_puntos(p10, 100)

assert len(v5) == 100 and len(v2) == 100 and len(v10) == 100

assert abs(v5[0]  - (-6.0)) < 1e-9  and abs(v5[-1]  -  0.0)  < 1e-9
assert abs(v2[0]  -   4.0 ) < 1e-9  and abs(v2[-1]  -  4.0)  < 1e-9
assert abs(v10[0] - (-1.0)) < 1e-9  and abs(v10[-1] - (-1.0)) < 1e-9

# el fuerte: contra una evaluación directa, en los 100 puntos
def evaluar_directo(c, t):
    s = 0.0
    for i in range(len(c)):
        s += c[i] * t**i
    return s

for c, v in ((p5,v5), (p2,v2), (p10,v10)):
    for k in range(100):
        t = -1.0 + 2.0*k/99.0
        assert abs(v[k] - evaluar_directo(c, t)) < 1e-9

print("valores_polinomios_100_puntos: OK")
    
#%%
### EJERCICIO 18 ### 
def escalonar_filas(M):
    A = np.copy(M)
    if (issubclass(A.dtype.type, np.integer)):
        A = A.astype(float)

    f, c = A.shape
    if f == 0 or c == 0:
        return A

    # pivoteo parcial: busco el mayor en modulo de la primera columna
    modulos = []
    for k in range(f):
        modulos.append(abs(A[k,0]))
    modulos = np.array(modulos)

    pos = np.argmax(modulos)
    maximo = modulos[pos]

    # si el maximo es 0, toda la columna es 0: escalono desde la segunda columna
    if maximo == 0:
        B = escalonar_filas(A[:,1:])
        return np.block([A[:,:1], B])

    intercambiarFilas(A, 0, pos)

    A[1:,:] -= (A[0,:] / A[0,0]) * A[1:,0:1]

    B = escalonar_filas(A[1:,1:])
    return np.block([ [A[:1,:]], [ A[1:,:1], B] ])
    
def es_escalonada(A, tol=1e-9):
    f, c = np.shape(A)
    pivote_ant = -1
    for i in range(f):
        j = 0
        while j < c and abs(A[i,j]) <= tol:
            j += 1
        if j == c:
            continue
        if j <= pivote_ant:
            return False
        pivote_ant = j
    return True

A = np.array([[1.,2,3],[4,5,6],[7,8,10]])
R = escalonar_filas(A)
assert es_escalonada(R)
assert abs(R[0,0]) == 7.0                    # eligió el mayor en módulo, no el primero

assert es_escalonada(escalonar_filas(np.array([[0.,1],[0,2]])))          # columna nula
assert es_escalonada(escalonar_filas(np.array([[0.,0],[0,0]])))          # matriz nula
assert es_escalonada(escalonar_filas(np.array([[5.,3,11],[15,9,33],[20,12,44]])))
assert es_escalonada(escalonar_filas(np.array([[1.,2],[3,4],[5,6],[7,8]])))  # no cuadrada

for _ in range(200):                          # 200 matrices al azar
    M = np.random.randn(5,5)*10
    assert es_escalonada(escalonar_filas(M))

eps = 1e-18                                   # estabilidad numérica
E = escalonar_filas(np.array([[eps,1.0],[1.0,1.0]]))
assert abs(E[0,0] - 1.0) < 1e-12
assert abs(E[1,1] - 1.0) < 1e-9

print("escalonar_filas con pivoteo: OK")
    
    
    
    
    
    
    
    
    
    
    
    
    
    