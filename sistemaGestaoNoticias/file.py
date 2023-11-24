from noticia import Noticia
import os
class File:
    def cadastar_noticia(noticia):
        with open("noticias.csv", "a") as file:
            file.write(noticia.titulo+';'+noticia.categoria+';'+noticia.texto+';'+noticia.palavras_chave+'\n')

    def get_noticias():
        list = []
        with open("noticias.csv", "r+") as file:
            for linha in file:
                v = linha.split(';')
                p = Noticia(v[0], v[1], v[2], v[3])
                list.append(p)
        return list
    
    def salva_lista(list):
        os.remove("noticias.csv") 
        with open("noticias.csv", "a") as file:
            for noticia in list:
                file.write(noticia.titulo+';'+noticia.categoria+';'+noticia.texto+';'+noticia.palavras_chave)

