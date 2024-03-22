
from tabulate import tabulate
import datetime

data_hora_atual = datetime.datetime.now()
hora_atual  = data_hora_atual.strftime("%H:%M")
data_atual = data_hora_atual.date()

#base de dados
medicamentos = {
    "nome": ["Paracetamol", "Amoxicilina", "Omeprazol", "Dipirona", "Ibuprofeno"],
    "data fabricacao": ["2023-01-15", "2023-02-28", "2023-03-10", "2023-04-05", "2023-05-20"],
    "data validade": ["2025-01-15", "2025-02-28", "2025-03-10", "2025-04-05", "2025-05-20"],
    "quantidade": [50, 30, 20, 40, 60],
    "preco unitario": [10.50, 20.00, 15.75, 5.90, 8.25],
    "fabricante": ["Farmax", "Generico", "Medley", "Neo Química", "EMS"]
}

#criando funcoes
def set_senha():
    nome = "administrador"
    usuario = input("digite seu usuario")
    senha = input("digite sua senha")
    while senha!="adm" or usuario!="adm":
        print("usuario ou senha invalidos")
        print("tente novamente")
        usuario = input("digite seu usuario")
        senha = input("digite sua senha")
    print(f"seja bem vinddo: {nome}")
    return nome

def cadastrar(medicamentos):
    novo_medicamento = {}
    for key in medicamentos.keys():
        info = input(f'Diga o {key} do novo medicamento: ')
        novo_medicamento[key] = info
        medicamentos[key].append(info)
    return novo_medicamento

def printa_chave_valor(dicionario):
    """Imprime as chaves e valores de um dicionário."""
    for chave in dicionario:
        valor = dicionario[chave]
        print(chave, " ", valor)
def forca_opcao(lista, msg):
    printa_chave_valor(lista)
    opcao = input('Selecione uma das opções: ')
    while opcao not in [str(chave) for chave in lista]:
        opcao = input(msg)
    return opcao



def parar_execução(continuar):
    while continuar != "n" and continuar != "s":
        print("comando invalido")
        continuar = input("Deseja continuar? (s/n): ")
    if continuar == "n":
        print("fechando programa")
        return "stop"
    return "continue"
def acha_

log = set_senha()



while True:



    acoes = {"1": "cadastrar", "2": "consultar", "3": "deletar", "4": "sair"}



    escolha = forca_opcao(acoes, "opçao invalida!")
    if escolha== "1":
        print(f"voce escolheu {acoes[escolha]}")
        new= cadastrar(medicamentos)
        print("cadastro com efetuado com sucesso ")
        print(f"o usuario: {log} cadastrou um novo medicamento chamado {new['nome']} em {data_atual} as {hora_atual}")
        continuar = input("Deseja continuar? (s/n): ")
        resultado = parar_execução(continuar)
        if resultado=="stop":
            break

    elif escolha =="2":
        print(tabulate(medicamentos, headers="firstrow", tablefmt="grid"))
        print(f'o usuario {log} acessou o sistema em {data_atual} as {hora_atual}')
        continuar = input("Deseja continuar? (s/n): ")
        resultado = parar_execução(continuar)
        if resultado == "stop":
            break



    elif escolha == "4":
        break
