

# PROGRAMA PRINCIPAL
valor_total = 0

print("Seja bem-vindo!!")
print("Sistema desenvolvido por Miguel José Rodrigues de Oliveira.\n")

# MENU DA PIZZARIA =========================================
print("+", "=" * 47, "+")
print("|", "=" * 14, "PIZZARIA OLIVEIRA", "=" * 14, "|")
print("+", "=" * 47, "+")
print("| Tamanho |  Pizza Salgada (PS) | PIZZA DOCE (PD) |")
print("|    P    |       R$ 30.00      |     R$ 34.00    |")
print("|    M    |       R$ 45.00      |     R$ 48.00    |")
print("|    G    |       R$ 60.00      |     R$ 66.00    |")
print("+", "=" * 47, "+")
# ==========================================================

while True: #  Vou deixar em loop até digitar N

    # ESCOLHER SABOR E TAMANHO ==============================
    # Escolher sabor
    sabor = input("\nDigite o sabor desejado (PS/PD): ")
    sabor = sabor.upper() # Garantir que esteja em maúsculo
    if sabor != "PS" and sabor != "PD":
        # Digitando errado, volta para o início
        print("Sabor inválido. Tente novamente.")
        continue

    # Escolher o tamanho
    tamanho = input("Digite o tamanho desejado (P/M/G): ")
    tamanho = tamanho.upper()
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        # Digitando errado, volta para o início
        print("Tamanho inválido. Tente novamente.")
        continue
    # ========================================================

    # CALCULAR O VALOR DA PIZZA ==============================
    if sabor == "PS":
        if tamanho == "P":
            preco = 30
        elif tamanho == "M":
            preco = 45
        else:
            preco = 60
        print(f"Você selecionou uma Pizza Salgada no tamanho {tamanho}: R$ {preco:.2f}")
    else:
        if tamanho == "P":
            preco = 34
        elif tamanho == "M":
            preco = 48
        else:
            preco = 66.0
        print(f"Você selecionou uma Pizza Doce no tamanho {tamanho}: R$ {preco:.2f}")
    # ========================================================

    # ACUMALAR O VALOR TOTAL =================================
    valor_total += preco
    # ========================================================

    # COMPRAR MAIS PIZZA, SIM OU NÃO =========================
    resp = input("\nDeseja mais alguma coisa? (S/N): ")
    resp = resp.upper()

    # Verificar se foi digitado S ou N
    if resp != "S" and resp != "N":
        while True:
            print("Digite S ou N...")
            resp = input("Deseja mais alguma coisa? (S/N): ")
            resp = resp.upper()

            # Quando digitar o certo, ele sai desse loop
            if resp == "S" or resp == "N":
                break

    # Lugar onde vai decidir se volta para o início ou se finaliza
    elif resp == "S":
        continue
    elif resp == "N": # Finaliza o loop
        break
    # ========================================================

# VALOR TOTAL A SER PAGO =================================
print() # Dar um espaço para ficar mais organizado
print("+", "=" * 47, "+")
print(" " * 6, f"Valor total a ser pago: R$ {valor_total:.2f}")
print("+", "=" * 47, "+")
# ========================================================

print("\nEncerrando...")
input()