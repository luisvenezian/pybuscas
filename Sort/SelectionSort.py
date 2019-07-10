import random
import time
# Onde v é a lista a ser ordenada.


def selection_sort(v):
    i = 0
    while i < len(v) - 1:
        menor = i
        j = i + 1
        # busca o menor elemento.
        while j < len(v):
            if v[j] < v[menor]:
                menor = j
            j += 1

        if menor != i:
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp

        i += 1


vetor = list(range(0,10000))
random.shuffle(vetor)
antes = time.time()
selection_sort(vetor)
depois = time.time()
total = (depois - antes) * 1000

print("Tempo de processamento Selection Sort: {:.2f} ms".format(total))
# $Saída: Tempo de processamento Selection Sort: 13603.68 ms
