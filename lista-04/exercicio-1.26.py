""" 
De acordo com o próprio enunciado da questão, o algoritmo buble_sort compara pares adjacentes (lista[j] e lista[j+1]) e troca se estiverem fora de ordem.

O algoritmo realiza esse processo até a lista estar ordenada.


Sendo assim, foram implementadas duas estruturas de loop for: 
a primeira (`for i in range(n)`) controla o número de passagens necessárias sobre a lista, 
enquanto a segunda (`for j in range(n - 1 - i)`) percorre os elementos adjacentes da lista a cada iteração.

A condição `n - 1 - i` faz com que o algoritmo não percorra os elementos que já estão ordenados ao final da lista.

"""

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = [50, 12, 5, 69, 1, 56, 10, 2]
lista_ordenada = bubble_sort(lista)
print("Lista ordenada:", lista_ordenada)
