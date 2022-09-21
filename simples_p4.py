def Conta(c,s):
    r=0
    for l in s:
        if(c==l):
            r+=1
    return r

print(Conta('a','uma frase generica de questões de programação'))