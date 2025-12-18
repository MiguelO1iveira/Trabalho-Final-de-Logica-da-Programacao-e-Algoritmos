# FUNÇÃO PARA COLOCAR BORDA NAS MENSAGENS
def borda(mensagem):
    print("+", "=" * len(mensagem), "+")
    print("|", mensagem, "|")
    print("+", "=" * len(mensagem), "+")

# FUNÇÃO PARA ESCOLHER O TIPO DA MADEIRA
def escolha_tipo():
    preco = 0.0

    while True:
        print("\nEntre com o tipo de madeira desejado")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")
        resp = input(">> ")
        # Serve para garantir que o utilizador ao digitar certo, mesmo em minúsculo, o Sistema funcione
        resp = resp.upper()

        if resp == "PIN":
            preco = 150.40
        elif resp == "PER":
            preco = 170.20
        elif resp == "MOG":
            preco = 190.90
        elif resp == "IPE":
            preco = 210.10
        elif resp == "IMB":
            preco = 220.70
        else: # Caso digite algo diferente
            print("[ERRO] Tipo inexistente, entre com o modelo novamente!")
            continue
        break
    return preco

# FUNÇÃO PARA SABER A QUANTIDADE DE TORAS
def qtd_toras():
    desc = 0.0

    while True:
        try:
            quant_toras = int(input("\nDigite a quantidade de toras (m³): "))
            if quant_toras <= 0: # Garantir que não seja digitado números negativos
                print("Por favor, digite um valor maior que zero!")
                continue
            elif quant_toras < 100:
                desc = 0
            elif quant_toras < 500:
                desc = 4/100
            elif quant_toras < 1000:
                desc = 9/100
            elif quant_toras <= 2000:
                desc = 16/100
            else:
                # Caso o pedido seja maior que 2000
                print("Não aceitamos pedidos com essa quantidade de toras.")
                print("Por favor, entre com a quantidade novamente!")
                continue
            break
        except ValueError:
            # Caso o utilizador digite String
            print("Quantidade inválida, tente novamente.")
    return quant_toras, desc

# FUNÇÃO PARA ESCOLHER O MEIO DE TRANSPORTE
def transporte():
    preco_transp = 0.0

    while True:
        try:
            print("\nSelecione o tipo de transporte: ")
            print("[1] Transporte Rodoviário  - R$ 1000.00")
            print("[2] Transporte Ferroviário - R$ 2000.00")
            print("[3] Transporte Hidroviário - R$ 2500.00")
            op = int(input(">> "))

            # Estrutura de escolha para definir qual vai ser o valor retornado
            match op:
                case 1:
                    preco_transp = 1000.00
                case 2:
                    preco_transp = 2000.00
                case 3:
                    preco_transp = 2500.00
                case _:
                    print("[ERRO] Opção invalida, tente novamente!")
                    continue
            break
        except ValueError:
            print("[ERRO] Digite uma opção válida!")

    return preco_transp




# PROGRAMA PRINCIPAL
print("Seja bem-vindo!!")
print("Projeto desenvolvido por Miguel José Rodrigues de Oliveira\n")

#
borda("MADEIREIRA DO MIGUEL OLIVEIRA")

# Lugar onde as variáveis que vou utilizar recebem os valores das funções
tipoMadeira = escolha_tipo()
qtdToras, desconto = qtd_toras()
transporte = transporte()

# CÁLCULO DO VALOR FINAL A SER PAGO
total = ((tipoMadeira * qtdToras) * (1 - desconto)) + transporte

print()
borda(f"Total: {total:.2f}")

print("\nEncerrando...")
input()
