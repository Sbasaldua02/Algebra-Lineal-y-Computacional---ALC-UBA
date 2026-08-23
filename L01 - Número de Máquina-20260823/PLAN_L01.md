# Plan de enseñanza — Labo Números de Máquina

Documento de trabajo para acompañar a Santos en este labo. Se rige por el
`CLAUDE.md` de la carpeta raíz: preguntar antes de explicar, pistas nunca código,
diagnosticar si falla la matemática o la programación.

---

## 0. Nota sobre la numeración

La carpeta se llama `L01` pero **el enunciado dice «Laboratorio N° 1»**, igual que
el de numpy (que está en la carpeta `L00`). Los dos PDFs dicen "Laboratorio N°1".
Santos lo llamó "L02" al subirlo. Al hablar con él, usar **"el labo de números de
máquina"** y evitar el número, que genera confusión.

---

## 1. Inventario del material

| Archivo | Qué es | Para qué sirve |
|---|---|---|
| `labo01_numerosDeMaquina_ejercicios.pdf` | **El enunciado.** 10 ejercicios + 3 funciones del módulo ALC | La fuente de verdad |
| `apunte_bits_punto_flotante.pdf` | Apunte de la cátedra: binario, enteros, IEEE 754 paso a paso | Teoría base. Tiene el procedimiento completo de conversión a IEEE 754 con un ejemplo (13,375) |
| `alc_tn_error_numerico.pdf` | Slides de la clase (versión Google Slides) | `fl(x)`, truncamiento vs redondeo, operaciones entre representaciones, el caso del misil Patriot |
| `slides_nromaquina.pdf` | **Slides de la cátedra (LaTeX). La mejor fuente teórica de las cuatro.** | Definiciones formales de error absoluto y relativo (coinciden exactas con los tests), tabla de casos especiales IEEE, machine epsilon vs unit roundoff, y **el ejemplo resuelto de `(1−cos x)/x²`, que es el molde del Ejercicio 4b** |
| `ALC-Clase numero de maquina-2C2026.ipynb` | Notebook de la clase | Demos ejecutables: `np.finfo`, `np.frexp`, `np.nextafter`, float16 |
| `tests01.py` | Tests provistos por la cátedra | **Ver sección 3, tiene una trampa de nombre** |

**Del notebook, lo que más sirve** (celdas por tema):
- `np.finfo(float).max / .tiny / .eps` y `np.nextafter` → el vocabulario del labo
- La demo de que `1 + eps != 1` pero `1 + eps/2 == 1` → definición operativa de epsilon
- `np.frexp` → separa mantisa y exponente, útil para el Ejercicio 3
- Toda la sección de **float16**: es el mejor laboratorio didáctico, porque el
  epsilon es ~0.001 y los efectos se ven a ojo desnudo
- "Problema 1/1'/1''" (sumar magnitudes distintas) → precalienta el Ejercicio 6
- "Problema 2" (cancelación catastrófica con 256.22 − 256.02) → precalienta el Ejercicio 4

---

## 2. El entregable

**Tres funciones para el módulo ALC:**

```python
def error(x, y):            # error de aproximar x usando y, en float64
def error_relativo(x, y):   # error relativo de aproximar x usando y
def matricesIguales(A, B):  # True si son iguales; contemplar dimensiones distintas
```

Más los **10 ejercicios**, que en su mayoría son de exploración y análisis, no de
programar funciones. Es un labo mucho más conceptual que el de numpy.

**Diferencia clave con el labo anterior:** acá **no hay restricción de numpy**. El
enunciado usa `np.sqrt`, `np.float32`, `np.finfo`, `np.linalg.inv` y `@` sin
problema. No repetir la discusión de `np.zeros`.

---

## 3. Trampa en `tests01.py` — resolver esto primero

```python
from lab1 import error, error_relativo, matricesIguales, esSimetrica
```

Dos cosas:

1. **El módulo tiene que llamarse `lab1.py`**, no `librerias.py`. El enunciado no
   fija el nombre, pero el archivo de tests de la cátedra sí lo asume.
