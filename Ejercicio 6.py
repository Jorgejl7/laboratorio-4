class ArbolNodo(object):
    def __init__(self, x):
        self.val = x
        self.izq = None
        self.der = None

def kth_smallest(raiz, j):
    apilar = []
    while raiz or apilar:
        while raiz:
            apilar.append(raiz)
            raiz = raiz.izq
        raiz = apilar.pop()
        j -= 1
        if j == 0:
            break
        raiz = raiz.der
    return raiz.val

raiz = ArbolNodo(7)  
raiz.der = ArbolNodo(6)  
raiz.izq = ArbolNodo(25) 
raiz.der.der = ArbolNodo(18)  
raiz.izq.der = ArbolNodo(6) 
raiz.izq.der.izq = ArbolNodo(19)  
raiz.izq.der.der = ArbolNodo(15)  
raiz.der.der = ArbolNodo(4) 
raiz.der.der.izq = ArbolNodo(16)

print(kth_smallest(raiz, 2))
print(kth_smallest(raiz, 3))
    