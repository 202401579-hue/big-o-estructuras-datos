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

## Preguntas de la plantilla

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

## Árbol binario de búsqueda (paso 8)

| Caso | Tiempo | Big O |
|---|---:|---|
| BST mezclado con random.shuffle (5,000 nodos) | 0.0000008190 s | ~O(log n) |
| BST con carnets ya ordenados (2,000 nodos) | 0.0001296190 s | O(n) |

### Punto de control 8
La conclusión no puede afirmar que todo árbol binario de búsqueda garantiza O(log n):
eso solo ocurre si el árbol está razonablemente balanceado. La evidencia lo muestra con
claridad. El árbol degenerado tardó 0.0001296 s en buscar sobre apenas 2,000 nodos, unas
158 veces más que el árbol mezclado, que resolvió la búsqueda en 0.0000008 s sobre 5,000
nodos, más del doble de elementos. La causa es estructural, no de tamaño: al insertar
carnets ya ordenados, cada nuevo nodo siempre es mayor que el anterior, así que el árbol
crece en una sola dirección y se convierte prácticamente en una lista enlazada de un solo
brazo. De hecho, con la inserción recursiva original, esa cadena de 2,000 niveles superaba
el límite de recursión de Python y el programa fallaba con `RecursionError`, por lo que
hubo que reescribir la inserción de forma iterativa para completar la medición. Mezclar
los datos con `random.shuffle` antes de insertar es justamente lo que evita este
escenario, porque reparte los valores y el árbol se ramifica en ambas direcciones.

## Carnet inexistente (paso 9)

| Estructura | Tiempo buscando EST999999 | Big O |
|---|---:|---|
| List | 0.0049407950 s | O(n) siempre |
| Set | 0.0000001260 s | O(1) promedio |
| Dict | 0.0000001490 s | O(1) promedio |
| Lista enlazada | 0.0003419980 s | O(n) siempre |

Al no existir el carnet, List y la lista enlazada ya no pueden detenerse al encontrar una
coincidencia, así que recorren los n elementos completos antes de concluir que no está.
List tardó 0.00494 s, prácticamente lo mismo que en su búsqueda exitosa del último
registro, porque en ambos casos revisa toda la colección. Set y Dict, en cambio, casi no
cambian frente a una búsqueda exitosa (0.000000126 s y 0.000000149 s): el hash los lleva
directo a la posición donde debería estar el carnet y, al no encontrarlo ahí, responden
de inmediato sin recorrer nada más. En este caso, List fue unas 39,000 veces más lenta
que Set.

## Construcción vs consulta (sección 6)

Construir el Set tardó 0.0103227 s y el Dict 0.0169172 s. Es un costo que se paga una
sola vez, y debe compararse con lo que se ahorra en cada consulta: buscar un carnet en
List cuesta unos 0.0046 s, mientras que en el Dict cuesta 0.000000149 s, así que cada
consulta ahorra prácticamente 0.0046 s. Dividiendo 0.0169 s entre 0.0046 s, construir el
Dict se paga solo después de unas 4 consultas (y el Set después de unas 3). A partir de
ahí, cada búsqueda adicional es ganancia neta, lo cual es inmediato en cualquier sistema
que consulte estudiantes con cierta frecuencia.

## Preguntas obligatorias de análisis (sección 9 de la guía)

**1. ¿Por qué una búsqueda secuencial sobre List se clasifica como O(n)?**
Porque la lista no sabe en qué posición está el carnet: debe compararlo elemento por
elemento desde el inicio. En el peor caso (el último registro o un carnet que no existe)
revisa los n elementos, así que el trabajo crece en proporción directa a n. En nuestra
tabla, al multiplicar n por 10 el tiempo de List también se multiplicó aproximadamente
por 10.

**2. ¿Por qué Set y Dictionary tienen búsqueda O(1) en promedio?**
Porque usan una tabla hash: calculan el hash del carnet y eso indica directamente la
posición donde debería estar, sin recorrer los demás elementos. Se dice "en promedio"
porque pueden ocurrir colisiones (dos claves que caen en la misma posición); en ese caso
se revisan unas pocas entradas extra. Con una buena función hash las colisiones son
raras, y el costo se mantiene constante aunque n crezca.

