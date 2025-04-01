# src/app/table_extractor.py
import os
import tabula
import pandas as pd

def extract_rol_table(pdf_path: str, csv_output: str) -> None:
    """
    Lê o PDF que contém a tabela 'Rol de Procedimentos e Eventos em Saúde' (Anexo I)
    e salva em um CSV.
    """
    # Força a JVM a usar a codificação cp1252 (padrão Windows)
    os.environ["JAVA_TOOL_OPTIONS"] = "-Dfile.encoding=cp1252"
    
    try:
        # Lê todas as páginas e tenta extrair múltiplas tabelas
        dfs = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    except Exception as e:
        print(f"[ERRO] Falha ao ler o PDF {pdf_path}: {e}")
        return

    if not dfs or len(dfs) == 0:
        print(f"[AVISO] Nenhuma tabela encontrada no PDF {pdf_path}")
        return

    # Concatena as tabelas encontradas
    df_final = pd.concat(dfs, ignore_index=True)

    df_final.to_csv(csv_output, index=False)
    print(f"[INFO] Tabela extraída e salva em: {csv_output}")