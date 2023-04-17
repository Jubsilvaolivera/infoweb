#1
print("Digite seu primeiro nome:")
A = input()

print("Bem-vindo ao Python," , A)


#2
print("Digite seu nome completo:")
A = input().split()

print("Bem-vindo ao Python," , A [0])


#3
print("Digite a nota do primeiro bimestre da disciplina:")
n1 = int(input())
print("Digite a nota do segundo bimestre da disciplina:")
n2 = int(input())

M = (n1 * 2 + n2 * 3) / 5

print("Média parcial =" , M)


#4
print("Digite a base e a altura do retângulo:")

B = int(input())
A = int(input())

Àrea = B * A
Perímetro = B**2 + A**2
Diagonal = (B**2 + A**2)**0.5

print("Àrea -", f"{Àrea:.2f}")
print("Perímetro -", f"{Perímetro:.2f}")
print("Diagonal -", f"{Diagonal:.2f}")