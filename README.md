# Teste-IntuitiveCare

## Instalação

1. Clone o repositório
```bash
git clone https://github.com/gabrielaugz/Teste-IntuitiveCare.git
```

2. Instale as dependências
```bash
pip install -r requirements.txt
```

3. Realize o download dos arquivos utilizando
```bash
python backend/src/main.py
python backend/src/main_step2.py
```

4. Rode o servidor localemnte
```bash 
python backend/server.py
```

## Utilização da API
1. Listar todas operadoras
GET http://localhost:5000/api/operadoras

2. Buscar operadoras por termo
GET http://localhost:5000/api/search?q={termo}