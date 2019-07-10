import random
import time
# Onde v é a lista a ser ordenada.


def insertion_sort(v):
    i = 1
    while i < len(v):
        temp = v[i]
        trocou = False
        j = i - 1
        while j >= 0 and v[j] > temp:
            v[j+1] = v[j]
            trocou = True
            j -= 1

        if trocou:
            v[j+1] = temp

        i += 1


vetor = list(range(0,10000))
random.shuffle(vetor)
antes = time.time()
insertion_sort(vetor)
depois = time.time()
total = (depois - antes) * 1000

print("Tempo de processamento Insertion Sort: {:.2f} ms".format(total))
# Tempo de processamento Insertion Sort: 6421.84 ms

