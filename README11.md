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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebedd79e-fb74-3d1f-b773-0a544321782e | -3.69489 | -52.00772 | 2024-10-21 01:05:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9992bff7-bcbd-3dd5-97e7-c38809abc390 | -3.65111 | -54.10004 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 04a45502-0844-3245-b719-3d7acab7d50a | -3.63717 | -45.75942 | 2024-10-21 01:05:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 74d3a1f2-907d-3a54-b683-5945c59188d7 | -3.62995 | -45.76622 | 2024-10-21 01:05:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 4213aa6f-ad19-3c18-ada1-e6bfa08e4705 | -3.62882 | -50.80188 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7bff0457-f4ca-3f51-b022-bc5b25cb0be3 | -3.62759 | -50.79307 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 99707284-5c22-3b24-93d3-2c7467c7255d | -3.62635 | -50.78426 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 30b3d999-eb1f-3574-b557-82285476001f | -3.6135 | -45.81802 | 2024-10-21 01:05:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 34f3e036-fbe1-3a80-9a86-a3c73c7b4bec | -3.60804 | -50.58888 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 840566a4-0f5c-3a44-81a3-d91ed5d1380d | -3.6068 | -50.58003 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 09dbd6da-bbc3-3c13-a93a-2237bdedee77 | -3.59919 | -50.59015 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7630cd87-bbde-3a5f-a535-fb6bc27a4488 | -3.59795 | -50.58131 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e8b90a36-a07d-3c8a-b235-a8d08c44155c | -3.58656 | -51.28889 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 524f3607-7485-30f7-ae0b-fe1531da9f7f | -3.5731 | -53.53171 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4d5ff84a-6bc2-3b65-8294-c12c0af627db | -3.56358 | -53.53308 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ae25622-a9ec-394d-8f64-ed6c353577af | -3.55164 | -50.31606 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 96ade3ef-3363-3a03-b42b-2005d3db916b | -3.55038 | -50.30712 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| d72d657c-cc5f-3851-8989-4879527a82df | -3.54453 | -51.3909 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| dde9a51c-b17f-3d0b-be9f-a0a9d127aa41 | -3.54331 | -51.38211 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| f3b57595-705c-310e-bdf4-73ce8d829cd5 | -3.54108 | -53.02463 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a53d939b-7dda-389e-b774-511ce28fd61b | -3.53378 | -51.24885 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9b071d4-5145-36ba-a0a8-07228ce2fd8f | -3.51485 | -49.99065 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 03c0fa00-7cee-3d34-b334-64761f5758eb | -3.50308 | -51.35185 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c31a5b2-9337-3715-b174-f68dbac3e45c | -3.50269 | -52.08997 | 2024-10-21 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16246cdd-9ff4-331d-8427-3dd1fca2788e | -3.49974 | -50.53797 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ebf1dbe0-a6a8-3827-952d-e47ebdf7dbcf | -3.48197 | -51.60371 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| ba570115-78cc-38ea-94de-d24a8530c60f | -3.48123 | -55.38539 | 2024-10-21 01:05:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5722e33d-82e3-36b0-ae00-bbb3f798b7bf | -3.48074 | -51.59486 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 95d3305d-b3c9-35b9-8cac-bf7ec7efde8b | -3.4704 | -55.3868 | 2024-10-21 01:05:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ee8fc2e0-c386-392b-8379-cdd44cd12922 | -3.46529 | -52.21546 | 2024-10-21 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 7af30d2f-d0a9-3b57-a271-ba623c9b9924 | -3.45918 | -47.67395 | 2024-10-21 01:05:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 08b99f37-ed8b-3c10-beb0-d9f81fa04db3 | -3.45378 | -52.86951 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bda8ecef-a2af-3fdd-afa0-fd6abc308c33 | -3.45247 | -52.85987 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4c3c9047-5197-3ebf-a7c0-0746819a5c81 | -3.4305 | -51.57225 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3a30966d-a35d-3b1e-ac3b-5cbc12be0d03 | -3.43046 | -49.98078 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 56826bcd-eef5-3b41-b9a8-bdf034a4c688 | -3.42918 | -49.97168 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b66c9d3-a81e-3e11-b874-a534b07581e0 | -3.4234 | -50.32823 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 441313ef-65e3-334b-9103-2130443b117e | -3.41954 | -54.27668 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bca095ea-b7de-3503-9af7-64a3204c2f39 | -3.40411 | -53.18031 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ee5ebdbc-1b1b-3251-9110-6c690e539015 | -3.39645 | -51.24728 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 63ab73ff-d2d6-3bac-b64c-b8f01716ae8a | -3.39547 | -49.73294 | 2024-10-21 01:05:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a08c4cc2-ad1a-3d87-b3cd-7561b7f8e895 | -3.38737 | -50.6654 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e6c8d39e-72c6-36c8-b6b7-17ef78babb99 | -3.38018 | -50.34348 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 49f86e1d-38af-3432-96b5-67ef5fc1ab11 | -3.37076 | -51.06276 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 823f3025-7381-3aa1-8ac6-217418414196 | -3.34181 | -49.01925 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cec9fa98-abb6-3958-a4eb-f5963292bf89 | -3.31404 | -53.37801 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ad55ac5-074c-3285-894f-3a2583f70101 | -3.28052 | -45.7542 | 2024-10-21 01:05:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bfb36a1a-f034-3e40-b3f5-affde248c70f | -3.2775 | -51.05542 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2c100e24-4bf9-36a5-a7a5-0343c5eb209d | -3.27349 | -54.17688 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 14b44fad-3a56-313b-a982-fb04cb15bdec | -3.27222 | -53.708 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ef92fec6-1fd8-3633-b5e4-7d033bf33a58 | -3.27199 | -54.16585 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 01a924b8-678a-3b5b-bde5-62b81838e02f | -3.27176 | -50.22768 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c773ca55-33cd-39e2-a3d2-f456552c9bc5 | -3.26985 | -53.7897 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e110de25-0139-345f-8ad4-ef4482f8f042 | -3.26839 | -53.77927 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| cb609ddc-469c-3184-9a1b-334396e9d301 | -3.26022 | -53.79107 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f0d50b38-8572-31d8-965d-8c3fc1f69ef6 | -3.25877 | -53.78066 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8efbf5df-5406-31ea-9c22-2e1828b685ce | -3.25025 | -50.93968 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1c68cc48-57bc-3e24-b056-fd680827cabb | -3.24207 | -51.7374 | 2024-10-21 01:05:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 844cb4d4-b779-3135-828d-b4217e614098 | -3.23858 | -54.15388 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d9edab87-d5f9-3215-935e-721d0c4b04d5 | -3.23799 | -50.85168 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 72df9016-a8b8-36e8-bc08-94d03c7a7449 | -3.23429 | -51.14807 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b57b3282-b597-33bb-afb5-74824da4ae09 | -3.23307 | -51.13929 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| bffb8509-60b6-37ac-b12c-16ad16fb8149 | -3.23132 | -51.256 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4ea36c41-bbbf-3224-b147-b2f69eb10eba | -3.23074 | -51.72089 | 2024-10-21 01:05:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 08411960-edf1-3878-806d-efe74b59a85e | -3.2225 | -51.25724 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5b8152e2-b88a-352e-a919-d084ff852948 | -3.22127 | -51.24846 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3cc2ad72-35db-3f53-b9fb-319067a8a319 | -3.21661 | -48.61277 | 2024-10-21 01:05:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1993a99e-044b-37ff-8f39-3d1f9d0d10dc | -3.21481 | -54.86626 | 2024-10-21 01:05:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e5ab2b32-1829-3707-b50a-847495e1b29d | -3.21419 | -50.81015 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 0fc7e363-246a-3c5f-90e2-edf8940213a9 | -3.21394 | -51.19574 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f7797828-1b3c-37c7-8ded-a1363ffd7a9d | -3.21311 | -54.85395 | 2024-10-21 01:05:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 89bb0e85-b490-384e-90b8-3b79b8158403 | -3.21296 | -50.80133 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| f88e1ef5-b2f2-344e-af93-97c3cde9dfdf | -3.21173 | -50.79251 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8499169a-9dcc-3f14-9d33-1dcfae495a1c | -3.20705 | -48.61414 | 2024-10-21 01:05:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6963f1d8-f8e9-39d5-90ec-540a39fc0dff | -3.20535 | -50.8114 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bff09382-5dad-32c1-b8b6-b136052e095b | -3.20468 | -51.59824 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 1f536912-3b19-319e-b3ad-1802cf24431a | -3.20412 | -50.80259 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 4551f3ec-f538-36d9-82ab-d436f9956851 | -3.20345 | -51.5894 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 2bb4a35b-25dc-3c25-a129-0ade7e2594e0 | -3.20289 | -50.79377 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| aa691b22-c511-34f3-9552-fe58c26a7eba | -3.15351 | -51.16571 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d9eeddc8-29de-3c96-a718-0063cc6b030f | -3.15229 | -51.15692 | 2024-10-21 01:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3520607-322d-3637-bdcf-5e8d0ef2e8b7 | -3.13493 | -54.28782 | 2024-10-21 01:05:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6894b2b0-c9b2-3c81-a793-2cdca45405eb | -3.12252 | -51.34614 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 25b48785-dcda-33b7-b588-8f378ec58b0c | -3.11146 | -53.12881 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 9481e363-53d2-3a35-8402-96f45dd1368b | -3.11103 | -53.73201 | 2024-10-21 01:05:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f758f9db-1bb6-3fc6-8d11-f30edf668386 | -3.11014 | -53.11913 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| a2b42879-57ea-3e4c-8919-5f7a2c27a076 | -3.1096 | -54.17724 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1953ccf3-5526-3438-967a-5a284b140ecf | -3.10882 | -53.10941 | 2024-10-21 01:05:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| eb02d5e6-89f4-3cb6-a8c9-35ff7cf46cca | -3.10808 | -54.16615 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5d88094e-aa87-3a68-874d-d529b5ace403 | -3.1039 | -51.27708 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bde12719-5716-3556-841a-1a631f8164f3 | -3.10127 | -54.18975 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 2edaca5b-01b9-34fc-ad16-d78fe01c2cf0 | -3.09973 | -54.17852 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 472.4 |
| 90c72f63-980e-3ac9-bb61-e20a79129856 | -3.09822 | -54.16748 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| c536162d-5521-3150-a62a-97d55a028a03 | -3.09673 | -54.15659 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9a45ab5f-5547-34bd-bd3b-8bf15fad6da2 | -3.09139 | -54.19099 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| a03af801-8835-3648-8a9d-88e98f9089a5 | -3.08988 | -54.17987 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 774.0 |
| f7a61906-9952-31e7-894c-9c3795e1efe9 | -3.08838 | -54.16887 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 563.4 |
| 8901bfed-cfe5-3889-9696-12e8d68bcf87 | -3.08689 | -54.15792 | 2024-10-21 01:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 155.6 |
| d42e8691-64d3-3e8b-980b-4141505a911c | -3.08651 | -51.21685 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d0c53dda-db0c-3dad-a8db-ba6a359f58e8 | -3.08625 | -51.27958 | 2024-10-21 01:05:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |


[Clique aqui para ver as próximas entradas](README12.md)
