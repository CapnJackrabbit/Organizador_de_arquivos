import os

os.chdir('c:\\Users\\acemu\\OneDrive\\Desktop\\Arquivos_python\\arquivos')        #selecionando a pasta de trabalho
os.listdir()

for arquivo in os.listdir():        #percorrendo os itens da pasta
    print(arquivo)

