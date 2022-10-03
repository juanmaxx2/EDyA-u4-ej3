import string
from arbol import Arbol, Nodo

class Huffman:
    __archivo = None

    def Inicio(self):
        archivo = open(r"D:\Documentos\Juanma\Facultad\Segundo Año\Estructura de Datos y Algoritmos\Unidad 4\ejercicio 4\archivo.txt")
        texto = ''
        lista = []
        unArbol = Arbol()
        for linea in archivo:
            texto += linea
        archivo.close()
        texto = texto.translate({ord(c): None for c in string.whitespace}).lower()
        for i in range(len(texto)):
            if texto[i] not in lista:
                unNodo = unArbol.Insertar(unArbol.getRaiz(), texto[i], texto.count(texto[i]))
                lista.append(unNodo)
        unArbol.Inorder(unArbol.getRaiz())