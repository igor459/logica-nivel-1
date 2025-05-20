#Verificação de Nota - Peça ao usuário para digitar sua nota (0 a 10) e classifique:
Nota ≥ 7: Aprovado
Nota entre 5 e 6.9: Recuperação
Nota < 5: Reprovado

valores = []
for i in range(3):
    valores.append(int(input(f"Digite o {i+1}º valor: ")))

valores.sort(reverse=True)
soma = valores[0] + valores[1]
print("A soma dos dois maiores é:", soma)
