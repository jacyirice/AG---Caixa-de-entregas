import random
from constants import *

def avalia_lista_cromossomos(lista):
    ''' Avalia uma lista de cromossomos '''
    for i in lista:
        i.avalia_cromossomo()

def criaString():
    #cria uma string com oito valores zeros ou uns, retornando-a
    size=8
    char='01'
    return ''.join(random.choice(char) for _ in range(size))

def criaListaDeStrings():
    #cria uma lista com cem strings, cada string composta por
    #oito valores zero ou um (podem ser criadas aleatoriamente),
    #retornando-a
    lista = [criaString() for _ in range(100)]
    return lista

def dezMenores(lista):
    #recebe uma lista de cem sublistas que têm a seguinte forma:
    #[string original, número real qualquer], ordene-as do menor
    #para o maior número real, e retorne uma lista com as dez primeiras
    #strings desta lista recém-ordenada.
    novaLista = sorted(lista, key = lambda x: x[1])
    print(novaLista)
    return novaLista[:10]

def muda(string):
    #recebe uma string de oito valores zeros ou uns e, **aleatoriamente**,
    #modifique um de seus valores trocando de zero para um ou vice-versa,
    #retornando a string modificada.
    pos = random.randint(0, 7)
    lista = list(string)
    print(lista)

    if (lista[pos] == '1'):
        lista[pos] = '0'
    else:
        lista[pos] = '1'

    return ''.join(lista)

def combina(lista):
    print(lista)
    print('\nLista tuplas\n')
    novaLista=[]
    for i in range(len(lista)):
        for j in range(len(lista)):
            if j != i:
                novaLista.append([lista[i], lista[j]])
    return novaLista

def cruzaUm(stringA,stringB):
    novaStringA = stringA[:4] + stringB[4:]
    novaStringB = stringB[:4] + stringA[4:]

    lista = [novaStringA, novaStringB]
    return lista

def cruzaDois(stringA,stringB):
    novaStringA = stringA[:2] + stringB[2:6] + stringA[6:]
    novaStringB = stringB[:2] + stringA[2:6] + stringB[6:]

    lista = [novaStringA, novaStringB]
    return lista

def main():
    
    print(criaString())
    #saida na tela: 11001100

    print('\nFuncao 4\n')
    print(criaListaDeStrings())
    #saida na tela: ['10101101','10110101','01101010',...,'10101010']

    print('\nFuncao 5\n')

    print(binarioSeguidoDeReal('11001101'))
    #saida na tela: ['11001100',2.02]

    print('\nFuncao 6\n')
    print(criaListaDeListas(criaListaDeStrings()))
    #saida na tela: [['11001100',4.43],['10001000',0.54],...,['01000100',2.12]]

    print('\nFuncao 7\n')
    print(subtrai(1.2))
    #saida na tela: 0.56
    print(subtrai(2.2))
    #saida na tela: 2.84

    print('\nFuncao 8\n')
    print(dezMenores(criaListaDeListas(criaListaDeStrings())))
    #saida na tela: [[['10001000',0.54],['01000100',2.12],...,['11001100',4.43]]

    print('\nFuncao 9\n')
    print(muda('10110110'))
    #saida na tela: 11110110

    print('\n Funcao 10\n')
    print((combina(criaListaDeStrings()[:10])))
    #saida na tela: [['10101010','11111111'],['10101010','00110011'],... ['11111111','10101010'],...]
    
    print('\nFuncao 11\n')
    print(cruzaUm('10110100','11001000'))
    #saida na tela: ['10111000','11000100']
    
    print('\nFuncao 12\n')
    print(cruzaDois('10110100','11001000'))
    #saida na tela: ['10001000','11110100']


if __name__ == '__main__':
    main()