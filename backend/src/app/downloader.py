import requests

def download_file(url: str, file_path: str) -> bool:
    """
    Faz download do arquivo em 'url' e salva em 'file_path'.
    Retorna True se sucesso, False se houver erro.
    """
    try:
        resp = requests.get(url, stream=True)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERRO] Falha ao baixar {url}: {e}")
        return False

    with open(file_path, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    return True