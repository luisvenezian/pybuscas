import time


#  Onde V é o vetor dos dados,
#       X o valor desejado,
#       P é a posição Incial
#       R é a posição Final


def busca_binaria(v, p, r, x):
    # Condição de existência
    if p <= r:
        q = (p+r) // 2  # Índice da metade do vetor.
        if x > v[q]:
            return busca_binaria(v, q+1, r, x)  # Busca direita
        elif x < v[q]:
            return busca_binaria(v, p, q-1, x)  # Busca esquerda
        else:
            return q  # Encontrou elemento.

    return -1  # Não encontrou elemento

vetor = list(range(0, 10000001))
chave = 10000000
# Calcular o tempo
antes = time.time()
posicao = busca_binaria(vetor, 0, len(vetor)-1, chave)
depois = time.time()
diferenca = (depois - antes) * 1000

if posicao >= 0:
    print('Elemento encontrado na posição {}.'.format(posicao))
else:
    print('Elemento não encontrado.')

print("Configurações da busca.:\n\tValor Pesquisado: {}\n\tTamanho da Lista: {}\n".format(chave, len(vetor)))
print("O tempo total da busca foi: {:.2f} ms".format(diferenca))

