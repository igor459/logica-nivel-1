# Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.
a = int(input("digite o primeiro valor:"))
b = int(input("digite o segundo valor:"))
c = int(input("digite o terceiro valor:"))
maior = a
if b > maior:
    maior = b
    if c > maior:
        maior = c
        print("O maior valor é:", maior)
