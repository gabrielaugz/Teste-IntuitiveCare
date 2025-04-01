import os
import pandas as pd
import zipfile
import glob

def processar_dados():
    pasta_zip = "zip_files"
    pasta_temp = "temp_demonstracoes"
    os.makedirs(pasta_temp, exist_ok=True)
    
    todas_planilhas = []

    for zip_path in glob.glob(os.path.join(pasta_zip, "Q[1-4]-*.zip")):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(pasta_temp)
        
        for filename in os.listdir(pasta_temp):
            file_path = os.path.join(pasta_temp, filename)
            if filename.endswith((".csv", ".xlsx", ".xls")):
                if filename.endswith(".csv"):
                    df = pd.read_csv(file_path, encoding="ISO-8859-1")
                else:
                    df = pd.read_excel(file_path)
                
                df.rename(columns={
                    "Registro_ANS": "operadora_registro_ans",
                    "Data": "data",
                    "Descrição da Categoria": "categoria",
                    "Valor (R$)": "valor"
                }, inplace=True)
                
                # Converte a coluna "data" para o formato YYYY-MM-DD
                df["data"] = pd.to_datetime(df["data"], errors="coerce").dt.strftime("%Y-%m-%d")
                
                todas_planilhas.append(df)
    
    df_final = pd.concat(todas_planilhas, ignore_index=True)
    df_final = df_final.dropna(subset=["valor", "data"])  # Remove linhas com valores nulos
    df_final.to_csv("output/despesas_processadas.csv", index=False, encoding="utf-8")
    
    print("Arquivo 'output/despesas_processadas.csv' gerado com sucesso!")

if __name__ == "__main__":
    processar_dados()