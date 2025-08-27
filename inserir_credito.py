#Insert coins

def insert_coin(saldo):
    try:
        print("Escolha uma opção de crédito:")
        print("1- 2,00", "2- 5,00", "3- 10,00", "4- 15,00", "5- 20,00", sep="\n")
        opcao = int(input("Digite o número da opção desejada: "))

        valores = {
        1: 2,
        2: 5,
        3: 10,
        4: 15,
        5: 20,
        }
        if opcao in valores:
            coins = valores[opcao]
            confirmar = input(f"Confirmar {coins:.2f}? (S/N): ").strip().upper()
            if confirmar == "S":
                saldo += coins
            else:
                print("Operação Cancelada")
        else:
            print("Operação realizada com sucesso")

    except ValueError:
        print("Entrada inválida. Digite apenas numeros, de 1 a 5.")
        saldo = insert_coin(saldo)
  
    return saldo

saldo = 0
saldo = insert_coin(saldo)
print(saldo)


    