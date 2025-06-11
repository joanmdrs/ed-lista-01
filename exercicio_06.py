class Aluno:
    def __init__(self, nome, nota_1, nota_2):
        self.nome = nome
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.media_final = self.calcular_media_final()
        
    def calcular_media_final(self):
        return (self.nota_1 + self.nota_2) / 2
    
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

def exibir_relatorio(alunos):
    print("\nRELATÓRIO DE NOTAS E MÉDIAS")
    print(f"{'Nome':<15}{'Nota 1':<10}{'Nota 2':<10}{'Média':<10}")
    for a in alunos:
        print(f"{a.nome:<15}{a.nota_1:<10}{a.nota_2:<10}{a.media_final:<10.2f}")

def main():
    quant_alunos = 3
    dados = cadastrar_notas(quant_alunos)
    exibir_relatorio(dados)

main()
        
        

    
    
    