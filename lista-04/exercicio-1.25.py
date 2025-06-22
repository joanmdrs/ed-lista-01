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

"""
A sequência de Fibonacci é uma sequência numérica, onde cada termo, a partir do terceiro, é a soma dos dois termos anteriores. 

Sendo assim, a função fibonacci recebe como parâmetro um número n. 
 
Se n = 1, o programa retorna 0 (caso trivial onde sabemos o resultado).
Se n = 2, o programa retorna 1 (caso trivial onde sabemos o resultado).

Se não, o programa realiza duas chamadas recursivas, calculando o valor das posições (n - 1) e (n - 2), e retorna a soma desses dois valores.

Isso gera um efeito de empilhamento de chamadas recursivas, até que se alcancem os casos triviais. A partir daí, os valores começam a ser somados e retornados para as chamadas anteriores, até que se obtenha o valor final da posição n.

Por exemplo:
fibonacci(5)
= fibonacci(4) + fibonacci(3)
= (fibonacci(3) + fibonacci(2)) + (fibonacci(2) + fibonacci(1))
= ((fibonacci(2) + fibonacci(1)) + 1) + (1 + 0)
= ((1 + 0) + 1) + (1 + 0)
= (1 + 1) + 1
= 2 + 1
= 3

Portanto, o valor da 5ª posição da sequência de Fibonacci (considerando n = 1 como a primeira posição) é 3.
"""

def fibonacci(n):
    
    if n == 1:
        return 0
    
    elif n == 2:
        return 1
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
numero = int(input("Informe a posição que deseja saber o valor na sequência de Fibonacci: "))
resultado = fibonacci(numero)
print(f"O valor da posição {numero}º na sequência de Fibonacci é: {resultado}")
