
from tabulate import tabulate
#base de dados
medicamentos = [
    {"id": "id", "nome": "nome", "data_fabricacao": "data_fabricacao", "data_validade": "data_validade"},
        {"id": 1, "nome": "Paracetamol", "data_fabricacao": "2023-01-15", "data_validade": "2025-01-15"},
        {"id": 2, "nome": "Amoxicilina", "data_fabricacao": "2023-02-28", "data_validade": "2025-02-28"},
        {"id": 3, "nome": "Omeprazol", "data_fabricacao": "2023-03-10", "data_validade": "2025-03-10"},
        {"id": 4, "nome": "Dipirona", "data_fabricacao": "2023-04-05", "data_validade": "2025-04-05"},
        {"id": 5, "nome": "Ibuprofeno", "data_fabricacao": "2023-05-20", "data_validade": "2025-05-20"}
    ]


#criando funcoes
def set_senha():
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

acoes = {1: "cadastrar", 2: "consultar", 3: "deletar", 4: "sair"}



escolha = forca_opcao(acoes,"erro")
if escolha =="2":
    print(tabulate(medicamentos, headers="firstrow", tablefmt="grid"))

#criando objeto medicamento



acoes