import os, shutil

caminho = r"C:\Users\acemu\OneDrive\Desktop\Arquivos_python"

origem = r'C:\Users\acemu\OneDrive\Desktop\Arquivos_python\arquivos\\'
destino = r'C:\Users\acemu\OneDrive\Desktop\Arquivos_python\arquivos_movidos'

os.chdir('c:\\Users\\acemu\\OneDrive\\Desktop\\Arquivos_python\\arquivos')
arquivos = os.listdir()

ext = {

     "jpg": "imagens",
     "png": "imagens",
     "ico": "imagens",
     "gif": "imagens",
     "svg": "imagens",
     "sql": "sql",
     "exe": "programas",
     "msi": "programas",
     "pdf": "pdf",
     "xlsx": "excel",
     "csv": "excel",
     "rar": "arquivo",
     "zip": "arquivo",
     "gz": "arquivo",
     "tar": "arquivo",
     "docx": "palavra",
     "torrent": "torrent",
     "txt": "texto",
     "ipynb": "python",
     "py": "python",
     "pptx": "powerpoint",
     "ppt": "powerpoint",
     "mp3": "audio",
     "wav": "áudio",
     "mp4": "vídeo",
     "m3u8": "vídeo",
     "webm": "vídeo",
     "ts": "vídeo",
     "json": "json",
     "css": "web",
     "js": "web",
     "html": "web",
     "apk": "apk",
     "sqlite3": "sqlite3",
}

for extensao, pastas in ext.items():
    for arquivo in arquivos:
        if extensao in arquivo:
            if not os.path.isdir(caminho + '\\arquivos_movidos\\{}\\'.format(pastas)):
                print('Criando pasta ' + pastas)
                os.mkdir(r'C:\Users\acemu\OneDrive\Desktop\Arquivos_python\arquivos_movidos\{}'.format(pastas))
                shutil.move(arquivo, destino+'\{}\{}'.format(pastas,arquivo))
            else:
                print('Pasta {} já existe. Movendo...'.format(pastas))
                shutil.move(arquivo, destino+'\{}\{}'.format(pastas,arquivo))