'''
Multiprocessing Proof of Work.
'''

import hashlib
import multiprocessing
import time


def calculate_hash(data):

    return hashlib.sha256(data.encode()).hexdigest()


def find_nonce(difficulty, block_data, start_nonce, step, stop_event, queue, process_num):

    nonce = start_nonce
    target = '0' * difficulty

    while not stop_event.is_set():

        block = block_data + str(nonce)
        hash_value = calculate_hash(block)

        if hash_value[:difficulty] == target:
            queue.put((nonce, hash_value, process_num))  # Enviar el resultado y el número de proceso a la cola
            stop_event.set()  # Detener los otros procesos
            return
        
        nonce += step


if __name__ == "__main__":

    test_difficulty = 4
    test_block_data = "Algoritmia"

    # Cores disponibles
    num_cores = multiprocessing.cpu_count()
    print(f"\nUtilizando {num_cores} núcleos...")

    # Crear un evento para detener los procesos
    stop_event = multiprocessing.Event()

    # Crear una cola para recuperar el resultado del proceso que encuentra el nonce
    queue = multiprocessing.Queue()

    # Crear pool de procesos
    processes = []
    start_time = time.time()

    # Iniciar los procesos
    for i in range(num_cores):
        process = multiprocessing.Process(target=find_nonce, args=(test_difficulty, test_block_data, i, num_cores, stop_event, queue, i))
        processes.append(process)
        process.start()

    # Esperar a que un proceso encuentre el nonce
    nonce, hash_result, process_num = queue.get()

    # Mostrar el resultado
    print(f"\nEl proceso {process_num} encontró el nonce: {nonce}")
    print(f"Hash: {hash_result}")

    # Resultado
    print(f"\nTiempo total: {time.time() - start_time:.2f} segundos")

    # Detener todos los procesos
    stop_event.set()

    # Asegurar que todos los procesos terminen
    for process in processes:
        process.join()
