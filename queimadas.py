import requests
import pandas as pd
from datetime import datetime

# Caminho para os arquivos README e CSV
CAMINHO_DADOS = "dados_diarios.csv"

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
    colunas_necessarias = ['id', 'lat', 'lon', 'data_hora_gmt', 'satelite', 'municipio', 
                           'estado', 'pais', 'municipio_id', 'estado_id', 'pais_id', 
                           'numero_dias_sem_chuva', 'precipitacao', 'risco_fogo', 
                           'bioma', 'frp']
    
    if not all(coluna in df.columns for coluna in colunas_necessarias):
        print("Colunas necessárias ausentes no CSV diário. Ignorando.")
        return []

    dados_estruturados = []
    for index, row in df.iterrows():
        linha_formatada = (
            f"| {row['id']} | {row['lat']} | {row['lon']} | {row['data_hora_gmt']} | "
            f"{row['satelite']} | {row['municipio']} | {row['estado']} | "
            f"{row['pais']} | {row['municipio_id']} | {row['estado_id']} | "
            f"{row['pais_id']} | {row['numero_dias_sem_chuva']} | {row['precipitacao']} | "
            f"{row['risco_fogo']} | {row['bioma']} | {row['frp']} |"
        )
        dados_estruturados.append(linha_formatada)

    return dados_estruturados

def salvar_dados_csv(df):
    df.to_csv(CAMINHO_DADOS, index=False)
    print(f"Dados salvos em {CAMINHO_DADOS}.")

def atualizar_readme(dados_diarios, numero_inicial, total_entradas):
    # Atualiza o README.md com os dados fornecidos
    conteudo = (
        "# Monitoramento de Queimadas na Amazônia\n\n"
        "Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. "
        "Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.\n\n"
        
        "## Estrutura dos Dados\n\n"
        "Cada entrada na tabela representa um foco de incêndio com as seguintes informações:\n\n"
        "- **ID:** Identificador único do foco de incêndio.\n"
        "- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.\n"
        "- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).\n"
        "- **Satélite:** Satélite responsável pela detecção do foco de incêndio.\n"
        "- **Município, Estado e País:** Localização administrativa do foco detectado.\n"
        "- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.\n"
        "- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.\n"
        "- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.\n"
        "- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.\n"
        "- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.\n\n"
        
        "## Visualização Gráfica\n\n"
        "Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. "
        "Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.\n\n"
        
        "## Informação Adicional\n\n"
        "As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. "
        "O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.\n\n"
        
        f"## Dados Diários - Página {numero_inicial // 100 + 1}\n\n"
        "| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |\n"
        "|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|\n"
    )

    for linha in dados_diarios:
        conteudo += linha + "\n"

    conteudo += "\n\n"
    # Link para o próximo README, se aplicável
    proximo_numero = (numero_inicial // 100) + 2
    if (numero_inicial + 100) < total_entradas:
        conteudo += f"[Clique aqui para ver as próximas entradas](README{proximo_numero}.md)\n"
    
    # Salva o arquivo
    nome_arquivo = f"README.md" if numero_inicial == 0 else f"README{numero_inicial // 100 + 1}.md"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"{nome_arquivo} atualizado com sucesso.")

def main():
    url_diaria = construir_url_diaria()
    
    dados_diarios = baixar_e_processar_csv(url_diaria)
    
    if dados_diarios is not None:
        print("Analisando dados...")
        
        # Salva todos os dados em um arquivo CSV separado
        salvar_dados_csv(dados_diarios)

        # Divide os dados em arquivos de 100 entradas
        entradas_por_arquivo = 100
        total_entradas = len(dados_diarios)

        for i in range(0, total_entradas, entradas_por_arquivo):
            dados_chunk = reestruturar_dados_diarios(dados_diarios.iloc[i:i + entradas_por_arquivo])
            atualizar_readme(dados_chunk, i, total_entradas)

if __name__ == "__main__":
    main()
