import zipfile
import os

def compress_files(file_paths, zip_path):
    """
    Recebe uma lista de caminhos de arquivos (file_paths)
    e cria um arquivo ZIP em 'zip_path'
    """
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for path in file_paths:
            if os.path.isfile(path):
                arcname = os.path.basename(path)
                zipf.write(path, arcname=arcname)
            else:
                print(f"[AVISO] Arquivo não encontrado: {path}")