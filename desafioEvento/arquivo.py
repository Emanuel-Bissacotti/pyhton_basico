from participante import *
import datetime
class Arquivo:
    def adiciona_lista(participante):
        arquivo = open('inscricoes.dat', 'a')
        arquivo.write(participante.matricula+';'+participante.nome+';'+participante.email+'\n')
        arquivo.close()
        
    def pegar_arquivo(Lista):
        leitor = open('inscricoes.dat', 'r')
        for linha in leitor:
            v = linha.split(';')
            p = Participante(v[0], v[1], v[2])
            Lista.append(p)
        return Lista
    
    def grava_entrada(matricula):
        arquivo = open('entrada.dat', 'a')
        arquivo.write(matricula+'--'+datetime.time)