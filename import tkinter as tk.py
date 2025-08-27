import random

def gerar_raspadinha():
    premios = ["Nada :(", "Nada :(", "R$25", "Nada :(", "Nada :(", "R$5", "R$200"]
    numero = random.randint(1, 100)
    premios_raspadinha = random.sample(premios, 3)
    premio_revelado = random.choice(premios_raspadinha)

    print(" Raspadinha ".center(40, "-"))
    print(f"Número da Raspadinha: {numero}")
    print("Prêmios:")
    for premio in premios_raspadinha:
        print(f"- {premio}")
    print("Raspe e Descubra:")
    print("_______")

    # Pergunta se o usuário quer raspar para revelar o prêmio
    resposta = input("Quer raspar esta raspadinha? (s/n) ").strip().lower()
    if resposta == 's':
        print(f"Você ganhou: {premio_revelado}!")
    else:
        print("Raspadinha não raspada.")

def main():
    while True:
        gerar_raspadinha()
        resposta = input("Quer raspar outra raspadinha? (s/n) ").strip().lower()
        if resposta != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    main()

