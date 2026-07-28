def sumar_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

numeros = []
for i in range(5):
    valor = int(input(f"Ingrese número {i+1}: "))
    numeros.append(valor)
    
    total = sum(numeros)
    total_sum = sumar_lista(numeros)
    
    print("Suma con bucle:", total)
    print("Suma con sum():", total_sum)