from claseArbolBinario import ArbolBinario

if __name__ == '__main__':
    objArbol = ArbolBinario()
    objArbol.insertar(objArbol.getRaiz(),50)
    objArbol.insertar(objArbol.getRaiz(), 45)
    objArbol.insertar(objArbol.getRaiz(), 48)
    objArbol.insertar(objArbol.getRaiz(),60)
    objArbol.insertar(objArbol.getRaiz(), 55)
    objArbol.postOrder(objArbol.getRaiz())
    print(objArbol.Camino(objArbol.getRaiz(),50,55))


    '''if objArbol.Padre(45, 50):
        print('es padre')
    else:
        print('No es padre')
    print(objArbol.Nivel(objArbol.getRaiz(), 45))
    print('Altura del arbol: {}' .format(objArbol.Altura(objArbol.getRaiz())))
    #objArbol.suprimir(objArbol.getRaiz(), 50)
    #objArbol.preOrder(objArbol.getRaiz())
    if objArbol.Hoja(60):
        print('si')
    else:
        print('no')
    print('Antes de suprimir')
    objArbol.preOrder(objArbol.getRaiz())
    objArbol.suprimir(objArbol.getRaiz(), 55)
    print('Despues de suprimir')'''