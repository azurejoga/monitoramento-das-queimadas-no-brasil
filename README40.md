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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52cfbd07-e9c9-3b0d-91f8-b130d48f81a7 | -5.0943 | -37.78333 | 2025-11-15 04:25:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5ea5246d-58af-332c-975d-f0460735f052 | -4.3605 | -47.57983 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a3a0d80-57b0-350d-bb2f-6d371597362e | -8.66434 | -45.45909 | 2025-11-15 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36aab3f4-a58e-3a30-a1e5-1d2edb1eca97 | -6.16887 | -48.04794 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9908e438-d5b5-339e-a3b9-94ff4886884e | -5.29557 | -46.74636 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8694ba40-46c4-36db-a144-1eb19193ace0 | -4.10827 | -48.01775 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 64fcca6e-56a3-3a96-ae77-2212e7b7031e | -5.37255 | -44.92256 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 763ac396-80e8-3ab3-9925-b235c9d8e715 | -4.47834 | -46.62804 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3175ae46-fb8d-397e-810c-7ac4b27cf345 | -3.24174 | -50.80527 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75991bc4-56df-3098-85dc-0c7865f312dc | -7.29154 | -45.11578 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a84d109e-17ff-309a-9e81-33fa13c83141 | -7.55016 | -47.24953 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2820e855-08a5-30f2-a3ee-030263dc87c4 | -6.15243 | -48.04154 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c120966b-fbd6-3ef9-a6a3-62dff19e56f6 | -2.79298 | -52.97475 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c90566ca-5856-3c43-9008-9f38daa9ac07 | -3.00988 | -49.43556 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2292d6c6-279a-31cd-8ecc-290bcca286bf | -4.98109 | -43.88675 | 2025-11-15 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0d2dbe6-b986-3263-8f8b-7e20c5e26610 | -3.86005 | -49.1279 | 2025-11-15 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 44046223-f989-3033-8ef1-a250ebe89de5 | -6.25482 | -47.08158 | 2025-11-15 04:25:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e62dbfe2-b0b5-3e8c-938d-bcdb5835d2ad | -6.03233 | -45.80479 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34328f36-11a9-3070-9e91-3fc684b9fa00 | -4.2211 | -45.48417 | 2025-11-15 04:25:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d68c28f-469b-3492-9b2b-cf840a19694d | -4.35355 | -46.49413 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 709d2584-f97b-3b71-b4e7-e3755992cbaa | -2.86599 | -51.47386 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5035f51d-89be-3978-929b-2dcc7fdf96ee | -5.65042 | -47.89103 | 2025-11-15 04:25:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0826c23-d399-3242-9962-4bb9d4a95854 | -2.15526 | -48.29268 | 2025-11-15 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0646df67-1ace-3715-a09b-e895800fa4a0 | -5.09058 | -47.70841 | 2025-11-15 04:25:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b90b8386-181c-3696-b2ef-4441e48c461d | -3.99102 | -44.2836 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf2bc499-ee39-34a0-9b8d-5ea54a463b15 | -9.7258 | -46.33717 | 2025-11-15 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d33a7b6-fc9d-3f66-a4da-8ed891331d56 | -4.33789 | -47.56868 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6744ffd5-1686-37fc-80cc-0840d43ccf91 | -3.26717 | -43.61884 | 2025-11-15 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f8f74f4c-f602-32ed-99a4-03bf26447c7d | -7.28927 | -48.32421 | 2025-11-15 04:25:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a74e5089-e3c4-3d22-a234-8f8085e62da1 | -4.85514 | -43.25492 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b8cf5a6b-4693-3d35-9c11-454fceeb6909 | -5.51822 | -41.76564 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e5c3cd21-ffe6-3693-b3ac-10c314a82b1f | -7.38715 | -44.06082 | 2025-11-15 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbd1fd70-0d8b-3650-a5d2-ad65484625db | -5.54003 | -42.69741 | 2025-11-15 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c7033ba6-afd6-326a-aa6b-7f2ba28caae2 | -6.95041 | -46.33947 | 2025-11-15 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a91a22f1-552a-3cc9-a563-144c44756d3e | -5.12699 | -55.9782 | 2025-11-15 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 736682e3-7ab2-34e9-942d-10101077fd27 | -4.00277 | -47.6667 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c7d4d1a-37df-313e-8f3e-82e473a00572 | -4.27159 | -46.83894 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d701d5d9-e91d-3445-a08f-75833d0ecc94 | -9.5242 | -47.27367 | 2025-11-15 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dc0ff59-5f09-3b8c-bf54-693d927266ba | -6.08127 | -48.17842 | 2025-11-15 04:25:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 491b9d65-930c-3426-8e02-f487db428ae1 | -7.43937 | -42.76924 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a9482ea9-df9f-3bf9-a63a-e0baa98be88f | -8.33191 | -45.41177 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa51b4ed-669d-350b-8949-458116f2b75b | -7.69292 | -47.1862 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c760e8b9-3866-31e0-9e3b-49e71d731152 | -4.64709 | -43.36406 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d333935d-aaa7-35c2-bcaa-287ee125a0b5 | -7.23388 | -46.26421 | 2025-11-15 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87901e59-a8ef-3e8b-a74d-08cc367ef6e1 | -3.93517 | -42.74612 | 2025-11-15 04:25:00 | NOAA-20 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 27763a12-7b09-3912-9450-f53746cf7416 | -5.63762 | -51.30288 | 2025-11-15 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8c1e3f8-13c6-3396-8750-43f439bc938f | -3.13411 | -48.63142 | 2025-11-15 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 151ccb9a-1456-3732-a9d4-e1e6b76e8460 | -7.21193 | -35.02892 | 2025-11-15 04:25:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 669c2eed-f801-33da-860e-5c2be58103f7 | -9.66195 | -43.8992 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a6f0d6b4-4bda-3947-bf74-c8886ed40979 | -7.1051 | -42.73006 | 2025-11-15 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f67b3976-0e48-3274-a0d6-b4a898a98408 | -5.67317 | -42.75515 | 2025-11-15 04:25:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c2e83245-153e-384a-8084-4f0bae1b93ee | -4.52539 | -47.97353 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 770bd09a-f734-35da-8d6f-8a91fbef1a6f | -4.10542 | -48.01341 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be43fadc-11ae-3b9c-8322-e62578ca0ac0 | -1.34038 | -54.60858 | 2025-11-15 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 589e91f9-d648-3c6c-852e-37f0c7c672fc | -5.02816 | -44.51203 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72b580c9-9410-3e9e-a9b9-7c674580ba23 | -3.46415 | -50.11761 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 19ba4c39-dd32-3dee-b560-12c08362360d | -8.56854 | -46.05057 | 2025-11-15 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ca1e9231-12f5-35cf-a2ef-7d3a3e9e03ae | -8.58163 | -46.07415 | 2025-11-15 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 277925b1-ae34-3bbe-b329-dde50932024a | -4.05563 | -46.42204 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8970192-614d-380e-b649-feb5d7f57fbf | -7.29546 | -45.11272 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a73008ea-c2c6-39f2-b992-e0d5eb4a1620 | -5.37735 | -45.36796 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1228bb3f-aa81-33e8-bfab-0133334f3a79 | -6.5518 | -44.46742 | 2025-11-15 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a736e8f-f4ab-38f9-a3cb-0193fcb0dc2c | -4.55751 | -46.68703 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a16b63fa-5e11-307d-b724-0e2631237254 | -3.89199 | -46.21195 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 327e02ec-077d-3e45-9b5c-b3fa9eb0b864 | -5.05794 | -43.63354 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c39d81c4-fbb8-36f3-a78b-f8a56d31b63f | -2.86875 | -48.65492 | 2025-11-15 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73a9029c-0033-3c53-afa4-2ec158e49659 | -9.74569 | -43.95407 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dc05b2b-7449-3f07-b5bf-4c79ab2e23a3 | -2.43082 | -48.04357 | 2025-11-15 04:25:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e911bd6-35e3-3534-a9b1-adb4350a14b1 | -2.73412 | -45.30328 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54d57b49-ca53-3fcd-8db8-3ba9d77c5a6a | -7.21886 | -47.97879 | 2025-11-15 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9527f772-52c5-386a-a5fd-1b9bb1a70e93 | -3.24119 | -50.80474 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6ed802c-30d1-3f05-abc8-9e93642136d5 | -5.23776 | -44.35172 | 2025-11-15 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 5e23b641-9cbf-3b6c-9e5a-969a25c5086e | -7.88425 | -48.40004 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0f30856d-7817-366c-a47c-6872b696de9f | -4.33391 | -47.57175 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 349cac28-af6b-31c1-a198-10039c019eb0 | -3.10825 | -45.49237 | 2025-11-15 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47f62370-7c22-3562-a783-22e0fb747791 | -5.08288 | -42.65609 | 2025-11-15 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc659e5e-54d0-36ed-bb5c-ef9b9503bf08 | -3.99381 | -44.26569 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f718be69-c977-3a1f-9152-daf1c749e5ad | -7.42555 | -45.23125 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78837d0f-3260-3540-ac33-b5559317ee6b | -4.88186 | -49.38772 | 2025-11-15 04:25:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 496e7f88-85ec-397c-a377-43fe3479aa00 | -4.32506 | -48.63391 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6d3a8de-bac9-3c72-ba9f-af7f1d43f68c | -3.19788 | -51.37706 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2950488-f774-360a-bbd9-b1d18a682e75 | -5.33355 | -43.04003 | 2025-11-15 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0cdfd0a6-e6b6-3902-bc7e-4f61ee3863d1 | -4.80834 | -41.61653 | 2025-11-15 04:25:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7e938cb2-b0c3-31dd-8505-f7fc5a023ed9 | -5.58023 | -46.15053 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29dfe712-f791-3f74-afe9-f04137c632d8 | -6.16547 | -48.04737 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98b69c64-d509-37bf-ae3c-40debe56025a | -5.6086 | -41.06248 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 25bc8c37-c8fa-3d07-b6e9-6f4532ba38de | -5.36999 | -44.06668 | 2025-11-15 04:25:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0734c779-51d0-32b7-b330-9e36a744fbe9 | -4.45824 | -49.78459 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d3b1ec8-7cfe-31c6-a763-4c0afe0d0d9f | -2.73467 | -45.29985 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6781edda-fb98-3680-8f6c-b9dccb76b009 | -3.99637 | -47.68466 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1aa9046b-6bb9-30ea-9477-da924f894ba0 | -2.79222 | -52.9775 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc609fd7-9ee3-3509-9fdd-f7b4fdbc1db2 | -5.16587 | -44.85429 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cceea71f-68ae-37dd-9da5-648f5bef5c1e | -3.79777 | -52.01087 | 2025-11-15 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b8dd500-fb29-3d48-be38-bef8b0af0a93 | -4.47114 | -43.42235 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0510e34-f83f-3f55-bca7-d9d4c9aeca65 | -4.41728 | -50.831 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2204a6b7-fd09-326b-bdcc-d030fb840c9d | -4.27492 | -46.83946 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b278979-65e3-30ca-b668-00f768031489 | -2.60449 | -51.0293 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dec0cdfb-2451-3ace-87d2-be6a4fabc8dd | -9.49223 | -47.28282 | 2025-11-15 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7da9b9c2-00b1-380e-b0ef-4ef6ae5765c1 | -7.88546 | -48.39268 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76480a45-64bb-3406-88fc-ccd4a6a77d45 | -7.70752 | -49.38429 | 2025-11-15 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README41.md)
