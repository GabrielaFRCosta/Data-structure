# Calcule o tempo gasto para que todos os N veículos passem pelo posto de pesagem da rodovia. Os fiscais sempre começam a abordagem a partir do primeiro veículo. O fator de amostragem F determina quais veículos serão abordados. F = 1, todos os veículos são abordados, F = 2 os veículos são fiscalizados alternadamente, e assim por diante. Os veículos que possuem carga maior que a permitida e que são abordados, após a abordagem descartam 2kg e retornam ao final da fila de veículos. 
#Cada abordagem gasta um determinado tempo conforme as instruções:
#ti = 1; para veículos que não são abordados pelos fiscais
#ti = 5; veículos abordados e que estão dentro do peso limite
#ti- = 10; veículos abordados que ultrapassam o peso limite.


#Entrada
#A primeira linha da entrada contém três números inteiros separados por um espaço em branco 1≤N≤104, 1≤F≤100, 1≤P≤103 indicando a quantidade de veículos, o fator de amostragem e o limite de peso (em kg) da rodovia, respectivamente. A próxima linha contém N valores inteiros a1,...aN, em que cada 1≤ai≤103 está associado com o peso (em kg) do veículo i.

#Saída
#Imprima um valor inteiro associado ao tempo total para que todos os N veículos passem pelo posto de pesagem.

class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items == []:
            return True
        else:
            return self.items.pop()
    
    def size(self):
        return len(self.items)

pesos = []
qtd_veiculos, amostragem, limite_peso = map(int, input().split())
pesos = input().split()
q = Queue()
tempo = 0
for i in pesos:
    q.enqueue(int(i))
while not q.isEmpty():
    primeiro = int(q.dequeue())
    if primeiro <= limite_peso:
        tempo += 5
    else:
        primeiro -= 2
        q.enqueue(int(primeiro))
        tempo += 10
    if amostragem > 1:
        i = 1
        while True:
            if i == amostragem:
                break
            else:
                if not q.isEmpty():
                    q.dequeue()
                    tempo += 1
                    i += 1
                else:
                    break
   
print(tempo)
