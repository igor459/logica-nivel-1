
valores = []
for i in range(3):
    valores.append(int(input(f"Digite o {i+1}º valor: ")))

valores.sort(reverse=True)
soma = valores[0] + valores[1]
print("A soma dos dois maiores é:", soma)
