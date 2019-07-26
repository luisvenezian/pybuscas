import time


class SortTest:
    def __init__(self, v, start):
        self.vetor = v
        self.start = start

    def bubble_sort(self):
        fim = len(self.vetor)
        while fim > 0:
            i = 0
            # Percorrer o vetor
            while i < fim-1:
                if self.vetor[i] > self.vetor[i+1]:
                    temp = self.vetor[i]
                    self.vetor[i] = self.vetor[i+1]
                    self.vetor[i+1] = temp
                i += 1
            fim -= 1
        return (time.time() - self.start) * 1000

    def selection_sort(self):
        i = 0
        while i < len(self.vetor) - 1:
            menor = i
            j = i + 1
            # busca o menor elemento.
            while j < len(self.vetor):
                if self.vetor[j] < self.vetor[menor]:
                    menor = j
                j += 1
            if menor != i:
                temp = self.vetor[i]
                self.vetor[i] = self.vetor[menor]
                self.vetor[menor] = temp
            i += 1
        return (time.time() - self.start) * 1000

    def insertion_sort(self):
        i = 1
        while i < len(self.vetor):
            temp = self.vetor[i]
            trocou = False
            j = i - 1
            while j >= 0 and self.vetor[j] > temp:
                self.vetor[j+1] = self.vetor[j]
                trocou = True
                j -= 1
            if trocou:
                self.vetor[j+1] = temp
            i += 1
        return (time.time() - self.start) * 1000
