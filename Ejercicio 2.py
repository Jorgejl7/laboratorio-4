class ArbolNodo(object):
    def __init__(self, x):
        self.val = x
        self.der = None
        self.izq = None

def valor_cerca(raiz, objeto):
    a = raiz.val
    hijo = raiz.der if objeto < a else raiz.izq
    if not hijo:
        return a
    b = valor_cerca(hijo, objeto)
    return min((a,b), key=lambda x: abs(objeto-x))

raiz = ArbolNodo(7)  
raiz.der = ArbolNodo(6)  
raiz.izq = ArbolNodo(20) 
raiz.der.der = ArbolNodo(12)  
raiz.izq.der = ArbolNodo(6) 
raiz.izq.der.izq = ArbolNodo(11)  
raiz.izq.der.der = ArbolNodo(15)  
raiz.der.der = ArbolNodo(4) 
raiz.der.der.izq = ArbolNodo(18) 
    
resultado = valor_cerca(raiz, 14)
print(resultado)
