class Util:
    def altera_noticia(titulo, list):
        for noticia in list:
            if(noticia.titulo == titulo):
                print("1 - "+noticia.titulo)
                print("2 - "+noticia.categoria)
                print("3 - "+noticia.texto)
                print("4 - "+noticia.palavras_chave)
                opcao = int(input("O que deseja alterar"))
                list.remove(noticia)
                match opcao:
                    case 1:
                        noticia.titulo = input("Digite o novo titulo")
                    case 2:
                        noticia.categoria = input("Digite a nova categoria")
                    case 3:
                        noticia.texto = input("Digite o novo texto da noticia")
                    case 4:
                        noticia.palavras_chave = input("Digite as novas palavras chaves")
                list.append(noticia)
    
    def remover_noticia(titulo, list):
        for noticia in list:
            if(noticia.titulo == titulo):
                list.remove(noticia)