2. **Importa `esSimetrica`**, que es del labo anterior. O sea que `lab1.py` tiene
   que exponer también las funciones viejas (importándolas de `librerias.py` o
   reuniendo todo).

Esto hay que decidirlo antes de escribir la primera línea, porque define la
estructura de archivos. Es una decisión de organización, no de contenido:
plantearla como tal y dejar que elija.

---

## 4. Las tres funciones del módulo: qué dicen los tests

Los asserts del enunciado **fijan la definición**. No hay que adivinar.

### `error(x, y)`

```python
assert(not sonIguales(1, 1.1))                                   # |1-1.1| = 0.1  > 1e-8
assert(sonIguales(1, 1 + np.finfo('float64').eps))               # 2.2e-16 < 1e-8
assert(not sonIguales(1, 1 + np.finfo('float32').eps))           # 1.19e-7 > 1e-8
```

→ **`error(x,y) = |x - y|`**, el error absoluto. Los tests solo comparan contra
`atol`, así que el valor absoluto es obligatorio.

**El test que enseña algo** es el cuarto:
```python
assert(not sonIguales(np.float16(1), np.float16(1) + np.finfo('float32').eps))
```
Parece contradictorio: en float16, `1 + 1.19e-7` debería redondear a 1 y dar error 0.
No pasa eso porque **numpy promueve el tipo**: `float16 + float32 → float32`. El
resultado nunca se guarda en float16. Buen ejercicio de lectura.

### `error_relativo(x, y)`

```python
assert(np.allclose(error_relativo(1, 1.1), 0.1))
assert(np.allclose(error_relativo(2, 1), 0.5))
assert(np.allclose(error_relativo(-1, -1), 0))
assert(np.allclose(error_relativo(1, -1), 2))
```

→ **`error_relativo(x,y) = |x - y| / |x|`**. Verificado: dividir por `x`, no por `y`.
El segundo test lo decide — con `/|y|` daría 1, no 0.5. Coherente con el docstring:
"aproximar **x** usando y", así que `x` es el valor verdadero y va al denominador.

Y coincide **textual** con la definición de las slides (lámina 13):
> error absoluto = |x − x̂|,  error relativo = |x − x̂| / |x|  (x ≠ 0)

O sea que las dos funciones no son una convención del enunciado: son las definiciones
de la teoría. Si duda de la fórmula, mandarlo a esa lámina antes que a los tests.

Caso borde no cubierto por los tests: `x = 0`. Decisión suya.

### `matricesIguales(A, B)`

```python
assert(matricesIguales(np.diag([1,1]), np.eye(2)))
assert(matricesIguales(np.linalg.inv(np.array([[1,2],[3,4]])) @ np.array([[1,2],[3,4]]), np.eye(2)))
assert(not matricesIguales(np.array([[1,2],[3,4]]).T, np.array([[1,2],[3,4]])))
```

**El segundo assert es todo el ejercicio**: `inv(A) @ A` **no da la identidad exacta**
en punto flotante. Si `matricesIguales` compara con `==`, ese test falla. Necesita
tolerancia sí o sí.

→ Es **exactamente su `casi_iguales` del labo pasado**, más el chequeo de dimensiones
distintas que ya tiene. Señalárselo: puede reusarla casi tal cual. Buen momento para
que vea que las auxiliares que escribió sin que se las pidieran ahora valen puntos.

---

## 5. Conceptos base, en el orden en que los va a necesitar

1. **Un float no guarda el número, guarda una aproximación.** `format(0.1,'.20f')`
2. **Estructura IEEE 754**: signo, exponente, mantisa. El bit implícito. El sesgo.
   (Apunte, sección 8-9, con el ejemplo de 13,375 hecho paso a paso.)
3. **Qué se puede representar exacto**: fracciones cuya parte fraccionaria en binario
   termina, o sea denominadores potencia de 2. `0.25 = 2⁻²` exacto; `0.1` y `0.3` no.
