class Noticia:
    def __init__(self, título, categoria, texto, palavras_chave):
        self.titulo = título
        self.categoria = categoria
        self.texto = texto
        self.palavras_chave = palavras_chave

    def __str__(self) -> str:
        return self.titulo+" "+self.categoria+" "+self.texto+" "+self.palavras_chave