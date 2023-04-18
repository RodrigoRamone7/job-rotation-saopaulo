# Recebe a string do usuário
string = input("Digite uma string: ")

# Cria uma lista vazia para guardar os caracteres invertidos
invert_char = []

# Percorre a string de trás para frente, adicionando cada caractere na lista
for i in range(len(string)-1, -1, -1):
    invert_char.append(string[i])

# Junta os caracteres invertidos em uma nova string
invert_str = "".join(invert_char)

# Imprime a string invertida
print("A string invertida é:", invert_str)