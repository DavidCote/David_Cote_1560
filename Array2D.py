class Array2D:

    def __init__(self,rows,cols):
        self.__rows=rows
        self.__cols=cols
        self.__data=[]
        for r in range(self.__rows):
            tem=[]
            for c in range(self.__cols):
                tem.append(None)
            self.__data.append(tem)

    def to_string(self):
        for i in self.__data:
            print(i)

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def clearing(self,value):
        for r in range(self.__rows):
            for c in range(self.__cols):
                self.__data[r][c]=value

    def set_item(self,r,c,value):
        self.__data[r][c]=value

    def get_item(self,r,c):
        return self.__data[r][c]
'''
def main():
    a2d=Array2D(2,3)
    a2d.to_string()
    cols=a2d.get_num_cols()
    rows=a2d.get_num_rows()
    print(f"cols: {cols}, rows: {rows}")

    a2d.clearing(5)
    a2d.to_string()
    a2d.set_item(0,2,10)
    a2d.to_string()
    item=a2d.get_item(0,2)
    print(f"obtenido: {item}")

main()
'''


