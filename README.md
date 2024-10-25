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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2ba1197-df66-399d-a461-d3839dde4979 | -1.0445 | -47.6237 | 2024-10-25 00:05:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1b791d81-1d96-3eeb-984c-30f41d71766c | -1.0446 | -47.602 | 2024-10-25 00:05:11 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 4881ed94-69ad-3568-9cba-78421bf37cb1 | -1.165 | -53.6773 | 2024-10-25 00:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4f924d2a-fa1b-31d4-99ab-264d18358931 | -1.165 | -53.6571 | 2024-10-25 00:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| bb2c31df-7c92-3e65-a36d-89231edfd56f | -1.1834 | -53.6771 | 2024-10-25 00:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5cd1d809-3b28-3878-bf3c-18a65bc1e906 | -1.1834 | -53.6569 | 2024-10-25 00:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 39a4a30d-b5b3-39fa-afcb-7c470afc8ccf | -2.6192 | -52.4564 | 2024-10-25 00:05:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 20cec262-ae16-3398-aa88-1e14a71b1d92 | -2.6193 | -52.4359 | 2024-10-25 00:05:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 60bf2128-8813-3cea-a041-a008ac80851d | -2.6297 | -49.247 | 2024-10-25 00:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| ce486245-3f78-3d49-bf29-b04ac141dd01 | -2.6482 | -49.2465 | 2024-10-25 00:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| a6689be1-d926-3339-9042-7fb5ccde0930 | -2.796 | -49.2636 | 2024-10-25 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 170.4 |
| 2c43e003-9672-3914-a99d-165e0554b916 | -2.796 | -49.2424 | 2024-10-25 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 247.9 |
| b83500bf-3f64-3e13-aaea-258dc2850582 | -2.8144 | -49.2631 | 2024-10-25 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 228.6 |
| e88860d4-92b1-386d-950d-621fcb2f803f | -2.8145 | -49.2418 | 2024-10-25 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 324.0 |
| b3fa1c1e-f824-37df-9936-ec91b751c82e | -3.0607 | -40.0333 | 2024-10-25 00:05:22 | GOES-16 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 62.3 |
| b0a7fb02-e1b7-3a51-828b-eb3be721eb48 | -2.9578 | -50.4198 | 2024-10-25 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| cc048290-042a-309b-aa49-fcd8d4aab26a | -3.1071 | -45.7232 | 2024-10-25 00:05:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e7dd0668-1ab4-3df8-96e9-1e8c5fc1459e | -3.1072 | -45.7009 | 2024-10-25 00:05:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 2372efb3-3c46-35b1-8207-12faf5c954c5 | -3.1258 | -45.7002 | 2024-10-25 00:05:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| d8d2609f-af1c-3d2c-aa46-98d5d54ea288 | -3.2368 | -45.8077 | 2024-10-25 00:05:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 104.5 |
| fa40d881-6017-37f3-82b1-db38acbd3075 | -3.2552 | -45.8293 | 2024-10-25 00:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 0ebd7e8b-430b-3009-b260-e10174d7e22c | -3.2553 | -45.807 | 2024-10-25 00:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 322.3 |
| fe803264-7468-3eab-92d6-159f82d05f26 | -3.2554 | -45.7846 | 2024-10-25 00:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| d6ebbf80-3688-3e57-894f-33cf7a37ce01 | -3.3124 | -49.5235 | 2024-10-25 00:05:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 0ed326a4-0061-31a8-867e-c0580988a18c | -3.4047 | -49.5415 | 2024-10-25 00:05:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 0acdd6f1-503f-3c25-bb7b-dc13a9e20b42 | -3.4048 | -49.5203 | 2024-10-25 00:05:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 28064c95-4ad4-33fe-be42-1cb690b4db67 | -3.4605 | -45.6645 | 2024-10-25 00:05:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 127.3 |
| e35f80b3-f0c2-324c-be2d-a3fb98c1eca7 | -3.4606 | -45.6421 | 2024-10-25 00:05:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e9500f07-3e11-3d95-bdb5-c002251bdc71 | -3.4791 | -45.6637 | 2024-10-25 00:05:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 259.3 |
| 596649e4-b6a5-3a55-9a04-e820ca32075f | -3.4792 | -45.6413 | 2024-10-25 00:05:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 333c5a5c-30a3-3c90-93c8-d7feb2ad3ec9 | -3.4951 | -54.4366 | 2024-10-25 00:05:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| f57d9d94-1fde-350d-a7f0-91b3fe7c8ec0 | -3.5088 | -51.0706 | 2024-10-25 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 125cfea3-d579-3962-8bbd-9b1a10a48595 | -3.6831 | -53.4243 | 2024-10-25 00:05:26 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 57a925e9-839c-3bdf-a4ee-8b5d5663f82b | -3.9394 | -46.445 | 2024-10-25 00:05:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 0bf43531-6692-30cb-a7c2-48c4e1d1b267 | -3.9396 | -46.4229 | 2024-10-25 00:05:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 7c1eb5af-6df5-353a-9c0c-d16c05f2bacc | -3.958 | -46.4442 | 2024-10-25 00:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| d62c83ef-4b5c-3feb-ac95-49154c5dcba9 | -3.9581 | -46.422 | 2024-10-25 00:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 108.7 |
| bed05e16-b170-303b-a872-a465e67a9bf2 | -4.2243 | -48.5482 | 2024-10-25 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 2ddb99d9-64ed-305a-b904-3afce31104ce | -4.2427 | -48.5689 | 2024-10-25 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 3672604d-3cb4-31d8-ae91-79a41bdf050f | -4.2429 | -48.5474 | 2024-10-25 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| f3f8edbb-5297-36bf-bfa3-a8c788dbacd2 | -4.244 | -48.3535 | 2024-10-25 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 77644b5c-525d-3048-a3be-5c5fea44c51d | -4.2441 | -48.332 | 2024-10-25 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 3bbf483a-4e99-35b0-9bca-f929082acc87 | -4.2625 | -48.3527 | 2024-10-25 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b1366080-44eb-38af-b470-edc363d99dfc | -4.2626 | -48.3311 | 2024-10-25 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 356c7db0-a68f-3a10-b565-7ae58dd053ae | -4.5045 | -48.2117 | 2024-10-25 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 49043c8d-2e92-3e60-9ec0-b45bdfebb6fc | -4.5371 | -46.0373 | 2024-10-25 00:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 6990df06-627c-3c7e-94dd-1b901e9cec9d | -4.5614 | -48.0141 | 2024-10-25 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| b4ba494b-05db-3cfb-9fc1-421d474f04cf | -4.58 | -48.0132 | 2024-10-25 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 939d73a3-eb8e-3a3e-84cb-b2cc11886aa1 | -4.9208 | -49.8378 | 2024-10-25 00:05:33 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| cf221e23-ac7c-3d15-8010-9709f5697621 | -4.9209 | -49.8166 | 2024-10-25 00:05:33 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| d32dc5d4-b7b2-359e-8671-82d1c019a781 | -5.6403 | -47.9104 | 2024-10-25 00:05:37 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ea2a525b-3bab-36b8-8237-2adaaa6943c4 | -5.8918 | -44.6418 | 2024-10-25 00:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 53497dbc-8ca7-3f63-96df-3170b948c988 | -6.5219 | -60.0457 | 2024-10-25 00:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 5eaefd67-910c-3afe-93bb-ebde9bd27692 | -6.522 | -60.0266 | 2024-10-25 00:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 368881f6-d7e3-393f-87bc-50d3ae0fafd5 | -6.5403 | -60.045 | 2024-10-25 00:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| dae35781-860a-3fba-9fae-a1733ec45701 | -6.5404 | -60.0259 | 2024-10-25 00:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 6a2aa9c4-97ff-31b0-b700-4fa47bdff3c2 | -6.6472 | -47.8642 | 2024-10-25 00:05:43 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| bc8467d5-8f35-3f87-b0a0-9238e49eb64c | -7.2736 | -64.6681 | 2024-10-25 00:05:47 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| fb3a330d-0043-3d7b-abd9-76d6c5f50643 | -7.2737 | -64.6495 | 2024-10-25 00:05:47 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| ba2fa9df-fa90-3def-9f15-179e57fdbba9 | -7.9046 | -63.7129 | 2024-10-25 00:05:51 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e7205bc2-910b-35b9-b9d6-66547d49ceed | -7.923 | -63.7123 | 2024-10-25 00:05:51 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 7b2f207d-f3b4-3426-adc7-a51ba14cd418 | -8.0313 | -49.6341 | 2024-10-25 00:05:51 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2a20605a-e7fd-353a-b507-eda339134ef7 | -8.9064 | -48.544 | 2024-10-25 00:05:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 111.1 |
| f66dc5b6-8bda-34f8-ae6a-c380ac932958 | -8.9066 | -48.5222 | 2024-10-25 00:05:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 49420e72-dd64-3635-84f8-b9fc2eac92b7 | -8.9244 | -67.1889 | 2024-10-25 00:05:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 76cb244a-c12d-3713-9035-e1a3c0659909 | -10.6519 | -47.9207 | 2024-10-25 00:06:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 3a098c4b-5124-3150-a813-de15fd516026 | -11.632 | -48.4617 | 2024-10-25 00:06:11 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 81193091-dae3-3c0d-862c-a2648bee9211 | -11.883 | -56.4152 | 2024-10-25 00:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| f8234672-b2c6-3b12-b15a-dd3e55f069ee | -11.8833 | -56.395 | 2024-10-25 00:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 58e748ae-b2b7-3951-9ccc-1dfc17b6d026 | -11.8854 | -56.2138 | 2024-10-25 00:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| da9edcec-e184-3932-bad4-fe93f0a2c373 | -11.902 | -56.4135 | 2024-10-25 00:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| eb1da849-8793-3851-b011-57435ae22fae | -11.9022 | -56.3934 | 2024-10-25 00:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| b558d910-d666-3f0f-87f2-cddf2d1aa416 | -12.0444 | -63.1547 | 2024-10-25 00:06:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f0689b1e-6906-3019-b4a7-b13635375910 | -12.0445 | -63.1356 | 2024-10-25 00:06:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c7bdbc60-7e02-3e33-8ea6-d7715dacb2df | -12.3782 | -63.8821 | 2024-10-25 00:06:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 546d1af5-d0b4-3648-918d-de1d262dc940 | -12.3783 | -63.863 | 2024-10-25 00:06:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 93bb7ead-e89a-341a-b40d-09969fef0df7 | -12.3971 | -63.8811 | 2024-10-25 00:06:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| bbc302bd-c26e-32b0-af08-e5571c230442 | -12.4589 | -63.1895 | 2024-10-25 00:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 94.5 |
| c32996f2-1f20-30d9-803b-a550a1855d6b | -12.4591 | -63.1704 | 2024-10-25 00:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 7285822c-b61f-326b-94c3-09d8e29c0f1c | -12.478 | -63.1693 | 2024-10-25 00:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.3 |
| ada2c8f4-f6fa-3635-acfe-e5d36c0fde3d | -12.5167 | -63.0521 | 2024-10-25 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| bb1b594e-a79e-33ba-9c39-582674223d7c | -12.5356 | -63.051 | 2024-10-25 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 43d50468-0eef-3cfc-b809-0edf3f61b43d | -13.4769 | -61.6217 | 2024-10-25 00:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c2b04f2a-177a-357f-9655-9bf2571b7e36 | -13.4957 | -61.6398 | 2024-10-25 00:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 94c13653-76ed-3faa-9f00-5c03d71e728c | -13.4959 | -61.6203 | 2024-10-25 00:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 119.5 |
| dea0fc8e-bd0b-3232-8f4b-1c50a368b70a | -14.1144 | -44.3072 | 2024-10-25 00:06:24 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 528f8427-5c04-39d3-a028-fd1108f7f822 | -15.6836 | -59.734 | 2024-10-25 00:06:34 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 6ab3e560-7265-3370-847d-5d7724c17b54 | -16.94 | -57.5268 | 2024-10-25 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.0 |
| ee5659ce-a4ad-315b-b317-def843f86ef3 | -16.9596 | -57.5245 | 2024-10-25 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.1 |
| 06c70e1f-c43c-3616-b251-35fb37d91d50 | -16.9792 | -57.5223 | 2024-10-25 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.2 |
| ac5b8c15-6e54-3a03-a61c-b4318933b7fa | -17.0184 | -57.5178 | 2024-10-25 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 10b3db0f-8671-3762-b327-238aadd88a29 | -17.0381 | -57.5155 | 2024-10-25 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| 587a1d55-81c0-39e9-a48e-5ee24c53f2f9 | -17.0384 | -57.495 | 2024-10-25 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 502ad2a2-c6dd-370f-bbf2-3b6c620103da | -17.039 | -57.454 | 2024-10-25 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.3 |
| 04783930-1ccf-3f14-87aa-6264d63c6224 | -17.0583 | -57.4722 | 2024-10-25 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 4bb68374-eac7-31ce-bf42-dc6cb4310e3f | -17.0586 | -57.4517 | 2024-10-25 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.5 |
| 3337999e-c718-37e5-ac9a-bc2e055d4cfc | -17.059 | -57.4312 | 2024-10-25 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| e61280ef-d9ce-33b3-95a4-26a892348c63 | -17.2186 | -57.2485 | 2024-10-25 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 2adab892-ddfe-3d71-ac09-538a25160052 | -17.2537 | -57.5108 | 2024-10-25 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.1 |
| 1d015d1e-b289-3262-92a8-f0b2075c9df6 | -17.254 | -57.4903 | 2024-10-25 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |


[Clique aqui para ver as próximas entradas](README2.md)
