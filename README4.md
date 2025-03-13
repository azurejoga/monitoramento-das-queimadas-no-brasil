# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a532fc48-3f11-3fdb-a8f3-8eb304a503ad | -14.4408 | -45.3957 | 2025-03-13 12:30:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| ce6603d1-2396-38c6-9c73-fb71cdabe583 | -17.5603 | -46.4863 | 2025-03-13 12:30:00 | GOES-16 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 58b48306-e68d-3bf1-b00f-833d6eebe8a0 | -14.4408 | -45.3957 | 2025-03-13 12:40:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| aa3450e6-feee-3cd9-b3e6-5e283b8cd3d4 | -14.4408 | -45.3957 | 2025-03-13 12:50:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 6ca9ca63-377c-3fd4-91eb-f4d23d28e467 | -14.4408 | -45.3957 | 2025-03-13 13:00:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| fa83be70-9c42-3499-adee-65b5d48b4011 | -7.8487 | -44.2172 | 2025-03-13 13:10:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3f1f56f2-4327-32d3-b82a-89491f60ddbf | -14.4408 | -45.3957 | 2025-03-13 13:10:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 2c88cf91-2327-3380-a58a-050e6929f93a | -7.8487 | -44.2172 | 2025-03-13 13:20:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 3313b4fa-21e3-3661-aebe-8d1d65ad9031 | -17.5603 | -46.4863 | 2025-03-13 13:20:00 | GOES-16 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 4e78e621-6943-3c12-9de5-081109f6f4e1 | -17.0533 | -46.937 | 2025-03-13 13:20:00 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b95383a4-26d3-3a9e-b262-06ec0395bba4 | -14.4408 | -45.3957 | 2025-03-13 13:20:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 67ab9c6b-4fe3-3a77-8a78-bded0f0ed566 | -7.8487 | -44.2172 | 2025-03-13 13:30:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ab2cbc65-d15b-3a6f-9afd-8e1808987e2d | -17.5603 | -46.4863 | 2025-03-13 13:30:00 | GOES-16 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 01a1018b-a897-3452-9842-d91d93ae15aa | -14.4408 | -45.3957 | 2025-03-13 13:30:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 0f26ccf9-16a9-3b38-9e08-b002f42bc799 | -14.4408 | -45.3957 | 2025-03-13 13:40:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| da774085-f21a-3e6d-b642-8acd170063f8 | -11.14 | -38.4968 | 2025-03-13 13:40:00 | GOES-16 | CIPÓ | BAHIA | Brasil | 2907905 | 29 | 33 | nan | nan | nan | Caatinga | 144.6 |
| e32bea22-337a-371f-a92f-a0831850853f | -7.8487 | -44.2172 | 2025-03-13 13:40:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 208267a0-c89b-3406-8057-cf000d78dff1 | -14.4408 | -45.3957 | 2025-03-13 13:50:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| d5716104-6732-3f37-96d4-90fd789c0814 | -14.4408 | -45.3957 | 2025-03-13 14:00:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| dcb18812-09ad-3769-92e3-07f9948924f4 | -7.8487 | -44.2172 | 2025-03-13 14:00:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |


