

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



#criando objeto medicamento

indificao=int(input("codigo do medicamento"))
nome= input("digite o nome do medicamento")
validade=int(input("digitr a data de validade "))
fabricacao=(int(input("digite a data de fabricação")))

