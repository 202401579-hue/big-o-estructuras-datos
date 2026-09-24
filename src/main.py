import csv
import io
import time
import urllib.request
from statistics import mean

from lista_enlazada import ListaEnlazada
import random
from arbol_bst import ArbolBST

URL = "https://raw.githubusercontent.com/202401579-hue/big-o-estructuras-datos/main/data/estudiantes.csv"
CARNET_BUSCAR = "EST099999"
REPETICIONES = 100


def descargar_datos(url):
    if "PEGAR_AQUI" in url:
        raise ValueError("Debe reemplazar URL por la dirección RAW de GitHub.")

    with urllib.request.urlopen(url) as respuesta:
        contenido = respuesta.read().decode("utf-8")

    return list(csv.DictReader(io.StringIO(contenido)))


def buscar_lista(estudiantes, carnet):
    for estudiante in estudiantes:
        if estudiante["carnet"] == carnet:
            return estudiante
    return None


def medir(funcion, repeticiones=100):
    muestras = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion()
        muestras.append(time.perf_counter() - inicio)
    return mean(muestras)


def main():
    print("1) Descargando datos desde GitHub...")
    estudiantes = descargar_datos(URL)
    print(f"   OK: {len(estudiantes):,} registros recibidos")

    print("2) Construyendo estructuras...")
    carnets_set = {e["carnet"] for e in estudiantes}
    estudiantes_dict = {e["carnet"]: e for e in estudiantes}
    print("   OK: list, set y dict preparados")

    print("3) Midiendo búsquedas...")
    t_lista = medir(lambda: buscar_lista(estudiantes, CARNET_BUSCAR), REPETICIONES)
    t_set = medir(lambda: CARNET_BUSCAR in carnets_set, REPETICIONES)
    t_dict = medir(lambda: estudiantes_dict.get(CARNET_BUSCAR), REPETICIONES)

    print("\nRESULTADOS PROMEDIO")
    print(f"LIST : {t_lista:.10f} s   -> O(n)")
    print(f"SET  : {t_set:.10f} s   -> O(1) promedio")
    print(f"DICT : {t_dict:.10f} s   -> O(1) promedio")

    print("\n4) Validación funcional")
    print("LIST encontrado:", buscar_lista(estudiantes, CARNET_BUSCAR) is not None)
    print("SET encontrado :", CARNET_BUSCAR in carnets_set)
    print("DICT encontrado:", estudiantes_dict.get(CARNET_BUSCAR) is not None)

    print("\n5) Efecto de n")
    tamanos = [100, 1_000, 10_000, 50_000, 100_000]
    for n in tamanos:
        muestra = estudiantes[:n]
        set_n = {e["carnet"] for e in muestra}
        dict_n = {e["carnet"]: e for e in muestra}
        carnet = muestra[-1]["carnet"]

        t_lista_n = medir(lambda: buscar_lista(muestra, carnet), REPETICIONES)
        t_set_n = medir(lambda: carnet in set_n, REPETICIONES)
        t_dict_n = medir(lambda: dict_n.get(carnet), REPETICIONES)

        print(f"n = {n:>7,} | LIST: {t_lista_n:.10f} s | SET: {t_set_n:.10f} s | DICT: {t_dict_n:.10f} s")

    print("\n6) Lista enlazada")
    lista_pequena = ListaEnlazada()
    for estudiante in estudiantes[:100]:
        lista_pequena.insertar_inicio(estudiante)

    lista_grande = ListaEnlazada()
    for estudiante in estudiantes[:10_000]:
        lista_grande.insertar_inicio(estudiante)

    print("Encontrado EST000001:", lista_grande.buscar("EST000001") is not None)

    t_busq_primero = medir(lambda: lista_grande.buscar(estudiantes[9_999]["carnet"]), REPETICIONES)
    t_busq_ultimo = medir(lambda: lista_grande.buscar(estudiantes[0]["carnet"]), REPETICIONES)

    lista_ins_grande = ListaEnlazada()
    for estudiante in estudiantes[:10_000]:
        lista_ins_grande.insertar_inicio(estudiante)

    nuevo = {"carnet": "EST999998", "nombre": "Prueba"}
    t_ins_pequena = medir(lambda: lista_pequena.insertar_inicio(nuevo), REPETICIONES)
    t_ins_grande = medir(lambda: lista_ins_grande.insertar_inicio(nuevo), REPETICIONES)

    print(f"Insertar en lista de 100 nodos    : {t_ins_pequena:.10f} s -> O(1)")
    print(f"Insertar en lista de 10,000 nodos : {t_ins_grande:.10f} s -> O(1)")
    print(f"Buscar primer nodo de la cadena   : {t_busq_primero:.10f} s -> mejor caso")
    print(f"Buscar ultimo nodo de la cadena   : {t_busq_ultimo:.10f} s -> O(n)")

    print("\n7) Arbol binario de busqueda")
    muestra = estudiantes[:5_000].copy()
    random.shuffle(muestra)

    arbol = ArbolBST()
    for estudiante in muestra:
        arbol.insertar(estudiante)

    carnet_bst = muestra[-1]["carnet"]
    t_bst = medir(lambda: arbol.buscar(carnet_bst), REPETICIONES)
    print(f"BST mezclado (5,000 nodos)   : {t_bst:.10f} s -> ~O(log n)")
    print("Encontrado:", arbol.buscar(carnet_bst) is not None)

    arbol_ordenado = ArbolBST()
    muestra_ordenada = estudiantes[:2_000]
    for estudiante in muestra_ordenada:
        arbol_ordenado.insertar(estudiante)

    carnet_deg = muestra_ordenada[-1]["carnet"]
    t_bst_deg = medir(lambda: arbol_ordenado.buscar(carnet_deg), REPETICIONES)
    print(f"BST degenerado (2,000 nodos) : {t_bst_deg:.10f} s -> O(n)")

    CARNET_INEXISTENTE = "EST999999"
    print("\n8) Carnet inexistente")
    t_lista_no = medir(lambda: buscar_lista(estudiantes, CARNET_INEXISTENTE), REPETICIONES)
    t_set_no = medir(lambda: CARNET_INEXISTENTE in carnets_set, REPETICIONES)
    t_dict_no = medir(lambda: estudiantes_dict.get(CARNET_INEXISTENTE), REPETICIONES)
    t_enlazada_no = medir(lambda: lista_grande.buscar(CARNET_INEXISTENTE), REPETICIONES)
    print(f"LIST           : {t_lista_no:.10f} s")
    print(f"SET            : {t_set_no:.10f} s")
    print(f"DICT           : {t_dict_no:.10f} s")
    print(f"LISTA ENLAZADA : {t_enlazada_no:.10f} s")

    print("\n9) Construccion vs consulta")
    t_constr_set = medir(lambda: {e["carnet"] for e in estudiantes}, 5)
    t_constr_dict = medir(lambda: {e["carnet"]: e for e in estudiantes}, 5)
    print(f"Construir SET  : {t_constr_set:.10f} s")
    print(f"Construir DICT : {t_constr_dict:.10f} s")
    print(f"Consultar DICT : {t_dict_no:.10f} s")


if __name__ == "__main__":
    main()