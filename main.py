from populacao import Populacao
from constants import item
# Armazena todas as populações que já existiram
geracoes = []

# Quantidade maxima de gerações
t=10

# Gera população inicial randomicamente, adiciona a lista de gerações e avalia
populacao_inicial = Populacao()
populacao_inicial.aptidao()
geracoes.append(populacao_inicial)

# print('\nPopulacao inicial\n',populacao_inicial)

for i in range(1,t,1):
    print('\nAptidao\n', geracoes[i-1])
    
    geracoes[i-1].selecionar()
    # print('\nSelecionados\n',geracoes[i-1].selecionados)
    
    print(f'\nGeração {i}\n')
    
    geracoes.append(Populacao())
    # print('\nNovaPopulação\n',geracoes[i])
    
    geracoes[i].cruzar(geracoes[i-1])
    # print('\nCruzamento\n', geracoes[i])
    
    geracoes[i].mutacao()
    # print('\nMutação\n', geracoes[i])
    
    geracoes[i].aptidao()

print('\nUltima geração\n', geracoes[-1])
melhorCromossomo = geracoes[-1].populacao[-1].cromossomo
print('\nMelhor cromossomo\n', melhorCromossomo)

print('Itens da mochila:\n')
for i, j in enumerate(melhorCromossomo):
    if j == '1':
        print(item[i])