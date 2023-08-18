def gerar_matriz (n_linhas, n_colunas):
    return [[0]*n_colunas for _ in range(n_linhas)]

def exibir_matriz(matriz, tamanho):
    for i in range(0, tamanho):
        for j in range(0, tamanho):
            print(matriz[i][j],"\t",end=" ")
        print()

def manipulaMatriz(matriz, tamanho):
    linha = tamanho - 1 # linha recebe o numero de linhas da matriz
    coluna = int(linha / 2) # coluna fica no meio da matriz
    tamanho_total = int((tamanho * tamanho))
    i = 1
    matriz[linha][coluna] = i
    
    while i < tamanho_total:       
        i += 1
        linha_save = linha
        coluna_save = coluna
        linha += 1
        coluna += 1

        if(linha == tamanho):
            linha = 0
        if(coluna == tamanho):
            coluna = 0
        if matriz[linha][coluna] == 0:
            matriz[linha][coluna] = i
        else:
            linha = linha_save - 1
            coluna = coluna_save
            if(linha == tamanho):
                linha = 0
            if(coluna == tamanho):
                coluna = 0
            matriz[linha][coluna] = i


    exibir_matriz(matriz, tamanho)
