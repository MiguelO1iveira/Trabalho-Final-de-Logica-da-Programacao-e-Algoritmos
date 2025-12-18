# PROGRAMA PRINCIPAL ===
# Mensagem de bem vindo
print("Seja bem vindo!\nSistema desenvolvido por Miguel José Rodrigues de Oliveira.\n")

# Início do aplicativo com uma aparência mais amigável
print("=== APP DE PLANO DE SAÚDE DA EMRESA X ===")

# Coleta dos dados
valorBase = float(input("Por favor, informe o valor base do plano: R$ "))
idade = int(input("Informe a idade do cliente: "))
while idade < 0: # Serve para impedir valores negativos
    print("[ERRO] Digite uma idade válida!")
    idade = int(input("Tente novamente, informe a idade do cliente: "))

# Calculando o valor do Plano...
if idade >= 0 and idade < 19:
    valorMensal = valorBase * (100 / 100)
elif idade < 29:
    valorMensal = valorBase * (150 / 100)
elif idade < 39:
    valorMensal = valorBase * (225 / 100)
elif idade < 49:
    valorMensal = valorBase * (240 / 100)
elif idade < 59:
    valorMensal = valorBase * (350 / 100)
else:
    valorMensal = valorBase * (600 / 100)

# Mostrando o valor final do plano
print("\n", "=" * 12, "RESULTADO FINAL", "=" * 12)
print(f'O valor mesal do plano é R$ {valorMensal:.2f}')
input()
