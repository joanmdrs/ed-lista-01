# Define uma lista de palavras
frutas = ["maçã", "banana", "laranja", "uva", "abacaxi", "manga", "melancia", "pera", "kiwi", "morango"]

# A variável quant armazena a quantidade de itens da lista
quant = len(frutas)

# Define um loop que executa a quantidade de itens que contém na lista.
for i in range(quant):
    # Caso a posição do item seja par, é exibido a palavra existente naquela posição
    if i % 2 == 0:
        print(frutas[i])