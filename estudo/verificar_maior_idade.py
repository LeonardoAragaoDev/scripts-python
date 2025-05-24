nome = input("Qual o seu nome? ")
idade = int(input("Quantos anos você tem? "))

if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você é menor de idade.")
