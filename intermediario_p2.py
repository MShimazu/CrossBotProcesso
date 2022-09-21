def TiraRep(lista):
    c=[]
    for i in lista:
        b = True
        for t in c:
            if(i==t):
                b=False
        if(b):
            c.append(i)

    return c

print(TiraRep([1,2,2,5,1,9,2,9]))