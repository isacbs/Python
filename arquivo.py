import os

# Acquire input file name
inputNome = input("Digite o nome do arquivo input: ")

# Acquire output file name
outputNome = input("Digite o nome do arquivo output: ")

# Open the input file e create output file

    # If file exists, abort
if os.path.exists(outputNome):
    print("O arquivo output requisitado já existe \nAbordando")
else:
    try:
        with open(inputNome, 'r') as arquivoInput, open(outputNome, 'w') as arquivoOutput:
            # Loop
            while True:
                # Read from input file
                linha = arquivoInput.readline()
                # Write to output file e until read fails
                arquivoOutput.write(linha)
                # Close output file
                if not linha:
                    break

            # Write completion message to screen e terminate normally
            print("Arquivo copiado com sucesso !!")

# If file doesn't exist, abort
    except FileNotFoundError:
        print("O arquivo input requisitado não existe \nAbortando")
