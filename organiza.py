def indice_maximo(lst: list[int]) -> int:
    assert len(lst) != 0
    imax = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[imax]:
            imax = i
    return imax

def organiza_em_ordem(lista: list[int]):
    
    j = len(lista)
    while j>1:
        imax = indice_maximo(lista[:j])
        aux = lista[imax]
        lista[imax] = lista[j -1]
        lista[j -1] = aux
        j = j - 1
    return lista
