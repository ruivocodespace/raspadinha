
import random

def insert_coin(saldo):
    while True:
        try:
            print("Escolha uma opção de crédito:")
            print("1- 2,00", "2- 5,00", "3- 10,00", "4- 15,00", "5- 50,00", sep="\n")
            opcao = int(input("Digite o número da opção desejada: "))

            valores = {1: 2, 2: 5, 3: 10, 4: 15, 5: 50}
            if opcao in valores:
                coins = valores[opcao]
                confirmar = input(f"Confirmar R${coins:.2f}? (S/N): ").strip().upper()
                if confirmar == "S":
                    saldo += coins
                    print(f"💰 Crédito adicionado! Novo saldo: R$ {saldo:.2f}")
                    return saldo
                else:
                    print("Operação Cancelada")
            else:
                print("⚠️ Opção inválida, tente novamente.")

        except ValueError:
            print("⚠️ Entrada inválida. Digite apenas números, de 1 a 5.")

def gerar_raspadinha():
    # sorteia 3 números de 1 a 3
    numeros = [random.randint(1,3) for _ in range(3)]
    numero = random.randint(1, 9999)  # número identificador da raspadinha

    print()   
    print(" Raspadinha ".center(40, "-"))
    print(f"Número da Raspadinha: {numero}")
    print("[ ? ] [ ? ] [ ? ]")  # oculto até raspar
    print(f"Créditos atuais: R$ {saldo:.2f}")
    print("========================\n")

    return numeros

def descontar_valor(valor_aposta):
    global saldo
    if saldo >= valor_aposta:
        saldo -= valor_aposta
        print(f"R$ {valor_aposta:.2f} descontado da aposta.")
        return True
    else:
        print(f"Saldo insuficiente para apostar. Valor da aposta R$ {valor_aposta:.2f}!")
        saldo_novo = insert_coin(saldo)
        if saldo_novo > saldo:  # só atualiza se realmente entrou crédito
            saldo = saldo_novo
            return descontar_valor(valor_aposta)  # tenta novamente após inserir
        return False

def calcular_premio(resultados):
    contador = 0
    # define prêmios para combinações iguais
    premios = {1: 5, 2: 20, 3: 100}
    contador += 1
    if resultados[0] == resultados[1] == resultados[2]:
        contador = 0
        return premios[resultados[0]]
    if contador > 4:
        resultados[0] == resultados[0] == resultados[0]
        return premios[resultados[0]]
        
    return 0

def main():
    global saldo
    saldo = 0.0  # saldo inicial do jogador
    valor_aposta = 10.0  # custo fixo da raspadinha

    while True:
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        if not descontar_valor(valor_aposta):
            break  # sai se não tiver saldo suficiente

        resultados = gerar_raspadinha()
        
        #loop para garantir resposta válida
        while True:
            resposta = input("Quer raspar esta raspadinha? (s/n) ").strip().lower()
            if resposta in ('s', 'n'):
                break
            print("⚠ Digite uma resposta válida (s/n).")

        if resposta == 's':
            print("🎉 Resultado da raspadinha:")
            print(f"[ {resultados[0]} ] [ {resultados[1]} ] [ {resultados[2]} ]")
            ganho = calcular_premio(resultados)
            if ganho > 0:
                saldo += ganho
                print(f"➡ Você ganhou R${ganho:.2f}!")
                print(f"Saldo atual R${saldo:.2f}")
            else:
                print("➡ Nada :(")
        else:
            print("Raspadinha não raspada.")
                
            

if __name__ == "__main__":

    main() 

