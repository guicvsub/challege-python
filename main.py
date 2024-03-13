'''Gestão de Medicamentos: Manter um registro dos medicamentos prescritos aos pacientes, incluindo dosagem e horários
de administração.
'''
'requisitos'
''''Cadastro de Medicamentos: O sistema deve permitir cadastrar medicamentos com nome, dosagem e forma de administração.

Associação com Pacientes: Deve ser possível associar medicamentos a pacientes específicos.

Registro de Dosagem e Horários: O sistema deve permitir registrar a dosagem prescrita e os horários de administração de cada medicamento.

Notificações de Administração: O sistema deve enviar notificações aos pacientes sobre os horários de administração de cada medicamento.

Controle de Estoque: O sistema deve manter um controle de estoque dos medicamentos cadastrados.

Integração com Prontuário Eletrônico: Deve haver integração com o prontuário eletrônico dos pacientes.

Relatórios de Administração: O sistema deve gerar relatórios sobre a administração de medicamentos.

Registro de Reações Adversas: Deve ser possível registrar reações adversas aos medicamentos.

Segurança e Privacidade: O sistema deve garantir a segurança e privacidade das informações.

Acesso Restrito: O acesso às informações sobre medicamentos deve ser restrito a profissionais autorizados.'''



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

