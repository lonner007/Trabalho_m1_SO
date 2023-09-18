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

def parallel_bubble_sort(arr):
    n = len(arr)
    mid = n // 2
    
    # Divida o array em duas partes para ordenação paralela
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    
    # Crie duas threads para ordenar as partes
    thread1 = threading.Thread(target=bubble_sort, args=(arr1,))
    thread2 = threading.Thread(target=bubble_sort, args=(arr2,))
    
    # Inicie as threads
    thread1.start()
    thread2.start()
    
    # Aguarde até que ambas as threads terminem
    thread1.join()
    thread2.join()
    
    # Mesclar as duas partes ordenadas
    sorted_arr = merge(arr1, arr2)
    return sorted_arr

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

    # Ordenar o array do menor para o maior usando Bubble Sort em multithread
    sorted_arr = parallel_bubble_sort(array_maior_para_menor)
    
    # Parar medição de tempo
    end_time = time.time()
    execution_time_multithread = end_time - start_time

    print("Array reorganizado do menor para o maior (Multi Thread):")
    print(sorted_arr)
    print("Tempo de execução (Multi Thread):", execution_time_multithread, "segundos")
  
