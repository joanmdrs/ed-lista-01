""" 
Este programa recebe como entrada uma lista de números. 

Após isso, é criado o conjunto (alunos_presentes) que será utilizado para armazenar os números dos alunos presentes.

Para preencher o conjunto de alunos_presentes, foi usado um loop for que itera sobre a lista de entrada. A cada iteração, um elemento é adicionado ao conjunto. 

Como a estrutura de conjunto não permite elementos repetidos, o mesmo irá realizar a inserção de números que já existem no conjunto. 

Por fim, é exibido a quantidade de alunos presentes.  
"""

lista_registro = [3,2,3,1]

alunos_presentes = set()

for i in range(len(lista_registro)):
    alunos_presentes.add(lista_registro[i])
    
print(len(alunos_presentes))