4. **Epsilon de máquina**: el menor `e` tal que `1 + e != 1`. Es *relativo*, no absoluto:
   mide la separación entre floats consecutivos **cerca de 1**.
   | tipo | eps = distancia de 1 al siguiente | unit roundoff (= eps/2) |
   |---|---|---|
   | float16 | 9.77e-04 | — |
   | float32 | 2⁻²³ ≈ 1.19e-07 | 2⁻²⁴ ≈ 5.96e-08 |
   | float64 | 2⁻⁵² ≈ 2.22e-16 | 2⁻⁵³ ≈ 1.11e-16 |

   Las slides distinguen **machine epsilon** (distancia entre 1 y el siguiente
   representable) de **unit roundoff u** (cota del error relativo al redondear al más
   cercano, que es la mitad). `np.finfo(t).eps` devuelve el primero. La distinción
   importa en el Ejercicio 9, que habla de "los epsilon de máquina".

4b. **Casos especiales de IEEE 754** (tabla en las slides): `E = 0` con mantisa no nula
   son los **subnormales**, que llegan más cerca del cero pero con menos precisión
   efectiva; `E = 255` da `inf` o `NaN`. Es lo que explica `np.finfo(float).tiny`
   (mínimo normalizado) contra `np.nextafter(0., 1.)` (mínimo subnormal), las dos
   celdas del notebook que parecen redundantes y no lo son.
5. **Los floats no están uniformemente distribuidos.** La separación crece con la
   magnitud. En float16, a partir de 2048 solo hay números pares.
6. **Las dos catástrofes**:
   - **Absorción**: sumar algo mucho más chico que el acumulador no cambia nada.
   - **Cancelación catastrófica**: restar dos números casi iguales destruye las
     cifras significativas.

---

## 6. Mapa de los 10 ejercicios

Para cada uno: qué entrena, dónde se va a trabar, y con qué pregunta abrir.

### Ej 1 — Representación de flotantes
- **Entrena:** que `print` miente y `format` no.
- **Trampa:** ninguna, es de calentamiento.
- **Abrir con:** «`0.1 + 0.1 + 0.1 == 0.3` da False. Usá `format(...,'.20f')` en los
  dos lados y decime cuál es el número que sobra o falta.»

### Ej 2 — El `while` que no termina
- **Entrena:** nunca comparar floats con `==` / `!=`.
- **Dato verificado:** `a = 1.0`, restando `0.1`, la sucesión pasa por
  `0.7000000000000001`, `0.6000000000000001`… y **al décimo paso vale
  `-0.4999999999999999`**. Nunca toca `0.1`. El loop es infinito.
- **Abrir con:** «Imprimí `a` con `format(a,'.20f')` en cada vuelta. ¿En qué paso
  deja de ser lo que esperabas?»
- **Solución que tiene que encontrar:** comparar con tolerancia (`while a > 0.1 + tol`)
  o —mejor— **iterar con un contador entero** y calcular `a` a partir de él.
  Esta segunda es la lección de fondo: si podés contar con enteros, contá con enteros.
- **Ojo:** el PDF tiene una errata, muestra `a = a = 0.1`; es `a = a - 0.1`.

### Ej 3 — Una inocente suma
- **Entrena:** por qué unos números son exactos y otros no.
- Tres partes: `0.3+0.25` vs `0.3-0.25`; escribir `0.25` en binario; escribir `0.3`.
- **La clave:** `0.25 = 2⁻²`, mantisa `1.0`, exponente `−2`. Termina. En cambio `0.3`
  en binario es **periódico** (`0.01001100110011...`), igual que `1/3` en decimal.
- **Abrir con:** «Convertí `0.25` a binario con el método del apunte (multiplicar la
  parte fraccionaria por 2 y anotar el bit). ¿En cuántos pasos termina? Ahora hacé
  lo mismo con `0.3`.» — que lo haga hasta aburrirse y vea que no corta.

