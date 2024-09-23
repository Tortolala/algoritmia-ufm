'''
RNGs comparison: middle square vs numpy.
'''

import numpy as np
import matplotlib.pyplot as plt


# Middle Square Method
def middle_square(n, seed=1234):
    
    rand_nums = []
    x = seed

    for _ in range(n):
        x = int(str(x * x).zfill(8)[2:6])   
        if x == 0:  
            x = seed
        rand_nums.append(x)

    # return np.array(rand_nums) 
    return np.array(rand_nums) / 10000


# Generate 90K digits (pixels) for a 300x300 image
n = 90000
seed = 1234
ms_numbers = middle_square(n, seed).reshape((300, 300))
# print(ms_numbers[0][:50])

# '''
# Numpy RNG (white noise)
numpy_random_numbers = np.random.rand(300, 300)


# Comparison viz

fig, axs = plt.subplots(1, 2, figsize=(16, 8))
axs[0].imshow(ms_numbers, cmap='gray')
axs[0].set_title('Middle Square Method - RNG Débil')
axs[1].imshow(numpy_random_numbers, cmap='gray')
axs[1].set_title('Numpy - RNG Fuerte')
plt.show()
# '''
