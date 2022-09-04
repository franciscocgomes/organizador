import utilitarios
import os
import shutil


def main():
    arquivos = os.listdir()
    for diretorio in ['documentos', 'planilhas']:
        utilitarios.cria_dir(diretorio)
        utilitarios.mov_arquivo(arquivos)
    
if __name__=="__main__":
    main()