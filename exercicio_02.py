"""
Foi definida a classe Candidato, que possui um construtor responsável por inicializar as propriedades: nome, nota_conhecimento, nota_comunicacao e nota_final.
Ao instanciar um objeto da classe, o método calcular_nota_final é automaticamente chamado para calcular e armazenar a nota final do candidato.
"""
class Candidato:
    def __init__(self, nome, nota_conhecimento, nota_comunicacao):
        self.nome = nome
        self.nota_conhecimento = nota_conhecimento
        self.nota_comunicacao = nota_comunicacao
        self.nota_final = self.calcular_nota_final()

    """
    Realiza o cálculo das notas do candidato, atribuindo peso 6 para a nota de conhecimento e peso 4 para a nota de comunicação.
    """
    def calcular_nota_final(self):
        return 0.6 * self.nota_conhecimento + 0.4 * self.nota_comunicacao
    
    
"""
A função realizar_cadastro_dos_candidatos inicializa uma lista vazia e, em seguida, executa um loop for 10 vezes.
Em cada iteração, são solicitadas as informações de nome, nota de conhecimento e nota de comunicação do candidato.
Com esses dados, é criada uma instância da classe Candidato, que é então adicionada à lista.
Ao final do processo, a lista preenchida é retornada.
"""
def realizar_cadastro_dos_candidatos():
    
    lista_candidatos = []
    
    for i in range(10):
        print(f"Cadastrar candidato nº {i + 1}\n")
        nome = input("Nome: ")
        nota_conhecimento = float(input("Nota de conhecimento: "))
        nota_comunicacao = float(input("Nota de comunicação: "))
        
        obj_candidato = Candidato(nome, nota_conhecimento, nota_comunicacao)
        lista_candidatos.append(obj_candidato)
        
    return lista_candidatos


"""
O método ordenar_lista_de_candidatos tem como função realizar a ordenação de toda a lista de candidatos, considerando a nota final, e em caso de notas finais iguais, é verificado qual candidato possui a maior nota em comunicação como critério de desempate. 
Para realizar essa ordenação, foi utilizada uma estrutura com dois loops for aninhados. O primeiro for (índice i) percorre cada elemento da lista, enquanto o segundo for (índice j) percorre os elementos restantes à frente do índice i."""
def ordenar_lista_de_candidatos(candidatos):
    quant = len(candidatos)
    """
    Essa estrutura percorre todas as combinações possíveis de pares de candidatos. O índice i representa o candidato atual, e o índice j percorre todos os candidatos à frente de i. Isso permite comparar o candidato i com os demais que ainda não foram posicionados corretamente.
    """
    for i in range(quant):
        for j in range(i + 1, quant):
            """
            Se o candidato j possuir nota final maior que o candidato i, ele deve vir antes na lista. 
            Se as notas finais forem iguais, então o desempate é feito pela nota de comunicação, e o candidato com maior nota de comunicação também deve vir antes.
            """
            if (candidatos[j].nota_final > candidatos[i].nota_final) or (
                candidatos[j].nota_final == candidatos[i].nota_final and
                candidatos[j].nota_comunicacao > candidatos[i].nota_comunicacao):
                
                candidatos[i], candidatos[j] = candidatos[j], candidatos[i]
    return candidatos

"""
O método exibir_resultados tem como objetivo exibir o resultado final, exibindo a lista de candidatos já ordenada. Para isso, ele recebe a lista de candidatos, começando pela posição 0. A cada iteração, a variável posição é incrementada em 1 até finalizar a lista de candidatos.
""" 
def exibir_resultados(candidatos):
    print("\nRESULTADO DA SELEÇÃO")
    posicao = 0
    for c in candidatos:
        print(f"{posicao}. {c.nome} - Final: {c.nota_final:.2f} (Conhecimento: {c.nota_conhecimento}, Comunicação: {c.nota_comunicacao})")
        posicao += 1

"""
Por fim, a função main() é responsável por executar o fluxo principal da aplicação. 
Primeiro, chama a função realizar_cadastro_dos_candidatos, que retorna a lista de candidatos preenchida.
Em seguida, essa lista é ordenada com a função ordenar_lista_de_candidatos.
Por fim, os resultados são exibidos com a função exibir_resultados.
"""
def main():
    candidatos = realizar_cadastro_dos_candidatos()
    lista_candidatos_ordenada = ordenar_lista_de_candidatos(candidatos)
    exibir_resultados(lista_candidatos_ordenada)

if __name__ == "__main__":
    main()
                
        
              
    