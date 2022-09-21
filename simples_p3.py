
def SeparaPrimo(lista):
    listaR = []
    for x in lista:
        b=True
        for i in range(x):
            if((i>=2) and (x%i==0)):
                b=False
        if(b and x>1):
            listaR.append(x)
    return listaR

print(SeparaPrimo([1,2,3,4,5,6,7,8,9,10,11,12]))