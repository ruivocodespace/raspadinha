def checkwin(resultados):
    return resultados[0] == resultados[1] == resultados[2] # até aqui é a função, dai o resto é só para demosntrar que deu certo.
resultado = [3, 3, 3]

if checkwin(resultado):
    print("Ganhou!")
else:
    print("Perdeu!")