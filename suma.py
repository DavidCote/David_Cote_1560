def suma_lista(lista):

    suma=lista[0]
    if len(lista)==1:
        return suma
    else:
        return suma+suma_lista(lista[1:])

def main():
    l=[3,5,2,4]
    print(suma_lista(l))

main()