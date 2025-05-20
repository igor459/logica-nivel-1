valores = []
for i in range(3):
    valores.append(int(input(f"Digite o {i+1}º valor: ")))

valores.sort()
print("Valores em ordem crescente:", valores)
