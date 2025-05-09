# Questão 5: Inverter string

def inverter_string(texto):
    invertida = ""
    for i in range(len(texto)-1, -1, -1):
        invertida += texto[i]
    return invertida

# Recebe a string do usuário
texto = input("Digite uma palavra ou frase: ")

# Verifica se a entrada contém apenas letras e espaços
if not texto.replace(" ", "").isalpha():
    print("Por favor, digite apenas letras e espaços.")
else:
    print(f"Texto invertido: {inverter_string(texto)}")
