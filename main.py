import inserir_credito
import print_saldo
import result_
import checkwin
import descontar_valor

#Insert coins

def insert_coin(saldo):
    while True:
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
                    print("Operação realizada com sucesso")
                else:
                    print("Operação Cancelada")
            else:
                print("Opção inválida, tente novamente.")

        except ValueError:
            print("Entrada inválida. Digite apenas numeros, de 1 a 5.")
        saldo = insert_coin(saldo)

#imprime raspadinha
def print_rasp(saldo):
    print("\n==== SUA RASPADINHA ====")
    print("[ ? ] [ ? ] [ ? ]")  # representando os 3 espaços da raspadinha
    print(f"Créditos atuais: R$ {saldo:.2f}")
    print("========================\n")

#gerar raspadinha
def gerar_raspadinha(saldo):
    import random
    premios = ["Nada :(", "Nada :(", "R$25", "Nada :(", "Nada :(", "R$5", "R$200"]
    numero = random.randint(1, 100)
    premios_raspadinha = random.sample(premios, 3)
    premio_revelado = random.choice(premios_raspadinha)

    print(" Raspadinha ".center(40, "-"))
    print(f"Número da Raspadinha: {numero}")
    print("Prêmios:")
    for premio in premios_raspadinha:
        print(f"- {premio}")
    print("Raspe e Descubra: [ ? ] [ ? ] [ ? ]")

    # Pergunta se o usuário quer raspar para revelar o prêmio
    resposta = input("Quer raspar esta raspadinha? (s/n) ").strip().lower()
    if resposta == 's':
        print(f"Você ganhou: {premio_revelado}!")
    else:
        print("Raspadinha não raspada.")


def main():
    saldo = 0
    saldo = insert_coin
    resposta = input("Quer jogar outra raspadinha? (s/n)")

    while True:
        gerar_raspadinha()
        resposta = input("Quer raspar outra raspadinha? (s/n) ").strip().lower()
        if resposta != 's':
            print(f"\nObrigado por jogar! Seu saldo final: R$ {saldo:.2f}")
            break
if __name__ == "__main__":
    main()