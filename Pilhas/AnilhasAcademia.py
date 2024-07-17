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

peso_total = removido = s.pop()
qtd = 1
print(f'Peso retirado: {removido}')
while peso_desejado != removido and not s.isEmpty():
    removido = s.pop()
    print(f'Peso retirado: {removido}')
    qtd += 1
    peso_total += removido
print(f'Anilhas retiradas: {qtd}')
print(f'Peso total movimentado: {peso_total}')
