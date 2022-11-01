import os
import glob
import shutil

caminho = r"C:\Users\acemu\OneDrive\Desktop\Arquivos_python"

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
    arquivos = glob.glob(os.path.join(caminho, f"*.{extensao}"))
    print(f"[*] Encontrados {len(arquivos)} arquivos com extensão '{extensao}'")
    
    if not os.path.isdir(os.path.join(caminho, pastas)) and arquivos:
        print(f"[+] Criando a pasta {pastas}")
        os.mkdir(os.path.join(caminho, pastas))
        
    for file in arquivos:
        basename = os.path.basename(file)
        dst = os.path.join(caminho, pastas, basename)
        
        print(f"[*] Movendo {file} para {dst}")
        shutil.move(file, dst)

