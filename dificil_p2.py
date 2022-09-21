
from operator import truediv


def VerLinha(m,x,y,cor):
    b = False

    for i in range(8):
        if(i==0):
            continue
        if(x+i>7):
            break
        if(cor == 'preto'):
            if(m[y][x+i]=='R'):
                b=True
                break
            elif(m[y][x+i]=='Q'):
                b=True
                break
            elif(m[y][x+i]!='.'):
                break
        else:
            if(m[y][x+i]=='r'):
                b=True
                break
            elif(m[y][x+i]=='q'):
                b=True
                break
            elif(m[y][x+i]!='.'):
                break

    for i in range(8):
        if(i==0):
            continue
        if(x-i<0):
            break
        if(cor == 'preto'):
            if(m[y][x-i]=='R'):
                b=True
                break
            elif(m[y][x-i]=='Q'):
                b=True
                break
            elif(m[y][x-i]!='.'):
                break
        else:
            if(m[y][x-i]=='r'):
                b=True
                break
            elif(m[y][x-i]=='q'):
                b=True
                break
            elif(m[y][x-i]!='.'):
                break

    for i in range(8):
        if(i==0):
            continue
        if(y+i>7):
            break
        if(cor == 'preto'):
            if(m[y+i][x]=='R'):
                b=True
                break
            elif(m[y+i][x]=='Q'):
                b=True
                break
            elif(m[y+i][x]!='.'):
                break
        else:
            if(m[y+i][x]=='r'):
                b=True
                break
            elif(m[y+i][x]=='q'):
                b=True
                break
            elif(m[y+i][x]!='.'):
                break

    for i in range(8):
        if(i==0):
            continue
        if(y-i<0):
            break
        if(cor == 'preto'):
            if(m[y-i][x]=='R'):
                b=True
                break
            elif(m[y-i][x]=='Q'):
                b=True
                break
            elif(m[y-i][x]!='.'):
                break
        else:
            if(m[y-i][x]=='r'):
                b=True
                break
            elif(m[y-i][x]=='q'):
                b=True
                break
            elif(m[y-i][x]!='.'):
                break

    return b

def VerDiagonal(m,x,y,cor):
    b = False

    for i in range(8):
        if(i==0):
            continue
        if(x+i>7 or y+i>7):
            break

        if(cor == 'preto'):
            if(m[y+i][x+i]=='B' or m[y+i][x+i]=='Q'):
                b=True
                break
            elif(m[y+i][x+i]!='.'):
                break
        else:
            if(m[y+i][x+i]=='b' or m[y+i][x+i]=='q'):
                b=True
                break
            elif(m[y+i][x+i]!='.'):
                break

    for i in range(8):
        if(i==0):
            continue
        if(x-i<0 or y-i<0):
            break

        if(cor == 'preto'):
            if(m[y-i][x-i]=='B' or m[y-i][x-i]=='Q'):
                b=True
                break
            elif(m[y-i][x-i]!='.'):
                break
        else:
            if(m[y-i][x-i]=='b' or m[y-i][x-i]=='q'):
                b=True
                break
            elif(m[y-i][x-i]!='.'):
                break

    for i in range(8):
        if(i==0):
            continue
        if(x+i>7 or y-i<0):
            break

        if(cor == 'preto'):
            if(m[y-i][x+i]=='B' or m[y-i][x+i]=='Q'):
                b=True
                break
            elif(m[y-i][x+i]!='.'):
                break
        else:
            if(m[y-i][x+i]=='b' or m[y-i][x+i]=='q'):
                b=True
                break
            elif(m[y-i][x+i]!='.'):
                break

    for i in range(8):
        if(i==0):
            continue
        if(x-i<0 or y+i>7):
            break

        if(cor == 'preto'):
            if(m[y+i][x-i]=='B' or m[y+i][x-i]=='Q'):
                b=True
                break
            elif(m[y-i][x-i]!='.'):
                break
        else:
            if(m[y+i][x-i]=='b' or m[y+i][x-i]=='q'):
                b=True
                break
            elif(m[y+i][x-i]!='.'):
                break

    return b

