class Array:
    def __init__(self,size):
        self.__size=size
        self.__data=[]
        for infex in range(size):
            self.__data.append(None)

    def legnght(self):
        return self.__size

    def get_Item(self,index):

        if index>=0 and index<self.__size:
            return self.__data[index]
        else:
            return None #index no valido

    def set_Item(self,index,valor):

        if index>=0 and index<self.__size:
            self.__data[index]=valor
        else:
            print("Valor fuera de rango")

    def clearing(self,valor):
        for i in range(self.__size):
            self.__data[i]=valor

    def to_string(self):
        print(self.__data)
'''
def main():
    adt=Array(10)
    adt.to_string()
    print(f"El tamaño del arreglo es: {adt.legnght()}")
    adt.set_Item(4,34)
    adt.to_string()
    print(f"El elemento 4 es: {adt.get_Item(4)}")
    adt.clearing(10)
    adt.to_string()

    adt.set_Item(14,10)
    adt.get_Item(12)
    adt.to_string()

main()
'''
