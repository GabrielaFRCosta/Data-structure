#Programa para editar uma lista dinâmica de chaves. O programa recebe comandos que devem ser executados, em sequência, sobre a lista. Ao final do processamento das operações, exiba a lista. Considere como chaves válidas Inteiros positivos. As operações são as seguintes:
#I insere o valor v no início da lista
#F insere o valor v no final da lista
#P remove do final e imprime o valor removido
#D remove do início e imprime o valor removido
#X indica o final das operações e que a lista resultante deve ser impressa

class Deque:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def addFront(self, item):
        self.items.append(item)
        
    def addRear(self, item):
        self.items.insert(0, item)
        
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

deque = Deque()
while True:
    entrada = input()
    opc = str(entrada.split()[0]).upper()
    if opc == 'X':
        break
    else:
        if opc == 'I':
            valor = int(entrada.split()[1])
            deque.addFront(valor)
        elif opc == 'F':
            valor = int(entrada.split()[1])
            deque.addRear(valor)
        elif opc == 'P':
            print(deque.removeRear())
        else:
            print(deque.removeFront())
while not deque.isEmpty():
    print(deque.removeFront())