def VerRedor(m,x,y,cor):
    b=False
    if(cor == 'preto'):
        if(y+1<8):
            if(x+1<8):
                if(m[y+1][x+1]=='P'):
                    b=True
            if(x-1>=0):
                if(m[y+1][x-1]=='P'):
                    b=True
    else:
        if(y-1>=0):
            if(x+1<8):
                if(m[y-1][x+1]=='p'):
                    b=True
            if(x-1>=0):
                if(m[y-1][x-1]=='p'):
                    b=True

    return b

def VerCavalo(m,x,y,cor):
    b=False
    if(cor=='preto'):
        if(y+2<8):
            if(x+1<8):
                if(m[y+2][x+1]=='N'):
                    b=True            
            if(x-1>=0):
                if(m[y+2][x-1]=='N'):
                    b=True
        if(y-2<8):
            if(x+1<8):
                if(m[y-2][x+1]=='N'):
                    b=True            
            if(x-1>=0):
                if(m[y-2][x-1]=='N'):
                    b=True

        if(y+1<8):
            if(x+2<8):
                if(m[y+1][x+2]=='N'):
                    b=True            
            if(x-2>=0):
                if(m[y+1][x-2]=='N'):
                    b=True
        if(y-1<8):
            if(x+2<8):
                if(m[y-1][x+2]=='N'):
                    b=True            
            if(x-2>=0):
                if(m[y-1][x-2]=='N'):
                    b=True

    else:
        if(y+2<8):
            if(x+1<8):
                if(m[y+2][x+1]=='n'):
                    b=True            
            if(x-1>=0):
                if(m[y+2][x-1]=='n'):
                    b=True
        if(y-2<8):
            if(x+1<8):
                if(m[y-2][x+1]=='n'):
                    b=True            
            if(x-1>=0):
                if(m[y-2][x-1]=='n'):
                    b=True

        if(y+1<8):
            if(x+2<8):
                if(m[y+1][x+2]=='n'):
                    b=True            
            if(x-2>=0):
                if(m[y+1][x-2]=='n'):
                    b=True
        if(y-1<8):
            if(x+2<8):
                if(m[y-1][x+2]=='n'):
                    b=True            
            if(x-2>=0):
                if(m[y-1][x-2]=='n'):
                    b=True

    return b

def VerCheckPasso(m,x,y,cor):
    b=False
    if(VerLinha(m,x,y,cor)):
        b=True
    if(VerDiagonal(m,x,y,cor)):
        b=True
    if(VerRedor(m,x,y,cor)):
        b=True
    if(VerCavalo(m,x,y,cor)):
        b=True
    return b

def VerVazio(m):
    b=True

    for x in range(8):
        for y in range(8):
            if(m[y][x]!='.'):
                b=False
                break

    return b

def VerCheck(m):
    #m=['..k.....','ppp.pppp','........','.R...B..','........','........','PPPPPPPP','K.......']
    kx=0
    ky=0
    Ky=0
    Kx=0

    for x in range(8):
        for y in range(8):
            if(m[y][x]=='k'):
                kx=x
                ky=y
            if(m[y][x]=='K'):
                Kx=x
                Ky=y
    
    r=0

    if(VerCheckPasso(m,kx,ky,'preto')):
        r=1
    elif(VerCheckPasso(m,Kx,Ky,'branco')):
        r=2

    return r


#m=['..k.....','ppp.pppp','........','.R...B..','........','........','PPPPPPPP','K.......']       

tVazio=['........','........','........','........','........','........','........','........'] 

m=tVazio
jogadas=[]
while(True):
    c=0
    inp=input()

    if(inp==''):
        if(VerVazio(m)):
            break
        resul = VerCheck(m)
        jogadas.append(resul)
        c=0
    else:
        m[c]=inp
        c+=1

jogoI=0
for i in jogadas:
    jogoI+=1
    if(i==0):
        print('Jogo '+str(jogoI)+': nenhum rei esta em cheque.')
    elif(i==1):
        print('Jogo '+str(jogoI)+': rei preto esta em cheque.')
    elif(i==2):
        print('Jogo '+str(jogoI)+': rei branco esta em cheque.')

