import random
saldo = 0.0 #saldo inicial
derrotas_consecutivas = 0 #contador de derrotas
simbolos = ["⭐", "🍀", "💎"] #simbolos que podem aparecer ao raspar

#funcao inserir creditos
def insert_coin(saldo): 
    while True:
        try:
            print("Escolha uma opção de crédito:")
            print("1- 2,00", "2- 5,00", "3- 10,00", "4- 15,00", "5- 50,00", sep="\n")
            opcao = int(input("Digite o número da opção desejada: "))

            #depositos possiveis
            valores = {1: 2, 2: 5, 3: 10, 4: 15, 5: 50}

            #verifica se a entrada é válida
            if opcao in valores:
                coins = valores[opcao]
                #confirmação para dc créditos
                confirmar = input(f"Confirmar R${coins:.2f}? (S/N): ").strip().upper()
                if confirmar == "S":
                    #ajusta o saldo somando o crédito inserido ao saldo
                    saldo += coins
                    print(f"💰 Crédito adicionado! Novo saldo: R$ {saldo:.2f}")
                    return saldo #grava o valor do saldo 
                else:
                    print("Operação Cancelada")
            else:
                print("⚠️ Opção inválida, tente novamente.")

        except ValueError:
            print("⚠️ Entrada inválida. Digite apenas números, de 1 a 5.")

def gerar_raspadinha():
    global derrotas_consecutivas

    #se o jogador perder 4 vezes seguidas, a quinta raspada da a vitória para o jogador
    if derrotas_consecutivas >= 4:
        n = random.choice(["⭐", "🍀", "💎"])   #escolhe qual símbolo vai dar vitória
        numeros = [n, n, n]
        derrotas_consecutivas = 0
    else:
        numeros = [random.choice(simbolos) for _ in range(3)]
    #gera um numero aleatorio para a raspadinha
    numero = random.randint(1, 100) 

    #raspadinha
    print()
    print(" Raspadinha ".center(40, "-"))
    print(f"Número da Raspadinha: {numero}")
    print("[ ? ] [ ? ] [ ? ]")
    print(f"Créditos atuais: R$ {saldo:.2f}")
    print("========================\n")

    return numeros
#funcao para descontar o valor da aposta
def descontar_valor(valor_aposta):
    global saldo
    if saldo >= valor_aposta:
        saldo -= valor_aposta
        print(f"R$ {valor_aposta:.2f} descontado da aposta.")
        return True
    else:
        #se o saldo for menor ue o valor da aposta:
        print(f"Saldo insuficiente para apostar. Valor da aposta R$ {valor_aposta:.2f}!")
        saldo_novo = insert_coin(saldo)
        if saldo_novo > saldo:  # só atualiza se realmente entrou crédito
            saldo = saldo_novo
            return descontar_valor(valor_aposta)  # tenta novamente após inserir
        return False

def calcular_premio(resultados):
    global derrotas_consecutivas  #contador de derrotas
    premios = {"🍀": 10, "⭐": 50, "💎": 80}

    if resultados[0] == resultados[1] == resultados[2]:
        derrotas_consecutivas = 0  #caso o jogador ganhe as derrotas zeram
        return premios[resultados[0]]

    #incrementa se o jogador perder
    derrotas_consecutivas += 1
    return 0

def main():
    global saldo
    saldo = 0.0  #saldo inicial do jogador
    valor_aposta = 10.0  #custo fixo da raspadinha

    while True:
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        
        #opção para sair ou continuar no jogo
        escolha = input("Pressione ENTER para continuar ou digite 'q' para sair: ").strip().lower()
        if escolha == "q":
            print("👋 Obrigado por jogar! Até a próxima.")
            break

        resultados = gerar_raspadinha()
        
        #loop para garantir resposta válida
        while True:
            resposta = input("Quer raspar esta raspadinha? (s/n) ").strip().lower()
            if resposta in ('s', 'n'):
                break
            print("⚠ Digite uma resposta válida (s/n).")

        if resposta == 's':
            if not descontar_valor(valor_aposta):
                break
            #gera resultados aleatorios e imprime na tela
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

