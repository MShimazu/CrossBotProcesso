
s = input()

s = s.replace('.','')

print(s)

d=0

while(True):
    b=True
    tirar = []
    for i in range((len(s)-1)):
        if(s[i]=='<' and s[i+1]=='>'):
            tirar.append(i)
            tirar.append(i+1)
            b=False
            d+=1
    
    for i in range(len(tirar)):
        index=len(tirar)-i-1
        index = tirar[index]
        s = s[:index]+s[index+1:]

    if(b):
        break

print(d)