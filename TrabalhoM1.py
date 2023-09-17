import threading
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def merge(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

if __name__ == "__main__":
    # Criar um array com 200 posições, inicialmente ordenado do maior para o menor
    array_maior_para_menor = list(range(200, 0, -1))
    
    # Embaralhar o array para reorganizá-lo do menor para o maior
    random.shuffle(array_maior_para_menor)

    # Iniciar medição de tempo
    start_time = time.time()

    # Criar uma thread para ordenar o array em single-thread
    sorting_thread = threading.Thread(target=bubble_sort, args=(array_maior_para_menor,))
    
    # Iniciar a thread de ordenação
    sorting_thread.start()
    
    # Aguardar até que a thread de ordenação termine
    sorting_thread.join()
    
    # Parar medição de tempo 
    end_time = time.time()
    execution_time_single_thread = end_time - start_time

    print("Array reorganizado do menor para o maior (Single Thread):")
    print(array_maior_para_menor)
    print("Tempo de execução (Single Thread):", execution_time_single_thread, "segundos")
