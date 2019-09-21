'''
Juego de la vida
-del tipo zero-player
-1970 por John H Conway
-ejemplifica el, ascenso, caida y alternancia de seres vivos

Reglas:
1: Si una celula esta viva y tiene 2 o 3 vecinos vivos la celula sobrevive a la siguente generacion.
Los vecinos son las 8 celulas que la rodean inmediataente, tanto en vertical, horizontal y diagonal
2: Una celula que no tiene vecinos vivos o que tiene un solo vecino vivo muere por soledad para la
siguiente generacion
3: Una celula viva que tiene 4 o mas vecinos vivos, muere por sobrepoblacion para la siguiente generacion
4: Una celula muerta con exactamente 3 vecinos vivos, resulta en un nacimiento cuya vida empezara la siguiente generacion.
Todas las celulas muertas restantes se mantienen muertas para la siguiente generacion

Soportevida
soportevida(rows, cols)
get_num_rows()
get_num_cols()
configure(lsta, generaciones)
clear_cell(row,col)->matar
set_cell()->revivir/nacimiento
is_alive_cell()->esta vivo True o False
get_alive_neightbors(row,cell)
'''
from Array2D import *
'''
0-->celula muerta
1-->celula viva
'''
class SoporteVida:
    def __init__(self,rows,cols):
        self.__rows=rows
        self.__cols=cols
        self.__grid=Array2D(rows,cols)
        self.__grid.clearing(0)

    def to_string(self):
        self.__grid.to_string()

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def configure(self,inicial):
        '''
        inicial es una lista de la forma:
        inicial=[[1,2],[2,1],[2,2],[2,3],[3,3]]
        '''
        for cell in inicial:
            self.__grid.set_item(cell[0],cell[1],1)


    def clear(self):
        self.__grid.clearing(0)

    def clear_cell(self,row,col):
        self.__grid.set_item(row,col,0)

    def set_cell(self,row,col):
        self.__grid.set_item(row,col,1)

    def is_alive_cell(self,row,col):
        if(self.__grid.get_item(row,col)==1):
            return True
        else:
            return False

    def get_alive_neighbors(self,row,col):
        limites=self.__calcula_vecinos(row,col)
        vivos=0

        for r in range(limites[2],limites[3]+1,1):
            for c in range(limites[0],limites[1]+1,1):
                if self.__grid.get_item(r,c)==1:
                    vivos+=1
                if row==r and col== c:
                    if self.__grid.get_item(r,c)==1:
                        vivos-=1

        return vivos

    def __calcula_vecinos(self,ren,col):

        x_ini=col-1
        x_fin=col+1
        y_ini=ren-1
        y_fin=ren+1

        if col==0:
            x_ini=0
        if col==self.__cols-1:
            x_fin=self.__cols-1
        if ren==0:
            y_ini=0
        if ren==self.__rows-1:
            y_fin=self.__rows-1

        return [x_ini,x_fin,y_ini,y_fin]

    def aplica_reglas(self,r,c):
        i = r
        j = c
        ls_ne = []

        est = self.is_alive_cell(i, j)
        vecinos = self.get_alive_neighbors(i, j)

        if  est == True and vecinos <= 1:
            return None

        if est == True and 2 <= vecinos <= 3:
            ls_ne.append(i)
            ls_ne.append(j)
            return ls_ne

        if est == False and vecinos == 3:
            ls_ne.append(i)
            ls_ne.append(j)
            return ls_ne

        if est == True and vecinos >= 4:
            return None

def main():

    juego = SoporteVida(5,5)
    juego.configure([[1,2],[2,1],[2,2],[2,3]])
    ls_tem = []
    print("Inicial")
    juego.to_string()
    print('---------------')

    for gen in range(1,15):
        print(f"Generacion: {gen}")
        ls_tem = []

        for i in range(5):
            for j in range(5):
                celula = juego.aplica_reglas(i, j)
                if celula != None:
                    ls_tem.append(celula)

        juego.clear()
        juego.configure(ls_tem)
        juego.to_string()
        print('---------------')

main()