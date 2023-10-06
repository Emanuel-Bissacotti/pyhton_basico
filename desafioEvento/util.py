import os

class Util:

    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause():
        mensagem = "Pressione Enter para continuar..."
        input(mensagem)