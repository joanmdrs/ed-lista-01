"""
A função calcular_fatorial recebe como parâmetro um número n.

Caso n = 0 ou n = 1, significa que encontramos nosso caso trivial, e portanto, retornamos 1.

Se não, o programa multiplica o valor de n pela chamada recursiva da função calcular_fatorial, que recebe como parâmetro (n - 1).

Isso provoca um efeito de empilhamento, onde as chamadas vão se acumulando na pilha de execução até atingir o caso base (n == 0 ou n == 1). 

A partir daí, as chamadas começam a ser resolvidas do último para o primeiro, multiplicando os valores retornados sucessivamente.

Por exemplo:
calcular_fatorial(4)
= 4 * calcular_fatorial(3)
= 4 * (3 * calcular_fatorial(2))
= 4 * (3 * (2 * calcular_fatorial(1)))
= 4 * (3 * (2 * 1))
= 24

Ao final, o valor calculado é retornado e exibido ao usuário.
"""

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

numero = int(input("Informe o número que deseja calcular o fatorial: "))
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")
