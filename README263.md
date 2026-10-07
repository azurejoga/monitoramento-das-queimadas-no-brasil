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

## Dados Diários - Página 263

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9717fb0-7c87-3d63-8de5-cfbd1756d9e2 | -3.6931 | -40.8572 | 2026-10-07 19:40:00 | GOES-19 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 0abb22cc-f5f4-3954-a539-3d05661f29d4 | -8.6291 | -67.0482 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 3ebf5441-4301-3455-aed7-91def9640006 | -5.8799 | -45.9761 | 2026-10-07 19:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0185d12f-033a-3de8-a464-d72383f1d3f7 | -6.1431 | -47.9214 | 2026-10-07 19:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 3e289e9b-f79b-3780-91da-9f3ad545bdfb | -5.7659 | -42.0389 | 2026-10-07 19:40:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 4d904994-544d-3159-b33a-d61c208624d9 | -7.6767 | -72.3142 | 2026-10-07 19:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 188.0 |
| bb2fa9ea-ab6f-3750-98a6-06a4bb59c6f6 | -3.5684 | -54.4946 | 2026-10-07 19:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| b2d2da3f-486c-36bb-8bd8-32c970fbe34e | -3.7166 | -54.2096 | 2026-10-07 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| bd64f91e-5ecb-35ed-9134-1fb1aeda040f | -13.3671 | -43.8742 | 2026-10-07 19:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 326.3 |
| feab33b1-6f88-3b48-be1f-146d8c3606c7 | -6.1429 | -47.9432 | 2026-10-07 19:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 168.8 |
| bd7b8edc-9c0b-3a00-89b2-478236a00947 | -6.8667 | -46.415 | 2026-10-07 19:40:00 | GOES-19 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 5af221e4-eaa2-3979-beed-7f1814a49eaa | 1.7121 | -55.6063 | 2026-10-07 19:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f0aa2452-449a-339f-8571-3574f5e0ffc0 | -11.2333 | -44.8678 | 2026-10-07 19:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 640a6797-e3b4-3f70-a46f-3aac0db32ac1 | -3.1951 | -42.9538 | 2026-10-07 19:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| e39233e2-00a1-3ad2-8e45-5ea9046172b2 | -9.5469 | -64.8008 | 2026-10-07 19:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 9f45e189-b22f-3619-83ef-33834a601569 | -8.5183 | -67.0139 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 375d9ef9-4469-34ca-8024-a82c006e8cc8 | -1.801 | -57.1161 | 2026-10-07 19:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 8044a1dd-ac58-3ab9-bff3-ad9833d54e06 | -7.1827 | -52.6078 | 2026-10-07 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 54824e1d-5608-3e27-8e9d-e2bd31ad2a29 | -2.6859 | -49.0325 | 2026-10-07 19:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 3ab26bb2-928c-3937-b1d3-927bffabdfdc | -11.7335 | -43.649 | 2026-10-07 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2c7a12cf-dffd-38fe-93dc-6d87017515c4 | -8.5184 | -66.9954 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 6579e6b2-247b-3a4e-b9cd-e0ded9da3421 | -3.269 | -51.0575 | 2026-10-07 19:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| e6fadd76-b64e-3130-8561-9ee68a14f190 | -8.5912 | -67.3084 | 2026-10-07 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| b59c3c1a-42f0-36dd-a3c6-694ffe09e5a9 | -3.2214 | -53.8818 | 2026-10-07 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0318ad0c-85b6-32af-a287-3e057bbf6249 | -4.7769 | -55.7302 | 2026-10-07 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 615aac53-1188-35af-bacf-c35db98d943a | -6.3003 | -43.0821 | 2026-10-07 19:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 257fef68-824d-332b-8118-354cd802e709 | -3.55 | -54.4952 | 2026-10-07 19:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 83895178-5b12-3eaa-879d-3f34a10cd032 | -7.3937 | -46.1921 | 2026-10-07 19:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a7853d68-cb7f-3f4a-819b-843fa6eb511d | -8.6106 | -67.0486 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 16b069c8-943f-3a8e-bfdc-44e8d800d532 | -7.4697 | -42.8315 | 2026-10-07 19:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 168.5 |
| 8dc49185-677c-3997-896f-a4d13a98e58d | -2.9996 | -54.2491 | 2026-10-07 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e51dca51-c772-3f5e-a216-6f2a558df30e | -11.1119 | -47.644 | 2026-10-07 19:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 76868325-8e3c-33f1-963d-a5b4ac74ed34 | -3.1972 | -50.5592 | 2026-10-07 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 513.7 |
| b763b794-b300-30bf-8e5f-f5205557c055 | -7.6583 | -72.3144 | 2026-10-07 19:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 9477eb72-f53b-37c1-a020-523612243061 | -4.3044 | -50.7909 | 2026-10-07 19:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| fae9f636-712e-3831-8df4-fc5f947a7b60 | -9.5468 | -64.8196 | 2026-10-07 19:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 116.4 |
| a79c507c-dbb0-3dc6-851f-6131e71eb913 | -3.0917 | -54.1666 | 2026-10-07 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ccaaa781-fbeb-38cf-890e-82de0eb8987e | -6.6599 | -52.9675 | 2026-10-07 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 8ea7c4c6-3658-3c7b-adfd-6a0b69ceca26 | -6.5853 | -53.0127 | 2026-10-07 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 93904ecd-90e1-3f0e-8d60-e69c103f84e9 | -2.9271 | -53.9295 | 2026-10-07 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| fe824fce-8abc-33be-9924-40030dbc0da2 | -3.3133 | -53.8793 | 2026-10-07 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 4e982277-4b9a-3368-b1d3-df8e44935d21 | -6.0075 | -53.5122 | 2026-10-07 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 3c3ec85f-47e9-3996-a3ba-a6e13e37efe0 | -3.4947 | -50.0877 | 2026-10-07 19:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 425f6de2-c6da-39ae-a19b-80ddb914a35a | 1.7488 | -55.5861 | 2026-10-07 19:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 67b08612-7b26-348b-be1f-ebdaae676148 | -3.5865 | -54.5742 | 2026-10-07 19:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| fcba7853-29fb-3851-b515-0a9f456a2a63 | 1.6937 | -55.6263 | 2026-10-07 19:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 690b7581-8b88-3c69-a276-b846dd888519 | -4.2859 | -50.7916 | 2026-10-07 19:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 08fb9dfa-e934-3043-84f3-63c02c1c0d52 | -3.2199 | -54.3038 | 2026-10-07 19:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 8c3a8505-67e5-3c77-bf16-4ebf7d52cdb7 | -3.0731 | -54.2473 | 2026-10-07 19:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 25b47fae-fb20-36dc-b5f3-8a1b016348ed | -3.8037 | -47.4839 | 2026-10-07 19:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7f3e2d03-08c7-30aa-bc09-aabffba4d951 | -9.507 | -70.4439 | 2026-10-07 19:40:00 | GOES-19 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 109.3 |
| d45c6c1b-c01a-3def-b2bd-bcec9217c42b | -3.1788 | -50.5388 | 2026-10-07 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1a2f0fbe-7106-3ba6-9eb5-63ff0cee5674 | -3.2268 | -57.8696 | 2026-10-07 19:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 10301011-5826-32c1-8349-ea9c8499397c | -3.1973 | -50.5382 | 2026-10-07 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 190.1 |