### Ej 4 — No tan distintos
- **Entrena:** cancelación catastrófica y cómo esquivarla reescribiendo la expresión.
- Parte a: `np.sqrt(2)**2 - 2` no da 0.
- Parte b: las dos expresiones, con `x ∈ [0, 5e-8]`:
  - `y = sqrt(2x²+1) − 1` → **mala**: para `x` chiquito, `sqrt(2x²+1) ≈ 1`, y restar
    dos números casi iguales tira todas las cifras.
  - `y = 2x² / (sqrt(2x²+1) + 1)` → **buena**: es la misma expresión racionalizada,
    pero **suma** en vez de restar.
- **Primero que demuestre que son iguales algebraicamente** (multiplicar y dividir por
  el conjugado). El enunciado lo pide («pruébenlo») y es la parte matemática.
- **Abrir con:** «¿Cuánto vale `sqrt(2x²+1)` cuando `x = 1e-8`? ¿Y qué pasa cuando le
  restás 1?»
- **Atajo que le va a servir:** las láminas 15 a 18 de `slides_nromaquina.pdf` tienen
  **este mismo ejercicio ya resuelto** con otra función: `(1−cos x)/x²` contra
  `2·sin²(x/2)/x²`. Misma estructura (reescribir para eliminar la resta), tabla numérica
  y gráfico en el rango `[−4e-8, 4e-8]`, casi idéntico al que le piden. Si se traba con
  qué graficar o cómo leer el gráfico, mandarlo ahí — no es la respuesta de su ejercicio,
  es el mismo razonamiento aplicado a otra fórmula.

### Ej 5 — Acumulación del error
- **Entrena:** que un error de redondeo inicial puede amplificarse hasta destruir todo.
- **La matemática:** `x₁ = √2` y `xₙ₊₁ = xₙ²/√2`. Si `xₙ = √2`, entonces
  `xₙ₊₁ = 2/√2 = √2`. **La sucesión es constante.** El límite es `√2`.
- **Lo que pasa en la máquina:** `√2` no es exacto. Si `xₙ = √2(1+δ)`, entonces
  `xₙ₊₁ = √2(1+δ)² ≈ √2(1+2δ)`: **el error se duplica en cada paso.** Es un punto
  fijo repulsivo (`f'(√2) = 2 > 1`).
- **Datos verificados:**
  | i | xᵢ |
  |---|---|
  | 1 | 1.4142135623730954 |
  | 30 | 1.414213655272305 |
  | 45 | 1.4172609621968253 |
  | 50 | 1.5150587093244452 |
  | 55 | 12.81674845920085 |
  | 60 | 6.07e+30 |
  | 64 | overflow |
  → **Se desestabiliza alrededor de i ≈ 45-50**, explota en i = 64.
- **La cuenta que explica el número:** el error relativo inicial es ~1e-16 y se duplica
  cada paso. `1e-16 · 2ⁿ ≈ 1` cuando `n ≈ 53`. Coincide.
- **Abrir con:** «Antes de programar nada: calculá `x₂` a mano, con `x₁ = √2`. ¿Cuánto
  da?» — que descubra que la sucesión es constante. Recién ahí el gráfico impacta.

### Ej 6 — Series
- **Entrena:** absorción. El acumulador crece y los términos se achican hasta que dejan
  de tener efecto.
- **Dato verificado (float32):** la suma armónica **se congela en 15.403682708740234**.
  El último `i` que la modifica es **2 097 151 = 2²¹ − 1**. Todo lo que viene después
  se suma en vano. En float64 la misma suma sigue creciendo (15.4913… a 3e6).
- **Por qué justo 2²¹:** cuando `s ≈ 15.4`, está entre 8 y 16, o sea exponente 3. La
  separación entre floats ahí es `2³ · 2⁻²³ = 2⁻²⁰ ≈ 9.5e-7`. Cualquier término menor a
  la mitad de eso (4.77e-7) redondea a nada. Y `1/i < 4.77e-7` cuando `i > 2²¹`.
