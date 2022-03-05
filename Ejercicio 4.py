class ArbolNodo(object):
    def __init__(self,x):
        self.val = x
        self.izq = None
        self.der = None
        
def eliminar_nodo(raiz, llave):
    if not raiz:
        return raiz
    
    if raiz.val > llave:
        raiz.izq = eliminar_nodo(raiz.izq, llave)
        
    elif raiz.val < llave:
        raiz.der = eliminar_nodo(raiz.der, llave)
        
    else:
        if not raiz.der:
            return raiz.izq
        if not raiz.izq:
            return raiz.der
        
        temp_val = raiz.der
        while temp_val.izq:
            temp_val = temp_val.izq
            
        raiz.der = eliminar_nodo(raiz.der,raiz.val)
    return raiz

def preOrden(nodo):
    if not nodo:
        return
    print(nodo.val)
    preOrden(nodo.izq)
    preOrden(nodo.der)

raiz = ArbolNodo(5)
raiz.izq = ArbolNodo(3)
raiz.der = ArbolNodo(6)
raiz.izq.izq = ArbolNodo(2)
raiz.izq.der = ArbolNodo(4)
raiz.izq.der.izq = ArbolNodo(7)
print("el nodo original es : ")
print(preOrden(raiz))
resultado = eliminar_nodo(raiz,4)
print("depues de elminar este es el nodo especifico: ")
print(preOrden(resultado))
    