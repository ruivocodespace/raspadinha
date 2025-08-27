import random

def gerar_raspadinha():
    print(" Raspadinha ".center(40, "-"))
    print("Número da Raspadinha: ", random.randint(1, 100))
    print("Prêmios:")
    print("Raspe e Descubra:")
    print("_______")

def main():
    quantidade = int(input("Quantas raspadinhas você deseja gerar? "))
    for i in range(quantidade):
        gerar_raspadinha()
        print("\n")


    main()