- **Las tres preguntas "para pensar" del enunciado apuntan todas a esto.**
- **La modificación que cambia el resultado**: sumar **de atrás para adelante**
  (`range(2*10**n, 0, -1)`) da un resultado mayor, porque acumula primero los términos
  chicos entre ellos y no los pierde contra un acumulador grande.
- **Abrir con:** «Cuando la suma va por 15, ¿cuál es el número float32 más cercano a 15
  que le sigue? Y en ese punto, ¿cuánto vale `1/i` si `i` es un millón?»
- **Ojo con el tiempo:** `n=7` son 10⁷ iteraciones en Python, tarda decenas de segundos;
  `5·10⁷` son minutos. Avisarle antes de que crea que se colgó.

### Ej 7 — Arrastre de error: LU
- **Entrena:** que un producto de matrices "exacto" en el papel no lo es en la máquina.
- **Dato verificado:** con la `A`, `L` y `U` del enunciado, `L@U` **difiere de `A` en
  8.88e-16**. No son iguales bit a bit.
- Es la justificación de por qué `matricesIguales` necesita tolerancia. Si la escribe
  con `==`, este ejercicio le da False y el enunciado dice que tiene que dar True.
- **Abrir con:** «Calculá `A - L@U` y mirá el resultado. ¿Es la matriz nula?»

### Ej 8 — Arrastre de error: `esSimetrica`
- **Entrena:** que dividir por un número no representable rompe una simetría exacta.
- **Datos verificados** (con `A = np.random.rand(4,4)`):
  | expresión | max\|M − Mᵀ\| | ¿exactamente simétrica? |
  |---|---|---|
  | `A.T@A` | 0.0 | **sí** |
  | `A.T@(A*0.25)/0.25` | 0.0 | **sí** |
  | `A.T@(A*0.2)/0.2` | 4.44e-16 | **no** |
- **La explicación:** `0.25 = 2⁻²` es exacto en binario, así que multiplicar y dividir
  por él no pierde nada. `0.2` **no** es representable, y el ida y vuelta deja residuo.
- **El giro interesante:** como su `esSimetrica` del labo pasado usa tolerancia, las
  tres van a dar `True`. La pregunta buena no es "¿qué devuelve?" sino **"¿por qué
  devolvería False si hubieras usado `==`?"**. Ahí se ve que la decisión de tolerancia
  que tomó en el labo anterior era la correcta.
- **Abrir con:** «Calculá `M - M.T` para los tres casos y mirá el máximo en módulo.»

### Ej 9 (extra) — Ángulos mínimos
- **Entrena:** que el error de representación tiene consecuencias geométricas.
- Usa `np.finfo(t).eps` para los tres tipos. Compara el ángulo calculado con
  `cos θ = aᵀb / (√(aᵀa) √(bᵀb))` contra el exacto `tan θ = √((n−1)γ² / (1−(n−1)γ²))`.
- **Dónde se va a trabar:** el `arccos` de un número muy cercano a 1 es él mismo un
  caso de cancelación — por eso el enunciado da la fórmula del ángulo exacto con
  tangente. Vale la pena que note *por qué* dan esa fórmula alternativa.
- Puede reusar su `calcularAx` / productos del labo anterior.

### Ej 10 (extra) — Eso no es la identidad
- `A = [[0.1, 1], [0, 1]]`. **`A⁻¹ = [[10, −10], [0, 1]]`** (verificable a mano).
- `A A⁻¹ = I` da bien. Pero `Aⁿ (A⁻¹)ⁿ` se degrada al crecer `n`, porque `0.1` no es
  exacto y el error se multiplica en cada potencia.
- **Abrir con:** «¿Cuánto vale `0.1` de verdad? Si `A` ya no es la matriz que creés,
  ¿qué es `A¹⁰⁰`?»

---

## 7. Orden de ataque sugerido

