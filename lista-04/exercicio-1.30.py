"""

O algoritmo Quick Sort utiliza como estratégia de ordenação, a definição de um pivô. Sendo assim, para implementar o algortimo Quick Sort, defini uma função onde defini o pivô como sendo o primeiro elemento da lista. 

Após isso, é executado um loop for que percorre os elementos da lista e os coloca em duas listas, sendo elas:

menores: armazena os elementos que são menores que o pivô
maiores: armazena os elementos que são maiores que o pivô

Logo em seguida, a função realiza duas chamadas recursivas para si mesma, primeiro passando como parâmetro a lista de menores, e depois passando a lista de maiores. 

O retorno da função é a junção do retorno à chamada recursiva para os elementos menores que o pivô, com o próprio pivô, e depois com o retorna à chamada recursiva para os elementos maiores que o pivô.

A condição base da função recursiva, é quando o tamanho da lista for menor ou igual a 1. Pois, neste caso, a lista já vai está ordenada por definição.

Quando a recursão chegar ao seu caso base, a mesma vai começar a realizar o retorno de cada chamada recursiva até chegar a primeira chamada da função, retornando a lista ordenada.

"""



def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[0]
    menores = []
    maiores = []
    # Já que escolhemos o pivo como sendo o primeiro elemento da lista, começamos o laço a partir do elemento da posição 1
    for elemento in lista[1:]: 
        if elemento < pivo:
            menores.append(elemento)
        else:
            maiores.append(elemento)

    return quick_sort(menores) + [pivo] + quick_sort(maiores)

# Teste
lista = [50, 12, 5, 69, 1, 56, 10, 2]
lista_ordenada = quick_sort(lista)
print("Lista ordenada:", lista_ordenada)

