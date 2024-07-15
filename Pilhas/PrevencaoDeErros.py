# Implementação da função Peek:
#    def peek(self):
#        return self.items[len(self.items) - 1]
#Dada a implementação, é possível perceber que se o método peek for chamado em uma pilha sem elementos, um erro irá ocorrer. Dessa forma, sua tarefa é consertar os métodos que podem realizar consultas a sua estrutura e apresentar erros devido a inexistência de elementos.

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            return
        else:
            return self.items.pop()

    def peek(self):
        if self.items == []:
            return
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)
