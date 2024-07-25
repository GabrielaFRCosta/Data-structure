# Entrada
# A entrada consiste no número de entradas e nas roupas em cima da cadeira na ordem em que foram inseridas. O formato é tipo cor x, onde tipo e cor são duas strings, e x é um inteiro em minutos de quanto tempo se demora para dobrar a roupa.

#Saída
# A saída consiste nas roupas já dentro da gaveta, na ordem em que foram inseridas, o total de roupas e o tempo total em minutos gasto para guardá-las, conforme os exemplos.

class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

s = Stack()  
roupa = [] 
n = int(input())
for i in range(n):
    peca = input()
    roupa = peca.split()
    s.push(roupa)

tempo = 0
qtd_roupas = s.size()
while not s.isEmpty():
    retirado = s.pop()
    print(f'Tipo: {retirado[0]}, Cor: {retirado[1]}')
    tempo += int(retirado[2])

print(f'Total de roupas: {qtd_roupas}')
print(f'Total de tempo: {tempo}')
