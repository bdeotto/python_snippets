
def power_set(lista):
    """ Conjunto de todos los subconjuntos que pueden extraerse del
    conjunto 'lista'.
    """

    def subset(subset_id):
        # mask: subset_id como lista de potencias de dos
        mask=list(map(lambda item: subset_id & (1<<item),range(len(lista))))
        # indices: posiciones de elementos de 'lista' no nulas en mask
        indices=list(filter(lambda item: mask[item],range(len(lista))))

        return list(map(lambda ix:lista[ix],indices))

    return list(map(subset,range(1<<len(lista))))
