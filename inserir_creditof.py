#Insert coins

def insert_coin(saldo):
    print("1- 2,00", "2- 5,00", "3- 10,00", "4- 15,00", "5- 20,00", sep="\n")
    coins = float(input("Quantos créditos você querer inserir?"))
    saldo += coins
    return saldo
saldo = 0

saldo = insert_coin(saldo)
print(saldo)
saldo = insert_coin(saldo)