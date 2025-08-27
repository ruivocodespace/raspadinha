import random

def numbers():
    jogar = True
    contador = 0

    while jogar:
        #sortear números
        valores = [random.randint(1, 3) for _ in range(3)]
        contador += 1

        print(valores)

        again = str(input("Jogar novamente? (S/N): ")).strip().upper()
        if again == "S":
            jogar = True
        else:
            jogar = False

    if contador >= 4:
        print("teste")

    return valores

result = numbers()
print("Último resultado:", result)
