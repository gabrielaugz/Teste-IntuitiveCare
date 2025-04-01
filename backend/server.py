from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

CSV_PATH = "backend/Relatorio_cadop.csv"

try:
    # Força a coluna 'CNPJ' a ser lida como string
    df = pd.read_csv(
        CSV_PATH,
        encoding="ISO-8859-1",
        delimiter=";",
        on_bad_lines='skip',
        dtype={'CNPJ': str} 
    )
    
    print("Colunas carregadas:", df.columns.tolist())
    print("Total de operadoras:", len(df))
    
except Exception as e:
    print(f"Erro crítico ao ler CSV: {e}")
    df = pd.DataFrame()

@app.route('/api/operadoras', methods=['GET'])
def get_operadoras():
    return jsonify(df.to_dict(orient="records"))

@app.route('/api/search', methods=['GET'])
def search_operadoras():
    query = request.args.get('q', '').lower()
    
    if df.empty:
        return jsonify([])
    
    try:
        filtered = df[
            df['Razao_Social'].str.lower().str.contains(query, na=False) |
            df['Nome_Fantasia'].str.lower().str.contains(query, na=False) |
            df['CNPJ'].str.contains(query, na=False)
        ]
        
    except KeyError as e:
        print(f"Erro crítico: Coluna {e} não existe")
        return jsonify([])
    
    return jsonify(filtered.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True, port=5000)