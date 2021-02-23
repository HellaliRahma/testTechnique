plateau = [[True,False,False,False],
            [False,True,True,False]]

nbLignes = len(plateau) 
nbColonne = len(plateau[0])

def voisinsCase (plateau, i,j):
    
    listCordonne = []
    if i <= nbLignes-1 and i>=0 and j <= nbColonne-1 and j >= 0 :  
        if i-1 <= nbLignes - 1 and i-1 >= 0 :
            if plateau[i-1][j] == False:
                listCordonne.append([i-1,j])
        if i+1 <= nbLignes - 1 and  i+1 >= 0 :
            if plateau[i+1][j] == False:
                listCordonne.append([i+1,j])
        if j+1 <= nbColonne - 1  and j+1 >= 0 :
            if plateau[i][j+1] == False:
                listCordonne.append([i,j+1])
        if j-1 <= nbColonne - 1 and j-1 >= 0 :
            if plateau[i][j-1] == False:
                listCordonne.append([i,j-1])
    else: 
        print("Les coordonnées de la case que vous avez entré sont invalides")
    return listCordonne


def voisinsCases(plateau, listCases):
    listFinal = []
    for i in range(len(listCases)):
        print(listCases[i][0])
        print(listCases[i][1])
        listResultat = voisinsCase(plateau, listCases[i][0], listCases[i][1])
        if listResultat:
            listFinal.append(listResultat)
    return listFinal

def accessibles(plateau, i, j):
    if i <= nbLignes-1 and i>=0 and j <= nbColonne-1 and j >= 0 : 
        res = voisinsCase(plateau, i,j)
        resfinal = []
        while res:      
            if len(res) == 1:
                res = voisinsCase(plateau, res[0][0],res[0][1])
            elif len(res) > 1:
                for p in range(len(res)):
                    if not(voisinsCase(plateau, res[p][0], res[p][1])) or (res[p][0] == i and res[p][1]== j):
                        resfinal.append([res[p][0], res[p][1]]) 
                        res = voisinsCases(plateau, res)
    else:
        print('Case invalide')
    return res

def chemin (plateau, iDeb, jDeb , iFin, jFin):
    casesAccessible = accessibles(plateau, iDeb,jDeb)
    if [iFin, jFin] in casesAccessible:
        return True
    else:
        return False

print(voisinsCase(plateau, 1,3))