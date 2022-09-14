from math import fabs
lista1 = []

def isfloat(a):
    try:
        float(a)
        return True
    except:
        return False


def creare_lista():
    lista=[]
    lungime =int(input("dati lungimea listei: "))
    for i in range(lungime):
        elem =input("Elementul "+str(i+1)+" : ")
        if elem == "exit":
            return 0
        while(isfloat(elem) == False):
            elem = input("Elementul "+str(i+1)+" : ")

        lista.append(float(elem))
    return lista
    
lista1 = creare_lista()
print(lista1)
