# Resultados del laboratorio

## Integrantes
- Samuel Martínez / carnet: 202401579
- Victor Alonzo / carnet: 202401578
- Gonzalo Guzman / carnet: 202401088

## URL RAW utilizada
`https://raw.githubusercontent.com/202401579-hue/big-o-estructuras-datos/main/data/estudiantes.csv`

## Mediciones

Carnet buscado: EST099999 (último registro, peor caso para List). 100 repeticiones por medición.
En la tabla por tamaños se busca el último carnet de cada muestra. Todas las filas se midieron
en la misma computadora para que la tendencia sea comparable.

| n | List O(n) | Set O(1) promedio | Dict O(1) promedio |
|---:|---:|---:|---:|
| 100 | 0.0000035650 s | 0.0000001060 s | 0.0000001310 s |
| 1,000 | 0.0000354200 s | 0.0000001080 s | 0.0000001160 s |
| 10,000 | 0.0003401150 s | 0.0000001110 s | 0.0000001270 s |
| 50,000 | 0.0021971790 s | 0.0000001150 s | 0.0000001260 s |
| 100,000 | 0.0046245090 s | 0.0000001150 s | 0.0000001230 s |

Validación funcional en n = 100,000: List, Set y Dict devolvieron `True`, es
decir que las tres encontraron el mismo registro. La diferencia no está en el
resultado sino en el costo: List tardó aproximadamente 40,000 veces más que Set
para resolver exactamente la misma consulta.

Tendencia observada: cada vez que n se multiplica por 10, el tiempo de List también
se multiplica aproximadamente por 10 (de 0.0000036 s a 0.0000354 s y luego a 0.00034 s),
y al pasar de 50,000 a 100,000 registros se duplica, igual que n. Set y Dict se mantienen
prácticamente planos, cerca de 0.0000001 s en todos los tamaños.

## Preguntas

**1. ¿Por qué List crece aproximadamente de forma lineal?**
Porque la búsqueda es secuencial: la lista no tiene forma de saber dónde está el
carnet sin revisarlo, así que recorre elemento por elemento comparando hasta
encontrarlo. Si se duplica la cantidad de registros, también se duplica la
cantidad de comparaciones en el peor caso, y por eso el tiempo crece en
proporción directa a n.

**2. ¿Por qué Set y Dict se comportan de forma distinta?**
Porque ambos usan hashing en lugar de recorrido: aplican una función hash al
carnet y eso les indica directamente en qué posición de memoria buscar, sin
revisar los demás elementos, por lo que el costo no depende de n. La diferencia
entre ellos está en lo que devuelven: el Set solo responde si el carnet existe,
mientras que el Dict recupera el registro completo asociado a esa clave.

**3. ¿Medir tiempo es lo mismo que demostrar Big O? Explique.**
No. El tiempo medido depende del hardware, del sistema operativo y de la carga
del equipo en ese momento, así que los mismos algoritmos dan números distintos
en cada computadora. Big O, en cambio, describe cómo crece el trabajo conforme
aumenta n, independientemente de la máquina. Las mediciones sirven como
evidencia empírica que respalda la tendencia, pero no la demuestran por sí solas.

**4. ¿Qué estructura elegiría para búsquedas por carnet y por qué?**
Dictionary, porque el carnet es un identificador único y funciona naturalmente
como clave, permitiendo recuperar el registro completo del estudiante en O(1)
promedio. Construirlo tiene un costo inicial, pero esa inversión se justifica
cuando el sistema hará miles o millones de consultas posteriores. Si únicamente
se necesitara saber si un carnet existe, sin recuperar los datos, bastaría con
un Set.

**5. ¿Qué cambia cuando el carnet buscado no existe?**
En List y en la lista enlazada cambia bastante, porque ya no pueden detenerse al
encontrar una coincidencia: deben revisar los n elementos completos antes de
concluir que el valor no está, es decir que toda búsqueda fallida cae en el peor
caso O(n). En Set y Dict prácticamente no cambia nada, porque el hash los lleva
igual de rápido a la posición donde debería estar el carnet y, al no encontrarlo
ahí, responden de inmediato manteniendo O(1) promedio.

