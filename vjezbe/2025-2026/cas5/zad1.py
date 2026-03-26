import networkx as nx
import matplotlib.pyplot as plt

def graficki(arr):
    '''
    Provjerava da li je graficki niz arr.
    '''

    if len(arr) == 0:
        return True

    arr = sorted(arr, reverse=True)
    d1 = arr[0]

    if d1 >= len(arr):
        return False
    
    for i in range(1, d1+1):
        arr[i] -= 1

    arr = arr[1:]

    return graficki(arr)

def konstruisi_graf(arr):
    '''
    Konstruise graf ciji je niz stepena cvorova arr
    '''

    G = nx.graph()

    def build(arr):
        
        if len(arr) == 0:
            return True
        
        arr = sorted(arr, reverse=True)
        d1 = arr[0]

        if d1 >= len(arr):
            return False
        
        for i in range(1, d1+1):
            arr[i] -= 1

        arr = arr[1:]
        build(arr)

        #Dodati cvor stepena d1 i povezati ga sa dog. cvorovima    
        

    build(arr)
    return G

arr = input("Unesite elemente stepene cvorova u jednom redu odvojene razmakom: \n")
arr = arr.split(" ")
arr = [int(n) for n in arr]

print(graficki(arr))