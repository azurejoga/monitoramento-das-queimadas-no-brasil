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
| 6599dd6c-a12d-305c-bf2d-17ce30135d6b | -3.43421 | -42.54375 | 2025-11-06 03:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1847be4b-bd91-33c8-9f1e-a7524742a96a | -4.58227 | -43.34344 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3708107c-51af-3931-9e45-b74129acd79a | -4.84888 | -40.63216 | 2025-11-06 03:55:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a3abb170-0a4f-3ba5-9433-59ff431fef8a | -3.92297 | -38.37523 | 2025-11-06 03:55:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 519f12b6-b87b-36b9-b15f-6b055f174901 | -4.75862 | -42.6578 | 2025-11-06 03:55:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 31d0ae94-4c63-3df9-9dc1-f67447b04c37 | -4.58578 | -43.34786 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9b42abd-c08b-3383-9a0b-3d522ed0b8a4 | -3.11572 | -51.21246 | 2025-11-06 03:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6b27806d-2026-35a9-97b1-90388192965f | -5.1471 | -41.24333 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b76bef55-5f06-3b70-90a1-3564d5eb28c7 | -3.89625 | -42.54785 | 2025-11-06 03:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 19dd11fa-cd8f-3253-ad31-5a82fb79bef4 | -3.47599 | -43.65455 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 800997da-8fb7-3356-a787-a91a4b9a484c | -3.93061 | -47.69513 | 2025-11-06 03:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5ea63de0-9fdc-377f-9f5b-d20582682baa | -3.89709 | -42.54273 | 2025-11-06 03:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b38a6583-e66a-3fb0-9679-1da23a5b19ee | -3.96524 | -41.81469 | 2025-11-06 03:55:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1f497fd1-aac7-3cfb-8179-3a99c587e668 | -3.4737 | -43.64175 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 126a7be5-e3c9-350d-885a-38dbe6e305a6 | -4.58588 | -43.33364 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e241f66b-07dd-3caf-9ad8-4d44e291a279 | -3.45134 | -45.6522 | 2025-11-06 03:55:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5822046e-c8cc-3daa-a6f3-84e8e5ba4982 | -3.89244 | -39.93154 | 2025-11-06 03:55:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 507d9547-c04e-31b4-a16b-10a39d6eebb2 | -5.14934 | -41.25224 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| df300b4f-f543-3fed-988d-6933646c0953 | -4.57994 | -43.34415 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2eeee352-4e41-3408-8c2c-6dcc8872275c | -4.58648 | -43.32991 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44846d17-786d-372f-8ed1-746a3afaf956 | -3.47169 | -43.65385 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 395329f8-e697-3464-bf5b-a485a36cb677 | -4.58353 | -43.33601 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 23000b26-f461-3229-8820-bf18f5c1b7fa | -3.92434 | -47.69804 | 2025-11-06 03:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b4b2935d-d5bf-3c50-b98f-42e55b828363 | -3.83133 | -44.40014 | 2025-11-06 03:55:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9d46ea7-df47-3535-8a86-264e24ed26bf | -4.78612 | -37.38469 | 2025-11-06 03:55:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6c1de720-8322-323c-abdf-8f8832b116b2 | -5.06369 | -40.60412 | 2025-11-06 03:55:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 748aadc2-8789-3241-ba45-ed20534fb4ce | -5.29032 | -40.88315 | 2025-11-06 03:55:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dfae075d-2b95-37d5-ba5e-2ffd8cfeece8 | -4.58641 | -43.34412 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 428c120e-8264-3f29-8da3-45c17acc363b | -5.15297 | -41.25274 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| da4e3e40-c15e-3a4f-81c6-1ea8755def31 | -4.81953 | -37.7541 | 2025-11-06 03:55:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7aa1e698-d578-3ef3-9622-7f0fe8d1ca9b | -4.58468 | -43.34109 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf3b62f2-d0ab-323c-a0b2-5cae22458e4c | -10.01389 | -38.16055 | 2025-11-06 03:55:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6b6055f7-9672-3e75-ba1e-dd428c928953 | -3.59837 | -42.86391 | 2025-11-06 03:55:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1deadd47-2e38-36bf-ac94-369c9583c4e9 | -3.47826 | -43.66751 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a81e5d4-c0de-388b-af86-c7e88f8a6667 | -9.44873 | -40.65322 | 2025-11-06 03:55:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2f7c1909-9d8e-3fa3-94d1-47e12fbb3f37 | -3.39923 | -40.83428 | 2025-11-06 03:55:00 | NOAA-20 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f0c076f-15df-3baa-aa75-f6ff7e295505 | -4.78666 | -37.38122 | 2025-11-06 03:55:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f110bc00-c3a7-3bb7-acf4-e8d1d50c3a2d | -3.925 | -47.69414 | 2025-11-06 03:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8b7bfd62-c6a3-3fa0-8bf4-cec639d9a911 | -4.5829 | -43.33974 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d0994ba-46de-3369-8c01-5fadd237fb8a | -3.44942 | -45.6564 | 2025-11-06 03:55:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12deb0ee-25b8-376c-baf0-bd2e1895e0de | -3.46307 | -43.65254 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15e53336-9aa3-3c2f-a102-7db3c605c94c | -3.92996 | -47.69901 | 2025-11-06 03:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a79e8586-6fd8-382b-ba73-8e459ace64bb | -16.55743 | -41.72076 | 2025-11-06 03:55:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6ea39287-cd8b-377f-80c5-09801cef4ffe | -3.90419 | -42.54913 | 2025-11-06 03:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 794d8f9b-c32b-3803-aa82-388ca657c611 | -4.58347 | -43.34858 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d2f1370-408e-3528-b4f7-8e3514d89198 | -3.46895 | -43.67032 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a7e0c07-1273-3484-848a-50b11d99e4d9 | -4.48131 | -43.42487 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33a16d87-6cad-3518-9b70-c66efd415572 | -4.59532 | -43.34175 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af7755b7-be95-3878-ab72-18f7d8517140 | -9.88075 | -40.56548 | 2025-11-06 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0b8c1de-5473-3eca-8046-6cb980a88ab6 | -3.92302 | -47.70587 | 2025-11-06 03:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db4b8677-4f88-32d0-b834-9081597c61d2 | -5.13568 | -41.26736 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ec2b1838-fd47-31e5-94c5-4278d9819cdf | -3.58957 | -46.05746 | 2025-11-06 03:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6258e051-53f4-3d27-8d24-6a79bfd0ff9a | -3.89228 | -42.5472 | 2025-11-06 03:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c7a24db6-843c-3131-b089-daba380f41c7 | -12.43281 | -39.52498 | 2025-11-06 03:55:00 | NOAA-20 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7b769adb-8232-37e1-9390-daf06f9db6b7 | -3.48324 | -43.66415 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03bc5f57-7cb5-3117-acaf-523b9a41b5ac | -4.94338 | -40.1358 | 2025-11-06 03:55:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 98decac8-fe49-3313-8834-b6aa36fe1347 | -3.86925 | -48.3352 | 2025-11-06 03:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7611eec6-6670-3902-9f08-61bf4ef26576 | -3.43022 | -42.54309 | 2025-11-06 03:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e75149c-e00f-3ca4-a6a2-008aa6fdb7d1 | -3.46373 | -43.64853 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eebb896a-29ae-3346-8cfa-15a2ec7588b1 | -3.46533 | -43.66548 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 292edd03-6d44-3d08-a62d-13af1d91b3a8 | -3.9293 | -47.70293 | 2025-11-06 03:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2842149c-210f-3c9e-a8ed-5ac22bd0c39f | -3.40294 | -50.27505 | 2025-11-06 03:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffc71bc2-857b-3d9c-a1d1-861c73324fb2 | -3.43364 | -42.54724 | 2025-11-06 03:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 198df0db-be66-3d43-826e-fc7563263cf1 | -11.82084 | -43.16213 | 2025-11-06 03:55:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 54ca9e6b-4400-33c2-8c85-5ef33a74e703 | -3.46738 | -43.6532 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a0679e0-3e03-3e26-b0ba-6cbe07194349 | -5.33201 | -35.5522 | 2025-11-06 03:55:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f2aae02e-2dfd-3e44-8782-5d6d238412cc | -3.7813 | -49.43444 | 2025-11-06 03:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e3ecb8d-779a-3e8e-8b1c-cc83ff28463c | -4.81898 | -37.75755 | 2025-11-06 03:55:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fdac4978-79e9-339c-b8f2-f2a5645d9ba7 | -4.58114 | -43.33671 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 527772a1-c8bd-3a19-899a-7f65ee84e3af | -15.29534 | -46.89958 | 2025-11-06 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8ddf20c-b03b-33af-a640-10967a469dd8 | -4.66871 | -43.20562 | 2025-11-06 03:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf203112-6ef2-339a-a25b-432981e7671a | -3.98537 | -47.30328 | 2025-11-06 03:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b3b71ac-9ca7-30ad-91f5-235ffed82705 | -3.92465 | -38.40748 | 2025-11-06 03:55:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 60c82731-b505-3667-8277-f44110b53b4f | -3.78214 | -49.42944 | 2025-11-06 03:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0348fb64-8858-3b69-a7af-6477e8ecc286 | -5.15227 | -41.25698 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1bf7143c-5b8f-3408-aa3b-b86a544d887b | -3.47758 | -43.6716 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c11d2b0c-3508-3768-ae84-54332c9cc48d | -16.66376 | -41.35694 | 2025-11-06 03:55:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6fb90b92-762e-3741-9e5e-c9a5c0605d70 | -5.13298 | -41.25495 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 59ced33f-d618-34ea-b81b-05879d1c0b33 | -4.10808 | -48.02049 | 2025-11-06 03:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1260a4ed-db14-3c90-8896-a53dc0d750ce | -9.42109 | -43.6197 | 2025-11-06 03:55:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5c47aff7-b039-37e6-9c97-aa3d7a113215 | -4.48896 | -45.92644 | 2025-11-06 03:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5cf0f145-fdf5-3c35-9054-bf323adc27a5 | -4.57519 | -43.34721 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a322035b-751e-3e33-9a58-5d272f24f94c | -3.47961 | -43.65935 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20dcd7e2-c7ef-3466-b3a9-48c635f55852 | -3.90022 | -42.54849 | 2025-11-06 03:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| afb497d5-0c68-3ef2-8c8f-fa9c936e7f49 | -3.43465 | -50.25056 | 2025-11-06 03:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c80b9294-5950-3c3f-9641-a3a6bc6f9610 | -10.0697 | -42.737 | 2025-11-06 03:55:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f890b88-c84e-31dd-b547-3c16b437f89c | -3.46239 | -43.65659 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42434535-ab7e-3363-a809-13f80cc54a48 | -3.48029 | -43.65525 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c975a2c-8eed-3858-8628-b7815901efd6 | -4.58164 | -43.34718 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cab334d-6fc0-306e-9b61-2586f12676fa | -4.5764 | -43.33975 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c458fce-0fd4-391c-ad9d-fc5bb1c0e614 | -4.75467 | -42.65716 | 2025-11-06 03:55:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 47.2 |
| 154ee88b-963a-343f-aae4-63db4d4a3212 | -4.15319 | -46.81778 | 2025-11-06 03:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69621b5a-0b38-39c7-8395-2aac52173615 | -4.81859 | -43.53412 | 2025-11-06 03:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9047b92b-eeed-382f-bbfd-9f56813b089c | -3.11139 | -51.21224 | 2025-11-06 03:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 243fc944-5fe8-3bc6-a18a-c52e578b57ce | -10.3287 | -49.63931 | 2025-11-06 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4a73764-6b74-317d-a003-b27781c8045d | -4.59945 | -43.34245 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ed6c2e6-5d6c-3dde-bb9d-c5c5497e7271 | -4.85304 | -40.62877 | 2025-11-06 03:55:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 128405b8-e8c8-3d60-bba9-fc61aba4ae7f | -4.7555 | -42.6521 | 2025-11-06 03:55:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 52.2 |
| 7c69e994-a529-3543-a86f-1c14d2bf1e6b | -4.1066 | -48.0293 | 2025-11-06 03:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 37640786-eeb5-3287-b523-337dea8db655 | -4.58528 | -43.33736 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README16.md)
