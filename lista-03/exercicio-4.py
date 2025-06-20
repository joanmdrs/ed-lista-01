dic1 = { "key1": 50, "key2": 100, "key3": 35, "key4": 15 }
dic2 = { "key1": 100, "key2": 15, "key3": 25 , "key4": 32 }

dicIguais = {}
dicDiferentes = {}

"""Para resolver este exercício, foi necessário usar a estrutura de conjuntos. Onde eu armazeno nas variáveis valores_dic1 e valores_dic2, os valores presentes nos dicionários dic1 e dic2 respectivamente."""

valores_dic1 = set(dic1.values())
valores_dic2 = set(dic2.values())

"""Por meio da operação de interseção, encontramos os valores em comum entre ambos os dicionários."""
valores_comuns = valores_dic1 & valores_dic2

"""Para preencher o dicIguais, foi realizado um loop for que percorre os valores de dic2 
e verifica se os mesmos estão em valores_comuns. Caso sim, o par chave-valor é adicionado 
ao dicionário dicIguais, utilizando as chaves originais de dic2."""
for key, value in dic2.items():
    if value in valores_comuns:
        dicIguais[key] = value

"""Por sua vez, para preencher o dicionário dictDiferentes, é necessário implementar um loop for que itera sobre os itens de dict1 e verifica se o value não está presente em valores_comuns. Caso sim, o value é armazenado em dictDiferentes, utilizando a chave original de dic1."""
for key, value in dic1.items():
    if value not in valores_comuns:
        dicDiferentes[key] = value

"""A mesma lógica do loop for anterior foi implementada para iterar sobre os valores exclusivos de dic2, e assim, armazená-los em difDiferentes, utilizando as chaves originais de dic2"""
for key, value in dic2.items():
    if value not in valores_comuns:
        dicDiferentes[key] = value

print("dicIguais =", dicIguais)
print("dicDiferentes =", dicDiferentes)
