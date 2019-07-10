import random
import time
# Onde v é a lista a ser ordenada.


def bublle_sort(v):

    fim = len(v)

    while fim > 0:

        i = 0
        # Percorrer o vetor
        while i < fim-1:
            if v[i] > v[i+1]:
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
            i += 1

        fim -= 1


vetor = list(range(0,10000))
random.shuffle(vetor)
antes = time.time()
bublle_sort(vetor)
depois = time.time()
total = (depois - antes) * 1000

print("Tempo de processamento do BubbleSort: {:.2f} ms".format(total))

