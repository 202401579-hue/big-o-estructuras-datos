class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def buscar(self, carnet):
        actual = self.cabeza
        while actual is not None:
            if actual.dato["carnet"] == carnet:
                return actual.dato
            actual = actual.siguiente
        return None