| # | Ejercicios | Por qué |
|---|---|---|
| 1 | **1, 2, 3** | Los tres son la misma idea vista de tres formas. Cortos, y arman la intuición. |
| 2 | **Módulo: `error`, `error_relativo`** | Salen en dos líneas cada una y los tests las definen sin ambigüedad. Victoria rápida. |
| 3 | **Módulo: `matricesIguales`** | Reusa `casi_iguales`. Y habilita el 7 y el 8. |
| 4 | **7 y 8** | Aplican `matricesIguales` y `esSimetrica` recién hechas. Son cortos y cierran la idea de "arrastre". |
| 5 | **4** | Primer ejercicio con contenido matemático propio (racionalizar) + gráfico. |
| 6 | **5** | El más lindo conceptualmente. Necesita ver primero que la sucesión es constante. |
| 7 | **6** | El más largo por tiempo de cómputo. Dejarlo cuando tenga paciencia. |
| 8 | **9 y 10** | Extras. Solo si va sobrado. |

---

## 8. Cómo aplicarle el `CLAUDE.md` en este labo

**Lo que ya domina** (del labo anterior, observado):
- Bajar una fórmula matemática a un doble bucle: sale solo.
- Patrón acumulador, early return, construcción con listas + `np.array`.
- Entendió vista vs copia, y aplicó `.copy()` por iniciativa propia.
- Tests de propiedad: ya los pide él.

**Lo que le cuesta** (observado, tres veces cada uno):
- **Bordes de rangos** (`range` inclusivo/exclusivo, 0-based vs 1-based). Acá aparece
  menos, pero va a volver en el Ej 6 con `range(1, 10**n + 1)`.
- **Interfaz de numpy**: qué shape devuelve algo, qué argumentos toma una función.
  En este labo: `np.finfo(t).eps`, `np.frexp`, `np.nextafter`, `np.float32(...)`.
- **Traducir enunciados densos.** Fue lo que más tiempo le costó (Ej 13 y 14 del labo
  pasado). Este enunciado tiene varios así — el 9 sobre todo.

**Táctica que le funcionó y hay que repetir:**
> **Papel antes que teclado.** Cuando se traba con un enunciado, hacer que escriba el
> resultado concreto esperado (la matriz 3×3, los primeros términos, el valor en un
> punto) **antes** de tocar código. Fue lo que lo destrabó todas las veces.

**Táctica nueva para este labo:**
> **float16 como microscopio.** Cuando un efecto en float64 sea invisible (10⁻¹⁶), pedirle
> que lo reproduzca en `np.float16`, donde el epsilon es ~0.001 y todo se ve a simple
> vista. El notebook de la cátedra usa ese truco y funciona muy bien.

**Sobre pedir soluciones:** en el labo anterior pidió el código directo dos veces y se
lo di una (Ej 18, tras insistir con frustración). Está dentro de lo pactado: ofrecer
pista más fuerte primero, y si insiste, es su decisión. Pero conviene ofrecerle un
corte antes: este labo es más corto y más conceptual, así que si se está frustrando
probablemente sea mejor **cortar la sesión** que entregarle el resultado.

---

## 9. Datos verificados (para no recalcular)

```
eps float16 = 9.765625e-04
eps float32 = 1.192093e-07
eps float64 = 2.220446e-16

Ej 2:  restando 0.1 desde 1.0, al paso 10 vale -0.4999999999999999. Nunca toca 0.1.
Ej 5:  se desestabiliza en i ≈ 45-50; overflow en i = 64.
       i=30 → 1.414213655272305   i=50 → 1.5150587093244452   i=55 → 12.816748459
Ej 6:  float32, suma armónica se congela en 15.403682708740234
       último i que la modifica: 2 097 151 = 2²¹ − 1
       en float64 a 3e6 términos: 15.491338678200574
Ej 7:  max|A − L@U| = 8.881784197001252e-16
Ej 8:  A.T@A y /0.25 → exactamente simétricas; /0.2 → max|M−Mᵀ| = 4.441e-16
Ej 10: A = [[0.1,1],[0,1]] → A⁻¹ = [[10,−10],[0,1]]
```
