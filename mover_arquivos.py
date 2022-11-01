import os

origem = 'c:\\Users\\acemu\\OneDrive\\Desktop\\Arquivos_python\\arquivos_movidos'
destino = 'c:\\Users\\acemu\\OneDrive\\Desktop\\Arquivos_python\\arquivos\\'

os.chdir(origem)        #selecionando a pasta de trabalho

for arquivo in os.listdir():        #percorrendo os itens da pasta
    os.rename(arquivo, destino + arquivo)

