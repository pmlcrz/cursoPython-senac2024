from datetime import datetime
import json

class Tarefa:
    def __init__(self, descricao, data_vencimento=None):
        self.descricao = descricao
        self.concluida = False
        self.data_vencimento = datetime.strptime(data_vencimento, "%Y-%m-%d") if data_vencimento else None

    def marcar_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        data_vencimento = self.data_vencimento.strftime("%Y-%m-%d") if self.data_vencimento else "Sem data"
        return f"{self.descricao} - {status} - Vencimento: {data_vencimento}"

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao, data_vencimento=None):
        tarefa = Tarefa(descricao, data_vencimento)
        self.tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    def listar_tarefas(self, status=None):
        tarefas_filtradas = [tarefa for tarefa in self.tarefas if (status is None or tarefa.concluida == (status == 'concluida'))]
        if not tarefas_filtradas:
            print("Nenhuma tarefa para exibir.")
        else:
            tarefas_filtradas.sort(key=lambda x: x.data_vencimento or datetime.max)
            for i, tarefa in enumerate(tarefas_filtradas, start=1):
                print(f"{i}. {tarefa}")

    def marcar_tarefa_concluida(self, indice):
        if 0 < indice <= len(self.tarefas):
            tarefa = self.tarefas[indice - 1]
            tarefa.marcar_concluida()
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido.")

    def remover_tarefa(self, indice):
        if 0 < indice <= len(self.tarefas):
            tarefa_removida = self.tarefas.pop(indice - 1)
            print(f"Tarefa '{tarefa_removida.descricao}' removida com sucesso!")
        else:
            print("Índice inválido.")

    def salvar_tarefas(self, arquivo):
        with open(arquivo, 'w') as f:
            json.dump([{
                'descricao': tarefa.descricao,
                'concluida': tarefa.concluida,
                'data_vencimento': tarefa.data_vencimento.strftime("%Y-%m-%d") if tarefa.data_vencimento else None
            } for tarefa in self.tarefas], f)
        print("Tarefas salvas com sucesso!")

    def carregar_tarefas(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                tarefas_dados = json.load(f)
                self.tarefas = [Tarefa(tarefa['descricao'], tarefa['data_vencimento']) for tarefa in tarefas_dados]
                for tarefa, dado in zip(self.tarefas, tarefas_dados):
                    tarefa.concluida = dado['concluida']
            print("Tarefas carregadas com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo.")

def menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Salvar Tarefas")
    print("6. Carregar Tarefas")
    print("7. Sair")

def main():
    gerenciador = GerenciadorDeTarefas()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            descricao = input("Descrição da tarefa: ")
            data_vencimento = input("Data de vencimento (YYYY-MM-DD) ou deixe em branco: ")
            gerenciador.adicionar_tarefa(descricao, data_vencimento)
        elif opcao == '2':
            status = input("Filtrar por status (pendente/concluida) ou deixe em branco: ")
            gerenciador.listar_tarefas(status=status.lower() if status else None)
        elif opcao == '3':
            gerenciador.listar_tarefas()
            indice = int(input("Número da tarefa a ser marcada como concluída: "))
            gerenciador.marcar_tarefa_concluida(indice)
        elif opcao == '4':
            gerenciador.listar_tarefas()
            indice = int(input("Número da tarefa a ser removida: "))
            gerenciador.remover_tarefa(indice)
        elif opcao == '5':
            arquivo = input("Nome do arquivo para salvar as tarefas: ")
            gerenciador.salvar_tarefas(arquivo)
        elif opcao == '6':
            arquivo = input("Nome do arquivo para carregar as tarefas: ")
            gerenciador.carregar_tarefas(arquivo)
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
