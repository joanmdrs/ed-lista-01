"""
Este exercício resolve o problema clássico de "maior substring sem caracteres repetidos".

Para cada palavra da lista, o programa percorre os caracteres um a um.

No caso de encontrar um caractere repetido na substring atual, é realizado o corte da parte da frente até esse caractere.

Após isso, continua construindo a substring sem repetição, mantendo assim o controle da maior substring encontrada até o momento.
"""

"""Entradas do programa"""
lista_palavras = ['abcabcbb', 'bbbbb', 'pwwkew'] 

"""
Primeiro, é executado um loop for que percorre a lista de palavras.
"""
for palavra in lista_palavras:
    
    """
    É definido duas variáveis: uma para guardar a maior substring sem repetição,
    e outra para armazenar a substring atual que está sendo construída.
    """
    maior_substring = ""        
    atual = ""                  

    """
    Segundo loop: percorre cada caractere da palavra atual. 
    """
    for c in palavra:
        """
        Verifica se o caractere já está na substring atual. Caso sim, é encontrado o índice da repetição e remove até esse ponto.
        """
        if c in atual:
            indice = atual.index(c)
            atual = atual[indice + 1:]

        """Adiciona o caractere atual à substring"""
        atual += c

        """Caso a substring atual for maior do que a maior já encontrada, atualiza"""
        if len(atual) > len(maior_substring):
            maior_substring = atual

    """Exibe os resultados para a palavra atual"""
    print("\nInput:", palavra)                      
    print("Output:", len(maior_substring))          
    print("Explanation: The answer is", maior_substring, "with the length of ", len(maior_substring))
