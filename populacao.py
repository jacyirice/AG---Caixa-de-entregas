import random
from cromossomo import Cromossomo

class Populacao:
    '''
    Classe criada para representar a população e suas caracteristicas
    '''
    populacao = []
    aptidao_total = 0
    selecionados = None

    def __init__(self, populacao=[], tam=10):
        '''Inicializa população com cromossomos randomicos ou com uma especificada'''
        if not populacao:
            self.populacao = [Cromossomo() for _ in range(tam)]
        else:
            self.populacao = populacao

    def aptidao(self):
        ''' 
        Avalia os cromossomos da população e ordena a lista
        '''
        for i in self.populacao:
            i.set_aptidao()
            self.aptidao_total += i.aptidao

        for i in self.populacao:
            i.aptidao_r = round(i.aptidao/self.aptidao_total,9)
        self.populacao = sorted(self.populacao, key=lambda x: x.aptidao)


    def selecionar(self):
        '''
        Seleciona cromossomos por meio do metodo da roleta
        '''
        aptidao_r_lista = [i.aptidao_r for i in self.populacao]
        k = int(len(self.populacao)/2)
        self.selecionados = Populacao(random.choices(self.populacao, aptidao_r_lista, k = k))

    def cruzaDois(self, cromossomoA, cromossomoB):
        '''
        Realiza o Cruzamento – Ponto Duplo
        '''
        novoCromossomoA = cromossomoA.cromossomo[:2] + \
            cromossomoB.cromossomo[2:6] + cromossomoA.cromossomo[6:]
        novoCromossomoB = cromossomoB.cromossomo[:2] + \
            cromossomoA.cromossomo[2:6] + cromossomoB.cromossomo[6:]

        return [Cromossomo(novoCromossomoA), Cromossomo(novoCromossomoB)]

    def cruzar(self):
        '''
        Cruza os elementos selecinados da população com os outros selecionados
        exceto ele mesmo utilizando Ponto Duplo
        '''
        novaPop = []
        selecionados = self.selecionados.populacao
        quant_s = len(selecionados)

        for i in range(quant_s):
            pos = random.randint(0,quant_s-1)
            if i == pos:
                pos += 1
            if pos == quant_s:
                pos = -1
            novaPop.extend(self.cruzaDois(selecionados[i],selecionados[pos]))
        
        return Populacao(novaPop)

    def mutacao(self):
        '''
        Realiza a mutação aleatória de todos os cromossomos
        '''
        for i in self.populacao:
            i.mutacao()

    def __str__(self):
        '''
        Formata o retorno para string
        '''
        texto = 'cromossomo - aptidao - aptidao relativa'
        for i in self.populacao:
            texto+='\n'+str(i)
        return texto
