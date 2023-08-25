from util import Util

tamanho = int(input("Digite o tamanho da matiz: "))

lista = []

lista = Util.gerar_lista(tamanho)

matriz = Util.gerar_matriz(tamanho)

matriz = Util.retorna_matriz(lista, matriz, tamanho)

# Util.exibir_matriz(matriz, tamanho)