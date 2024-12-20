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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e9d9fca-9015-38f7-8d37-5a462e6014f9 | -4.5543 | -43.5586 | 2024-12-20 13:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 64488e54-be79-3f23-9110-71c68e6e3193 | -4.5543 | -43.5586 | 2024-12-20 13:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 873ae136-457b-304c-9886-5c62facbccda | -4.5543 | -43.5586 | 2024-12-20 13:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 0795ec9f-2c71-3f08-b532-7ad9b9849fa9 | -4.5543 | -43.5586 | 2024-12-20 13:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| bdfeb0e5-214e-359f-b51a-7aac68a0aabb | -3.7675 | -43.9941 | 2024-12-20 14:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 82cb1f8e-10b0-3372-98a6-31f978eb303f | -3.5486 | -39.984 | 2024-12-20 14:20:00 | GOES-16 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 6eb2baa1-fb81-3a45-a2eb-c8b1d89d1107 | -3.7675 | -43.9941 | 2024-12-20 14:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| d376f092-3dbc-3ad7-9296-9c9c905e4ac4 | -3.4882 | -40.6735 | 2024-12-20 14:30:00 | GOES-16 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 8f05dcab-3c58-3c64-b447-e01855b0998b | -3.3842 | -39.2225 | 2024-12-20 14:30:00 | GOES-16 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 101.2 |
| d9ac86c4-bb1f-3fb7-b421-2d731668bc4c | -3.5069 | -40.6726 | 2024-12-20 14:30:00 | GOES-16 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 164970e2-57ca-3bf4-b56c-fd398caa56e7 | -5.2114 | -38.9472 | 2024-12-20 14:40:00 | GOES-16 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 78.7 |


