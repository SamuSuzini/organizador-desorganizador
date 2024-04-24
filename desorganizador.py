import os

os.chdir(r'C:\Users\Usuario\Downloads')

import shutil

pasta_download = "C:\\Users\\Usuario\\Downloads"

if not os.path.exists(pasta_download):
    os.makedirs(pasta_download)

for pasta, sub_pastas, arquivos in os.walk(os.getcwd()):
    for arquivo in arquivos:
        origem = os.path.join(pasta, arquivo)
        destino = os.path.join(pasta_download, arquivo)
        # Verifica se o arquivo já existe na pasta de download, 
        # se sim, renomeia antes de mover
        if os.path.exists(destino):
            nome_base, extensao = os.path.splitext(arquivo)
            novo_nome = nome_base + "_1" + extensao
            destino = os.path.join(pasta_download, novo_nome)
        shutil.move(origem, destino)


diretorio_raiz = "C:\\Users\\Usuario\\Downloads"

# Percorre todos os diretórios dentro do diretório pai
for diretorio_atual, subdiretorios, arquivos in os.walk(diretorio_raiz):
    # Itera sobre os subdiretórios
    for subdiretorio in subdiretorios:
        # Obtém o caminho completo para o subdiretório
        caminho_subdiretorio = os.path.join(diretorio_atual, subdiretorio)
        # Verifica se o subdiretório está vazio
        if not os.listdir(caminho_subdiretorio):
            # Se estiver vazio, exclui o subdiretório
            os.rmdir(caminho_subdiretorio)
            print(f"O diretório vazio {caminho_subdiretorio} foi excluído.")