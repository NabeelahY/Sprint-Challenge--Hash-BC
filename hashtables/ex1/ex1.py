#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable, hash_table_insert)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    arr_len = 0
    arr = []

    while arr_len < length:
        diff = limit - weights[arr_len]
        for i in range(length):
            hash_table_insert(ht, weights[i], i)
            if diff == weights[i] and arr_len != i:
                arr.append(i)
       
        arr_len += 1

    if len(arr) == 0:
        return None
    return arr

    print(arr) 

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
