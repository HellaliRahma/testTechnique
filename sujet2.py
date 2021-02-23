def CalculQuotientReste (A , B):
    Q = 0
    R = A

    while (R >= B) :
        Q = Q + 1
        R = R - B
    
    return Q , R


nbr= input("Donnez un entier :  ")

somme = 0
for i in range(len(nbr)):
    somme += int(nbr[i])

quotient , reste = CalculQuotientReste(somme , 3)

if reste == 0 :
    print("Le nombre  " ,nbr,"  est divisible par 3")
else:
    print("Le nombre  " ,nbr,"  n'est pas divisible par 3")