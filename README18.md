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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65de841c-ad9c-36b6-b81e-df9aa7fd5407 | -3.56794 | -53.10283 | 2024-12-23 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41518e44-db54-3c03-ada1-144988fc2567 | -6.94529 | -43.54232 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8af7473d-8bb7-3523-bcfe-ad2ce040d834 | -3.65059 | -54.73669 | 2024-12-23 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d588b31-9b3a-325a-8fbe-082d2ecb8d3a | -6.9494 | -43.54216 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 95421a33-ec90-3ea9-8405-a0a38ea9524d | -3.42702 | -55.37751 | 2024-12-23 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10a01f7d-5e3b-32f5-9dee-152fb1d1847a | -5.93159 | -45.48727 | 2024-12-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69a2d0a3-6ee9-39c2-b21e-50a1a5a3058d | -3.53395 | -52.6716 | 2024-12-23 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8785f2bc-fdfa-3e51-b203-3c5873bfaf76 | -6.94406 | -43.53701 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2d920dd2-a814-3edc-8e29-2231d7b96aa8 | -5.43302 | -47.61364 | 2024-12-23 04:55:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96559bf1-633f-370b-bb24-64df699ec779 | -4.27998 | -55.74295 | 2024-12-23 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34d84298-736d-3b02-b15a-a703075093cd | -3.58296 | -54.68607 | 2024-12-23 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be75677e-a46f-34cf-805c-d6fd4982a602 | 0.69534 | -51.44301 | 2024-12-23 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e77f11f8-0901-332d-b15b-f22733f1bba2 | -16.69152 | -43.35995 | 2024-12-23 04:57:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 579cd394-780d-36af-8eb5-7082bcf53815 | -18.51381 | -53.4021 | 2024-12-23 04:57:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ffc0297-9c10-3b33-a61b-4b28ab5d7414 | -18.51809 | -53.39807 | 2024-12-23 04:57:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c69744a3-ab18-3e4e-a21e-ce62d5444960 | -18.51442 | -53.39761 | 2024-12-23 04:57:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8acbd57-e839-38b4-8ac5-f7122e486336 | -19.33683 | -54.17604 | 2024-12-23 04:59:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 200e8310-57a4-39d4-bd8b-b172132bc334 | -19.34039 | -54.1766 | 2024-12-23 04:59:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c20323e5-ade2-3b9b-adfa-52f46e0fee01 | -22.17525 | -56.72409 | 2024-12-23 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d573d3e-0285-3c8f-b72d-97aadd9814af | -19.33743 | -54.17184 | 2024-12-23 04:59:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 22fee174-3e41-32c1-89bd-fe529abdcc49 | -19.06653 | -53.47084 | 2024-12-23 04:59:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 359a69d5-568c-34af-804f-b2514d11ba44 | -4.37184 | -43.99279 | 2024-12-23 05:12:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c47d977e-10af-3eb7-8c0d-548a4bfbbc55 | -4.37041 | -44.0021 | 2024-12-23 05:12:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 35ae0b1a-104e-310b-bca6-24c06f625d03 | -9.82745 | -36.02458 | 2024-12-23 05:14:00 | AQUA_M-M | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 9b39279d-028c-37e8-9c26-1ebddc62b771 | -8.78977 | -49.79575 | 2024-12-23 05:14:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c9be0bc7-ab40-3607-a2a4-54789bb5e5f0 | -8.80114 | -49.79248 | 2024-12-23 05:14:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2b85d1c4-7f11-3999-8177-8d4754a7758a | -6.93785 | -43.52328 | 2024-12-23 05:14:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 3597f052-4ef1-327d-9a9d-1397aafe617d | -12.3337 | -43.67923 | 2024-12-23 05:14:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2d3897a1-d98a-30b5-a568-6fd5e7f98bb5 | -5.82177 | -35.47363 | 2024-12-23 05:14:00 | AQUA_M-M | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 42.9 |
| eec77e19-4cdf-3ba9-9c40-9097db021baf | -6.9467 | -43.52459 | 2024-12-23 05:14:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f656ada1-f2aa-303c-b54b-94b811bf6f39 | -6.94535 | -43.53347 | 2024-12-23 05:14:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2d3e39d0-9e28-3a7a-9c4b-706aaf8679c2 | -6.92731 | -43.52409 | 2024-12-23 05:14:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| cabbd97e-3597-363b-a51e-737c7b0b7b30 | -5.44716 | -44.80404 | 2024-12-23 05:14:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 212d42c7-c9b5-3926-a3d4-c66a36458a5f | -6.90695 | -43.53921 | 2024-12-23 05:14:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| be4c13d8-c2e6-392f-8fcc-417b8dc12cd1 | -6.8981 | -43.5379 | 2024-12-23 05:14:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 42e20ef3-f7aa-390c-bb08-d69172c1bdb2 | -4.71795 | -46.45723 | 2024-12-23 05:14:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 93b822ec-3a5a-3fcc-bc0f-94df734b4601 | -10.02128 | -36.16122 | 2024-12-23 05:14:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| 7603652f-1160-33f5-8cd2-4c3cffb4a5f8 | -4.44 | -45.92736 | 2024-12-23 05:14:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e9297d9b-4873-3b7a-a384-46e06a0fc880 | -6.94401 | -43.54235 | 2024-12-23 05:14:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 2f2d3728-5ba1-3208-ba12-f16ea8124723 | -6.93651 | -43.53216 | 2024-12-23 05:14:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 1741935c-51cd-30a7-9c1c-41d247989677 | -4.44091 | -45.92111 | 2024-12-23 05:14:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7bb7e336-cd5d-3e0d-b7e1-eee646ae39cb | -6.9542 | -43.53477 | 2024-12-23 05:14:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b5748729-c806-301f-ad38-97b62e0d7402 | -3.65387 | -54.73912 | 2024-12-23 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab42748a-ee56-3126-bdd7-4898f4753bf7 | -3.09636 | -54.60019 | 2024-12-23 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 985e89c6-ce32-3284-8b29-a79c6d1c742a | 0.87377 | -60.08444 | 2024-12-23 05:48:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5405054a-3d42-3af9-8021-c22d8a37b670 | -2.40788 | -54.2003 | 2024-12-23 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 56dacab3-0d1c-3c0c-84db-82e6880e59c9 | 0.64909 | -59.74058 | 2024-12-23 05:48:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79398698-4828-31ad-81d6-4f542a83d949 | -3.09978 | -54.60065 | 2024-12-23 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7006c637-f419-36ff-ae27-903d36f1cc0e | -2.94163 | -53.05951 | 2024-12-23 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 632ec75e-8b4c-3721-8e56-5a7771d02516 | -3.09566 | -54.60509 | 2024-12-23 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5467fab-0d2a-39a0-bc57-cec30ccfb099 | 0.64847 | -59.73666 | 2024-12-23 05:48:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f646f4e-601c-38ab-a9a9-2c8abe9dbda4 | -1.36035 | -53.69664 | 2024-12-23 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 84136f99-9f7e-376d-b3bd-06b1ab0e695c | -2.40315 | -54.19886 | 2024-12-23 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f5c0bac7-430b-3fd4-8ad7-ccf57224e619 | -2.40339 | -53.74245 | 2024-12-23 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eed28bca-1ac1-3ed0-906b-a00e12d1fd48 | -2.40256 | -53.74806 | 2024-12-23 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a17c82b2-26dc-3cd8-94a3-a5cd5b76a750 | -2.40915 | -53.7491 | 2024-12-23 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d96e74f-dad6-3a8c-a6bd-0eea864be780 | -3.10098 | -54.54959 | 2024-12-23 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1b6927d0-e401-34b2-ad59-0e0ae7b184e8 | -2.94254 | -53.05329 | 2024-12-23 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a32563c-4992-38ca-8f8c-acd55ec4d30b | -2.40997 | -53.74354 | 2024-12-23 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 357d18bc-bd3f-3adb-8169-8fb462b5b472 | -1.06729 | -53.61328 | 2024-12-23 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1e977882-ef04-3707-b064-ab489b88ad33 | 0.37003 | -60.46146 | 2024-12-23 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 893f66c0-3c78-3caa-a4e9-b3c3717524df | -4.1615 | -43.6507 | 2024-12-23 05:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| bdc0e405-925c-333f-900a-26e37c5a1d17 | -6.9344 | -43.5401 | 2024-12-23 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ad6cb879-c490-39f0-b873-56b98ea8c5cf | -6.9532 | -43.5384 | 2024-12-23 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 38d446c1-024d-32cf-bd50-4edce463e6e4 | -4.8881 | -65.17141 | 2024-12-23 05:50:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 24dd6cf5-0f95-3bd9-82ef-01b96e186970 | -7.91739 | -61.54104 | 2024-12-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 65fdd15e-6e42-3414-8532-799084da419c | -6.9344 | -43.5401 | 2024-12-23 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b09098b4-c69b-3c58-b86f-f195e1de5d55 | -6.9532 | -43.5384 | 2024-12-23 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 5f10fa8b-d83d-360c-8f19-ce872816f07e | -6.9532 | -43.5384 | 2024-12-23 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| f7d30f62-5931-3514-b0b9-55f42926a5ba | -6.9344 | -43.5401 | 2024-12-23 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| a3f529c2-c6b7-38f9-8806-7f1f5b695ea5 | 0.64807 | -59.74087 | 2024-12-23 06:12:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 276733c0-6b10-3534-97a0-8279a03ddfe6 | -6.9344 | -43.5401 | 2024-12-23 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3fce882b-db6c-3718-a808-527d1c1bbb42 | -6.9532 | -43.5384 | 2024-12-23 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 76c7bf36-cbce-36cf-be38-e266af3fbef5 | -6.9344 | -43.5401 | 2024-12-23 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| fd2791c3-4d09-36aa-86c8-b69a32ac6868 | -6.9532 | -43.5384 | 2024-12-23 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 8abdb7c5-1af3-3e7b-a078-3b116e067b2a | -1.6637 | -52.065 | 2024-12-23 06:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 5e293a8e-dea7-308c-9a66-e4ba960feeef | -6.9532 | -43.5384 | 2024-12-23 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 7c071933-35c0-3917-ac27-762d92273a55 | -6.9344 | -43.5401 | 2024-12-23 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6d401a10-dcc7-3281-ae74-a645df5b41f5 | -6.9532 | -43.5384 | 2024-12-23 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b41d081d-6558-3141-a541-3d830e9d896c | -6.9344 | -43.5401 | 2024-12-23 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7d7cb9d1-6190-3954-90e1-ba96004b6a88 | -6.9344 | -43.5401 | 2024-12-23 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| cb51d9c3-450d-3560-b48c-2bae99349d13 | -6.9532 | -43.5384 | 2024-12-23 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| bf99574f-3d04-3d68-8071-987d6cd02ee0 | -2.97718 | -42.0792 | 2024-12-23 12:46:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e66b9ab3-6f58-32d6-8338-525b00f482f9 | -1.36332 | -53.69245 | 2024-12-23 12:46:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 75c8b9e5-43a5-36d8-a2b9-68d016728eff | -2.29235 | -47.91311 | 2024-12-23 12:46:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b71b3051-2e13-3d43-82d4-6eec2b351ddb | -4.06304 | -47.08109 | 2024-12-23 12:46:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c6c548a1-0d47-30ad-ab02-5883d34a6b3e | -4.57401 | -45.8595 | 2024-12-23 12:46:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| e15e392a-c5f0-34f8-9280-eede0bf841a1 | -1.37517 | -53.69428 | 2024-12-23 12:46:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 8782a868-1e97-3d37-b008-77bc068ab4e4 | -3.19475 | -46.12524 | 2024-12-23 12:46:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 26281794-e4e8-3254-a1a2-aad2ec0dffc5 | -1.97066 | -45.89761 | 2024-12-23 12:46:00 | TERRA_M-T | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 10dce764-7acb-3cad-a645-04a568c5050c | -3.90436 | -45.01729 | 2024-12-23 12:46:00 | TERRA_M-T | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 60dad7a1-e36e-3fc9-9ad5-ad5e0bfb465f | -5.35389 | -42.11901 | 2024-12-23 12:46:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 64b067f0-cce1-3fd4-9c45-b1af090bf011 | -3.19623 | -46.11492 | 2024-12-23 12:46:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6b7e0353-d9b2-38aa-a110-c270181edd0e | -0.9677 | -47.56308 | 2024-12-23 12:46:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 205.9 |
| 1de1a7ff-894a-3aca-8bf1-16596d245aeb | -0.96898 | -47.55424 | 2024-12-23 12:46:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 464.5 |
| 7c3da834-f75f-3cfe-bb4e-2722aa1990b1 | -2.26955 | -46.39426 | 2024-12-23 12:46:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2ef3e416-9d11-33ce-bd50-c5c3dd951100 | -4.15163 | -43.65197 | 2024-12-23 12:46:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 5fbe01d8-e104-31be-8553-01fce07e813b | -4.3243 | -45.88619 | 2024-12-23 12:46:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f4c2be35-fd4c-3914-b2c3-3ea83abc6eb2 | -2.2835 | -47.91189 | 2024-12-23 12:46:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0ddcee14-e2b3-34a4-a814-915e26196cfd | -2.09931 | -45.33647 | 2024-12-23 12:46:00 | TERRA_M-T | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |


[Clique aqui para ver as próximas entradas](README19.md)
