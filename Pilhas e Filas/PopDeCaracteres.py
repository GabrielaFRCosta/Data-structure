#Imprima a sequência de caracteres retornados pelas operações de dequeue quando esta sequência de operações é realizada em uma fila de caracteres inicialmente vazia
# Uma letra significa a operação push e um asterisco significa a operação pop

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

def pilhacetamol(frase):
    s = Stack()
    for e in frase:
        if e == '*':
            print(s.pop(), end='')
        else:
            s.push(e)
    
frase = input()
pilhacetamol(frase)
