"""

O algoritmo Quick Sort utiliza como estratégia de ordenação, a definição de um pivô. Sendo assim, para implementar o algortimo Quick Sort, defini uma função onde defini o pivô como sendo o primeiro elemento da lista. 

Após isso, é executado um loop for que separa os elementos da lista e os separa em três novas listas, sendo elas: 

menores: armazena os elementos que são menores que o pivô
iguais: armazena os elementos que são iguais ao pivô
maiores: armazena os elementos que são maiores que o pivô

Logo em seguida, a função realiza duas chamadas recursivas para si mesma, primeiro passando como parâmetro a lista de menores, e depois passando a lista de maiores. 

O retorno da função é a junção das três listas. 

A condição base da função recursiva, é quando o tamanho da lista for menor ou igual a 1. Pois, neste caso, a lista já vai está ordenada. 

Quando a recursão chegar ao seu caso base, a mesma vai começar a realizar o retorno de cada chamada recursiva até chegar a primeira chamada da função, retornando a lista ordenada.

"""



def quick_sort(lista):
    if len(lista) <= 1:
        return lista  

    pivo = lista[0]
    menores = []
    iguais = []
    maiores = []

    for elemento in lista:
        if elemento < pivo:
            menores.append(elemento)
        elif elemento > pivo:
            maiores.append(elemento)
        else:
            iguais.append(elemento) 

    return quick_sort(menores) + iguais + quick_sort(maiores)

lista = [50, 12, 5, 69, 1, 56, 10, 2]
lista_ordenada = quick_sort(lista)
print("Lista ordenada:", lista_ordenada)
