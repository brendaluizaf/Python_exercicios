arquivo = open("texto.txt", "r")

conteudo = arquivo.read()
print(conteudo)

arquivo.close()

arquivo = open("texto.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

arquivo = open("texto.txt", "w")
arquivo.write("Hello, world!\n")
arquivo.write("This is a simple file.")
arquivo.close()

arquivo = open("texto.txt", "a")
arquivo.write("\nThis is additional content. ")
arquivo.close()