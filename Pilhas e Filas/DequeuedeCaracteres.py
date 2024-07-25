# Uma letra significa a operação enqueue e um asterisco significa a operação dequeue
# Exemplo de uma instrução em filacetamol 
# >>> ola*** mundo
# ola

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

def filacetamol(frase):
    q = Queue()
    for e in frase:
        if e == '*':
            print(q.dequeue(), end='')
        else:
            q.enqueue(e)

frase = input()
filacetamol(frase)