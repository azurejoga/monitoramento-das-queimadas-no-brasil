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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffec5bc0-b49c-3782-b576-73a0c2cb31fc | -1.75785 | -52.17041 | 2024-11-24 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 617247e4-c154-3758-8d82-a54d1c803899 | -3.0781 | -49.19793 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05880b9b-63f9-3e6e-8e14-d3fa87558ce8 | -3.57886 | -41.95569 | 2024-11-24 03:57:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac2b5483-1d6c-32cb-95d7-09fbd0772f2b | -3.27012 | -50.62687 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d68457d3-6751-333f-b171-f5f4ef15d21f | -4.10205 | -46.80906 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 850f384d-cece-344d-ac65-9aa6172d3ca4 | -3.74584 | -50.00958 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2b2fcdf-0d9b-3d79-a0f7-5a714f2c9ab4 | -4.08276 | -50.36849 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f37849a-8e59-3d35-b9f2-d029cc76311e | -5.94859 | -48.04601 | 2024-11-24 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00ac2746-98a2-3fcc-8104-7be7b859692b | -5.06967 | -42.57525 | 2024-11-24 03:57:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 97cbcbd7-6e93-3c5a-a947-4c3491f9f5e0 | -2.47029 | -47.09343 | 2024-11-24 03:57:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c584d996-2ad7-3de3-b179-6cf5ec9473d1 | -2.12091 | -46.71342 | 2024-11-24 03:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab065f36-498a-3ebb-886c-ef1535a99d65 | -5.33215 | -44.78656 | 2024-11-24 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8580068-7569-3f8f-911e-bec9aa5a9419 | -2.57592 | -51.89213 | 2024-11-24 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2e5f6161-85c3-37bb-a4d2-bf6432d2131e | -2.55799 | -46.55811 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f0d5987-3713-319e-a7eb-442b6eb0a4da | -2.204 | -48.92306 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61bb9d29-68d9-375d-a3d9-c8131d571a3d | -2.0571 | -45.73916 | 2024-11-24 03:57:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d5f3ba0-097f-3f99-bc2e-86f68dcc1896 | -3.25251 | -42.02428 | 2024-11-24 03:57:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86748300-21cc-3e5c-9c15-8474e263b41f | -5.1497 | -44.55362 | 2024-11-24 03:57:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6aaa7b61-ed04-368f-aa9b-283ca3bce0e4 | -4.08877 | -50.36959 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fb0bd00-5b4d-304d-b285-ebbd9465ee90 | -2.21734 | -46.39202 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 53340c0f-9443-32cd-9e24-2beb0f651019 | -1.82036 | -46.38746 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5297e792-97cb-3b6e-be83-41215eee0efd | -4.51227 | -45.72167 | 2024-11-24 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74c92353-ef3f-31bc-a02c-bb0275a33acc | -3.96119 | -50.20266 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e2224da-cd80-3c8a-bb77-e9a452ff2bc1 | -2.70939 | -46.26429 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5411dd1-0d36-359d-a34b-58cd77696ddc | -2.70616 | -46.28396 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8dcb0a81-6a0f-31ac-b471-ee2744a249ad | -2.70173 | -46.10816 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54a32849-ef98-3342-b645-db40ff6ee88a | -1.76526 | -52.71841 | 2024-11-24 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a1b5c021-855a-3069-827c-d513390d3502 | -5.10802 | -43.15069 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e07f0163-f187-3733-b9b8-ff61134243eb | -2.70249 | -46.11045 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 359453ce-404b-3573-8b61-51769f542782 | -2.29617 | -46.53753 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33bde23c-6c06-3bce-adf6-bf3589df04e4 | -2.73674 | -49.1246 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65875d5d-491f-39be-8a79-ee2d6fc067e5 | -5.60207 | -46.29678 | 2024-11-24 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0d1d081-0034-3b5f-9629-5185b1608fbb | -1.8409 | -46.64731 | 2024-11-24 03:57:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7b7945bf-3eb6-3cc0-8b19-2bcc3051472a | -3.49274 | -49.91503 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b92a55f-6741-3b03-b3fa-8668676e49f9 | -2.70147 | -46.28321 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70c32c0d-09e4-3c7c-92e0-144b39110a4d | -3.95895 | -50.19874 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 699615a4-a76e-3bdc-84fe-46ff9e1a82e3 | -4.26219 | -48.68992 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4314faab-f2f3-376f-8f32-0036d7fcb0c7 | -2.27718 | -46.20565 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3dd114d3-4e24-3903-9a9f-14b032b701f7 | -4.21612 | -50.407 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e9a5c30d-8f84-3980-84e5-6fdc052cb212 | -2.74546 | -49.12086 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ed537663-53cc-3181-a016-01cad1c2b0f8 | -3.90707 | -46.53049 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0dce477-d86a-308d-bdd3-a720b4361567 | -5.3281 | -44.78584 | 2024-11-24 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eef4270d-26f3-307c-8f74-0891fbe9a448 | -3.48612 | -49.91828 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03782a45-b79a-3473-ade6-985dcb362638 | -3.86031 | -50.0602 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e63ab512-3e1c-3a9e-917e-869194567a73 | -4.52491 | -46.42906 | 2024-11-24 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efb43e9a-d041-321d-acb1-241680f93287 | -4.53293 | -42.90628 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9d829dd-466d-3e43-9cbe-1c6a661e3867 | -2.32216 | -46.34647 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb4a7f19-b99b-3aef-81bc-c9b489cd1890 | -3.48538 | -49.92253 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8d78891-2562-3b2b-b502-abfb3c429bab | -4.59882 | -44.73004 | 2024-11-24 03:57:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1f83dac-674e-30c7-b85e-5dd55c89f525 | -3.78647 | -47.49013 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9fb7cf31-1eb2-38d5-82a6-60b504aab587 | -4.51665 | -45.72236 | 2024-11-24 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d6c5a12-db48-3eff-afb5-4d3e8f42249f | -3.67841 | -50.1188 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49a2ec1a-a2de-301d-a790-5c9b579ae73c | -2.70453 | -46.29387 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7acfa05e-cb60-3565-bb21-ae5a337ec6d7 | -0.57045 | -51.73108 | 2024-11-24 03:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 75ae21e9-5603-3a43-832f-0fb21389c16b | -1.31739 | -49.39368 | 2024-11-24 03:57:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6f9cd43-8899-38b7-acab-2c852d601d13 | -2.09996 | -46.26473 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97f066ce-23c0-3007-b137-1c0f54e25aa4 | -2.72732 | -48.83042 | 2024-11-24 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a128317-977d-3e24-a833-a6a57d2fe080 | -3.34583 | -50.51388 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b7a109a-2686-3f3e-a186-3353a6a38e18 | -2.73913 | -49.12379 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bda363bc-a905-377f-906f-8c586ed86538 | -3.74978 | -50.00954 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e6536a3-b55f-3bde-b37e-66be855cf44c | -3.62454 | -45.06495 | 2024-11-24 03:57:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8af7e5c6-3af8-3ee4-8894-bb8ad7f67667 | -4.65396 | -46.05801 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58b26e5c-e5f7-347a-adfd-75767577b89f | -3.0661 | -49.19991 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d01f5115-0920-30d8-8ed6-f14ca7a742a8 | -5.08688 | -46.16847 | 2024-11-24 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04033502-2ac6-3d7f-88b2-4ccdc3ead9c7 | -6.06304 | -46.35038 | 2024-11-24 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad458c4d-1d4d-39ae-9e3a-b4fc624b2b43 | -6.03872 | -44.03727 | 2024-11-24 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32a4daa8-e137-37f5-bf86-26ad7dd05660 | -4.08861 | -47.03909 | 2024-11-24 03:57:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f78a956d-b038-35c0-ad6c-5bb9b97239d4 | -2.80096 | -46.80905 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2640d355-3c63-3aad-ac85-9ccfdf9d47bd | -3.38456 | -50.32264 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08d1ee1a-01a9-3e37-8724-c40f908de4ad | -2.07324 | -47.07223 | 2024-11-24 03:57:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d69baf2c-ad7b-3d44-8955-cd38f476e0e3 | -3.98037 | -44.79411 | 2024-11-24 03:57:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6274e6f4-d465-3504-ab7d-88a688ed69ed | -2.86456 | -45.83487 | 2024-11-24 03:57:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 8795dc66-d07b-3444-81a3-d3018359bb46 | -5.51337 | -41.90892 | 2024-11-24 03:57:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b5f0da68-388f-326d-82d7-cd36ff78e906 | -5.10065 | -43.14948 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ec48af46-3aa3-3f5f-9605-23fa5cba4c01 | -3.17413 | -45.29973 | 2024-11-24 03:57:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4043ce18-241b-325a-8d11-0da58cbb61e2 | -3.54614 | -50.19363 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 853cd81f-8094-33ee-8c5d-b4936f7af0df | -3.32546 | -41.86424 | 2024-11-24 03:57:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3d34c46e-f6d7-341a-92b7-08eeb428e442 | -3.13035 | -45.37146 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12823e97-4a3e-359e-81a3-30f0ca2c17a2 | -4.08153 | -46.15192 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 305d5962-6fd2-3487-9c97-5678ea9f395e | -3.8457 | -44.05329 | 2024-11-24 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 52982774-384e-3aa2-8feb-a9d76043637a | -1.86314 | -48.17061 | 2024-11-24 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a57b31c-6e49-3ec8-9bef-7986062fec1d | -3.94243 | -46.00033 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e8f6937-7e45-3f15-b7a3-2ae8aa8089d6 | -5.19576 | -49.15884 | 2024-11-24 03:57:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 502ca134-4473-308e-879d-55854e073e32 | -4.13451 | -46.70816 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fa8cf3b-ef91-3dad-924b-214cea27fa4c | -3.63547 | -50.22497 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4903559-c112-37d9-9162-7c13398e6615 | -3.17345 | -45.30388 | 2024-11-24 03:57:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5fea91e-cbbb-3bf8-929a-0cafb72c62e0 | -3.83859 | -44.04704 | 2024-11-24 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7a7a1fd-a746-3902-b2a0-98bf1d53b05c | -4.51548 | -45.81032 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3933c439-d6ea-35cc-9460-645ee20290f1 | -3.13412 | -52.9901 | 2024-11-24 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04c07411-f1e6-3d40-a3bd-5be1ab585698 | -3.6999 | -47.60888 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f304ef7b-8f15-37e3-a42a-acee6a2feba5 | -5.8528 | -40.7995 | 2024-11-24 03:57:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9106c307-14fb-370d-ac72-4b706292d74a | -4.83639 | -43.65562 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d9c3534-f9bd-35d5-a621-aa723df461f5 | -3.47117 | -43.88624 | 2024-11-24 03:57:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9384ce03-68b3-3632-afce-fe6f46a89028 | -4.72398 | -43.25269 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aff5d94d-42a3-3752-8651-784f38ec983e | -3.1031 | -45.78514 | 2024-11-24 03:57:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a372ca18-bea0-38e5-9fac-1794ba9a7015 | -1.29074 | -51.74028 | 2024-11-24 03:57:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 847f37b9-930d-3b32-a7c0-6a7f2674a9f7 | -2.74368 | -49.11773 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 15215025-562a-3093-b606-311a42c93110 | -5.60727 | -46.29329 | 2024-11-24 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c673676b-74ac-309a-9747-489eb1a96790 | -6.53774 | -42.48314 | 2024-11-24 03:57:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8c95d828-6da6-333f-a50a-e1532601ddaa | -5.48458 | -46.24332 | 2024-11-24 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README29.md)
