class Nodo:
    def __init__(self, value, siguiente=None):
        self.data = value
        self.next = siguiente

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, value):
        self.data = value

    def set_next(self, value):
        self.next = value

# ADT linked list
class Linked_List:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self):
        return self.__head is None

    def get_size(self):
        return self.__size

    def get_tail(self):
        return self.__tail.get_data()

    def get_head(self):
        return self.__head.get_data()

    def append(self, value):
        temp = Nodo(value)
        if self.is_empty():
            self.__head = temp
            self.__tail = self.__head
        else:
            self.__tail.next = temp
            self.__tail = self.__tail.next
        self.__size += 1

    def transversal(self):
        cur_node = self.__head
        while cur_node.next != None:
            print(cur_node.data)
            cur_node = cur_node.next
        print(cur_node.data)

    def prepend(self, value):
        self.__head = Nodo(value, self.__head)
        self.__size += 1

    def Add_before(self, ref, value):
        if ref < 0 or ref > self.__size:
            raise Exception("Posicion fuera de rango")
        curr = self.__head
        n = Nodo(value)
        if ref == 0:
            self.prepend(value)
        else:
            for i in range(1, ref - 1):
                curr = curr.next
            tem, curr.next = curr.next, n
            n.next = tem
        self.__size += 1

    def Add_affter(self, ref, value):
        if ref < 0 or ref > self.__size:
            raise Exception("Posicion fuera de rango")
        curr = self.__head
        n = Nodo(value)
        if ref == 0:
            self.prepend(value)
        else:
            for i in range(1, ref):
                curr = curr.next
            tem, curr.next = curr.next, n
            n.next = tem
        self.__size += 1

    def remove(self, val):
        curr = self.__head
        ant = None
        flag = False
        while not flag:
            if curr.get_data() == val:
                flag = True
            else:
                ant = curr
                curr = curr.next
        if ant is None:
            self.__head = curr.next
        else:
            ant.next = curr.next
        self.__size -= 1

    def pop(self):
        new_tail = self.__head
        for i in range(1,self.__size-1):
            new_tail = new_tail.next
        old=self.__tail
        self.__tail, self.__tail.next = new_tail, None
        self.__size -= 1
        return old.get_data(), self.__tail.get_data()

def main():
    nl = Linked_List()
    nl.append(10)
    nl.append(26)
    nl.append(25)
    nl.append(25)
    nl.append(50)
    print(f"cabeza = {nl.get_head()}")
    print(f"cola = {nl.get_tail()}")
    print('---------------------')
    nl.prepend(12)
    print(f"nueva cabeza = {nl.get_head()}")
    print('---------------------')
    nl.transversal()
    print('---------------------')
    print(f"Tamaño = {nl.get_size()}")
    print('---------------------')
    nl.Add_affter(3, 15)
    nl.transversal()
    print('---------------------')
    nl.Add_before(3, 25)
    nl.transversal()
    print('---------------------')
    print(f"Tamaño = {nl.get_size()}")
    print('---------------------')
    nl.remove(25)
    nl.transversal()
    print('---------------------')
    print(f"Tamaño = {nl.get_size()}")
    print('---------------------')
    a,b=nl.pop()
    print(f"cola anterior= {a}, cola nueva = {b}")
    print('---------------------')
    nl.transversal()
    print('---------------------')
    print(f"Tamaño = {nl.get_size()}")


main()
