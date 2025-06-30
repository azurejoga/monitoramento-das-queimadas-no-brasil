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
| 1b5fd109-ab0e-3210-9f47-143c77527d80 | -10.80189 | -44.25037 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 64928377-acb5-3077-b21e-0b5571e1fff1 | -10.80306 | -44.24463 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 1f0e2ec0-8afc-36b2-9f79-7bb0cf3ebdfc | -10.79601 | -44.25134 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 4d270f8e-1889-3fdc-bc83-ab41163c578e | -10.79827 | -44.23988 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| edbc74f7-77b8-3982-8b2e-52d060479f81 | -10.79714 | -44.24562 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 0e3b3a63-dd8b-38d4-ad72-3783accaf753 | -10.80597 | -44.2353 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 66f2a631-ca7c-3c4c-bb48-c223c005cda7 | -10.79654 | -44.24326 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 541c3204-482b-3bd4-90f8-7efbc5b4a0ec | -12.75731 | -44.40528 | 2025-06-30 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba8bf7fa-0fde-3053-ab87-6f7a48b78254 | -17.70592 | -42.72371 | 2025-06-30 03:25:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 767bc26f-9972-34db-81b8-3aaa7b0ed2e8 | -10.80425 | -44.23879 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 67e0fa36-56b6-3682-bb13-bf60961e7361 | -10.65318 | -44.48476 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 626a2391-1df7-312a-9604-b8c374d8b5f3 | -10.80366 | -44.24704 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 673a996f-d390-3f24-8f20-e1dc4f174391 | -15.98838 | -41.98628 | 2025-06-30 03:25:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2133ce3f-3f5d-3f1a-8b80-43617f8bf17d | -10.65199 | -44.49062 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 680894be-c3a1-36cc-8adc-3d57b4bb6447 | -10.64885 | -44.48807 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 82e8736e-ff96-3f81-b309-31999bba754c | -11.84734 | -43.80152 | 2025-06-30 03:25:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 860ad6cd-a43d-3826-a94d-bd8ea142a4d6 | -15.98702 | -41.9931 | 2025-06-30 03:25:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7289d8d-fdb5-311b-a9e7-0d74ac0564fb | -10.79537 | -44.24897 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 81115bee-2146-3ef9-8b0e-943300addb98 | -10.6555 | -44.48939 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a5acd6f1-c519-35e5-a021-b977f8c9fe21 | -10.8048 | -44.24121 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 3ba41329-c3dd-3fda-aaff-e640b142652d | -12.7562 | -44.41066 | 2025-06-30 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29ece88e-7212-3004-b946-502482cb646a | -10.64769 | -44.49393 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c116fe10-d103-3b70-beac-69e806451370 | -12.7637 | -44.40657 | 2025-06-30 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b962e1a5-a3c9-32d8-b6ad-898f9037f683 | -22.67447 | -43.04542 | 2025-06-30 03:28:00 | NOAA-21 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5aab8c3b-b4d4-36d2-8b89-3d948145c632 | -20.4203 | -43.5563 | 2025-06-30 03:28:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7259e151-5b14-3291-9b21-ae703425338e | -19.26869 | -40.00887 | 2025-06-30 03:28:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 60eeaa57-cb96-3a44-88a9-3e0e2921bbf6 | -21.1797 | -43.98261 | 2025-06-30 03:28:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2e0b137b-191d-3c68-b0f7-a540eb9c8202 | -22.17284 | -45.1027 | 2025-06-30 03:28:00 | NOAA-21 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d6729f8a-554e-3a8f-9edb-14f07b3b8e7e | -21.66755 | -41.94818 | 2025-06-30 03:28:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 92814fc6-a68d-33e8-83b5-dde6f0f58b26 | -10.805 | -44.2319 | 2025-06-30 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 187.2 |
| a4c1ce53-531f-3895-9e50-5433fa89d567 | -10.8046 | -44.2553 | 2025-06-30 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| a17cc0b4-0995-32de-9987-abb30b62c0a5 | -28.58706 | -49.44197 | 2025-06-30 03:30:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e3c8dd59-646f-3e66-92f6-7533e9e25b22 | -10.8046 | -44.2553 | 2025-06-30 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 3589a354-8b28-3ac7-ab24-e4b02ab58382 | -12.6319 | -54.2087 | 2025-06-30 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 171ae08e-e476-37f6-868f-a1b50e11045d | -10.805 | -44.2319 | 2025-06-30 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 163.6 |
| b7f0d3d1-e9c6-3f2c-8d53-27743054d46e | -8.54401 | -48.26361 | 2025-06-30 03:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3494c565-e3f5-3c26-aa98-b40adb54b606 | -7.86089 | -47.12357 | 2025-06-30 03:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb4061ee-a906-3294-88e5-f973c4ce14d6 | -4.55948 | -38.46126 | 2025-06-30 03:49:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 34542274-03b9-3bd2-96ae-013f0ed939d8 | -4.32249 | -48.08474 | 2025-06-30 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6bf13e5-17a5-3462-ae1a-de345556de58 | -7.26295 | -43.16708 | 2025-06-30 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 945814e0-be70-31c8-b78c-dac9321733ee | -4.31791 | -48.0849 | 2025-06-30 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1257611d-41ac-330c-b13d-1482821b4106 | -7.22474 | -44.22651 | 2025-06-30 03:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96372f8c-27df-300d-bd3f-e3d60162f30a | -7.25858 | -43.16634 | 2025-06-30 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c49a93fa-3d5d-3556-99c5-c0c6a4abcca2 | -4.31705 | -48.07845 | 2025-06-30 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dc6f9cf0-e9ac-3f02-8636-892a51485585 | -4.31965 | -48.07519 | 2025-06-30 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 59f64387-20fe-318b-9b82-abed709ed2cc | -8.65686 | -47.81205 | 2025-06-30 03:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf2a5b56-f465-3bc5-956d-7203a9a38f30 | -6.42755 | -43.13093 | 2025-06-30 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2676969-1af3-32e9-b6c1-3d77c6967a5a | -4.3188 | -48.07991 | 2025-06-30 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| deaff714-5a01-3e07-829b-95efc5b328d4 | -7.25349 | -43.16982 | 2025-06-30 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 63a72e50-cc45-3ce5-a60d-3c2b59399e39 | -8.54994 | -48.265 | 2025-06-30 03:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e1be18d-5b19-3fdb-bf95-fef7a5b86179 | -7.26441 | -43.15862 | 2025-06-30 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 305f019b-5611-386e-9dde-4f734cd23aa6 | -8.65186 | -47.80678 | 2025-06-30 03:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a79fde47-6c02-3004-b0be-b3e2dbc01ea2 | -7.38826 | -43.87767 | 2025-06-30 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5f77e06-5d64-3ff1-9886-906f5c177e97 | -6.8381 | -42.0312 | 2025-06-30 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45a1ab90-44af-333e-b962-ce199907e2a7 | -7.1936 | -43.70102 | 2025-06-30 03:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf46e5ec-c175-3146-bc12-668947e61294 | -7.18908 | -43.7002 | 2025-06-30 03:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d4e361e-3bce-36b0-be0b-eb432950320d | -7.84852 | -42.90514 | 2025-06-30 03:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 04af3df3-0725-3ed7-8601-4a3f83977bdf | -8.70869 | -47.85603 | 2025-06-30 03:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cac7e91-758d-3f6b-a9b4-91b4c9bd14a4 | -7.63439 | -44.66037 | 2025-06-30 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 015cc2b0-0b9b-3ca1-93ff-c86899f957c9 | -7.18751 | -43.70929 | 2025-06-30 03:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 142f4279-8c60-3697-9882-5762a010ba47 | -7.25785 | -43.17057 | 2025-06-30 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8d11d8fe-8a90-3dbc-b866-244a58075ff6 | -7.18829 | -43.70475 | 2025-06-30 03:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c409948-3e8a-303a-8c65-b62cc2ac4600 | -4.89773 | -37.62263 | 2025-06-30 03:49:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 08805cfb-3790-3e3d-8ad2-ee50832af0e8 | -8.71452 | -47.85705 | 2025-06-30 03:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1640d78-3bef-3250-86ad-57be9549fa7b | -7.25932 | -43.1621 | 2025-06-30 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 998fc984-226e-3daf-bfe5-9366952a3063 | -7.8602 | -47.12735 | 2025-06-30 03:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15efcabb-3787-305a-a072-29dca7e76c71 | -6.83748 | -42.03485 | 2025-06-30 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ae149457-7f6b-3da2-bfb7-cd2e656d8b7c | -4.81938 | -47.32026 | 2025-06-30 03:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b1ec5cf-1150-3791-9ebd-f30d618b3175 | -4.31619 | -48.08342 | 2025-06-30 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a0ff0224-39bb-38d5-af07-4d12a9cbfe6a | -6.84216 | -42.03196 | 2025-06-30 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf06aa19-f8f7-3811-b8e4-dffa8ff1ae20 | -7.38744 | -43.88247 | 2025-06-30 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 841d0138-a85a-3caa-aa81-2808ab67c280 | -7.22389 | -44.23141 | 2025-06-30 03:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 719aae4e-4518-30d2-9f8e-29e973510c62 | -4.32333 | -48.07987 | 2025-06-30 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 784e4a17-0a29-3588-9ac4-93fa88b645dd | -6.8334 | -42.03426 | 2025-06-30 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7dcf2d18-4a02-3182-9c13-a26fde49fad7 | -7.63828 | -44.66631 | 2025-06-30 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bd2db82-d486-37c8-897a-9ea95cc47bf5 | -4.81334 | -47.31946 | 2025-06-30 03:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de16fb2b-e8b5-3a7b-b4af-025a139080bf | -7.63136 | -44.64966 | 2025-06-30 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f13bdc24-a091-3ece-9b11-bc72146fd08d | -7.62744 | -44.64759 | 2025-06-30 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b1d799f-61d0-3016-b6f9-26b0fd4aec64 | -10.7859 | -44.2346 | 2025-06-30 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 6cd119b3-9146-35f5-8ccc-ba056cf2124f | -10.8046 | -44.2553 | 2025-06-30 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 605624ab-a260-3468-bf27-fe797865ccfe | -10.805 | -44.2319 | 2025-06-30 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 221.0 |
| 15ed22ec-4aed-3395-80e2-ab906dbdd19a | -10.79527 | -44.23909 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b43a41c-03cd-3d3a-b961-248485b9d905 | -10.79449 | -44.24347 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c92217d8-b5f5-3682-a23c-1ef6d3134745 | -9.14023 | -46.36486 | 2025-06-30 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04581d4d-94f0-3a72-b21a-b2e7a0d79b34 | -13.47656 | -47.72152 | 2025-06-30 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6595dd49-1eb5-3d5e-8699-a8283a2c2403 | -15.98897 | -41.99319 | 2025-06-30 03:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0539e134-3b6c-35d7-9215-756116451c77 | -10.55 | -52.04533 | 2025-06-30 03:51:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 88708484-0c1e-3c7f-8182-376990d53b7c | -10.79813 | -44.2487 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 85929490-2f58-3caf-b458-e46f5c0cd49b | -9.14052 | -46.36824 | 2025-06-30 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcc6033c-df3c-3194-88be-d48c05f3ee73 | -9.43842 | -47.94149 | 2025-06-30 03:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf215d7c-14d6-3237-8d9d-190fb88568f9 | -10.80487 | -44.23631 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| ea43e08d-da7d-3f64-9dca-905cf8616c86 | -11.58943 | -44.66265 | 2025-06-30 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af087cf4-5043-35bb-9dfc-aba3036c3de8 | -14.43443 | -45.15782 | 2025-06-30 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15d2ed63-4766-34db-8ea6-5ae2c33be1c2 | -12.2017 | -49.64018 | 2025-06-30 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 79bf890a-cd25-3515-ad17-52ffc268d285 | -15.98797 | -41.9906 | 2025-06-30 03:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c67f6eb-f451-369c-8c57-7c2b7d7eb8d9 | -8.8643 | -47.95465 | 2025-06-30 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae4b3b80-af5d-39ec-809b-74056d0ecc33 | -15.98725 | -41.99487 | 2025-06-30 03:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae3f6dfe-ce5a-3312-863c-599a6a00a8d9 | -9.09351 | -47.96441 | 2025-06-30 03:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9e019e5f-8540-3b9d-a681-81fe045395a7 | -14.43802 | -45.16312 | 2025-06-30 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f80e31f8-b928-3700-b21b-a960e1963836 | -14.53971 | -46.6221 | 2025-06-30 03:51:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
