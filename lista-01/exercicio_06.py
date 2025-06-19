""" 
Para este exercício foi definido uma classe Aluno, que representa um modelo de um aluno. 

O método especial __init__ é o construtor da classe, que é chamado automaticamente quando um objeto Aluno é criado. Ele inicializa os atributos: nome, nota_1, nota_2, e também calcula a média final do aluno ao chamar o método calcular_media_final() e armazena esse valor no atributo media_final.
"""
class Aluno:
    def __init__(self, nome, nota_1, nota_2):
        self.nome = nome
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.media_final = self.calcular_media_final()
        
    def calcular_media_final(self):
        return (self.nota_1 + self.nota_2) / 2

"""
A função cadastrar_notas recebe como parâmetro a quantidade de alunos. 

Esta função define uma estrutura de lista para armazenar os objetos Aluno. 

Após isso, é executado um loop for que executa um trecho de código onde são solicitados o nome e as notas 1 e 2 do aluno em questão. Após o preenchimento das informações, é criado um objeto Aluno, passando as informações como parâmetro, e inserido o objeto Aluno na lista de alunos. Além disso, é exibido automaticamente a média final do aluno, calculada no momento de criação do objeto Aluno. 

Por fim, retorna a lista contendo todos os objetos Aluno cadastrados.
"""
def cadastrar_notas(quant_alunos):
    lista_alunos = []
    for i in range(quant_alunos):
        nome = input(f"Nome do(a) aluno(a) {i + 1}: ")
        nota_1 = float(input("Nota 1: "))
        nota_2 = float(input("Nota 2: "))
        
        aluno = Aluno(nome, nota_1, nota_2)
        lista_alunos.append(aluno)
        print(f"Média do(a) aluno(a) {nome}: {aluno.media_final}")
    
    return lista_alunos

""" 
A função exibir_relatorio recebe como parâmetro uma lista de objetos Aluno e imprime um relatório formatado na tela.

Primeiro, imprime um cabeçalho com os títulos das colunas (Nome, Nota 1, Nota 2 e Média.).

Depois, para cada aluno da lista, imprime as informações formatadas: nome, notas e média, alinhadas para facilitar a leitura. Para isso, foi usada um loop for. 

O formato <15 e <10 define o alinhamento e largura de cada coluna.

O formato .2f exibe a média com duas casas decimais.
"""
def exibir_relatorio(alunos):
    print("\nRELATÓRIO DE NOTAS E MÉDIAS")
    print(f"{'Nome':<15}{'Nota 1':<10}{'Nota 2':<10}{'Média':<10}")
    for a in alunos:
        print(f"{a.nome:<15}{a.nota_1:<10}{a.nota_2:<10}{a.media_final:<10.2f}")

""" 
A função main é o ponto de partida do programa, onde é definido que serão cadastrados 3 alunos.

Após isso, chama cadastrar_notas para obter os dados dos alunos e armazena a lista retornada em dados.

Por fim, chama exibir_relatorio para imprimir os dados formatados na tela.

"""
def main():
    quant_alunos = 3
    dados = cadastrar_notas(quant_alunos)
    exibir_relatorio(dados)

main()
        
        

    
    
    