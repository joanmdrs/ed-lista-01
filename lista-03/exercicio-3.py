lista_registro = [1, 0, 5, 6, 0, 12, 25, 6, 2, 6, 5, 0, 25, 13, 2]

registro_unico = set()
registro_repetido = set()

for i in lista_registro:
    if i not in registro_unico:
        registro_unico.add(i)
    else:
        registro_repetido.add(i)

resultado = registro_unico - registro_repetido

print(len(resultado))
