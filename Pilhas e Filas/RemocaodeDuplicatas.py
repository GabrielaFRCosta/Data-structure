# Na matemática, o parêntese representa a prioridade de resolução em uma expressão algébrica. Além dos parênteses, apesar de menos usuais, os símbolos de colchetes e chaves também podem ser utilizados para criar uma ordem de prioridade na resolução
#Para todos esses casos descritos, um fator em comum é que, se qualquer uma dessas representações de prioridades for duplicada em uma expressão, ela é insignificante. Exemplo: 5∗((1001+110)) é equivalente a 5∗(1001+110)
# Sua tarefa é, dada uma lista de expressões algébricas válidas, verificar se há algum símbolo de prioridade duplicado dentro de cada expressão.
# Entrada: A entrada é composta por várias linhas. A primeira linha possui um inteiro N(1≤N≤100) que indica o número de expressões a serem verificadas. A seguir, as próximas N linhas possuem, cada uma, um string E (de comprimento entre 4 e 1000, inclusive), sem espaços, que representa a expressão algébrica a ser analisada.
# Saída: Para cada expressão, a saída deve ser "A expressão possui duplicata.", se houver um símbolo de prioridade duplicado dentro da expressão ou "A expressão não possui duplicata." caso não haja um mesmo símbolo de prioridade duplicado dentro da expressão, de acordo com os exemplos.

class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

def duplicatas(expressao, a, f):
    s = Stack()
    for e in expressao:
        if e == a or e != f:
            s.push(e)
        else:
            if not s.isEmpty() and s.peek() != a:
                    while s.peek() != a:
                        s.pop()
                    s.pop()
            else:
                return False
            
    return True

n = int(input())
for i in range(n):
    expressao = input()
    if duplicatas(expressao, '(' , ')') and duplicatas(expressao, '[', ']') and duplicatas(expressao, '{', '}'):
        print('A expressão não possui duplicata.')
    else:
        print('A expressão possui duplicata.')
