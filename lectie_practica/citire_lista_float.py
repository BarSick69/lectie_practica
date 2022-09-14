lista1 = []
def creare_lista():
    lista=[]
    lungime =int(input("dati lungimea listei: "))
    for i in range(lungime):
        elem = eval(input("Elementul "+str(i+1)+" : "))   
        lista.append(float(elem))
    return lista
lista1 = creare_lista()
print(lista1)