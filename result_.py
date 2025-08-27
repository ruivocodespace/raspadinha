#Result
import random

def numbers():
    #sort numbers
    valores = [random.randint(1, 3) for _ in range(3)]
    return valores

result = numbers()
print(result)
