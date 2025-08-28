def gerar_raspadinha():
    premios = ["R$300", "R$25", "R$5", "R$200"]
    numero = random.randint(1, 100)
    premios_raspadinha = random.choices(premios, k=3)  # permite repetição
    print(" Raspadinha ".center(40, "-"))
    print(f"Número da Raspadinha: {numero}")
    print("Prêmios:")
    for premio in premios_raspadinha:
        print(f"- {premio}")
    print("[ ? ] [ ? ] [ ? ]")  #representando os 3 espaços da raspadinha
    print(f"Créditos atuais: R$ {saldo:.2f}")
    print("========================\n")

    return premios_raspadinha
