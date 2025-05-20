# Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.
etapas para resolver:
	1 - peça os 3 valores
	2 - descobrir e mostrar o maior

valores = []
for i in range(3):
    valores.append(int(input(f"Digite o {i+1}º valor: ")))

valores.sort()
print("Valores em ordem crescente:", valores)
