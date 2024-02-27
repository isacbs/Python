# Acquire input file name
inputNome = input("Digite o nome do arquivo input: ")

# Acquire output file name
outputNome = input("Digite o nome do arquivo output: ")

# Open the input file and create output file
try:
    with open(inputNome, 'r') as arquivoInput, open(outputNome, 'w') as arquivoOutput:
            # Loop
            while True:
                # Read from input file
                linha = arquivoInput.readline()
                # Write to output file
                arquivoOutput.write(linha)
                # Close output line
                if not linha:
                    break

            # Write completion message to screen
            print("Arquivo copiado com sucesso !!")

# If file doesn't exist, abort
except FileNotFoundError:
    print("O arquivo input requisitado não existe \nAbortando")

# If file exists, abort
except FileExistsError:
    print("O arquivo output requisitado já existe \nAbortando")

# Terminate normally