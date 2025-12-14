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
| d3a5b0f0-813f-3cd8-9a26-f2ecd6deface | -8.0327 | -43.0786 | 2025-12-14 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 43a77ee4-31e5-3210-b1f4-461bd8dfc43a | -3.7317 | -43.7424 | 2025-12-14 00:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| aa30575f-dcd4-35a6-ba8b-18cd474b4cef | -3.6277 | -45.6797 | 2025-12-14 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 6c9936b0-cadf-3f2e-93fe-1dcafcb7ce14 | -2.2907 | -45.5709 | 2025-12-14 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7bc3b9da-b898-3213-ac7d-e8f21029e644 | -5.68 | -39.259 | 2025-12-14 00:00:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 46.9 |
| c610812f-fe04-3a8a-b56e-83f9cba5eff6 | -2.2906 | -45.5933 | 2025-12-14 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| c5e6c73d-41d6-3498-b316-bd5f817f2fae | -5.6797 | -39.2841 | 2025-12-14 00:00:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 42.1 |
| fb72788d-0ffc-3571-b0f2-b75a6774efca | -2.272 | -45.5938 | 2025-12-14 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 83d8d4c5-c4d2-3700-8abb-2b34dd380eeb | -3.7316 | -43.7655 | 2025-12-14 00:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| df57acfe-4045-3544-a012-74c94a40f6f0 | -2.1425 | -45.4628 | 2025-12-14 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 56b0a31a-3085-3885-9418-5b402b422630 | -2.8485 | -45.3963 | 2025-12-14 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1f9a201e-9905-31e4-83e0-eb0846a55d51 | -2.4768 | -45.4309 | 2025-12-14 00:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b173e903-ff7b-36f1-8597-2b2f8bd56f68 | -8.0324 | -43.1022 | 2025-12-14 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 160.9 |
| 1ea2949b-3d86-388f-918e-18bda48fc10a | -2.0768 | -56.4674 | 2025-12-14 00:00:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d5b11e33-ce30-3a3d-b35e-4ab88b15b264 | -3.5186 | -48.9201 | 2025-12-14 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| f880ebc4-ae55-360e-9802-0fe742215f29 | -3.4451 | -41.6413 | 2025-12-14 00:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 63.5 |
| 3ced00fc-7508-38ad-be87-8cad5dcec388 | -2.1426 | -45.4403 | 2025-12-14 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e0ec5440-4f98-39a9-96a7-f4ac123894eb | -8.0696 | -43.1452 | 2025-12-14 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| dd704479-c946-38fc-9e17-1f753e07941b | -8.0886 | -43.1431 | 2025-12-14 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| cbe20076-1316-317e-91b8-dbe546f7827c | -8.0513 | -43.1001 | 2025-12-14 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| c57ea694-4e6f-3876-94ff-d173f1231400 | -16.2383 | -58.8395 | 2025-12-14 00:00:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 61cece51-6646-32e0-81ed-bbf85969b45a | -2.8429 | -46.7312 | 2025-12-14 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f62f3c9a-2134-34dc-8a73-7b4d2f60566f | -2.2721 | -45.5714 | 2025-12-14 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 08185039-e43c-3282-9dc1-f5bb2e708faa | -8.0324 | -43.1022 | 2025-12-14 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.9 |
| c1d43291-ea30-3787-a4c2-f12a99c2d9a7 | -2.0768 | -56.4674 | 2025-12-14 00:10:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 8f8d3290-7fc2-374a-8972-f7ed0f05c3c3 | -2.2907 | -45.5709 | 2025-12-14 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 6ecc58bc-d3ed-3be2-b3cb-995b5a6a55e1 | -3.6277 | -45.6797 | 2025-12-14 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 68145db7-5e5c-305e-8fff-b4e9d40de5e1 | -2.2721 | -45.5714 | 2025-12-14 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 00a2f6e0-7458-38ec-9c87-d6d096feb5a9 | -8.0327 | -43.0786 | 2025-12-14 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| aa878b58-4818-3c9f-9031-096eda3a10df | -5.6797 | -39.2841 | 2025-12-14 00:10:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 51.5 |
| a2f13579-0e46-3126-8458-28cfd24d3f92 | -2.1425 | -45.4628 | 2025-12-14 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ead5cb33-5d97-32f0-8f5d-c6162ac88475 | -8.0886 | -43.1431 | 2025-12-14 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| e9108da1-0def-3bf1-8cf9-8f7b7cbede91 | -2.8429 | -46.7312 | 2025-12-14 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| fcc8951c-9a99-30da-8a4b-d52ce8cef9ef | -8.0696 | -43.1452 | 2025-12-14 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 331fdbaa-258e-346a-ab00-5dc38ec0b11c | -2.2906 | -45.5933 | 2025-12-14 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 8c213398-3a48-3e2c-9d88-a9e26eca0462 | -3.5371 | -48.9195 | 2025-12-14 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 69975afc-4d69-35e4-a7ee-05bff9082928 | -2.272 | -45.5938 | 2025-12-14 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| a43ff1d4-3f8e-30f3-95db-80c516b14ee6 | -3.4451 | -41.6413 | 2025-12-14 00:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| bcbd3810-4072-3f98-b706-6aa42b5fe9d0 | -1.0367 | -53.5575 | 2025-12-14 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 5eb7e640-cdd5-3ccb-8c3a-1382fcfa5329 | -5.68 | -39.259 | 2025-12-14 00:10:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 47.4 |
| ab1bc3d6-aad7-39a0-ba23-b30a2cef44b4 | -8.0513 | -43.1001 | 2025-12-14 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| a04d4d7c-a385-3de6-98d5-03fe6c0f714c | -1.0184 | -53.5576 | 2025-12-14 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| cc1edc21-b949-3cdd-a0fc-09e23db71ba0 | -5.6608 | -39.2858 | 2025-12-14 00:10:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 37.1 |
| 2832e603-62ee-345e-aba4-6b5234021015 | -3.5186 | -48.9201 | 2025-12-14 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| db48a790-c8ba-3106-981b-0c324dd1437b | -8.0373 | -43.106998 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3a1dc39a-267b-3baa-8526-cde1d6778d02 | -4.3461 | -43.642601 | 2025-12-14 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 759a7b2e-504a-35d4-ba7d-d15ea7657ad1 | -2.1324 | -45.463001 | 2025-12-14 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d4aca05d-62a6-305a-86dd-c23aae31bb98 | -4.3445 | -43.6357 | 2025-12-14 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| faaef208-f390-3275-9634-e70ed2f422a8 | -8.0681 | -43.1521 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c16900a1-7046-349c-8a62-8e6809b4a9fc | -8.0358 | -43.099998 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 674b0d74-887e-31a0-9d17-ac1784c0e8fb | -2.8842 | -44.963299 | 2025-12-14 00:18:00 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53688214-8737-3a1f-bf02-129d6d47befd | -3.7424 | -40.8344 | 2025-12-14 00:18:00 | METOP-C | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 920b99d9-ec2d-3c2a-9745-dc7df029ed64 | -4.6923 | -43.261501 | 2025-12-14 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77a08c74-ad2f-39ed-904b-2de5cf2940e4 | -3.6674 | -44.8283 | 2025-12-14 00:18:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5e17084-074c-3d42-ac6e-bc591a13b4be | -9.105 | -40.462101 | 2025-12-14 00:18:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 5d3a0372-6fa8-3817-a56e-47c27eaaec4b | -2.7659 | -45.213402 | 2025-12-14 00:18:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c79c73e9-2251-35ef-a681-79c4c88fae9b | -3.4354 | -41.6492 | 2025-12-14 00:18:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ff258391-fee5-3c61-82fc-1510948570e7 | -3.4931 | -41.989601 | 2025-12-14 00:18:00 | METOP-C | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e164366d-9e7f-3331-923e-0e610cbbb10f | -3.6219 | -45.6735 | 2025-12-14 00:18:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7a2f54-8a10-3755-b6e2-0f94e02507aa | -5.004 | -42.774899 | 2025-12-14 00:18:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a0dd25c5-1c39-39b0-b6d8-681bd49c0816 | -2.8858 | -44.9706 | 2025-12-14 00:18:00 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82b0c29d-59e2-36c4-923a-a6aea70ec496 | -2.8339 | -46.739201 | 2025-12-14 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5836c0e-9fde-38c4-b461-29234d4a6248 | -6.5939 | -39.52 | 2025-12-14 00:18:00 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 20f12151-1b6d-3a57-a499-a91cc1b1671f | -4.9334 | -43.959702 | 2025-12-14 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed56f7de-528a-3808-9eb3-0c2d9e674dc0 | -5.3486 | -40.686699 | 2025-12-14 00:18:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fe423032-d7bf-3e53-bb75-c2528b161121 | -3.881 | -42.510201 | 2025-12-14 00:18:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 38c94535-7c0c-33a6-b4e3-f4dd827e7649 | -4.343 | -43.628799 | 2025-12-14 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eefbd886-f29e-3870-b700-f036d13f74d3 | -3.1423 | -45.3741 | 2025-12-14 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bfe2e935-13a7-34e8-849b-e078d394c7d4 | -2.7676 | -45.220798 | 2025-12-14 00:18:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 157e6b80-92f7-3fc9-9c50-61c217d4d862 | -5.6669 | -39.264301 | 2025-12-14 00:18:00 | METOP-C | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fb315302-029a-355d-92f6-eeea4966d8b7 | -9.1165 | -40.4669 | 2025-12-14 00:18:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| abf35650-9a2f-3aed-b2d0-b54bac3357b9 | -8.026 | -43.1022 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 779a3c1d-f5e8-392b-8137-1c55cba9b770 | -5.6787 | -39.270401 | 2025-12-14 00:18:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4e47dd4e-03b6-363b-88a7-99e709e7b2fd | -6.5276 | -39.281601 | 2025-12-14 00:18:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3764422a-a4a2-3476-8000-e461b8650ea2 | -2.2816 | -45.756599 | 2025-12-14 00:18:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2bf7b81c-ea04-3f05-9cc2-fb6d5784baf8 | -3.7232 | -43.7593 | 2025-12-14 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96eadc81-1cf1-3e91-bd66-83152f150c49 | -3.1406 | -45.366501 | 2025-12-14 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 806260e8-f3da-3772-80cf-970e323c8b7e | -7.0149 | -38.546101 | 2025-12-14 00:18:00 | METOP-C | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 55dbf69f-95e2-39df-b8a8-8dad582af384 | -3.7298 | -43.743301 | 2025-12-14 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be1fc375-99eb-3525-b2b0-0652304ff9f1 | -6.5958 | -39.527901 | 2025-12-14 00:18:00 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6099b67e-cbd3-35a8-ac46-d1798e37fe90 | -1.4526 | -46.276901 | 2025-12-14 00:18:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6a126d-f458-369a-858b-051b230c770c | -8.0342 | -43.092899 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7f5c9f47-aba1-3c15-bf7b-3bcdf9a5f577 | -3.5007 | -42.3363 | 2025-12-14 00:18:00 | METOP-C | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8c0998bb-b6a1-34b3-b306-e02e9c956931 | -2.1307 | -45.455502 | 2025-12-14 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36a6c861-1593-3d94-8505-93760bcdd7bb | -2.1422 | -45.4608 | 2025-12-14 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 488203ba-ad6b-3fe8-b3e8-9caa4a4ff703 | -1.5235 | -45.684601 | 2025-12-14 00:18:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb37e1e-74bf-3d89-b7d3-ad9e83efeed5 | -2.1405 | -45.4534 | 2025-12-14 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17fe81f7-21a2-34e3-b269-707cbcea7882 | -8.0665 | -43.145 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d5edf9f3-128b-3493-bd08-c98925eaadaa | -2.4761 | -45.434101 | 2025-12-14 00:18:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f5dbde9-7d7f-3300-8449-6bd340daa1ea | -3.8841 | -42.5238 | 2025-12-14 00:18:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 50549c2e-5948-3b64-8093-5918559286ec | -3.437 | -41.6563 | 2025-12-14 00:18:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 73385f59-2728-3f5b-bf04-0af20b27f76c | -8.0697 | -43.1591 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 66ce9479-dbae-3cf2-bed9-6996befe6a77 | -3.7406 | -40.8269 | 2025-12-14 00:18:00 | METOP-C | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b68389b4-4b81-36ab-ba61-66cb1a8044cb | -2.8493 | -45.399101 | 2025-12-14 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c68cf1da-0795-3839-a838-ff263245f9d4 | -4.6907 | -43.254601 | 2025-12-14 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bdb9c7e-82a2-3428-b641-58c35b15abc1 | -5.011 | -41.2784 | 2025-12-14 00:18:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 94f17846-abf9-3651-9d13-73c22378a594 | -2.8476 | -45.391602 | 2025-12-14 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e1254663-329e-3af2-af5c-8ab2ccfe765b | -2.2843 | -45.587601 | 2025-12-14 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ec794cbd-313a-31b4-a66b-d59d19b75fc0 | -11.7095 | -37.652802 | 2025-12-14 00:18:00 | METOP-C | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c92ccb7d-b16a-33a4-89ae-13bf37b58c9b | -9.1148 | -40.459801 | 2025-12-14 00:18:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
