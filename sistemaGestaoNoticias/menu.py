import sys
from file import File
from noticia import Noticia
from util import Util

class Menu:
    def menu(list):
        while(True):
            print("1 - cadastre")
            print("2 - altere")
            print("3 - listar")
            print("4 - remova")
            print("5 - sair")
            opcao = int(input("\nopção: "))

            if(opcao == 1):
                Menu.criar_noticia(list)
            elif(opcao == 2):
                Menu.alterar_noticia(list)
            elif(opcao == 3):
                Menu.listar(list)
            elif(opcao == 4):
                Menu.remover(list)
            elif(opcao == 5):
                sys.exit()
            else:
                print("opção inválida")

    def criar_noticia(list):
        titulo = input("Digite o titulo da noticia: ")
        categoria = input("Digite a categoria: ")
        texto = input("Digite o texto da noticia: ")
        palavras_chave = input("Digite as palavras chaves: ")
        noticia = Noticia(titulo, categoria, texto, palavras_chave)
        File.cadastar_noticia(noticia)
        list.append(noticia)

    def alterar_noticia(list):
        titulo = input("digite o titulo da noticia: ")
        Util.altera_noticia(titulo, list)
        File.salva_lista(list)
    
    def listar(list):
        for noticia in list:
            print(noticia)

    def remover(list):
        titulo = input("digite o titulo da noticia: ")
        Util.remover_noticia(titulo, list)
        File.salva_lista(list)
        print("noticia removida")