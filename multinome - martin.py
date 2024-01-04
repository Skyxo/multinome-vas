from sympy import *

# Renvoie le factorielle de n
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n*factorielle(n-1)

# Renvoie le produit des éléments de la liste donnée en argument
def prod_(my_list):
    result = 1
    for element in my_list:
        result *= element
    return result

# Renvoie le coefficient multinomial correspondant à (sum(my_list))/produit des fact des éléments de my_list
def multinomial_coefficient(my_list):
    return int(factorielle(sum(my_list))/prod_([factorielle(x) for x in my_list]))

# Cas m=2
def list_multinomiale_simplifiee(n):
    return [[x, n-x] for x in range(n+1)]

def true_insert(my_list, a, b):
    list_ = my_list
    list_.insert(a, b)
    return list_

'''
Function(2, n) renvoie une liste de listes de ce genre : [[0 ; n], [1 ; n-1], …, [n ; 0]]
My_list[j].insert(0, k) renvoie alors [[0, 0, n], [0, 1, n-1], …, [0, n, 0]]
On fait ça pour toutes les valeurs de k (au-dessus c’était k=0)
[[1, 0, n-1], [1, 1, n-2], …, [1, n-1, 0]]
Et on concatène le tout à la fin
'''

def list_multinomiale(m, n):
    my_list = []
    if m == 2:
        return list_multinomiale_simplifiee(n)
    else:
        for k in range(n+1):
            my_list1 = list_multinomiale(m-1, n-k)
            my_list2 = [true_insert(x, 0, k) for x in my_list1]
            my_list.extend(my_list2)
        return my_list
        

def pimaj(listevariable, nbrvariable, combinaisons, i):  
    add = 1

    for o in range(nbrvariable):
        add *= listevariable[o]**(combinaisons[i][o])
    
    return add
    
def multinome(listevariable, n):
    nbrvariable = len(listevariable)                        
    combinaison = list_multinomiale(nbrvariable, n)
    m = len(combinaison)
    list_coef = [multinomial_coefficient(combinaison[i]) for i in range(m)]                          
    resultat = 0
    
    listevar = []
    for o in range(len(combinaison)):
        add = 1
        for i in range(len(listevariable)):
            add*=listevariable[i]**combinaison[o][i]
        listevar.append(add)
    
    for i in range(m):
        resultat += list_coef[i]*listevar[i]

    return resultat
    
a, b, c, d, e, f, g = Symbol('a'), Symbol('b'), Symbol('c'), Symbol('d'), Symbol('e'), Symbol('f'), Symbol('g')
print(multinome([a,b,c], 2))