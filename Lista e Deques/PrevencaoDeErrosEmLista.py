#A implementação de lista sem ordem definida (UnorderedList), apresentada no livro didático da disciplina, utiliza a abstração de nós para manter os elementos inseridos na estrutura. Por exemplo, a função add é responsável por adicionar um elemento a estrutura. 
#Já a função remove necessita de uma lógica mais elaborada, já que primeiro o elemento a ser removido precisa ser localizado, ao mesmo tempo em que não se perca a referência do nó anterior ao elemento a ser removido, que deverá ser ligado ao nó posterior ao elemento removido.
#Dada a implementação do livro, é possível perceber que se esse método for chamado para remover um elemento que não se encontra na estrutura, um erro irá ocorrer. Dessa forma, sua tarefa é, dada a implementação abaixo, consertar a função remove de forma a não incorrer em erros, caso o elemento a ser removido não se encontre na estrutura.

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()
            
        return lstr

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def remove(self,item):
        current = self.head
        previous = None
        while True:
            if current == None:
                return
            if current.getData() == item:
                break
            else:
                previous = current
                current = current.getNext()
 
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
