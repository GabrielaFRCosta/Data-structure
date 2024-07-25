#você e sua equipe decidiram construir uma fila eterna de pessoas, com o seguinte comportamento:
#1 - Após uma eternidade, a primeira pessoa da fila é chamada;
#2 - Quando a pessoa finalmente sai da frente da fila, ela é redirecionada ao fim da fila;
#3 - Veja o passo 1.
#Dada a quantidade de "eternidades" passadas, indique as pessoas que estão no início e no fim da fila.
#A entrada consiste de uma linha com os nomes das pessoas (somente o primeiro nome) no estado atual da fila, separados por espaço. A seguir, é fornecida uma linha com um número inteiro não negativo X, representando o número de avanços que serão feitos na fila.
#A saída consiste do nome das pessoas que estão na frente e no fim da fila, depois de X avanços. Apresente-os, nessa ordem, um por linha, conforme os exemplos.

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

fila = []
q = Queue()
fila = input().split()
for pessoa in fila:
    q.enqueue(pessoa)
eternidade = int(input())
for i in range(eternidade):
    q.enqueue(q.dequeue())
fila = q.items
print(f'Pessoa da frente: {fila[-1]}')
print(f'Pessoa do fim: {fila[0]}')
