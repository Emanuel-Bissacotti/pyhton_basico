import sys
from participante import * 
from arquivo import * 
def menu(Lista):
    
    print('MENU')
    print('1-Fazer inscrição')
    print('2-Listar inscritos')
    print('3-Entrar do Evento')
    print('4-Sair do evento')
    print('5-Finalizar')
    opcao = int(input('OPÇÃO:'))
    match opcao:
        case 1:
            inscricao(Lista)
        case 2:
            inscritos(Lista)
        case 3:
            entrar(Lista)
        case 4:
            sair()
        case 5:
            sys.exit()

def inscricao(Lista):
    matricula = input('Matrula: ')
    nome = input('Nome: ')
    email = input('Email: ')
    p = Participante(matricula, nome, email)

    if p in Lista:
        print ('Participante ja insccrito')
    else:
        Lista.append(p)
        Arquivo.adiciona_lista(p)
        print('Inscricao feita com sucesso')
        
def inscritos(Lista):
    for participante in Lista:
        print(participante)
        
def entrar(Lista):
    matricula = input('Matricula: ')
    for participante in Lista:
        if(participante.matricula == matricula):
            Arquivo.grava_entrada(matricula)