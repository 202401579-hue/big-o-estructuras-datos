# Laboratorio Big O y Estructuras de Datos

## Descripción del problema
Una universidad necesita consultar rápidamente a sus estudiantes por carnet. Este
laboratorio compara cómo se comportan distintas estructuras de datos al buscar un
carnet dentro de 100,000 registros: List, Set, Dictionary, lista enlazada y árbol
binario de búsqueda (BST). Los datos se generan en un CSV, se publican en GitHub y
se descargan desde Python mediante la URL RAW. Con las mediciones de tiempo se
analiza la complejidad Big O de cada operación y se justifica qué estructura
conviene según el tipo de consulta.

## Integrantes
- Samuel Rafael Martínez Ramírez, carnet 202401579
- Victor Eduardo Alonzo López, carnet 202401578
- Gonzalo Ricardo Guzman Sosa, carnet 202401088

## Estructura del repositorio
- `data/estudiantes.csv`: dataset de 100,000 estudiantes
- `src/generar_datos.py`: genera el CSV
- `src/main.py`: descarga los datos desde GitHub y ejecuta todas las mediciones
- `src/lista_enlazada.py`: implementación de la lista enlazada
- `src/arbol_bst.py`: implementación del árbol binario de búsqueda
- `resultados/resultados.md`: tablas de tiempos, análisis Big O y conclusión

## Cómo ejecutar el proyecto desde cero
Requisitos: Python 3 y Git. No se necesitan librerías externas.

    git clone https://github.com/202401579-hue/big-o-estructuras-datos.git
    cd big-o-estructuras-datos
    python src/main.py

El programa descarga el CSV desde la URL RAW ya configurada en `src/main.py`,
muestra los 100,000 registros recibidos e imprime las mediciones de List, Set,
Dict, lista enlazada, BST, carnet inexistente y construcción vs consulta.

> Los tiempos cambian según el equipo y la carga del momento. Lo que se compara es
> la tendencia al crecer n, no los segundos exactos.