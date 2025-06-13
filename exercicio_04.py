"""
O método solicitar_numeros permite o cadastro de uma lista de números positivos. 

Primeiro, é definido uma estrutura de lista para armazenar os números. A estrutura em lista foi escolhida, devido a mesma permitir o armazenamento de uma quantidade variável de elementos, assim como vantagens de: facilidade de iteração, acesso direto a elementos, flexibilidade e utilização de métodos agéis como o append e len. 

Segundo, enquanto o usuário não digitar -1, o mesmo poderar informar números para a análise. A medida que o usuário informa ps números é verificado e o mesmo não é -1 ou menor que 0. Caso o número seja positivo, o mesmo é adicionado a lista. 

Caso o usuário informe -1, o loop é encerrado. Caso o usuário informe valores menores que ou iguais a 0, é informado uma mensagem ao usuário. 

Após o loop é verificado se a lista contém mais de um elemento ou não, e retorna a lista. 

"""
def solicitar_numeros():
    numeros_positivos = []

    print("Digite números positivos para a análise. Para encerrar, digite -1.")

    while True:
        entrada = input(f"Informe o {len(numeros_positivos)+1}º número: ")

        try:
            numero = float(entrada)

            if numero == -1:
                break 

            if numero > 0:
                numeros_positivos.append(numero)
            else:
                print("Por favor, informe apenas números positivos.")

        except ValueError:
            print("Entrada inválida. Digite um número ou -1 para encerrar.")

    if len(numeros_positivos) > 1:
        print("\nNúmeros inseridos com sucesso!")
        print(numeros_positivos)
        return numeros_positivos
    else:
        print("\nÉ necessário informar pelo menos dois números positivos para a análise.")
        return []
        
"""
O método calcular_media recebe uma lista de números por parâmetro. Com base nessa lista, o método executa um loop para percorrer todas as posições da lista de números, somando cada elemento ao total acumulado.

Após o término do loop, o método divide o valor total da soma pela quantidade de elementos presentes na lista (quant), obtendo assim a média aritmética dos números fornecidos.

Por fim, essa média é retornada como resultado da função.
"""
def calcular_media(numeros):
    total = 0
    quant = len(numeros)
    for n in numeros:
        total += n
    return total / quant  

"""
O método `calcular_maximo` recebe uma lista de números por parâmetro. Com base nessa lista, o método executa um loop para percorrer todas as posições da lista de números. 

À medida que o loop executa, é feita uma verificação para identificar se o número atual (`n`) é maior do que o valor armazenado na variável `maior`. Caso sim, o valor de `maior` é atualizado com o novo número.  

Dessa forma, ao final do loop, a variável `maior` conterá o maior valor presente na lista.  Esse valor é então retornado como resultado da função.
"""
def calcular_maximo(numeros):
    maior = numeros[0]
    for n in numeros:
        if n > maior:
            maior = n
    return maior


"""
O método `calcular_desvio_padrao` recebe uma lista de números por parâmetro e tem como objetivo calcular o desvio padrão amostral desses valores.

Primeiramente, ele chama o método `calcular_media` para obter a média dos números da lista.  
Em seguida, inicializa a variável `soma_quadrados` com zero. Essa variável será usada para acumular a soma dos quadrados das diferenças entre cada número da lista e a média.

O loop percorre todos os elementos da lista, calcula a diferença entre cada número e a média, eleva essa diferença ao quadrado e adiciona esse valor à `soma_quadrados`.

Após o loop, a variância é calculada dividindo a soma dos quadrados pelo número de elementos menos 1 (n - 1), o que corresponde à fórmula da **variância amostral**.  
Caso a lista tenha apenas um elemento (ou esteja vazia), o desvio padrão é considerado 0, evitando uma divisão por zero.

Por fim, o método retorna a **raiz quadrada da variância**, que é o valor do desvio padrão.
"""
def calcular_desvio_padrao(numeros):
    media = calcular_media(numeros)
    soma_quadrados = 0
    for n in numeros:
        soma_quadrados += (n - media) ** 2
    variancia = soma_quadrados / (len(numeros) - 1) if len(numeros) > 1 else 0
    return variancia ** 0.5

"""
O método contar_numeros_unicos recebe uma lista de números e retorna a quantidade de valores únicos (ou distintos) nela.

Ela percorre a lista original e, para cada número, verifica se ele já foi adicionado à lista unicos. Se não tiver sido, ele é adicionado.

Ao final, a função retorna o comprimento da lista unicos, que representa a quantidade de números diferentes na lista original.
"""

def contar_numeros_unicos(numeros):
    unicos = []
    for n in numeros:
        if n not in unicos:
            unicos.append(n)
    return len(unicos)

"""
O método gerar_analise é responsável por exibir uma análise estatística simples da lista de números recebida como parâmetro."""
def gerar_analise(numeros):
    print("\nANÁLISE DOS NÚMEROS")
    print("Total de números:", len(numeros))
    print("Números únicos:", contar_numeros_unicos(numeros))
    print("Média:", calcular_media(numeros))
    print("Máximo:", calcular_maximo(numeros))
    print("Desvio padrão: ", calcular_desvio_padrao(numeros))

""" 
O método main realiza a chamada ao método solicitar_numeros. Após isso, o main chama o método gerar_analise, passando como parâmetro a lista de números recebida do método solicitar_numeros. 
"""
def main():
    numeros = solicitar_numeros()
    gerar_analise(numeros)

main()