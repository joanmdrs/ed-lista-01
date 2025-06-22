"""
Para implementar este exercício, foram utilizadas duas estruturas de loop for.

O primeiro for itera sobre o tamanho da lista recebida por parâmetro. Sua função é percorrer a posição atual da borda entre a parte ordenada e a parte não ordenada.

No início da iteração, a parte ordenada está vazia. Assim, começamos com o índice 0. Assume-se que o menor elemento da parte não ordenada está na posição i. Por isso, inicializamos indice_menor = i.

Por sua vez, o segundo for compara os elementos da parte não ordenada (isto é, os elementos à direita de i). Se encontrar um valor menor, atualiza a variável indice_menor.

Após o segundo loop, é realizada a troca do menor elemento encontrado com o elemento da posição i. Isso move o menor valor da parte não ordenada para a parte ordenada, na posição correta.

Dessa forma, a cada iteração do primeiro for, a parte ordenada cresce uma posição à direita, até que toda a lista esteja ordenada.
"""


def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
    return lista

lista = [50, 12, 5, 69, 1, 56, 10, 2]
lista_ordenada = selection_sort(lista)
print("Lista ordenada:", lista_ordenada)