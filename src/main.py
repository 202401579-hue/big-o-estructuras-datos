import csv
import io
import time
import urllib.request
from statistics import mean

# Pegue aquí la URL RAW del CSV alojado en GitHub.
URL = "https://raw.githubusercontent.com/202401579-hue/big-o-estructuras-datos/refs/heads/main/data/estudiantes.csv"
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


if __name__ == "__main__":
    main()
