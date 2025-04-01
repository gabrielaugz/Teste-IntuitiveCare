import os
from app.table_extractor import extract_rol_table
from app.compressor import compress_files

def main():
    pdf_path = os.path.join("downloads", "Anexo_I.pdf")

    # Verifica se existe
    if not os.path.isfile(pdf_path):
        print(f"[ERRO] PDF não encontrado em {pdf_path}")
        return

    csv_path = "Rol_de_Procedimentos.csv" 

    print("[INFO] Iniciando extração de dados do PDF...")
    extract_rol_table(pdf_path, csv_path)

    # Verifica se o CSV foi criado
    if not os.path.isfile(csv_path):
        print(f"[ERRO] Não foi possível gerar o arquivo CSV em {csv_path}")
        return

    print("[INFO] Compactando CSV em Teste.zip...")
    zip_filename = "Teste_Gabriel_Augusto_Leite_Souza_de_Castro.zip"
    compress_files([csv_path], zip_filename)

    print("[SUCESSO] Etapa 2 concluída!")

if __name__ == "__main__":
    main()