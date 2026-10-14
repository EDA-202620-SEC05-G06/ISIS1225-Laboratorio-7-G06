"""
Implementación de una Tabla de Símbolos Ordenada (Ordered Map)
basada en un Árbol Binario de Búsqueda (BST).

Entrega inicial (release 0.0.1): new_map, put/insert_node,
get/get_node, size/size_tree y default_compare.
"""

from DataStructures.Tree import bst_node as bst_node


def new_map():
    """
    Crea una nueva tabla de símbolos ordenada basada en un BST.

    :returns: árbol vacío {"root": None}
    :rtype: binary_search_tree
    """
    my_bst = {"root": None}
    return my_bst


def default_compare(key, element):
    """
    Compara una llave con la llave de un nodo del árbol.

    :param key: llave a comparar
    :param element: nodo del árbol (bst_node)

    :returns: 0 si son iguales, 1 si key es mayor, -1 si key es menor
    :rtype: int
    """
    element_key = bst_node.get_key(element)
    if key == element_key:
        return 0
    elif key > element_key:
        return 1
    return -1


# ---------------------------------------------------------------------------
# Máscaras
# ---------------------------------------------------------------------------

def put(my_bst, key, value):
    """
    Agrega una pareja llave-valor al árbol. Si la llave ya existe,
    actualiza su valor.

    :returns: el árbol actualizado
    :rtype: binary_search_tree
    """
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst


def get(my_bst, key):
    """
    Retorna el valor asociado a la llave, o None si no existe.
    """
    node = get_node(my_bst["root"], key)
    return bst_node.get_value(node)


def size(my_bst):
    """
    Retorna el número de parejas llave-valor del árbol.
    """
    return size_tree(my_bst["root"])


# ---------------------------------------------------------------------------
# Funciones recursivas
# ---------------------------------------------------------------------------

def insert_node(root, key, value):
    """
    Inserta recursivamente un nodo en la posición correcta del subárbol
    con raíz ``root`` y actualiza el tamaño de cada nodo en el camino.

    :returns: la raíz del subárbol actualizado
    :rtype: bst_node
    """
    if root is None:
        return bst_node.new_node(key, value)

    cmp = default_compare(key, root)
    if cmp < 0:
        root["left"] = insert_node(root["left"], key, value)
    elif cmp > 0:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value

    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root


def get_node(root, key):
    """
    Busca recursivamente el nodo con la llave dada.

    :returns: el nodo encontrado o None
    :rtype: bst_node
    """
    if root is None:
        return None

    cmp = default_compare(key, root)
    if cmp < 0:
        return get_node(root["left"], key)
    elif cmp > 0:
        return get_node(root["right"], key)
    return root


def size_tree(root):
    """
    Retorna el tamaño del subárbol con raíz ``root`` (0 si es vacío).
    """
    if root is None:
        return 0
    return root["size"]
