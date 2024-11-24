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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98372988-174f-30c1-9079-43764aeaf4fb | -4.48963 | -45.49139 | 2024-11-24 00:49:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 454e6873-3c37-39eb-afb1-e531603cfea5 | -3.29735 | -49.91034 | 2024-11-24 00:49:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 920e03f5-11fb-331a-b958-12d87f70cb6f | -4.09499 | -50.37236 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 7172bb86-2c9a-3300-9634-ab07de32e51b | -2.91536 | -45.36021 | 2024-11-24 00:49:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 366.0 |
| 64c6e250-0f75-3175-934c-fc438272c741 | -1.41942 | -46.0597 | 2024-11-24 00:49:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5756a5ce-620b-3078-805b-ca4d7241db2d | -4.48813 | -48.11861 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 9f7954fc-cdf6-3777-a3df-404db6e78caa | -1.94644 | -49.51854 | 2024-11-24 00:49:00 | TERRA_M-M | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fe4d1d7d-66e3-3e70-b4d8-deebb774cee4 | -3.77332 | -44.04698 | 2024-11-24 00:49:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 5bacede2-0f77-332f-90f0-85dbed045a79 | -2.87202 | -45.84341 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 678ee429-f6d9-39a8-aa40-ce540b6a023a | -1.60753 | -54.40423 | 2024-11-24 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 84833e34-a3c4-39b4-9278-98afdf58c2be | -0.88079 | -52.75901 | 2024-11-24 00:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 178.0 |
| 386b0c2b-96f1-344e-a6de-41d5b740dffd | -1.35912 | -53.82558 | 2024-11-24 00:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6ee9c79e-dcb2-3cc9-bfb3-e6e16c9af805 | -1.37148 | -53.82392 | 2024-11-24 00:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 9381b543-9dce-3a54-acb8-6bdecba2e17b | -2.58971 | -46.06744 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 2bd82f2b-2461-390a-a35a-d311d238feba | -3.85601 | -44.05262 | 2024-11-24 00:49:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 916bb1f9-5138-3980-8686-30b87eb107a7 | -3.63637 | -50.23094 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f686d3d6-c389-35cd-872a-5101aff8ad26 | -0.3991 | -51.58622 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0f232d92-7365-3841-81f2-360bdc05cf4a | -1.95695 | -49.52682 | 2024-11-24 00:49:00 | TERRA_M-M | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e002b435-4084-3af8-8eb5-ce61117ffd90 | -3.77502 | -44.05864 | 2024-11-24 00:49:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| dbb2bd3f-5085-3ea5-bb6f-f2f99066955e | -3.00183 | -52.50174 | 2024-11-24 00:49:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2e9ce9d4-32ab-3405-b1b6-5f15faee5ac1 | -3.7094 | -47.60927 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d6fdb1f0-e352-32a4-8ef3-ca11236106b0 | -3.93994 | -48.14996 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| bf1111cd-fa6f-324d-a651-0e31631e4fa7 | -2.6811 | -46.25508 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4d18c435-d74a-320e-b622-ad3c586dc1e8 | -3.41076 | -50.38041 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 30b46ddf-73ba-3be1-9fcb-f6a6d13c49f6 | -2.58881 | -46.19225 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3e78189f-96e2-3fca-9bd8-8311779fd21c | -2.70799 | -46.05395 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc1f1dff-3e8e-313f-8d43-a29b692a3b8d | -2.28686 | -47.31721 | 2024-11-24 00:49:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 20690406-610d-3537-b133-42f51a947d8a | -3.60399 | -47.51319 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 665fe819-8877-3c18-b526-382080a3bc7b | -0.25262 | -51.6311 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c37229a5-7bf1-3e35-ba64-91f3c4a67810 | -4.95204 | -47.80664 | 2024-11-24 00:49:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 69b59c87-1063-34ae-b420-3cdab59b4960 | -3.47117 | -47.6881 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5121519b-3ca6-376b-81b5-9519f31ae877 | -2.70048 | -46.1986 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5cf89569-2fe5-34c9-a987-a636163f9a79 | -2.92619 | -45.36892 | 2024-11-24 00:49:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3ad1e9c3-0c32-3a82-a0af-d9d9591b1a01 | -3.23196 | -54.2261 | 2024-11-24 00:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| bb3abaf2-fa40-3ba9-86da-7e67ff1d427e | -4.63393 | -48.84404 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 20a931c3-5310-315e-928b-018b5fa102e2 | -3.47219 | -50.01714 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2532145c-fc61-3e97-abfc-5adedb595283 | -4.05691 | -48.32964 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7777adff-77a3-3a6d-8562-ca92cc4f41d5 | -5.11399 | -49.13102 | 2024-11-24 00:49:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d96f97bf-e742-3414-845e-46e954e1aa26 | -2.64473 | -46.85197 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 189fb02e-9487-382c-8f92-acbb74757fc7 | -3.38771 | -50.73196 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 921afa7d-c2b7-3cc8-9111-87997b9060b5 | -2.62012 | -54.93485 | 2024-11-24 00:49:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 2e9b7e4b-02ba-392d-989f-c6e6dbb1d337 | 0.41787 | -50.85414 | 2024-11-24 00:49:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3c0a5854-b618-3763-8ede-55b84cecc25e | -1.84217 | -46.64516 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 9315fcd7-2341-3358-bd71-9ba1658f7c1d | -4.35419 | -48.68114 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c5aded2a-d8bc-3621-928f-43b1a840fe18 | -4.37642 | -48.5083 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bf01c6c6-b276-318e-ad89-6dc7d82feaba | -3.99148 | -47.72851 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 233b7b37-06c0-3289-8393-2abf502afef8 | -4.29252 | -46.90759 | 2024-11-24 00:49:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8f77637e-0af0-35e5-b3c7-f9114dce20a1 | -2.61743 | -46.19769 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2bbfc149-0cc0-3bbf-b218-4b14c3ab1bbe | -2.38143 | -47.41194 | 2024-11-24 00:49:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 90b1f234-9ba5-3d02-9e4e-a7cb909aa1be | -4.41977 | -47.69149 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 709d343c-c4cb-36fb-9dd7-ef9e40df6381 | -4.24666 | -48.63617 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6df8ab9b-98e3-368b-af89-294c35bf428e | -0.28672 | -51.50609 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f04aa51e-b201-3017-bbcc-15c219b9b035 | -2.19655 | -50.6833 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d90f0407-cfe0-38b0-8128-e4b6c5122f53 | -2.52653 | -45.41982 | 2024-11-24 00:49:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| b82ac4fd-f926-35ba-81d3-2b5127948a89 | -3.24792 | -53.29393 | 2024-11-24 00:49:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| f092190f-62da-3f28-a85b-0809e0c662f9 | -3.04856 | -52.76426 | 2024-11-24 00:49:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0e0cde84-1250-3906-9de3-5f523bb2f399 | -4.07465 | -49.18935 | 2024-11-24 00:49:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fa7d9e9b-4c85-3154-8d98-11dc2c7752a9 | -3.84742 | -44.06012 | 2024-11-24 00:49:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 955d6c20-e6c1-3539-b691-e17d1644e693 | -3.98304 | -49.93113 | 2024-11-24 00:49:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 00ad36ff-e1a0-3016-b126-9500cd0c0b92 | -0.37434 | -51.54721 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ec632e79-e848-3787-9c3b-23ce9a7285d6 | -4.37514 | -48.49909 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 0316ee48-cb9e-304a-abf1-e673a0c407c6 | -2.99487 | -45.4751 | 2024-11-24 00:49:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ee7b6165-9d59-3d4a-b91a-2c5e5c45f60f | -3.13708 | -45.38136 | 2024-11-24 00:49:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 3d1ca432-a886-353c-9475-3b87461e13cf | -3.18877 | -54.7753 | 2024-11-24 00:49:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 7b163854-589a-3469-9b94-fa391095230f | -2.96007 | -45.16019 | 2024-11-24 00:49:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 282c0e97-d7b7-3672-b251-ea4ede6f5e26 | -3.96212 | -45.99917 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c2328f61-7dff-3089-8175-fb03bfc86cc5 | -2.2051 | -48.92119 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| f1daa5d5-c7fd-3cfc-bdb3-cf0c51b6c04b | -4.24268 | -48.67453 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 306c0fe7-b1bf-319a-907f-e6322c4c8c2e | -4.04391 | -45.28087 | 2024-11-24 00:49:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 43428b9e-24a1-39b4-a39e-66d5b30c402b | -2.68477 | -46.15322 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8d9c98be-8085-3cfc-b66e-4fc314700861 | -3.30317 | -50.02552 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad039271-df12-32a9-a46c-1e446fa5cd06 | -3.672 | -45.77132 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 971b4289-47eb-344a-ab7d-1e07b804d87d | -1.87063 | -48.16722 | 2024-11-24 00:49:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 5140daf2-1a71-3ad3-ac96-a3cac0c26133 | -4.6157 | -44.06898 | 2024-11-24 00:49:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 60d17634-5822-32f5-af9c-6e79bd69b87b | -2.3829 | -50.33747 | 2024-11-24 00:49:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 17226bce-5aa4-30f5-b2ab-a323011b4531 | -3.54865 | -51.53984 | 2024-11-24 00:49:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 9b0deff2-121d-3a57-a103-a322eb87676a | -2.73287 | -46.09845 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 7b95a579-7a04-38b5-9824-98d82454cffb | -4.53906 | -42.91921 | 2024-11-24 00:49:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| bbbc875b-0144-3d3f-8942-8961d29db302 | -2.15846 | -50.49578 | 2024-11-24 00:49:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1b123085-4e22-381d-8294-63ea76171c75 | -2.24218 | -46.86927 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9aac39ea-93b0-383d-9310-b9f28e3a4f33 | -4.37924 | -49.75055 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 9ea4e25e-b0d7-3d03-bc6f-c7ef262862b9 | -4.29357 | -48.241 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c159735-26d1-32c5-a52f-e527794ad736 | -4.22173 | -50.40567 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1a7c8565-e346-3647-b49e-040eef1e6338 | -4.11914 | -49.44279 | 2024-11-24 00:49:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| bf046a2e-504e-3368-9769-9c8127646d0b | -3.85825 | -50.05155 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| bedb230c-4c36-3919-bccf-5d539248c8f7 | -3.19989 | -48.58794 | 2024-11-24 00:49:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1b287d7-1b33-3dbe-a226-add86b09fd5b | -4.69984 | -47.18597 | 2024-11-24 00:49:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 90accd43-9e90-3ed6-909e-2fc66b5060f0 | 0.40826 | -50.85279 | 2024-11-24 00:49:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 926ec7c6-992b-312d-a404-363147b8dea4 | -4.10991 | -48.51103 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f3e22b6-b43d-3f31-97d7-ea1a72e3e4da | -3.29666 | -45.72278 | 2024-11-24 00:49:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a5dad8fd-19da-3556-95c1-2fe4923cb5de | -3.06764 | -53.22427 | 2024-11-24 00:49:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 74e4dc90-1e0f-3b5a-bbf3-9027ea0fc3ca | -3.5451 | -51.51371 | 2024-11-24 00:49:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b7474772-1a1c-3f5f-8159-d0202523d4f0 | -4.54117 | -44.5533 | 2024-11-24 00:49:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| eac5d241-ef19-3010-8722-003eb76c3678 | -4.31768 | -43.21619 | 2024-11-24 00:49:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5e8ae70c-5e98-3dbd-b51e-6fe8dc1d1da8 | -0.95162 | -51.65008 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c699e938-a22b-39fb-9942-610c694f9f8f | -4.35786 | -45.27786 | 2024-11-24 00:49:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 4d06e783-4286-36eb-a7d3-7d903689dfb2 | -2.67073 | -46.24711 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1db1ec43-7457-37e5-b6ad-f2c39baef679 | -3.31598 | -43.51091 | 2024-11-24 00:49:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 440753cf-c5b6-3ce5-a633-3af85b1e6383 | -3.9579 | -50.20176 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 68a70bcb-ed49-342c-ba5c-b9fea32661bd | -2.43191 | -46.51564 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README16.md)
