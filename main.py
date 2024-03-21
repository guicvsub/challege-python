
from tabulate import tabulate
#base de dados
medicamentos = {
    "id":["nome","data_fabricacao","data_validade","quantidade","preco_unitario","fabricante"],

    "nome": ["Paracetamol", "Amoxicilina", "Omeprazol", "Dipirona", "Ibuprofeno"],
    "data_fabricacao": ["2023-01-15", "2023-02-28", "2023-03-10", "2023-04-05", "2023-05-20"],
    "data_validade": ["2025-01-15", "2025-02-28", "2025-03-10", "2025-04-05", "2025-05-20"],
    "quantidade": [50, 30, 20, 40, 60],
    "preco_unitario": [10.50, 20.00, 15.75, 5.90, 8.25],
    "fabricante": ["Farmax", "Generico", "Medley", "Neo Química", "EMS"]
}

#criando funcoes
def set_senha():#bug
    usuario = input("digite seu usuario")
    senha = input("digite sua senha")
    while senha!="adm"and usuario!="adm":
        print("usuario ou senha invalidos")
        print("tente novamente")
        usuario = input("digite seu usuario")
        senha = input("digite sua senha")



log = set_senha()

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

acoes = {"1": "cadastrar", "2": "consultar", "3": "deletar", "4": "sair"}

escolha = forca_opcao(acoes, "erro")
if escolha== "1":
    print(f"voce escoljeu {acoes[escolha]}")
    for key in medicamentos.keys():
        info = input(f'Diga o/a {key} do novo medicaneto: ')
        medicamentos[key].append(info)

if escolha =="2":
    print(tabulate(medicamentos, headers="firstrow", tablefmt="grid"))

#criando objeto medicamento



