"""
Este exercício recebe como entrada uma string de letras, representando a quantidade de vezes que cada alternativa foi escolhida.

Após isso, foi definido o dicionário dic_alternativas para armazenar a quantidade de vezes que cada letra foi escolhida.

Sendo assim, foi executado um loop for que percorre cada caractere da string de entrada. Dentro do for, é verificado se o caractere já existe no dicionário. Caso sim, o valor associado a essa chave é incrementado em 1. Caso contrário, a chave é criada no dicionário com o valor inicial 1.

Por fim, outro loop percorre as alternativas de 'a' até 'e' e imprime, para cada uma, a quantidade de vezes que foi escolhida, mesmo que tenha sido zero.
"""


string_alternativas = "aaabbccdeee"

dic_alternativas = dict()


for caractere in string_alternativas:
    if caractere in dic_alternativas:
        dic_alternativas[caractere] += 1
        
    else:
        dic_alternativas[caractere] = 1
        

for letra in ['a', 'b', 'c', 'd', 'e']:
    if letra in dic_alternativas:
        print(f"A alternativa {letra} foi escolhida {dic_alternativas[letra]} vezes")
    else:
        print(f"A alternativa {letra} foi escolhida 0 vezes")

