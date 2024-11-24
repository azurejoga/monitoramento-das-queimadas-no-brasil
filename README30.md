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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61851ec9-35a9-35cc-a7bf-5ad44c89e1f9 | -4.6334 | -46.86885 | 2024-11-24 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b69b6956-6969-364e-9899-fcd43f603235 | -3.06544 | -49.20378 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 614cc3fe-5bc4-3ed4-8088-aa934ec3289f | -3.49568 | -49.93338 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10b714ac-8be8-30ff-8a13-f43eb6ab5280 | -4.373 | -49.75585 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cbeb720a-5688-3a95-8326-8cc13d0adb58 | -3.11834 | -45.27919 | 2024-11-24 03:57:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cf043f0b-d035-3e35-8aa1-9caeb3dbeccd | -2.85645 | -43.56011 | 2024-11-24 03:57:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69a0a036-fa40-3891-a266-6bb31577e492 | -5.0771 | -44.16642 | 2024-11-24 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb8159ff-5d64-32e5-9c23-028b1e6f9dd5 | -4.43489 | -45.40466 | 2024-11-24 03:57:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b1948da-65ea-3168-9794-74a5e63c23a0 | -6.39365 | -44.27947 | 2024-11-24 03:57:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ca7c220-9b4d-317f-8e06-e799fd8f1d49 | -7.47997 | -37.84616 | 2024-11-24 03:57:00 | NOAA-20 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d5876b3-90ae-3330-adfd-f581fba6cf77 | -4.08953 | -46.83003 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30fb6c03-c744-3598-9873-955c0a0a33f4 | -4.99878 | -42.94515 | 2024-11-24 03:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad2f5110-fc9f-3827-af64-372a8564a506 | -3.70494 | -47.6098 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bc85c0c-090e-31b8-994b-aab7f1148ad2 | -3.95224 | -45.99691 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e84adf84-47ce-3ab4-b042-2f14b2a66fcb | -2.43938 | -46.13726 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23ca0ed1-68e9-3238-b05f-d158e6a207fa | -3.70038 | -47.60599 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| acadbd45-e56f-32e8-bb14-dbaa7b091057 | -2.70556 | -46.11373 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bffe6847-f57c-368f-be9e-2e0fdf9a3eb5 | -3.03462 | -49.45525 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ad460e37-abae-3af3-a18f-4d550c87dc68 | -4.19593 | -45.36427 | 2024-11-24 03:57:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc7c0744-eebb-3d86-831a-21d8fd7e5ef7 | -3.47429 | -51.99942 | 2024-11-24 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| beaf6099-3975-31c2-965d-4e56c9c8a6f6 | -1.59618 | -52.59361 | 2024-11-24 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 09f12428-45c0-334d-9f54-8488f5ffeeff | -4.41928 | -49.69339 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d738e203-8d75-328c-8e49-e11157b1bf7d | -4.69763 | -45.85418 | 2024-11-24 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed2a5d77-b721-3c38-8b05-f35b81d75058 | -1.79313 | -45.71602 | 2024-11-24 03:57:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 192474dd-dee4-3bcf-b010-c4424680b504 | 0.42126 | -50.85839 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05c241e9-4495-3e21-9d61-1783407ebf53 | -2.53972 | -46.4024 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74a5686f-79b3-30e7-a995-03a081bf5dd1 | -3.86546 | -44.18391 | 2024-11-24 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8bd2efc1-3b14-3907-9983-23f42e15ee3f | -4.2153 | -50.41164 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5c0e889c-1fd7-3813-918e-789f650b0148 | -4.73272 | -46.50836 | 2024-11-24 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e73cdf6f-8a55-32f1-8217-7018f5e54472 | -5.94707 | -48.05469 | 2024-11-24 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09f7d217-6e98-3cb0-abfc-179cbe8d9347 | -4.52927 | -42.90567 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a83eb33c-4390-36f0-9d14-5b3783dde075 | -2.22186 | -46.39027 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fb23386d-f088-3e97-94c1-1d05cd105104 | -3.64069 | -50.23051 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6acfc65-2ff2-32c8-b2eb-9e8b06b1e9ab | -3.0898 | -51.32766 | 2024-11-24 03:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e0ad8b62-fbad-31ef-a63c-d683091fba9c | -3.63839 | -50.23266 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87198915-21fd-312c-b22a-6b2ccc42cfb6 | -5.48676 | -46.24057 | 2024-11-24 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9130416e-e71c-30c1-a9f0-7bb94aad9120 | -2.57694 | -51.88602 | 2024-11-24 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d3f32bc-881d-343b-a663-055c07db45ce | -2.70858 | -46.26921 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84509e92-1c67-3003-b4a8-7ea45b044a67 | -6.05713 | -44.04495 | 2024-11-24 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e0785c86-5274-3c9b-8861-24aeca18a912 | -2.46052 | -49.03865 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 344edb30-032c-32d2-8894-639a118cccca | -3.12696 | -52.98902 | 2024-11-24 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f807e4d7-a6e7-38ff-b7ed-12e8af0bba45 | -4.23659 | -48.71004 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c75309a8-915e-3418-8d79-709238d1208a | -4.21482 | -50.40449 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 74a6e84c-fa58-30ec-9897-ce70a602a5e0 | -2.14331 | -46.7471 | 2024-11-24 03:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb3dcf99-3b19-3062-bf56-03076a79208e | -2.20462 | -48.91924 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 93965601-00d7-39b2-8537-17cdb01e6083 | -1.83352 | -46.64468 | 2024-11-24 03:57:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36d56830-0651-390b-853b-6b2cbafd7fcd | -2.71326 | -46.26995 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64f05c3e-3cc0-38c3-8f50-6534dfbed46b | -3.55172 | -44.98223 | 2024-11-24 03:57:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8c89ba44-543e-3ff5-a72c-ced7f34e3caf | -5.38072 | -45.76585 | 2024-11-24 03:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcfdb465-9ced-3c20-8f7c-a65cefc451cc | -2.55406 | -46.55216 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09154076-c60f-3b63-8d37-9e1625feb21f | 1.77578 | -50.95838 | 2024-11-24 03:57:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b405913-bd8d-342d-a263-93d27ec811f9 | -2.68479 | -46.16199 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff1c464d-aff7-38a4-8df7-ff6f347eef2d | -3.38983 | -50.32846 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b947504f-22ee-3541-b705-7039373dfed2 | -5.25977 | -43.0215 | 2024-11-24 03:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdcd3cfd-d0d5-36cc-9d09-a78e11a533fa | -2.13206 | -46.40172 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f641392f-bbef-37ba-91cd-5ac038e34624 | -4.31364 | -43.19852 | 2024-11-24 03:57:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb5178de-68f0-3a7e-9773-5b39647ccab5 | -3.24402 | -50.66733 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b90fdc5-c762-396d-8f2f-aae1d7dc24a2 | -2.79702 | -46.80288 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 184316f7-cce3-35a5-97d9-076fdc02152f | -3.70184 | -47.59722 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 792cd764-38c7-380f-880b-8ec78ffe0fbd | -2.0737 | -47.06936 | 2024-11-24 03:57:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8090cfe4-4292-3cf3-bbb5-f842746eaab2 | 0.41155 | -50.85474 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bf4e8a0b-ad26-394c-812c-110d17e7858d | -4.02689 | -46.67581 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bcffee7-cf20-3129-b70f-68883979a73e | -1.04894 | -51.74811 | 2024-11-24 03:57:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 604963a6-bb5d-3797-97ea-85e29c974962 | -4.20879 | -50.40352 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3135f311-c572-3b4c-9cc3-ffac54ec598d | -4.60778 | -45.49492 | 2024-11-24 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc31d5af-2546-3f17-9264-c7b9a92b344a | -2.00352 | -46.29024 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05ecf7d1-10b5-31cb-95d3-28fed8886e4c | -3.57921 | -41.95442 | 2024-11-24 03:57:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 97b057ef-dfc5-3470-bf34-4de91ed1b5c9 | -3.60784 | -47.51435 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0ba92cbc-23e4-3200-b40c-937e97e7b544 | -3.29637 | -45.73105 | 2024-11-24 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 017353cd-7573-3814-907d-534d33899c4c | -1.7648 | -52.17152 | 2024-11-24 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35343c20-6671-3c6c-bffe-727ca3898364 | -7.06592 | -39.20104 | 2024-11-24 03:57:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 5064e909-c262-31e0-9c64-c5758328fe19 | -6.57413 | -42.39278 | 2024-11-24 03:57:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 38539110-4741-3ac8-ad33-23a634c3d818 | -3.07112 | -49.20473 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 35ec4124-9d85-3d3b-8c84-d7a63204a01c | -4.18039 | -45.62521 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aba0b2e0-93a5-3c40-8a1b-ff8af48e59a2 | -2.64366 | -46.57498 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4846c26d-dbeb-32fe-a445-4b31517836d3 | -4.48319 | -48.11472 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1156ef45-92c5-3fea-a047-540a1641106c | -5.19552 | -46.13908 | 2024-11-24 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7dade43-b28d-33fb-b490-b5ac92f9e8a1 | -2.73645 | -46.09922 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09c43e17-279b-39e2-b483-0a225f9248a8 | -3.29418 | -45.72824 | 2024-11-24 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6ee3ec04-2a77-30b0-8ba7-7198f9fa6fbd | -2.86063 | -48.4402 | 2024-11-24 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b69a511e-8341-3ad2-833c-5ef9e4b2bca0 | -2.28933 | -49.20298 | 2024-11-24 03:57:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bd25928-60c1-36f7-b9d6-88a96d5b0432 | -4.59942 | -44.72641 | 2024-11-24 03:57:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 190ae512-c5fa-3c73-9900-a0af48f23cf0 | -2.91494 | -45.36583 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c0d19f5-14da-3307-89c4-bbb583cb585d | -3.13044 | -45.37415 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6dc2b8d-5b91-3d24-b1c8-76f132f5a72c | -2.8691 | -45.83558 | 2024-11-24 03:57:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 01cbbf8d-4511-3b24-8dd2-19a633a82199 | -3.49818 | -50.47191 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31cfa0ce-9fd2-315b-b9e4-2a9f69338f09 | -3.77158 | -43.09771 | 2024-11-24 03:57:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8669d381-563d-31e0-bc72-cd48f5dd619f | -3.9793 | -49.93235 | 2024-11-24 03:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0351cd66-98f5-3680-9444-7f3ca7b17a64 | -2.22107 | -46.39527 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fe1967eb-490c-3d28-ae57-124ecb1cf3d9 | -1.27248 | -47.86982 | 2024-11-24 03:57:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba485920-e2c6-3662-aa8a-857ebee59405 | -3.04036 | -49.45636 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4236c81a-a787-383d-a200-6f4ec52788dd | -3.35198 | -50.51483 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c8b0b948-7dab-317d-b90b-8d387b7eba0c | -4.0172 | -40.71811 | 2024-11-24 03:57:00 | NOAA-20 | PACUJÁ | CEARÁ | Brasil | 2309904 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6523e2d4-8f13-35b2-8783-5b709086e3ff | -3.63536 | -52.25822 | 2024-11-24 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 563d0491-c9c5-3155-b313-98d3edb76d27 | -5.84556 | -40.802 | 2024-11-24 03:57:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0f9e6b51-81e0-3365-a0d4-95c736adf2e8 | -4.079 | -46.83076 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71a1beb9-28cf-3f6c-8ad1-93c71f972d16 | -3.94562 | -46.8967 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf91769c-5d8e-3508-bc4c-d117231ecaf2 | -5.08101 | -44.16707 | 2024-11-24 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04e612b3-908e-38cc-bbd6-125fe2746427 | -5.94758 | -48.05179 | 2024-11-24 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c81d895-52a3-38db-830d-f814c39d3a33 | -4.42253 | -44.11599 | 2024-11-24 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README31.md)
