# Resultados del laboratorio

## Integrantes
- Samuel Martínez / carnet: 202401579
- Victor Alonzo / carnet: 202401578
- Gonzalo Guzman / carnet: 202401088

## URL RAW utilizada
`https://raw.githubusercontent.com/TU_USUARIO/big-o-estructuras-datos/main/data/estudiantes.csv`

## Mediciones

Carnet buscado: EST099999 (último registro, peor caso para List). 100 repeticiones por medición.

| n | List O(n) | Set O(1) promedio | Dict O(1) promedio |
|---:|---:|---:|---:|
| 100 | | | |
| 1,000 | | | |
| 10,000 | | | |
| 50,000 | | | |
| 100,000 | 0.0045153330 s | 0.0000001330 s | 0.0000001370 s |

Validación funcional en n = 100,000: List, Set y Dict devolvieron `True`, es
decir que las tres encontraron el mismo registro. La diferencia no está en el
resultado sino en el costo: List tardó aproximadamente 33,950 veces más que Set
para resolver exactamente la misma consulta.

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

## Conclusión

Al comparar las estructuras sobre el mismo conjunto de 100,000 estudiantes quedó
claro que el resultado funcional es idéntico, pero el costo no lo es. List
resolvió la consulta en 0.0045 segundos mientras que Set y Dict lo hicieron en
alrededor de 130 nanosegundos, una diferencia de más de 30,000 veces para la
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