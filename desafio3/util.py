import random
class Util:
    @staticmethod
    def gerar_lista(tamanho):
        tamanho = tamanho * tamanho
        lista = []
        for i in range(0, tamanho):
            lista.append(i)
        random.shuffle(lista)
        return lista
    
    @staticmethod
    def gerar_matriz (tamanho):
        return [[0]*tamanho for _ in range(tamanho)]

    @staticmethod
    def retorna_matriz(lista, matriz, tamanho):
        cont = 0
        for i in range(0, tamanho):
            for j in range(0, tamanho):
                matriz[i][j] = lista[cont]
                cont = cont + 1

        for i in range(0, tamanho):
            for j in range(0, tamanho):
                print(matriz[i][j],"\t",end=" ")
            print()


    @staticmethod
    def exibir_matriz(matriz, tamanho):
        for i in range(0, tamanho):
            for j in range(0, tamanho):
                print(matriz[i][j],"\t",end=" ")
            print()