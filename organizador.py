"""
Programa: Organizador
Requisitos: Este programa organiza os arquivos em função da extensão deles.
Autor: Francisco Gomes
Data: 27/08/2022
Versão: 0.0.1
"""

# Importação

import os

caminho = "C:/Users/chicg/Documents/FRANCISCO/CURSOS/TCERS/ExtDesempInstit/IntroducaoPython"
lista_arquivos = os.listdir(caminho + "/Projeto_1")
#print(lista_arquivos)

for arquivo in lista_arquivos:
    #print(arquivo)
    if ".xlsx" in arquivo:
        #print(arquivo)
        os.rename (f"C:/Users/chicg/Documents/FRANCISCO/CURSOS/TCERS/ExtDesempInstit/IntroducaoPython/Projeto_1/{arquivo}",
                   f"C:/Users/chicg/Documents/FRANCISCO/CURSOS/TCERS/ExtDesempInstit/IntroducaoPython/Projeto_1/Planilhas/{arquivo}")
    if ".docx" in arquivo:
        os.rename (f"C:/Users/chicg/Documents/FRANCISCO/CURSOS/TCERS/ExtDesempInstit/IntroducaoPython/Projeto_1/{arquivo}",
                   f"C:/Users/chicg/Documents/FRANCISCO/CURSOS/TCERS/ExtDesempInstit/IntroducaoPython/Projeto_1/Documentos/{arquivo}")
        
