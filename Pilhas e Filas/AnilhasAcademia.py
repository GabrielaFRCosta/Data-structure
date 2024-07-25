# A entrada do programa consiste de uma quantidade indeterminada de valores inteiros positivos distintos, um por linha e cada um representando o peso de uma anilha, na ordem em que foram empilhadas pelo último usuário. O último valor dessa sequência será 0, indicando que todas as anilhas já foram informadas. A seguir é fornecido o peso da anilha desejada, em uma linha.
# Apresente cada peso retirado, um por linha, e relate a quantidade de pesos retirados e o peso total movimentado.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
s = Stack()
while True:
    peso = int(input())
    if peso == 0:
        break
    else:
        s.push(peso)

peso_desejado = int(input())

soma_pesos = cont = 0
while not s.isEmpty():
    peso_retirado = s.pop()
    print(f'Peso retirado: {peso_retirado}')
    soma_pesos += peso_retirado
    cont += 1
    if peso_retirado == peso_desejado:   
        break

print(f'Anilhas retiradas: {cont}')
print(f'Peso total movimentado: {soma_pesos}')
