import multiprocessing


cores = multiprocessing.cpu_count()
print(f'Tienes {cores} núcleos disponibles.')
