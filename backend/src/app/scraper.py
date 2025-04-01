# src/app/scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_pdf_links(url_base: str) -> dict:
    """
    Acessa a página oficial da ANS e busca links PDF para Anexo I e Anexo II,
    baseado no texto do link que contenha "Anexo I" ou "Anexo II".
    Retorna: {'AnexoI': url_pdf, 'AnexoII': url_pdf}
    """
    urls_anexos = {}
    try:
        response = requests.get(url_base)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERRO] Falha ao acessar {url_base}: {e}")
        return urls_anexos

    soup = BeautifulSoup(response.text, 'html.parser')

    pdf_links = soup.find_all('a', href=lambda x: x and x.lower().endswith('.pdf'))

    for link in pdf_links:
        texto_link = link.get_text(strip=True) 
        texto_upper = texto_link.upper().replace('.', '')
        href = link['href']

        # Ajustar se o link for relativo
        if not href.startswith('http'):
            href = url_base.rstrip('/') + '/' + href.lstrip('/')

        print(f"[DEBUG] Texto do link: {texto_link}")
        print(f"[DEBUG] Href do link:  {href}")

        # Verifica se foi encontrado "Anexo I" ou "Anexo II"
        # Verifica primeiro se é Anexo II e depois Anexo I
        if "ANEXO II" in texto_upper:
            urls_anexos["AnexoII"] = href
        elif "ANEXO I" in texto_upper:
            urls_anexos["AnexoI"] = href

    return urls_anexos