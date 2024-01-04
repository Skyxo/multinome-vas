from math import *
from cmath import *
from sympy import *
from random import *
import time

def nbrcombo(m, n):                                                               
    nbr = 1
    for i in range(1,m):
        nbr*=(n+i)
    
    return nbr*(1/factorial(m-1))

def listeCombinaisons(nbrvariable, n):                
    try_list, final_list = [], []
    nbr = nbrcombo(nbrvariable, n)                 
    i = 0
    
    #for i in range(100000): 
        
    while len(final_list) < nbr:                                 
        #print(len(final_list))
        try_list.append([])
        s = 0
        
        for o in range(nbrvariable): 
            if s <= n:
                ai = randint(0, n-s)
                try_list[i].append(ai)
                s += ai
            else:
                break                
            
        if s == n and try_list[i] not in final_list:   
            final_list.append(try_list[i])
        i+=1
    
    return final_list
    
print(listeCombinaisons(3,5))

def listecoeff(listeCombinaisons, n):            
    liste = []
    
    for i in range(len(listeCombinaisons)):
        k = 1                                           
        
        for o in range(len(listeCombinaisons[i])):   
            k *= factorial(listeCombinaisons[i][o])
        
        liste.append(factorial(n)/k)               
    
    return liste

def pimaj(listevariable, nbrvariable, combinaisons, i): 
    add = 1

    for o in range(nbrvariable):
        add *= listevariable[o]**(combinaisons[i][o])
    
    return add
    
def multinome(listevariable, n):
    nbrvariable = len(listevariable)
     
    combinaisons = listeCombinaisons(nbrvariable, n) 
    
    coefficients = listecoeff(combinaisons, n) 
    
    m = len(coefficients)                                   
    resultat = 0
    
    for i in range(m):
        resultat += coefficients[i]*pimaj(listevariable, nbrvariable, combinaisons, i)

    return resultat

a, b, c, d, e, f, g = Symbol('a'), Symbol('b'), Symbol('c'), Symbol('d'), Symbol('e'), Symbol('f'), Symbol('g')
i = complex(1)

print(multinome([a,b], 5))



"""
def programme():      
    termes = []
    mode = int(input("Voulez vous rentrer des constantes (0) ou des variables (1) ? : "))
    lg = int(input("Entrer le nombre de termes que vous voulez : "))        

    for i in range(1, lg+1):
        print("Entrer terme", i, ": ", end="")
        a = input()
        if mode:
            a = Symbol(a)
        else:
            a = int(a)
        termes.append(a)
    n = int(input("Entrer la puissance à laquelle élever cette somme de terme : "))

    expression = "("
    expression += str(termes[0])
    for i in range(1, len(termes)):
        expression+= "+"+str(termes[i])
    expression+=")^"+str(n)

    print("Le développement de", expression, "donne :")
    print(multinome(termes, n))

#programme()
"""