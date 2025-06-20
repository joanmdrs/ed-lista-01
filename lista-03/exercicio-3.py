"""
Este programa recebe como entrada uma lista de números, representando registros de presença de alunos.

Em seguida, é criado o conjunto alunos_presentes, que será utilizado para armazenar os números dos alunos presentes de forma única.

Para preencher esse conjunto, é utilizado um loop for que percorre a lista de registros. A cada iteração, o número do aluno é adicionado ao conjunto.

Como conjuntos não permitem elementos duplicados, qualquer número repetido na lista será automaticamente ignorado ao ser inserido.

Ao final, é exibida a quantidade total de alunos presentes, ou seja, a quantidade de elementos únicos no conjunto alunos_presentes.
"""

lista_registro = [1, 0, 5, 6, 0, 12, 25, 6, 2, 6, 5, 0, 25, 13, 2]

registro_unico = set()
registro_repetido = set()

for i in lista_registro:
    if i not in registro_unico:
        registro_unico.add(i)
    else:
        registro_repetido.add(i)

resultado = registro_unico - registro_repetido

print(len(resultado))
