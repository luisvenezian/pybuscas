import time
# Onde V é o vetor dos dados, e X o valor desejado.


def busca_sequencial(v, x):
    i = 0
    # Percorrendo o vetor
    while i < len(v):
        if v[i] == x:
            return i

        i += 1
    # Um valor simbólico inválido, dado não encontrado.
    return -1


vetor = list(range(0, 10000001))
chave = 10000000
# Calcular o tempo
antes = time.time()
posicao = busca_sequencial(vetor, chave)
depois = time.time()
diferenca = (depois - antes) * 1000

if posicao >= 0:
    print('Elemento encontrado na posição {}.'.format(posicao))
else:
    print('Elemento não encontrado.')

print("Configurações da busca.:\n\tValor Pesquisado: {}\n\tTamanho da Lista: {}\n".format(chave, len(vetor)))
print("O tempo total da busca foi: {:.2f} ms".format(diferenca))

# O tempo total da busca foi: 2350.77 ms

