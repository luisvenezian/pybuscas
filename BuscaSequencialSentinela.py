import time
#  Onde V é o vetor dos dados, e X o valor desejado.


def busca_sequencial_sentinela(v, x):
    i = 0
    #  Atribui-se ao ultimo valor do vetor, a chave.
    v.append(x)
    #  Percorrendo o vetor, economizando uma condição.
    while v[i] != x:
        i += 1

    #  Um valor simbólico inválido, dado não encontrado.
    if i == len(v)-1:
        return -1

    return -1


vetor = list(range(0, 10000001))
chave = 10000000
#  Calcular o tempo
antes = time.time()
posicao = busca_sequencial_sentinela(vetor, chave)
depois = time.time()
diferenca = (depois - antes) * 1000

if posicao >= 0:
    print('Elemento encontrado na posição {}.'.format(posicao))
else:
    print('Elemento não encontrado.')

print("Configurações da busca.:\n\tValor Pesquisado: {}\n\tTamanho da Lista: {}\n".format(chave, len(vetor)))
print("O tempo total da busca foi: {:.2f} ms".format(diferenca))

