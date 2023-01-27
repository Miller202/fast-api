# Fast API

## Configuração local

1 - Ativar ambiente de virtualização

    .\env\Scripts\Activate.ps1

2 - Instalar dependências

    pip install -r requirements.txt

3 - Configurar BD local

    python .\cria_tabelas.py

4 - Executar a aplicação

    uvicorn main:app --reload