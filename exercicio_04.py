def solicitar_numeros():
    numeros_positivos = []
    quant = int(input("Informe quantos números deseja usar: "))
    
    if quant > 1:
        for i in range(quant):
            numero = float(input(f"Informe o {i+1}º número: "))
            
            numeros_positivos.append(numero)
            
        print("Números inseridos com sucesso!\n")
        print(numeros_positivos)
        return numeros_positivos
        
    else:
        print("A quantidade de números deve ser maior que 1.")
        
    
def calcular_media(numeros):
    total = 0
    quant = len(numeros)
    for n in numeros:
        total += n
    return total / quant  

def calcular_maximo(numeros):
    maior = numeros[0]
    for n in numeros:
        if n > maior:
            maior = n
    return maior

def calcular_desvio_padrao(numeros):
    media = calcular_media(numeros)
    soma_quadrados = 0
    for n in numeros:
        soma_quadrados += (n - media) ** 2
    variancia = soma_quadrados / (len(numeros) - 1) if len(numeros) > 1 else 0
    return variancia ** 0.5

def contar_numeros_unicos(numeros):
    unicos = []
    for n in numeros:
        if n not in unicos:
            unicos.append(n)
    return len(unicos)

def gerar_analise(numeros):
    print("\nANÁLISE DOS NÚMEROS")
    print("Total de números:", len(numeros))
    print("Números únicos:", contar_numeros_unicos(numeros))
    print("Média:", calcular_media(numeros))
    print("Máximo:", calcular_maximo(numeros))
    print("Desvio padrão: ", calcular_desvio_padrao(numeros))

def main():
    numeros = solicitar_numeros()
    gerar_analise(numeros)

main()