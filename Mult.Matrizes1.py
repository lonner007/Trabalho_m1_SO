import threading

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

# Função para calcular a multiplicação matricial
def calcula_matricial():
    global matrizResultadoMatricial
    for linha in range(tamanhoY):
        for coluna in range(tamanhoX):
            matrizResultadoMatricial[linha][coluna] = 0
            matrizResultadoMatricial[linha][coluna] = matrizA[linha][coluna] * matrizB[coluna][linha]

# Função para calcular a multiplicação posicional
def calcula_posicional():
    global matrizResultadoPosicional
    for linha in range(tamanhoY):
        for coluna in range(tamanhoX):
            matrizResultadoPosicional[linha][coluna] = matrizA[linha][coluna] * matrizB[linha][coluna]

if __name__ == "__main__":
    # Criar threads para calcular multiplicação matricial e multiplicação posicional
    thread_calcula_matricial = threading.Thread(target=calcula_matricial)
    thread_calcula_posicional = threading.Thread(target=calcula_posicional)

    # Iniciar as threads
    thread_calcula_matricial.start()
    thread_calcula_posicional.start()

    # Aguardar que ambas as threads terminem
    thread_calcula_matricial.join()
    thread_calcula_posicional.join()

    # Imprimir o resultado da multiplicação matricial e posicional
    print("Multiplicação Matricial:")
    for linha in matrizResultadoMatricial:
        print(linha)

    print("\nMultiplicação Posicional:")
    for linha in matrizResultadoPosicional:
        print(linha)
