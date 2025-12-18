# FUNÇÕES EXTRA COM INTUITO DE DEIXAR O AMBIENTE MAIS BONITO E MAIS PRÁTICO DE MONTAR
def menu_borda(mensagem):
    tam_total = 70
    # Defini a largura das mensagens
    tam_msg = len(mensagem)
    # Usei só para organizar o pensamento e pegar o valor de maneira mais fácil

    resto = tam_msg % 2
    # Valor do resto da divisão para eu conseguir saber se o tamanho da mensagem é ímpar ou par
    # Se for ímpar, vai subtrair menos de um dos lados para alinhar com as outras mensagens

    # Cálculo para saber a posição central
    # Eu vou pegar o tamanho total e dividir por 2, depois o tamanho da mensagem e dividir por 2
    # Assim eu vou saber o tamanho de um lado, subtraindo com o tamanho da mensagem, eu vou ter
    # o número exato de quantos "=" eu vou usar, depois eu subtraio - 2 que é equivalente aos "+" nas pontas
    tam_metade_msg = int(tam_total/2) - 2 - int(tam_msg / 2)

    print("\n+", "=" * (tam_total - 2), "+")
    if resto == 1:
        # Aqui vai subtrair - 1 do lado esquerdo para alinhar :)
        print("|", "=" * (tam_metade_msg - 1), mensagem, "=" * tam_metade_msg, "|")
    else:
        print("|", "=" * tam_metade_msg, mensagem, "=" * tam_metade_msg, "|")
    print("+", "=" * (tam_total - 2), "+")

def mensagem_borda(mensagem):
    tam_total = 70 # Largura do conteúdo
    tam_msg = len(mensagem) # Tamanho da mensagem

    tam_espacamento = tam_total - tam_msg - 3 # Quantos espaços vão ser necessários

    print("|", mensagem, " " * tam_espacamento, "|")
    # Aqui é a mensagem menos a quantidade de espaço
    # Já que não precisa centralizar, fica mais simples

# ==========================================================================================


# FUNÇÃO PARA O MENU PRINCIPAL
def menu_principal():

    menu_borda("MENU PRINCIPAL")
    mensagem_borda("Escolha a opção desejada:")
    mensagem_borda("[1] Cadastrar Contato")
    mensagem_borda("[2] Consultar Contato(s)")
    mensagem_borda("[3] Remover Contato")
    mensagem_borda("[4] Sair")
    print("+", "=" * 68, "+")

    while True:
        try:
            op = int(input(">> "))

            match op:
                case 1:
                    cadastrar_contato(id_global)
                case 2:
                    consultar_contatos()
                case 3:
                    remover_contato()
                case 4:
                    print("Encerrando...")
                case _:
                    print("[ERRO] Digite uma opção válida!")
                    continue
            break
        except ValueError:
            print("[ERRO] Opção inválida, tente novamente!")

# FUNÇÃO CADASTRAR
def cadastrar_contato(identificacao):
    global qtd_contatos
    id_novo = identificacao + qtd_contatos

    menu_borda("MENU CADASTRAR CONTATOS")
    print(f"| Id do Contato: {id_novo}")
    nome = input("| Digite o nome do Contato: ")
    atividade = input("| Digite o atividade do Contato: ")
    telefone = input("| Digite o telefone do Contato: ")
    print("+", "=" * 68, "+")

    print(id_novo)

    contato = {
        "Id": id_novo,
        "Nome": nome,
        "Atividade": atividade,
        "Telefone": telefone
    }
    qtd_contatos += 1

    # Adicionando o dicionário na Lista
    lista_contatos.append(contato.copy())

    menu_principal()

# FUNÇÃO PARA CONSULTAR
def consultar_contatos():


    while True:
        menu_borda("MENU CONSULTAR CONTATOS")
        mensagem_borda("Digite uma opção")
        mensagem_borda("[1] Consultar todos os Contatos")
        mensagem_borda("[2] Consultar Contato por id")
        mensagem_borda("[3] Consultar Contato(s) por Atividade")
        mensagem_borda("[4] Retornar")
        print("+", "=" * 68, "+")
        try:
            op_consulta = int(input(">> "))

            match op_consulta:
                case 1:
                    print("\nLista de Contatos: ")
                    for contato in lista_contatos:
                        print("+", "=" * 68, "+")
                        for keys, values in contato.items():
                            print(f"{keys}: {values}")
                    continue
                case 2:
                    controle = False
                    # Me deu muito trabalho essa parte
                    # Ele vai procurar na lista o dicionario que tem id igual ao informado

                    id_informado = int(input("Digite o Id do Contato: "))
                    for contato in lista_contatos:
                        if contato["Id"] == id_informado:
                            controle = True
                            print("\nDetalhes do contato: ")
                            for keys, values in contato.items():
                                print(f"{keys}: {values}")
                            break
                        else:
                            controle = False
                    if controle == False:
                        print("Contato não encontrado!")
                    continue
                case 3:
                    controle = False
                    atividade = input("Informe a atividade do Contato: ")
                    for contato in lista_contatos:
                        print("+", "=" * 68, "+")
                        # Segue a mesma lógica do anterior mas procurando pela atividade
                        if contato["Atividade"] == atividade:
                            controle = True
                            for keys, values in contato.items():
                                print(f"{keys}: {values}")
                        else:
                            controle = False
                    if controle == False:
                        print("Contato não encontrado!")
                        continue
                case 4:
                    menu_principal()
                    break
                case _:
                    print("[ERRO] Opção inválida!")
        except ValueError:
            print("[ERRO] Opção inválida!")

# FUNÇÃO REMOVER CONTATO
def remover_contato():
    while True:
        try:
            id_removido = int(input("Digite o Id do Contato a ser removido: "))
            controle = False # Me ajudar na lógica do controle

            for contato in lista_contatos: # Aqui eu vou procurar pelo ID
                if contato["Id"] == id_removido:
                    controle = True
                    lista_contatos.remove(contato) # Achando ele remove
                    print("Contato removido com sucesso!")
                    menu_principal()
                else:
                    print("Não foi possível remover") # Caso não encontre
                    continue
            break
        except ValueError:
            print("Dado inválido!")

# PROGRAMA PRINCIPAL
lista_contatos = []
qtd_contatos = 0
id_global = 5294941

print("Seja bem-vindo!!")
print("Programa desenvolvido por Miguel José Rodrigues de Oliveira")
print("\nLista de contatos do Miguel Oliveira:")
menu_principal()

input()