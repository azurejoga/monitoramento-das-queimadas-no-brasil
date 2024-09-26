import requests
import pandas as pd
from datetime import datetime
import os

# Caminho para o README.md
CAMINHO_README = "README.md"

def construir_url_diaria():
    agora_utc = datetime.utcnow()
    data = agora_utc.strftime("%Y%m%d")
    url_diaria = f"https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/diario/Brasil/focos_diario_br_{data}.csv"
    return url_diaria

def baixar_e_processar_csv(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            df = pd.read_csv(url)
            print(f"Dados carregados com sucesso de {url}")
            return df
        else:
            print(f"Erro ao acessar {url}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exceção ao baixar o CSV: {e}")
        return None

def reestruturar_dados_diarios(df):
    colunas_necessarias = ['id', 'lat', 'lon', 'data_hora_gmt', 'satelite', 'municipio', 'estado', 'pais',
                           'municipio_id', 'estado_id', 'pais_id', 'numero_dias_sem_chuva', 'precipitacao',
                           'risco_fogo', 'bioma', 'frp']
    if not all(coluna in df.columns for coluna in colunas_necessarias):
        print("Colunas necessárias ausentes no CSV diário. Ignorando.")
        print("Colunas disponíveis:", df.columns.tolist())
        return []
    
    dados_estruturados = []
    for index, row in df.iterrows():
        linha_formatada = (
            f"id: {row['id']}, "
            f"lat: {row['lat']}, "
            f"lon: {row['lon']}, "
            f"data_hora_gmt: {row['data_hora_gmt']}, "
            f"satelite: {row['satelite']}, "
            f"municipio: {row['municipio']}, "
            f"estado: {row['estado']}, "
            f"pais: {row['pais']}, "
            f"municipio_id: {row['municipio_id']}, "
            f"estado_id: {row['estado_id']}, "
            f"pais_id: {row['pais_id']}, "
            f"numero_dias_sem_chuva: {row['numero_dias_sem_chuva']}, "
            f"precipitacao: {row['precipitacao']}, "
            f"risco_fogo: {row['risco_fogo']}, "
            f"bioma: {row['bioma']}, "
            f"frp: {row['frp']}"
        )
        dados_estruturados.append(linha_formatada)
    return dados_estruturados

def atualizar_readme(dados_diarios):
    # Atualiza o README.md com os dados fornecidos
    conteudo = (
        "# Monitoramento de Queimadas\n\n"
        "## Importância das Queimadas na Amazônia\n\n"
        "As queimadas na Amazônia são um problema ambiental crítico que impacta a biodiversidade, "
        "o clima global e as comunidades locais. Estas queimadas podem resultar em perdas irreversíveis "
        "na flora e fauna da região, além de contribuir para a emissão de gases de efeito estufa. "
        "Este projeto visa monitorar e conscientizar sobre a situação das queimadas na Amazônia, "
        "fornecendo dados atualizados e análises que ajudem na preservação desse bioma vital.\n\n"
        "## Dados Diários\n\n"
        "```\n"
    )
    for linha in dados_diarios:
        conteudo += linha + "\n"
    conteudo += "```\n"
    
    with open(CAMINHO_README, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print("README.md atualizado com sucesso.")

def main():
    url_diaria = construir_url_diaria()
    
    dados_diarios = baixar_e_processar_csv(url_diaria)
    
    if dados_diarios is not None:
        print("Analisando dados...")
        dados_diarios_estruturados = reestruturar_dados_diarios(dados_diarios)
        
        # Atualiza o README.md com os novos dados
        atualizar_readme(dados_diarios_estruturados)

if __name__ == "__main__":
    main()
