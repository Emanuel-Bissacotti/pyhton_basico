import random

def gerarnumero(): 
    return str(random.randrange(0, 9))
    

def gerarLetra():
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 
                'g', 'h', 'i', 'j', 'k', 'l', 
                'm', 'n', 'o', 'p', 'q', 'r', 
                's', 't', 'u', 'v', 'w', 'x', 
                'y', 'z'
                ]
    return random.choice(alfabeto).upper()
        

def gerarPlaca():
    l1 = gerarLetra()
    l2 = gerarLetra()
    l3 = gerarLetra()
    l4 = gerarnumero()
    l5 = gerarLetra()
    l6 = gerarnumero()
    l7 = gerarnumero()

    return l1 + l2 + l3 + l4 + l5 + l6 + l7