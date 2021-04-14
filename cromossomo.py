import random
from constants import *

class Cromossomo:
    '''
    Classe criada para representar o cromossomo e suas caracteristicas
    '''
    cromossomo = None
    aptidao = 0
    gd_total = 0
    aptidao_r = 0

    def __init__(self, cromossomo='', size=8, char='01'):
        '''Inicializa o cromossomo com o cromossomo especificado ou um randomico'''
        if cromossomo:
            self.cromossomo = cromossomo
        else:
            self.cromossomo = ''.join(random.choice(char) for _ in range(size))

    def set_aptidao(self):
        '''
        Calcula a aptidao do cromossomo por meio do bonus e verifica
        se o grau de dificuldade do cromossomo está dentro dos requisitos,
        se não tiver seta a aptidao para 1 a fim de participar na seleção
        '''
        # Calcula o bonus e o grau de dificuldade do cromossomo
        for i in range(len(self.cromossomo)):
            if (self.cromossomo[i] == '1'):
                self.aptidao += bonus[i]
                self.gd_total += gd[i]

        # Verifica se o cromossomo está dentro do limite de dificuldade
        if self.gd_total > gd_max:
            self.aptidao = 1
        if self.aptidao < 1:
            self.aptidao = 1
            
    def mutacao(self):
        '''
        Realiza a mutação aleatoria do cromossomo
        '''
        pos = random.randint(0, 7)
        lista = list(self.cromossomo)
        if (lista[pos] == '1'):
            lista[pos] = '0'
        else:
            lista[pos] = '1'
        self.cromossomo = ''.join(lista)

    def __str__(self):
        '''
        Formata o retorno para string
        '''
        return '{} - {} - {}'.format(self.cromossomo,self.aptidao,self.aptidao_r)