class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        nuevo = NodoArbol(dato)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz
        while True:
            if dato["carnet"] < actual.dato["carnet"]:
                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    return
                actual = actual.izquierda
            elif dato["carnet"] > actual.dato["carnet"]:
                if actual.derecha is None:
                    actual.derecha = nuevo
                    return
                actual = actual.derecha
            else:
                return

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