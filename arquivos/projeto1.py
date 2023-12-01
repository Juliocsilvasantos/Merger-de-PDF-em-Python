import PyPDF2 # ferramenta que permite manipular PDF de modo eficiente
import os # ferramenta para manipular arquivos do nosso computador

merger = PyPDF2.PdfMerger()  #mesclador de pdf

lista_arquivos = os.listdir("arquivos") # "os.listdir" vai listar os arquivos dentro da pasta selecionada
lista_arquivos.sort() #colocar os arquivos em ordem
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo: # condição para mesclar somente arquivos ".pdf"
        merger.append(f"arquivos/{arquivo}") # ".append" vai add o arquivo que selecionamos no mesclador
merger.write("PDF FINAL.pdf") # ".write" serve pra salvar o pdf mesclado!!!