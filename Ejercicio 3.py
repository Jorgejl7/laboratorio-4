class ArbolNodo(object):
    def __init__(self, x):
        self.val = x
        self.der = None
        self.izq = None

def bts(raiz):
    apilar = []
    prev = None
    
    while raiz or apilar:
        while raiz:
            apilar.append(raiz)
            raiz = raiz.izq
        raiz = apilar.pop()
        if prev and raiz.val <= prev.val:
            return False
        prev = raiz
        raiz = raiz.der
    return True

raiz = ArbolNodo(2)  
raiz.izq = ArbolNodo(1)  
raiz.der = ArbolNodo(3) 
 
resultado = bts(raiz)
print(resultado)

raiz = ArbolNodo(1)  
raiz.izq = ArbolNodo(2)  
raiz.der = ArbolNodo(3) 
 
resultado = bts(raiz)
print(resultado)