**3. ¿Por qué O(1) no significa "cero tiempo" ni "exactamente el mismo tiempo siempre"?**
O(1) significa que el costo no crece con n, no que no exista. Calcular el hash y acceder
a la posición siempre toma algo de tiempo: en nuestras pruebas, cerca de 0.0000001 s.
Tampoco es idéntico en cada ejecución: Set varió entre 0.000000106 s y 0.000000115 s
según la medición, por efectos de la caché, del sistema operativo y de posibles
colisiones. Lo importante es que ese valor se mantuvo estable con 100 registros y con
100,000.

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

**6. ¿Qué condición permite que un árbol de búsqueda se acerque a O(log n)?**
Que esté razonablemente balanceado, es decir, que los valores se repartan entre el
subárbol izquierdo y el derecho en lugar de acumularse hacia un mismo lado. Así, cada
comparación descarta aproximadamente la mitad de los nodos restantes. Por eso, al
insertar la muestra mezclada con `random.shuffle`, el árbol de 5,000 nodos resolvió la
búsqueda en 0.0000008 s.

**7. ¿Qué ocurre con el BST si se inserta información ya ordenada?**
Se degenera en una cadena. Cada nuevo carnet es mayor que el anterior, así que siempre
se cuelga del mismo lado (la derecha) y el árbol termina teniendo la forma de una lista
enlazada. La búsqueda deja de descartar la mitad en cada paso y pasa a revisar los nodos
uno por uno, cayendo en O(n), como se vio con los 2,000 nodos ordenados (0.0001296 s,
158 veces más lento que el árbol mezclado).

**8. ¿Qué estructura elegiría para recuperar un estudiante completo por carnet? Justifique.**
Dictionary. El carnet es un identificador único y funciona naturalmente como clave: en
0.000000149 s el Dict devuelve el registro completo del estudiante, muy por debajo de
List (0.0046 s) o del árbol degenerado (0.00013 s), y ese tiempo no crece con n.

**9. ¿Qué estructura elegiría si solamente necesita saber si un carnet existe? Justifique.**
Set. Ofrece el mismo costo O(1) promedio que Dict para verificar pertenencia
(0.000000126 s en nuestra prueba), pero sin guardar el registro completo, así que ocupa
menos memoria cuando no se necesita recuperar los datos del estudiante.

**10. Si el sistema realiza 70% búsquedas, 20% inserciones y 10% reportes, ¿qué decisión de diseño tomaría y por qué?**
Usaría un Dictionary indexado por carnet. Las búsquedas dominan el uso (70%) y en el
Dict son O(1) promedio; el costo de construirlo (0.0169 s en nuestra máquina) se
recupera después de unas 4 consultas, porque cada una ahorra unos 0.0046 s frente a
List. Las inserciones (20%) también se benefician, ya que agregar una clave nueva a un
Dict es O(1) promedio. Solo si los reportes (10%) necesitaran recorrer los datos
ordenados por carnet valdría la pena mantener además una estructura ordenada aparte (o
ordenar al momento del reporte); para esta mezcla de operaciones, Dictionary es la base
más conveniente.

## Conclusión

Sobre los mismos 100,000 estudiantes, todas las estructuras encontraron el mismo registro,
pero con costos muy distintos: List tardó 0.0046 s y Set y Dict unos 120 nanosegundos,
más de 37,000 veces menos. La diferencia no viene del equipo sino de cómo cada estructura
organiza la información: List y la lista enlazada recorren elemento por elemento (O(n)),
mientras Set y Dict usan hashing (O(1) promedio). El BST se acerca a O(log n) solo si
está balanceado: con carnets ordenados degeneró en una cadena y fue 158 veces más lento.
Además, la complejidad depende de la operación y no solo de la estructura: la lista
enlazada inserta al inicio en O(1) pero busca en O(n). Para un sistema con 70% de
búsquedas, Dictionary es la mejor opción, y su costo de construcción (0.0169 s) se
recupera tras unas 4 consultas.