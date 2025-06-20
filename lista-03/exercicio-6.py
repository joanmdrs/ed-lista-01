nomes = { "Adeline": 10, "Emma": 1, "Zora ": 10, "Lily": 10, "Yoli": 10, "Brielle": 10, "Fiona": 2, "Ursula": 3, "Randalynn": 4, "Quinn": 6, "Juliana": 7, "Vivi": 7, "Nora": 7, "Kimber": 7, "Xenia": 7, "Winona": 7, "Crystal": 8, "Tianna": 8, "Merida": 8, "Delilah": 8, "Hendrix": 8, "Staci": 8, "Isabella": 9, "Phoenix": 9, "Georgia":9, "Orion": 9}

"""
Para resolver este exercício, foi definido um dicionário chamado novoDicionario, onde as chaves representam as notas (10, 9, 8, 7 e "menor que 7") e os valores são listas que armazenam os nomes dos alunos que obtiveram cada nota.
"""

novoDicionario = {
    10: [],
    9: [],
    8: [],
    7: [],
    "menor que 7": []
}


"""
Em seguida, é realizado um loop que percorre os itens do dicionário nomes. Nesse dicionário, a chave representa o nome do aluno e o valor representa a nota obtida.

De acordo com a nota, o nome do aluno é adicionado à lista correspondente no dicionário novoDicionario.
"""

for nome, nota in nomes.items():
    if nota == 10:
        novoDicionario[10].append(nome)
        
    elif nota == 9:
        novoDicionario[9].append(nome)
    elif nota == 8:
        novoDicionario[8].append(nome)
    elif nota == 7:
        novoDicionario[7].append(nome)
    else:
        novoDicionario["menor que 7"].append(nome)

"""
Por fim, outro loop percorre os itens de novoDicionario e imprime, para cada nota, a lista de alunos que obtiveram aquele resultado.
"""

for key, lista in novoDicionario.items():
    print(f"{key}: {lista}")
