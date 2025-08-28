def descontar_valor(valor_aposta):
    global saldo
    if saldo >= valor_aposta:
        saldo -= valor_aposta
        print(f"R$ {valor_aposta:.2f} descontado da aposta.")
        return True
    else:
        print("Saldo insuficiente para apostar R$ {:.2f}!".format(valor_aposta))
        return False 
