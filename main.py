

#criando funcoes
def printal_lista(lista):
    for elem in lista:
        print(elem)
def forca_opcao(lista,msg):
   printal_lista(lista)
   opcao = input('selecione uma da opçoes')
   while opcao not in lista:
        opcao =input(msg)
   return opcao



#criando menu
acoes=["cadastrar","consultar","deletar","sair"]
escolha= forca_opcao(acoes," opação invalida! opçao deve conter na lista ")


#criando objeto medicamento

indificao=int(input("codigo do medicamento"))
nome= input("digite o nome do medicamento")
validade=int(input("digitr a data de validade "))
fabricacao=(int(input("digite a data de fabricação")))

