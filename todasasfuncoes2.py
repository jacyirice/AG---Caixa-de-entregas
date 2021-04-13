'''
Faça um programa que 

1.	Gere 100 strings compostas por oito valores zeros ou uns e coloque em uma lista
2.	Crie uma lista com cada string sendo colocada junto com sua avaliação, em um formato [string, avaliação]
3.	Para a string ser avaliada, deve converter cada uma destas strings em um valor decimal fracionário: os dois primeiros equivalem à parte inteira e os demais equivalem a parte fracionária. Após, avalia cada um destes valores em relação ao número 2: cada um deles deve ser elevado ao quadrado e subtraído do número 2. Esta diferença, em módulo, é a avaliação.
4.	Imprima cada string, seu valor em número real e sua avaliação
5.	Verifique qual string tem menor avaliação, imprima-a seguido de seu valor em real
a.	Se esse valor (avaliação) for muito próximo de zero, para a execução
6.	As 10 strings com menor valor de avaliação devem ser separadas e, duas a duas, devem gerar duas novas strings (as duas novas devem ser compostas pela metade inicial de uma com a metade final da outra e vice-versa). Ou seja, vc está fazendo um arranjo simples que gerará 90 novas strings que devem ser colocadas em uma lista. Escolha dez strings aleatórias, modifique-as alterando um de seus valores, e acrescente-as na lista, totalizando 100 strings na nova lista.
7.	Refaça a partir do passo 2 com a nova lista até chegar a uma string com avaliação muito próxima de zero.
Apresente o valor desta string em binário e em decimal fracionário.
'''

import random

def converteBinarioReal(string):
    #recebe uma string com oito valores zero ou um sendo os dois primeiros
    #equivalentes à parte inteira e os seis restantes equivalente à parte
    #fracionária de um número binário.
    #A função deverá retornar este número convertido para um número real (float)
    parteInteira = int(string[:2], base=2)
    parteDecimal = int(string[2:], base=2)
    print(parteInteira)
    print(parteDecimal)

    return float('{}.{}'.format(parteInteira, parteDecimal))

print(converteBinarioReal('11001100'))
# saida na tela: 3.13

print('Funcao 2\n')

def converteRealBinario(numero):
    #recebe um valor real (float) e converte para binário fracionário
    #no formato de uma string com oito valores zero ou um, sendo
    #os dois primeiros equivalentes à parte inteira e os seis restantes
    #equivalente à parte fracionária do número binário.
    #A função deve retornar esta string.
    partes = str(numero).split('.')
    print(partes)
    parteInteira = format(int(partes[0]), 'b')
    parteDecimal = format(int(partes[1]), 'b')
    if len(parteDecimal) < 6:
        parteDecimal = '0'*(6-len(parteDecimal)) + parteDecimal
    print(parteInteira)
    print(parteDecimal)
    return '{}{}'.format(parteInteira, parteDecimal)

print (converteRealBinario(3.12))
#saida na tela: 11001100

print('funcao3\n')

def criaString():
    #cria uma string com oito valores zeros ou uns, retornando-a
    size=8
    char='01'
    return ''.join(random.choice(char) for _ in range(size))

print(criaString())
#saida na tela: 11001100

print('\nFuncao 4\n')

def criaListaDeStrings():
    #cria uma lista com cem strings, cada string composta por
    #oito valores zero ou um (podem ser criadas aleatoriamente),
    #retornando-a
    lista = [criaString() for _ in range(100)]
    return lista
print(criaListaDeStrings())
#saida na tela: ['10101101','10110101','01101010',...,'10101010']

print('\nFuncao 5\n')

def binarioSeguidoDeReal(string):
    #recebe uma string com oito zeros e uns e retorna uma lista no
    #formato [string original, número real qualquer] (o número real
    #pode ser gerado aleatoriamente)
    lista = [string, round(random.uniform(0.0, 10.0),2)]
    return lista

print(binarioSeguidoDeReal('11001101'))
#saida na tela: ['11001100',2.02]

print('\nFuncao 6\n')

