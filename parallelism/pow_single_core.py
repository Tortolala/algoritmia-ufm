'''
Proof of Work.
'''

import hashlib


def calculate_hash(text: str) -> str:      

    hash = hashlib.sha256(text.encode()).hexdigest()
    return hash


def find_nonce(block_data, difficulty):
    
    nonce = 0
    target = '0' * difficulty
    
    while True:    

        block = block_data + str(nonce)
        hash_value = calculate_hash(block)
        # print(nonce, hash_value)
        
        if hash_value[:difficulty] == target:
            return nonce, hash_value
        
        nonce += 1


if __name__ == "__main__":

    test_difficulty = 5
    test_block_data = 'Algoritmia'
    print(find_nonce(test_block_data, test_difficulty))
