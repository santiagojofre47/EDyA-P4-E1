from claseArbolBinario import ArbolBinario

if __name__ == '__main__':
    objArbol = ArbolBinario()
    objArbol.insertar(objArbol.getRaiz(),50)
    objArbol.insertar(objArbol.getRaiz(), 45)
    objArbol.insertar(objArbol.getRaiz(), 48)
    objArbol.insertar(objArbol.getRaiz(),60)
    objArbol.insertar(objArbol.getRaiz(), 55)
   
    if objArbol.Padre(45, 50):
        print('es padre')
    else:
        print('No es padre')
 
    print('Altura del arbol: {}' .format(objArbol.Altura(objArbol.getRaiz())))
    if objArbol.Hoja(60):
        print('Es hoja')
    else:
        print('no es hoja')
    print('Antes de suprimir')
    objArbol.preOrder(objArbol.getRaiz())
    objArbol.suprimir(objArbol.getRaiz(), 55)
    print('Despues de suprimir')
    objArbol.preOrder(objArbol.getRaiz())