def criaListaDeListas(lista):
    #recebe uma lista de cem strings de zeros e uns e retorna uma nova lista
    #composta por sublistas criadas da seguinte forma:
    #[string original, um número real qualquer].
    #(o número real pode ser gerado aleatoriamente
    for i in range(len(lista)):
        lista[i] = binarioSeguidoDeReal(lista[i])
    return lista

print(criaListaDeListas(criaListaDeStrings()))
#saida na tela: [['11001100',4.43],['10001000',0.54],...,['01000100',2.12]]

print('\nFuncao 7\n')

def subtrai(numero):
    #recebe um valor real e retorne o módulo (valor absoluto) do valor 2
    #subtraido deste valor real ao quadrado, ou seja :   |2 – real**2|
    return round(abs(2 - numero**2),2)
print(subtrai(1.2))
#saida na tela: 0.56

print(subtrai(2.2))
#saida na tela: 2.84

print('\nFuncao 8\n')

def dezMenores(lista):
    #recebe uma lista de cem sublistas que têm a seguinte forma:
    #[string original, número real qualquer], ordene-as do menor
    #para o maior número real, e retorne uma lista com as dez primeiras
    #strings desta lista recém-ordenada.
    novaLista = sorted(lista, key = lambda x: x[1])
    print(novaLista)
    return novaLista[:10]

print(dezMenores(criaListaDeListas(criaListaDeStrings())))
#saida na tela: [[['10001000',0.54],['01000100',2.12],...,['11001100',4.43]]

print('\nFuncao 9\n')

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

print(muda('10110110'))
#saida na tela: 11110110

print('\n Funcao 10\n')

def combina(lista):
    #recebe uma lista com dez strings e retorna uma lista de sublistas
    #as sublista é composta por duas strings, combinando duas a duas todas as
    #dez strings
    #como combinar:
    #--> pega a primeira string e faz sublistas dela com as outras
    # nove (e vai acrescentando na lista maior). [string1,string2],[string1,string3]...
    #--> pega a segunda string e também, faz sublistas dela com as outras nove, e
    #continua acrescentando na mesma lista maior [string2,string1],[string2,string3]...
    #faz isso com as dez strings
    print(lista)
    print('\nLista tuplas\n')
    novaLista=[]
    for i in range(len(lista)):
        for j in range(len(lista)):
            if j != i:
                novaLista.append([lista[i], lista[j]])
    return novaLista
print((combina(criaListaDeStrings()[:10])))
#saida na tela: [['10101010','11111111'],['10101010','00110011'],... ['11111111','10101010'],...]

print('\nFuncao 11\n')


def cruzaUm(stringA,stringB):
    #recebe duas strings de oito valores zeros ou uns e cria
    #duas novas strings no seguinte formato:
    #-->uma string será composta pelos quatro primeiros valores da primeira
    #seguidos pelos quatro últimos da segunda;
    #-->e a outra string será composta pelos quatro primeiros valores da segunda
    #string seguidos pelos quatro últimos da primeira string.
    #retorna as duas strings em uma lista
    novaStringA = stringA[:4] + stringB[4:]
    novaStringB = stringB[:4] + stringA[4:]

    lista = [novaStringA, novaStringB]
    return lista

print(cruzaUm('10110100','11001000'))
#saida na tela: ['10111000','11000100']

print('\nFuncao 12\n')

def cruzaDois(stringA,stringB):
    #recebe duas strings de oito valores zeros ou uns e cria
    #duas novas strings no seguinte formato:
    #-->uma string será composta pelos dois primeiros valores da primeira seguidos
    #pelos quatro do meio da segunda e pelos dois últimos da primeira;
    #-->e a outra string será composta pelos dois primeiros valores da segunda string
    #seguidos pelos quatro do meio da primeira e pelos dois últimos da segunda string
    novaStringA = stringA[:2] + stringB[2:6] + stringA[6:]
    novaStringB = stringB[:2] + stringA[2:6] + stringB[6:]

    lista = [novaStringA, novaStringB]
    return lista
print(cruzaDois('10110100','11001000'))
#saida na tela: ['10001000','11110100']