## Lista enlazada (paso 7)

| Operación | Tiempo | Big O |
|---|---:|---|
| Insertar al inicio (100 nodos) | 0.0000002290 s | O(1) |
| Insertar al inicio (10,000 nodos) | 0.0000002090 s | O(1) |
| Buscar primer nodo | 0.0000002380 s | Mejor caso |
| Buscar último nodo | 0.0004111750 s | O(n) |

### Punto de control 7
Una estructura no tiene una sola complejidad: cada operación tiene la suya. En la lista
enlazada, insertar al inicio tardó prácticamente lo mismo con 100 nodos (0.000000229 s)
que con 10,000 nodos (0.000000209 s), porque solo se crea un nodo y se reasignan dos
referencias, sin importar el tamaño: O(1). Buscar, en cambio, depende de la posición: el
primer nodo se encontró en 0.000000238 s, pero el último tardó 0.000411 s, unas 1,700
veces más, porque hubo que recorrer los 10,000 nodos uno por uno. La lista enlazada no
tiene acceso directo por posición: O(n).

## Preguntas obligatorias de análisis (sección 9 de la guía)

**4. ¿Cuál es la diferencia entre medir segundos y analizar Big O?**
Medir segundos da el tiempo real de una ejecución concreta, y ese valor depende del
hardware, del sistema operativo y de la carga del momento; por eso cambia de una
computadora a otra. Big O no mide tiempo: describe cómo crece la cantidad de trabajo
cuando aumenta n. En nuestra tabla, List pasó de 0.0000036 s con 100 registros a
0.0046 s con 100,000: al multiplicar n por 10 el tiempo creció aproximadamente 10 veces,
mientras Set y Dict se mantuvieron cerca de 0.0000001 s en todos los tamaños. Los
segundos son la evidencia; Big O es la explicación de esa tendencia.

**5. ¿Por qué una lista enlazada puede insertar al inicio en O(1) pero buscar en O(n)?**
Insertar al inicio no requiere recorrer la lista: solo se crea el nodo, se le asigna como
siguiente la cabeza actual y se actualiza la cabeza. Son siempre los mismos pasos sin
importar cuántos nodos haya, y por eso tardó lo mismo con 100 que con 10,000 nodos. Para
buscar, en cambio, solo se conoce la cabeza, así que hay que avanzar nodo por nodo hasta
encontrar el carnet. En el peor caso (el último nodo o un carnet que no existe) se
revisan los n nodos, como se vio en la diferencia entre buscar el primer nodo y el último.

## Conclusión

Al comparar las estructuras sobre el mismo conjunto de 100,000 estudiantes quedó
claro que el resultado funcional es idéntico, pero el costo no lo es. List
resolvió la consulta en 0.0046 segundos mientras que Set y Dict lo hicieron en
alrededor de 120 nanosegundos, una diferencia de más de 37,000 veces para la
misma búsqueda. Esa diferencia no viene del lenguaje ni del equipo, sino de cómo
cada estructura organiza la información: List y la lista enlazada recorren
elemento por elemento, por lo que su costo crece con n, mientras que Set y Dict
usan hashing y acceden de forma prácticamente directa. El árbol binario de
búsqueda se ubica en un punto intermedio, ya que descarta parte del espacio en
cada comparación y se acerca a O(log n), pero eso solo se cumple si el árbol
está razonablemente balanceado; un BST básico al que se le insertan carnets ya
ordenados degenera en una cadena y termina comportándose como O(n). También se
observó que no existe una única complejidad por estructura: una lista enlazada
inserta al inicio en O(1) pero busca en O(n), así que la complejidad depende de
la operación y no del nombre de la estructura. Por eso la decisión de diseño se
justifica según las operaciones predominantes del sistema: para consultar
estudiantes por carnet de forma constante, Dictionary es la opción más
conveniente.
