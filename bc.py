import pyminifier

def obfuscate_file(input_file, output_file):
    with open(input_file, "r") as file:
        code = file.read()

    obfuscated_code = pyminifier.obfuscate(code)

    with open(output_file, "w") as file:
        file.write(obfuscated_code)

    print("Arquivo obfuscado criado com sucesso!")

# Defina o arquivo de entrada e o arquivo de saída
input_file = input("Digite o nome do arquivo de entrada: ")
output_file = input("Digite o nome do arquivo de saída: ")

# Chama a função para obfuscar o arquivo
obfuscate_file(input_file, output_file)
