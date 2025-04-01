# src/main.py

import os
from app.scraper import scrape_pdf_links
from app.downloader import download_file
from app.compressor import compress_files

def main():
    url_base = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    
    # Scraping dos links
    urls_anexos = scrape_pdf_links(url_base)
    print("\n[INFO] Links identificados:")
    print(urls_anexos)

    if not urls_anexos.get("AnexoI") or not urls_anexos.get("AnexoII"):
        print("[ERRO] Não conseguimos localizar Anexo I e/ou Anexo II (links PDF).")
        return

    downloads_folder = "downloads"
    os.makedirs(downloads_folder, exist_ok=True)

    anexo_i_url = urls_anexos["AnexoI"]
    anexo_ii_url = urls_anexos["AnexoII"]

    anexo_i_path = os.path.join(downloads_folder, "Anexo_I.pdf")
    anexo_ii_path = os.path.join(downloads_folder, "Anexo_II.pdf")

    print(f"[INFO] Baixando Anexo I => {anexo_i_url}")
    download_file(anexo_i_url, anexo_i_path)

    print(f"[INFO] Baixando Anexo II => {anexo_ii_url}")
    download_file(anexo_ii_url, anexo_ii_path)

    zip_filename = "anexos_compactados.zip"
    print(f"[INFO] Compactando: {zip_filename}")
    compress_files([anexo_i_path, anexo_ii_path], zip_filename)

    print("[SUCESSO] Processo concluído!")

if __name__ == "__main__":
    main()