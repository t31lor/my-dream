import sys
a = float(input("Seja bem vindo à calculadora de testes\nDigite um valor: "))
b = float(input("Digite um segundo valor: "))
c = int(input("Agora escolha a operação aritmética desejada:\n 1 para Adiçao\n 2 para Subtraçao\n 3 para Multiplicaçao\n 4 para Divisao\n 0 para Cancelar\n"))

if c == 1:
    resultado = a + b
    print(f"O resultado de sua operação é:{resultado:.2f}")
elif c == 2:
    resultado = a - b
    print(f"O resultado de sua operação é: {resultado:.2f}")
elif c == 3:
    resultado = a * b
    print(f"O resultado de sua operação é: {resultado:.2f}")
elif c == 4:
    resultado = a/b
    print(f"O resultado de sua operação é: {resultado:.2f}")
elif c == 0:
    print("Operaçação cancelada!")
    sys.exit()
else:
    print("O valor digitado não corresponde a nenhuma operação!")
    