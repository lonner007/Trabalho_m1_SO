# Tamanho das matrizes
tamanhoX = 3
tamanhoY = 3

# Matrizes de exemplo 3x3
matrizA = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrizB = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

matrizResultadoMatricial = [[0] * tamanhoX for _ in range(tamanhoY)]
matrizResultadoPosicional = [[0] * tamanhoX for _ in range(tamanhoY)]

# Função para calcular a multiplicação matricial (single-thread)
def calcula_matricial_single_thread():
    global matrizResultadoMatricial
    for linha in range(tamanhoY):
        for coluna in range(tamanhoX):
            matrizResultadoMatricial[linha][coluna] = 0
            matrizResultadoMatricial[linha][coluna] = matrizA[linha][coluna] * matrizB[coluna][linha]

# Função para calcular a multiplicação posicional (single-thread)
def calcula_posicional_single_thread():
    global matrizResultadoPosicional
    for linha in range(tamanhoY):
        for coluna in range(tamanhoX):
            matrizResultadoPosicional[linha][coluna] = matrizA[linha][coluna] * matrizB[linha][coluna]

if __name__ == "__main__":
    # Calcular multiplicação matricial (single-thread)
    calcula_matricial_single_thread()

    # Calcular multiplicação posicional (single-thread)
    calcula_posicional_single_thread()

    # Imprimir o resultado da multiplicação matricial e posicional
    print("Multiplicação Matricial (Single-Thread):")
    for linha in matrizResultadoMatricial:
        print(linha)

    print("\nMultiplicação Posicional (Single-Thread):")
    for linha in matrizResultadoPosicional:
        print(linha)
