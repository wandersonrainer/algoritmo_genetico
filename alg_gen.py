#######################################################
# codigo basico de AG
# faca as alteracoes que julgar necessarias para aprimorar o algoritmo

import random
import string

# altere a variavel objetivo para a palavra que deseja obter
objetivo = "tecnologia"

# altere a variavel inicio para um valor aleatorio de caracteres
inicio = "aaa"

def avaliacao(inicio, objetivo):
    aval = 0
    for i in range(0, len(inicio)):
        aval += (ord(objetivo[i]) - ord(inicio[i])) ** 2
    return(aval)

def mutate(pai1, pai2):
    filho_dna = pai1['dna'][:]

    # Mistura ambos os DNA
    start = random.randint(0, len(pai2['dna']) - 1)
    stop = random.randint(0, len(pai2['dna']) - 1)
    if start > stop:
        stop, start = start, stop
    filho_dna[start:stop] = pai2['dna'][start:stop]

    # Mutacao de uma posicao
    charpos = random.randint(0, len(filho_dna) - 1)
    filho_dna[charpos] = chr(ord(filho_dna[charpos]) + random.randint(-1,1))
    filho_fitness = avaliacao(filho_dna, objetivo)
    return({'dna': filho_dna, 'fitness': filho_fitness})

def random_parent(genepool):
    nRAND = random.random() * random.random() * (tamanho_GER - 1)
    nRAND = int(nRAND)
    return(genepool[nRAND])

def descarta_genepool(geracao, genepool):
    for candidato in genepool:
        print ( geracao, candidato['fitness'],''.join(candidato['dna']))
    #print

tamanho_GER = 20
genepool = []
for i in range(0, tamanho_GER):
    dna = [random.choice(string.printable[:-5]) for j in range(0, len(objetivo))]
    fitness = avaliacao(dna, objetivo)
    candidato = {'dna': dna, 'fitness': fitness }
    genepool.append(candidato)

geracao = 0
while True:
    geracao += 1
    genepool.sort(key=lambda candidato: candidato['fitness'])
    descarta_genepool(geracao, genepool)

    if genepool[0]['fitness'] == 0:
        # objetivo reached
        break

    pai1 = random_parent(genepool)
    pai2 = random_parent(genepool)

    filho = mutate(pai1, pai2)
    if filho['fitness'] < genepool[-1]['fitness']:
        genepool[-1] = filho
#######################################################################