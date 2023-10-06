import sys
from participante import * 
from arquivo import * 
from util import Util

class Menu:
    def menu(lista):
        
        print('MENU')
        print('1-Fazer inscrição')
        print('2-Listar inscritos')
        print('3-Entrar do Evento')
        print('4-Sair do evento')
        print('5-Finalizar')
        opcao = int(input('OPÇÃO:'))
        Util.limpar_tela()
        match opcao:
            case 1:
                Menu.inscricao(lista)
                Util.pause()
            case 2:
                Menu.inscritos(lista)
                Util.pause()
            case 3:
                Menu.entrar(lista)
                Util.pause()
            case 4:
                Menu.sair(lista)
                Util.pause()
            case 5:
                sys.exit()
        Util.limpar_tela()

    def inscricao(lista):
        matricula = input('Matrula: ')
        nome = input('Nome: ')
        email = input('Email: ')
        p = Participante(matricula, nome, email)

        for p in lista:
            if p.matricula == matricula:
                print ('Participante ja inscrito')
                return
        lista.append(p)
        Arquivo.adiciona_lista(p)
        print('Inscricao feita com sucesso')
        
    def inscritos(lista):
        for participante in lista:
            print(str(participante))
            
    def entrar(lista):
        matricula = input('Matricula: ')
        for participante in lista:
            if participante.matricula == matricula:
                Arquivo.grava_entrada(matricula)
                print("Entrada Registrada")
                return
        print("Voce não está inscrito no evento")
                
    def sair(lista):
        matricula = input('Matricula: ')
        lista_entradas = Arquivo.pegar_entradas()
        for entrada in lista_entradas:
            if entrada == matricula:
                Arquivo.grava_saida(matricula)
                print("Saida registrada")
                return
        print("Algo deu errado")