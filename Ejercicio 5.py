class ArbolNodo(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bts_arreglo(numero):
    if not numero:
        return None
    mid_numero = len(numero)//2
    nodo = ArbolNodo(numero[mid_numero])
    nodo.izq = bts_arreglo(numero[:mid_numero])
    nodo.der = bts_arreglo(numero[mid_numero+1:])
    return nodo

def preOrden(nodo): 
    if not nodo: 
        return      
    print(nodo.val)
    preOrden(nodo.izq) 
    preOrden(nodo.der)   

numero = [1,2,3,4,5,6,7]

print("la matriz original:")
print(numero)
resultado = bts_arreglo(numero)
print("\nla nueva matriz balanceada en altura es :")
print(preOrden(resultado))
