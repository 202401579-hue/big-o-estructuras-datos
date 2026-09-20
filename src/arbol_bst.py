class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        self.raiz = self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if nodo is None:
            return NodoArbol(dato)

        if dato["carnet"] < nodo.dato["carnet"]:
            nodo.izquierda = self._insertar(nodo.izquierda, dato)
        elif dato["carnet"] > nodo.dato["carnet"]:
            nodo.derecha = self._insertar(nodo.derecha, dato)
        return nodo

    def buscar(self, carnet):
        actual = self.raiz
        while actual is not None:
            if carnet == actual.dato["carnet"]:
                return actual.dato
            if carnet < actual.dato["carnet"]:
                actual = actual.izquierda
            else:
                actual = actual.derecha
        return None
