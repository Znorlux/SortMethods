def quick_sort(lista, info):
  # Caso Base
  base = len(lista)
  if base <= 1:
    return lista

  pivote = lista.pop(base // 2)  # Elegir el pivote en el medio
  lista1 = []
  lista2 = []

  for item in lista:
    if item[info]<= pivote[info]:
      lista1.append(item)
    else:
      lista2.append(item)

  lista1 = quick_sort(lista1, info)
  lista2 = quick_sort(lista2, info)

  return lista1 + [pivote] + lista2