from participante import *
import datetime

class Arquivo:
    def adiciona_lista(participante):
        with open("inscricoes.dat", "a") as arquivo:
            arquivo.write(participante.matricula+';'+participante.nome+';'+participante.email+'\n')
        
    def pegar_arquivo(lista):
        with open('inscricoes.dat', 'r') as arquivo:
            for linha in arquivo:
                v = linha.split(';')
                p = Participante(v[0], v[1], v[2])
                lista.append(p)
        return lista
    
    def grava_entrada(matricula):
        with open('entrada.dat', 'a') as arquivo:
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arquivo.write(matricula+';'+data+'\n')


    def pegar_entradas():
        entradas = []
        with open("entrada.dat", "r") as arquivo:
            for linha in arquivo:
                v = linha.split(';')
                entradas.append(v[0])
        return entradas

    def grava_saida(matricula):
        with open("saida.dat", "a") as arquivo:
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arquivo.write(matricula+'--'+data)