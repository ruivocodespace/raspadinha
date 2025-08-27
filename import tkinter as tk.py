import random

def gerar_raspadinha():
    premios = ["R$10", "R$20", "R$50", "R$100", "Nada", "R$5", "R$200"]
    print(" Raspadinha ".center(40, "-"))
    print("Número da Raspadinha: ", random.randint(1, 100))
    print("Prêmios:")
    # Gerar 3 prêmios aleatórios para mostrar na raspadinha
    premios_raspadinha = random.sample(premios, 3)
    for premio in premios_raspadinha:
        print(f"- {premio}")
    print("Raspe e Descubra:")
    # O prêmio revelado (um dos três, aleatório)
    print(f"-> {random.choice(premios_raspadinha)}")
    print("_______")

def main():
    quantidade = int(input("Quantas raspadinhas você deseja gerar? "))
    for i in range(quantidade):
        gerar_raspadinha()
        print("\n")

if __name__ == "__main__":
    main()
