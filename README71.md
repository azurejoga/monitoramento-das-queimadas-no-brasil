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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e1ef0bb-9a71-39ac-838e-00569b4e0ae2 | -3.29674 | -51.59428 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46e5fd18-5f03-3d95-8478-24d45a12295e | -4.42723 | -48.91047 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa40614c-b199-3f19-a861-989618d5986e | -4.44984 | -43.64899 | 2025-10-28 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 617233c8-6817-3bde-975e-911fe9f2e23c | -1.00215 | -47.65432 | 2025-10-28 05:01:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec1b1e14-d03a-3b76-b3f4-221e96b20691 | -3.11222 | -51.2925 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 816e0c2f-9e3b-38ec-a35b-0bc813d5ddd2 | -3.46122 | -52.87646 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 340e6e2c-bfca-3fce-917b-3626b9c16f07 | -4.92654 | -48.56286 | 2025-10-28 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 516fc4eb-7ec9-3d7b-bd1e-44394293e7f9 | -6.09851 | -44.68121 | 2025-10-28 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 91c1a7b2-006c-3ab0-a053-efa63b324be0 | -3.95056 | -48.09377 | 2025-10-28 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73cfdfc2-b83d-3a2a-9057-5c0d490e1025 | -2.75532 | -47.75584 | 2025-10-28 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1943e6ac-732c-3ae0-aac7-67bfd048f6a2 | 0.40421 | -50.85088 | 2025-10-28 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31f9d329-4b61-3c85-af57-d0c401adfcff | -5.61628 | -45.98365 | 2025-10-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f72a14bf-c62d-31ff-bc2d-05c68f41f4d4 | -4.46447 | -43.23363 | 2025-10-28 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b7e11e12-1510-3fc4-9dbe-584bb7fd0165 | -3.62594 | -51.49442 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e3fca4d-e69e-3ea2-8e8e-3007d728af98 | -4.44079 | -45.97852 | 2025-10-28 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 626e3513-14d4-3e13-a139-e625df3ecae8 | -3.46968 | -49.9776 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae677d59-2e76-3b9f-b949-e0149730a997 | -6.69149 | -42.04064 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9b925c93-f688-3c71-a1d6-2431994261be | -3.58236 | -43.62826 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fb59607-7284-309a-bb76-7093cb815980 | -2.94779 | -54.1827 | 2025-10-28 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d1ef3d7-8cf6-3680-a690-c5d802ef5849 | -5.65374 | -46.45675 | 2025-10-28 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 997f7a92-fa45-389c-a75a-719eaa81eeba | -2.75421 | -45.40001 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e6b32f70-be66-3d00-b49d-ecdf8501f80a | -5.19852 | -46.14983 | 2025-10-28 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b3032b8-3aef-3a5f-a715-a01acf0e7fab | -3.47735 | -55.45809 | 2025-10-28 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bd459ac-ecb5-363f-9529-b951ea72a9ff | -1.50622 | -53.15716 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55e1a02b-ebe8-35ba-8146-5dd8d94db650 | -3.02451 | -45.36703 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9aba14ef-8415-3a60-97e0-465030e05f86 | -4.26668 | -48.69602 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e99d404e-630f-3d99-956d-06090b33403d | 1.62243 | -55.69889 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37a71768-cffc-3c12-b57d-e429f3d7fa00 | -4.19701 | -50.09282 | 2025-10-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4424d47c-29c9-358b-a691-3b6accd9be8b | -4.96513 | -48.26048 | 2025-10-28 05:01:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d453e6fa-ed4c-3574-bddd-f609f16cf5b9 | -2.88296 | -53.99101 | 2025-10-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6b9447a-bbdd-3ec2-be67-2af930dce016 | -3.11098 | -51.29047 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1370d195-be34-3fbe-afc8-794efb46b067 | -6.69863 | -42.04132 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 0cda1182-04be-34eb-9d23-660b11b27b6a | -3.23905 | -50.64916 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49f43d71-948d-3b71-8df5-6e4cd15349b8 | -3.39959 | -50.27841 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9c4f4c6-f073-3777-ad5e-4478d2bf76c0 | -3.79801 | -51.64257 | 2025-10-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aec90a6f-d58d-320f-9aec-bef281d348e5 | -4.87648 | -47.54672 | 2025-10-28 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| efb537d3-6281-3a4d-9a38-b6e6c8671042 | -3.38871 | -59.53772 | 2025-10-28 05:01:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 491d62c8-6d9f-30bb-9923-6da4422486b8 | -3.59657 | -48.99422 | 2025-10-28 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65144fa8-0e49-3f24-ab84-a2b649bbf145 | -3.7037 | -47.64295 | 2025-10-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abe01ac1-0472-3d75-8dff-57e75ed2b97c | -1.98115 | -56.55156 | 2025-10-28 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9a0ac827-0a92-38b2-aedb-aa374fe8e1fc | 1.60768 | -55.71622 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9313788d-4a2c-3ff3-a443-bc802efd8b06 | -2.75474 | -45.39648 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 78187f05-ea9a-339b-93a4-db7c3108d8ca | -5.61079 | -45.98296 | 2025-10-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c7207ad-6de4-3325-bd08-ca03022929be | -3.21005 | -50.81422 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 337acc00-c6f1-32e9-b54f-2351a7360d80 | -3.33306 | -50.74401 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9b6085a-6d5b-3226-b738-b7a316e2b9ea | -5.76693 | -48.64075 | 2025-10-28 05:01:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dba92bc9-5385-327c-969d-fcc93234d537 | -4.7059 | -50.46939 | 2025-10-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e94cb6f5-6b76-3290-845f-8cb4a04853a1 | -3.22531 | -50.73954 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 263355af-6021-332b-be9e-0382bf7e25c0 | -2.91222 | -54.10608 | 2025-10-28 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78198e82-db50-3ab6-b549-26307ed1e9bc | -4.70921 | -48.62603 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd0c55bf-cbb2-3f43-9b56-be2969020b54 | -6.03396 | -46.56696 | 2025-10-28 05:01:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95b1ea3f-6379-3068-82f6-7a95c16697b1 | -6.68348 | -42.04677 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1d4fc223-1d08-3191-9417-28cd0671d4f1 | -3.05956 | -54.61716 | 2025-10-28 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffbd239a-6288-32c8-85c5-9a660b72d863 | -5.5346 | -48.98809 | 2025-10-28 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25f1cf87-a712-39c8-ba4d-d11f8bf74fe5 | -5.48259 | -47.74751 | 2025-10-28 05:01:00 | NOAA-20 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 45ddaf32-5a8d-3546-b9af-02f9ad137fae | -3.75462 | -51.75358 | 2025-10-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 291dff1d-3705-3e7d-a922-12439a0f80a3 | -4.17681 | -47.65244 | 2025-10-28 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c609928-ddcd-3474-a156-aa76ba94703a | 1.89232 | -50.83497 | 2025-10-28 05:01:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7550a36-83e0-329d-b5ad-704f99848f85 | -1.55736 | -55.41506 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96108b2f-53be-3536-bc0d-fdd361341aef | -3.72126 | -47.6554 | 2025-10-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fe3c501-26b4-3949-b0d7-a781b0c7f834 | 1.05263 | -50.97396 | 2025-10-28 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf8844c0-b0f9-3963-b450-c0dccb88a5dc | -4.97431 | -47.81707 | 2025-10-28 05:01:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 122bb1df-6c7c-3d28-98f5-8f5899fcf294 | -5.47189 | -50.15845 | 2025-10-28 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fda0b19-e4e9-3c87-86ca-8838576e1335 | -1.50009 | -53.13058 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d7942eb-1648-3183-aea9-360070c1856e | 1.60144 | -55.72464 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e91108e5-2a55-3ee9-9ec0-58f9745f3272 | -6.68659 | -42.04555 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a70b3565-f57e-37f6-b03b-8646535b20cf | -3.37134 | -50.17881 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cb1c8ae-1b93-38f1-8e52-f40d7715baae | -3.66962 | -51.94581 | 2025-10-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2169aa2-771b-3daa-90f5-030118643952 | -3.53036 | -50.31564 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ca49ebb-808d-3713-b520-9da7c4583fae | -4.90611 | -48.56738 | 2025-10-28 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d039746a-887f-3e57-9b4f-5e223be38ae6 | -6.47842 | -42.23684 | 2025-10-28 05:01:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a439c0e9-faf0-3236-a83a-5da4f838a3a5 | -3.69028 | -60.56286 | 2025-10-28 05:01:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c82c0cac-75b1-3714-8c79-8f08a0ea00bf | -3.58785 | -43.63395 | 2025-10-28 05:01:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90785989-5a4d-3276-9547-426fdb78a9ed | -3.88067 | -47.99751 | 2025-10-28 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b04c0dd6-7311-34df-ae84-9033a5ed8cc8 | -4.18575 | -46.23104 | 2025-10-28 05:01:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae0196af-b5ad-3dfb-8c52-565d42531caf | -4.45729 | -43.238 | 2025-10-28 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 58c90e89-0d47-3f65-9603-71c54ed931aa | -1.39561 | -53.1032 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22a8343d-21c4-38d8-9201-4f40b4b41b79 | -3.58526 | -43.60871 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e252220d-3e8d-30b4-8677-fa66d07b7a77 | -3.70773 | -47.64845 | 2025-10-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 90431718-ead0-3fa5-b4d4-512d440c1f2e | -5.48331 | -47.75082 | 2025-10-28 05:01:00 | NOAA-20 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 74ee4403-b32b-3e05-96e8-515c1ac7ba63 | -2.90165 | -53.13713 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f57582ca-3c2b-30a7-b882-da64b21c1613 | -1.86564 | -54.51828 | 2025-10-28 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e1f68f9-a414-3eed-86d0-938cf950c739 | -2.74173 | -45.40881 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bbe21a7b-9aa3-3b2b-b3b1-ab39e5df49d4 | -3.05367 | -53.01766 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 319dae78-cd33-3d61-901b-0b6793f7050a | -3.24217 | -50.65453 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0b784ca-27d3-33ee-931b-20c05fef44c9 | -2.91159 | -49.81707 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39d4f662-fafe-39cc-bfb2-f774f3965841 | -2.74613 | -45.41667 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e5da064-a214-3ef7-8549-84a9fe143f55 | -1.55681 | -55.41854 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd40f007-271b-3736-9ba6-89e526e43d26 | -3.38791 | -59.54267 | 2025-10-28 05:01:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45bf763f-7b17-3ae3-a095-cf5f2f6d0b8a | -3.13305 | -53.00292 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b72a58f9-43e9-3c42-bdb8-4eb24239f85f | -6.03488 | -46.56051 | 2025-10-28 05:01:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8a53f15-ddaf-36f3-9e23-abe157917a71 | -3.54329 | -49.4362 | 2025-10-28 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f401f61d-c4e9-3941-9ffd-91c35754810a | -4.45328 | -43.65131 | 2025-10-28 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f3c7a3fb-0cf1-3002-b427-9efa42f25ea8 | -3.22434 | -48.77433 | 2025-10-28 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89545f74-35af-385f-9f0a-6e1a99077f42 | -3.24829 | -50.03688 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc800cb9-4637-3539-9947-d63b3681dc4f | -4.25763 | -53.5437 | 2025-10-28 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 726b5615-9c97-3eaf-acdf-2f51b652035e | 1.60825 | -55.71988 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7255f951-95b7-3197-a79c-a1955a608d7d | -3.58717 | -43.63857 | 2025-10-28 05:01:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a030e6f4-22b5-37c9-8816-7bdabc3a8720 | -1.4856 | -49.08151 | 2025-10-28 05:01:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ad938a0-d6e0-320e-ab9c-ed7d41d154f5 | -3.52921 | -53.00147 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README72.md)
