
#def culegere_sol(matrice):

#    for i in range(len(matrice)):
#        for j in range(len(matrice[0])):
#            suma=

def printare(matrice):
    for linie in matrice:
        print(*linie)
 
def reg_dreptunghi(x,y,a,b):
    return x*y-a*b

def schimb_coloana(matrice,contor_col):
    coloana_1 = contor_col
    coloana_2 = contor_col+1
    for i in range(len(matrice)):
        matrice[i][coloana_1], matrice[i][coloana_2] = matrice[i][coloana_2], matrice[i][coloana_1]

def schimb_linie(matrice,contor_lin):
    linie_1 = contor_lin
    linie_2 = contor_lin+1
    for i in range(len(matrice[linie_1])):
        matrice[linie_1][i], matrice[linie_2][i] = matrice[linie_2][i], matrice[linie_1][i]

def parcurgere(matrice,indici_var):
    for x in range(len(matrice)):
        printare(matrice)
        print("\n")
        pivot=matrice[x][x]
        contor_lin=x
        contor_col=x
        print(*indici_var)
        print("-"*10)   
        if pivot==0:
            if x==len(matrice)-1:
                break
            else:
                if matrice[x+1][x]!=0:
                    schimb_linie(matrice,contor_lin)
                    pivot=matrice[x][x]
                elif matrice[x][x+1]!=0:
                    schimb_coloana(matrice,contor_col)
                    indici_var[x],indici_var[x+1]=indici_var[x+1],indici_var[x]
                    pivot=matrice[x][x]

        for i in range(len(matrice)):
            for j in range(len(matrice[0])):
                if i!=x and x!=j:
                    matrice[i][j]=reg_dreptunghi(pivot, matrice[i][j], matrice[i][x], matrice[x][j])

        for i in range(len(matrice)):
            for j in range(len(matrice[0])):
                if x==j and  (i,j)!=(x,x):
                    matrice[i][j]=0



#culegere_sol
print("O zi frumoasa sa aveti! Acesta este proiectul nostru. Sper sa va placa...Acum putem trece la treaba.")
print("Introduceti o matrice, dar nu prea mareeee...")
#input()
matrice=[0,3,4,1],[2,3,2,2],[1,2,4,3]
indici_var = [i + 1 for i in range(len(matrice[0]))]  

parcurgere(matrice,indici_var)
        
print("Forma finala a matricei!")
for linie in matrice:  
    print(*linie)
print("-" * 10)


