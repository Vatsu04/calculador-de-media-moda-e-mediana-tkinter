# Bubble Sort

quant_idades = int(input("Quantas idades você gostaria de calcular a média, mediana e moda?"))



idades = [] 
for i in range(quant_idades):
    idade = int(input("\nDigite a %i° idade: " % (i+1)))
    idades.append(idade)

def crescente(lista):
    size = len(lista) - 1
    for i in range(len(lista)):
        for j in range(size):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
        size -= 1
    return lista

def media(lista):
    soma = 0
    for i in range(len(lista)):
        soma+=lista[i]
    media = soma/len(lista)
    print('Média', round(media,2))

def mediana(lista):
    lista = crescente(lista)
    # print(lista)
    if len(lista)%2 !=0:
        indice_mediana = int(len(lista)/2)
        print('Mediana', lista[indice_mediana])
    else:
        indice1 = int(len(lista)/2)
        indice2 = indice1 - 1
        soma = lista[indice1] + lista[indice2]
        mediana = soma/2
        print('Mediana', round(mediana,2))


def moda(lista):
    t = len(lista)
    repete = [0]*t
    conta = 0
    for i in range(t):
        for j in range(i+1, t):
            if lista[i] == lista[j]:
                repete[i] +=1
                if repete[i] > conta:
                    conta = repete[i]
                    moda = lista[i]
        repete[i] = 0
    if conta == 0:
        print('a lista não possui moda')
    else:
        print('Moda:', moda)




media(idades)
moda(idades)
mediana(idades)
