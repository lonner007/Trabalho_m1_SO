import threading
import time

# Função para multiplicação matricial entre duas matrizes (single-thread)
def multiply_matrices_single_thread(A, B):
    numRowsA = len(A)
    numColsA = len(A[0])
    numRowsB = len(B)
    numColsB = len(B[0])

    if numColsA != numRowsB:
        raise ValueError("As dimensões das matrizes não são compatíveis para multiplicação.")

    result = [[0.0 for _ in range(numColsB)] for _ in range(numRowsA)]

    for i in range(numRowsA):
        for j in range(numColsB):
            for k in range(numColsA):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Função para multiplicação posicional entre duas matrizes (single-thread)
def multiply_matrices_positional_single_thread(A, B):
    numRowsA = len(A)
    numColsA = len(A[0])
    numRowsB = len(B)
    numColsB = len(B[0])

    if numColsA != numRowsB:
        raise ValueError("As dimensões das matrizes não são compatíveis para multiplicação.")

    result = [[0.0 for _ in range(numColsB)] for _ in range(numRowsA)]

    for i in range(numRowsA):
        for j in range(numColsB):
            for k in range(numColsA):
                result[i][j] += A[i][k] * B[k][j]

    return result

if __name__ == "__main__":
    # Matrizes de exemplo 3x3
    A = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    B = [[9.0, 8.0, 7.0], [6.0, 5.0, 4.0], [3.0, 2.0, 1.0]]

    # Medindo o tempo de execução
    start_time = time.time()

    # Multiplicação matricial (single-thread)
    result_matrix_single_thread = multiply_matrices_single_thread(A, B)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Multiplicação matricial (single-thread):")
    for row in result_matrix_single_thread:
        print(row)

    print("Tempo de execução (single-thread):", elapsed_time, "segundos")

    # Medindo o tempo de execução
    start_time = time.time()

    # Multiplicação posicional (single-thread)
    result_positional_single_thread = multiply_matrices_positional_single_thread(A, B)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Multiplicação posicional (single-thread):")
    for row in result_positional_single_thread:
        print(row)

    print("Tempo de execução (single-thread):", elapsed_time, "segundos")
