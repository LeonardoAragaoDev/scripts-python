numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O {numero1} é maior que {numero2}.")
elif numero1 < numero2:
    print(f"O {numero2} é maior que {numero1}.")
else:
    print(f"Os {numero1} e {numero2} são iguais.")
