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

print('\nPopulacao inicial\n')

for i in range(1,t,1):
    print('\n', geracoes[i-1])
    geracoes[i-1].selecionar()
    print(f'\nGeração {i}\n')
    
    geracoes.append(Populacao())
    
    geracoes[i].cruzar(geracoes[i-1])
    
    geracoes[i].mutacao()
    
    geracoes[i].aptidao()

print(geracoes[-1])
melhorCromossomo = geracoes[-1].populacao[-1].cromossomo
print('\nMelhor cromossomo:', melhorCromossomo)

print('\nItens da mochila:')
for i, j in enumerate(melhorCromossomo):
    if j == '1':
        print('\t',item[i])