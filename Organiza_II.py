import os
import shutil       #para copiar arquivos

arquivos = os.listdir('arquivos')     #podemos especificar nos parênteses o endereço do arquivo. Em branco, ele vai tratar dos arquivos na pasta onde ele próprio se encontra.
print(arquivos)

caminho = os.getcwd()                 #este método serve para sabermos em que diretório estamos trabalhando por padrão. CWD = Current Working Directory
print(caminho)

#os.rename('arquivos\cert.pdf', 'arquivos_movidos\cert.pdf')            #método para renomear arquivos. Sintaxe é: (nome_atual_do_arquivo, novo_nome_do_arquivo) Aqui usamos para mover o arquivo de uma pasta para outra.

#shutil.copy2('arquivos\cert.pdf', 'arquivos_movidos\cert.pdf')         #método para copiar arquivos.

for arquivo in arquivos:
    if 'pdf' in arquivo:
        if not os.path.isdir(caminho + 'arquivos_movidos\PDF\\'):
            os.mkdir(r"C:\Users\acemu\OneDrive\Desktop\Arquivos_python\arquivos_movidos\PDF")
            os.rename('arquivos\\'+arquivo, 'arquivos_movidos\PDF\{}'.format(arquivo))
        else:
            os.rename('arquivos\\'+arquivo, 'arquivos_movidos\PDF\{}'.format(arquivo))
    
    elif 'jpg' in arquivo:
        if not os.path.isdir(caminho + 'arquivos_movidos\Imagens\\'):
            os.mkdir(r"C:\Users\acemu\OneDrive\Desktop\Arquivos_python\arquivos_movidos\Imagens")
            os.rename('arquivos\\'+arquivo, 'arquivos_movidos\Imagens\{}'.format(arquivo))
        else:
            os.rename('arquivos\\'+arquivo, 'arquivos_movidos\Imagens\{}'.format(arquivo))
    
    elif 'docx' in arquivo:
        if not os.path.isdir(caminho + 'arquivos_movidos\Word\\'):
            os.mkdir(r"C:\Users\acemu\OneDrive\Desktop\Arquivos_python\arquivos_movidos\Word")
            os.rename('arquivos\\'+arquivo, 'arquivos_movidos\Word\{}'.format(arquivo))
        else:
            os.rename('arquivos\\'+arquivo, 'arquivos_movidos\Word\{}'.format(arquivo))

    elif 'txt' in arquivo:
        if not os.path.isdir(caminho + 'arquivos_movidos\\Texto\\'):
            os.mkdir(r"C:\Users\acemu\OneDrive\Desktop\Arquivos_python\arquivos_movidos\Texto")
            os.rename('arquivos\\'+arquivo, 'arquivos_movidos\\Texto\{}'.format(arquivo))
        else:
            os.rename('arquivos\\'+arquivo, 'arquivos_movidos\\Texto\{}'.format(arquivo))