Organizador e Desorganizador de Arquivos
Bem-vindo ao projeto Organizador e Desorganizador de Arquivos! Este é um script desenvolvido em Python que organiza automaticamente seus arquivos na pasta Downloads e remove diretórios vazios.

📸 Demonstração
Assista à Demonstração

https://github.com/SamuSuzini/organizador-desorganizador/assets/168037378/8518caa8-425b-4f48-85c8-0c53b48ae5b0



🛠️ Tecnologias Utilizadas

Python: Linguagem de programação utilizada para automação de tarefas e manipulação de arquivos.
✨ **Funcionalidades Principais**


**Organizador:**
**Migração Automática:** Transfere arquivos da pasta Downloads para uma nova pasta específica, categorizando-os por tipo de extensão.
- **Prevenção de Duplicatas:** Verifica e evita a criação de arquivos com nomes iguais durante a transferência.

**Desorganizador:**
- **Reagrupamento:** Retorna arquivos da localização atual para a pasta Downloads, facilitando o acesso rápido.
- **Limpeza Eficiente:** Elimina diretórios que ficam vazios após o processo de organização, mantendo o sistema limpo e ordenado.

📋 Requisitos

Python 3.6 ou superior.
🔧 Como Usar

Instale o Python: Se ainda não tiver, faça o download e instale a versão mais recente do Python.
Clone o Repositório: Faça o download dos arquivos do projeto.
bash
Copiar código
git clone https://github.com/seuusuario/organizador-desorganizador.git
Execute o Script:
bash
Copiar código
python organizador_desorganizador.py

💡 Como Funciona

O script muda o diretório atual para a pasta Downloads.
Percorre todos os arquivos e pastas, movendo os arquivos para a pasta Downloads.
Em caso de arquivos duplicados, renomeia adicionando um sufixo numérico.
Após mover os arquivos, verifica se há diretórios vazios e os remove.

📝 Código de Exemplo

python
Copiar código
import os
import shutil

os.chdir(r'C:\Users\Usuario\Downloads')

pasta_download = "C:\\Users\\Usuario\\Downloads"

if not os.path.exists(pasta_download):
    os.makedirs(pasta_download)

for pasta, sub_pastas, arquivos in os.walk(os.getcwd()):
    for arquivo in arquivos:
        origem = os.path.join(pasta, arquivo)
        destino = os.path.join(pasta_download, arquivo)
        if os.path.exists(destino):
            nome_base, extensao = os.path.splitext(arquivo)
            novo_nome = nome_base + "_1" + extensao
            destino = os.path.join(pasta_download, novo_nome)
        shutil.move(origem, destino)

diretorio_raiz = "C:\\Users\\Usuario\\Downloads"

for diretorio_atual, subdiretorios, arquivos in os.walk(diretorio_raiz):
    for subdiretorio in subdiretorios:
        caminho_subdiretorio = os.path.join(diretorio_atual, subdiretorio)
        if not os.listdir(caminho_subdiretorio):
            os.rmdir(caminho_subdiretorio)
            print(f"O diretório vazio {caminho_subdiretorio} foi excluído.")
            
📧 Contato
Obrigado por visitar o meu projeto! 😊
