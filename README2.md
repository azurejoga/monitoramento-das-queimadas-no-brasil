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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f921d860-d097-3336-9bd8-bd2fa5deb280 | -17.77794 | -42.80564 | 2025-04-25 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb185487-8abb-3807-a66f-32589ac4db68 | -17.8855 | -43.76716 | 2025-04-25 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77c06a54-4a29-30c1-9fd1-ced2ca852cf8 | -17.53368 | -40.04818 | 2025-04-25 04:04:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 52ccf6ad-3019-35ce-8041-76c544b3be63 | -17.65558 | -42.26353 | 2025-04-25 04:04:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 71df0698-6335-330a-b8b4-7f2fd9c2ea89 | -17.75364 | -42.89435 | 2025-04-25 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fcd1d398-f29c-3adb-a31e-2fa9a27bb5bb | -17.37972 | -42.48291 | 2025-04-25 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b2e0a12b-c7af-3727-b816-b62687221867 | -17.65832 | -42.26768 | 2025-04-25 04:04:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0140cd7-a180-3ca1-a124-f107dddb052b | -17.65501 | -42.26714 | 2025-04-25 04:04:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 95603af3-e25a-37d8-8edc-817b9b22439b | -17.78067 | -42.80982 | 2025-04-25 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74b43b59-e07d-3f42-a04d-0ee910163a43 | -28.39308 | -52.87985 | 2025-04-25 04:06:00 | NOAA-21 | NÃO-ME-TOQUE | RIO GRANDE DO SUL | Brasil | 4312658 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3fc60c12-5945-3632-814f-314145868252 | -6.2411 | -43.3677 | 2025-04-25 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 0222cb3a-39e4-3bfc-aa8d-77dc5a57cd51 | -11.3963 | -52.9477 | 2025-04-25 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 903798bd-f6fd-3e12-b6e6-0e69ea8c376c | -6.2224 | -43.3693 | 2025-04-25 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 2ffba9c9-1514-395f-a4a0-ccc61fe30863 | -11.3963 | -52.9477 | 2025-04-25 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 3c4bb552-38f2-3560-a09a-368c186e49dd | -6.2411 | -43.3677 | 2025-04-25 04:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 5728ee3c-81d4-327a-bf7f-9578813b803f | -6.2344 | -43.37671 | 2025-04-25 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 713c28db-c8c8-3923-b51f-179c2bfc746d | -6.23565 | -43.36859 | 2025-04-25 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b92e9565-9964-3b88-8fa3-27bfd1c2015d | -1.6244 | -50.10568 | 2025-04-25 04:25:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b499980c-4fc1-3ea1-bb53-63b168a345bb | -6.2302 | -43.3802 | 2025-04-25 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2381992d-041c-3fca-a584-a2db645ab4bd | -6.23628 | -43.36452 | 2025-04-25 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e94b79c3-7a75-330b-b91a-aa173b614646 | -6.23145 | -43.37212 | 2025-04-25 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9030dcda-6706-3adb-863a-dc7e8d56716e | -6.23502 | -43.37265 | 2025-04-25 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6c5b164-a97f-3898-801b-db42346621a3 | -3.43699 | -51.24627 | 2025-04-25 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3e0ccaa-cd37-349c-8a25-a744b58d58e0 | -6.2386 | -43.37318 | 2025-04-25 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 900d83f3-3df0-3345-a781-86723e8208ed | -5.84963 | -47.89096 | 2025-04-25 04:25:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8edff37c-7895-3760-9376-8917bd6177ad | -1.62842 | -50.10633 | 2025-04-25 04:25:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef3ed104-8294-3387-926b-fd0d7321efdc | -6.23082 | -43.37617 | 2025-04-25 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfa85f52-2a3c-3d59-9400-5f3a5cf1ec5d | -9.61041 | -37.03282 | 2025-04-25 04:27:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dc2cc1aa-43f0-3ac8-af5f-0b4ea16fef9d | -9.71689 | -36.69928 | 2025-04-25 04:27:00 | NPP-375D | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 546b6131-daa5-31a2-a3ea-0962fc04cd05 | -11.27905 | -52.46109 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cf8e49e-841c-3176-a30a-757c18645cc3 | -11.40283 | -52.95179 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64bec9c7-82ff-36cb-b38e-4ccc0218b5e6 | -11.40514 | -52.94421 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c89be6b-9f3d-32a8-9d86-70d54db9558b | -11.40217 | -52.95562 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf5cfb1d-5648-33c9-9950-1930b2f6f839 | -11.40792 | -52.95262 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| afe90905-4a10-3338-b3f9-560920913fc1 | -11.39935 | -52.94718 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c7bedca-09ff-3d47-9802-200342decebf | -8.79213 | -49.80495 | 2025-04-25 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e187b05f-eb06-3a30-a139-20e2aef7fe94 | -8.07978 | -43.11433 | 2025-04-25 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5384a29c-1df4-3c53-a624-898bf265021b | -11.39686 | -52.94265 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 735d8041-ba4f-33a7-ab4c-1c2bd1a15d68 | -11.39963 | -52.95102 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb0717bc-0826-3c09-b893-7457db7cedac | -9.71742 | -36.69519 | 2025-04-25 04:27:00 | NPP-375D | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0ccf1cf1-08f0-3170-92fd-67e771922f97 | -8.86766 | -49.89276 | 2025-04-25 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e59dbb2-f8e8-3ffa-95c1-2842da1dda49 | -11.4 | -52.94339 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 565826d2-3b72-3826-80ce-5e8a4863d0ee | -11.40066 | -52.93961 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d3195bf3-d36b-3d63-b090-fe2345bc6c96 | -8.17917 | -46.70573 | 2025-04-25 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1d4a40d-3beb-346b-a494-6187934f2423 | -11.39894 | -52.95485 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 238a8830-6df0-3e09-97a2-e9bf923ae02f | -11.27438 | -52.46393 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cb0efe5-f449-314f-a882-697c89fe4357 | -9.61309 | -37.03427 | 2025-04-25 04:27:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 780bc9dd-9464-3ba2-8266-e34e3e023fcd | -11.40309 | -52.95564 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d22b82c9-779b-3c47-9c9d-9361dab0b6c2 | -8.08348 | -43.11488 | 2025-04-25 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9687e424-0f85-389b-a2b1-a666eedd276d | -11.4015 | -52.95949 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97394afc-9ca1-3f08-a56d-547c66743f4f | -8.11106 | -43.12152 | 2025-04-25 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7e44aa13-ef1b-3197-8412-bc305d826c73 | -11.39869 | -52.951 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90c09663-a11d-3384-a54a-acf5937617a1 | -8.72869 | -44.01779 | 2025-04-25 04:27:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c15b6d8f-c166-3437-9155-4196dfe74dc1 | -11.40723 | -52.95644 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8711ca84-536c-3684-812d-0aa93cc85c1f | -8.10871 | -43.12318 | 2025-04-25 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 712c807c-97de-309f-bb77-02839d3de010 | -11.27841 | -52.46468 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 547323c9-5ba0-3702-88ac-b0caf531b32a | -11.80256 | -43.79731 | 2025-04-25 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30412a8f-d507-3f53-b130-6346b3e7dfa0 | -8.72808 | -44.02179 | 2025-04-25 04:27:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f76d588-296f-33c5-a585-331db8cc8720 | -11.40349 | -52.94797 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3847768-503f-31dc-a94b-73edda57b315 | -11.27374 | -52.46753 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6274c0a-1e6f-3efd-9e76-af315c7f4fb3 | -8.72513 | -44.01724 | 2025-04-25 04:27:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0859e4a-2dda-32a8-ae62-ded8fe45c413 | -11.27777 | -52.46828 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ca9fae2-b0dc-3f04-a4a5-7f0cf461e28a | -11.40239 | -52.95948 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 79f738ad-0f0e-3991-8b02-540401e019b0 | -8.86406 | -49.89215 | 2025-04-25 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24847ce9-9835-3644-b3f3-44789d2bee98 | -9.62126 | -37.03798 | 2025-04-25 04:27:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d1e8c214-ab51-31ef-af3f-ceaf343c5378 | -11.40032 | -52.94721 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a6ef0627-76bc-3433-b4ac-25123784329b | -11.401 | -52.94343 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7c1049c9-bae0-3fda-9783-1f9983d733b4 | -11.40415 | -52.94418 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 69b9e6bd-981b-3a87-9427-8a1fede658df | -11.27502 | -52.46035 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa608473-f96f-391b-b3c6-e7c7ec7836fb | -9.62175 | -37.03413 | 2025-04-25 04:27:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 58cbc31b-c356-38fc-9cc6-5232d0f31a6d | -9.61607 | -37.03349 | 2025-04-25 04:27:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac956e78-92ba-3640-ac37-8e8cbfaa474a | -11.96734 | -44.00752 | 2025-04-25 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 894724f8-fa37-3e92-a768-6ace6ed80e1d | -11.39754 | -52.93889 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7e6540c5-da63-36ce-bace-efaca1bccf84 | -9.72323 | -36.69579 | 2025-04-25 04:27:00 | NPP-375D | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 58af5f64-11e7-3d66-8994-3962b76df3ae | -11.40378 | -52.95181 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47ec541b-1eb6-32c5-b410-0f697df3fe90 | -10.2683 | -51.14155 | 2025-04-25 04:27:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1edd79bc-4111-3142-97c8-08ffe05068d8 | -11.4048 | -52.9404 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 69817fc1-6c77-32e6-9f9b-ba4653aea80e | -9.61876 | -37.03487 | 2025-04-25 04:27:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4abca7ef-8050-3a80-a89a-af4a75807c8d | -11.93578 | -46.40446 | 2025-04-25 04:27:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48875fb8-5948-306c-a5a3-ddf30fbdc160 | -9.6136 | -37.03041 | 2025-04-25 04:27:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0daf79e-171d-31dc-9738-7a457377178a | -8.72452 | -44.02124 | 2025-04-25 04:27:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 736a75a7-c9ed-31d2-8b2e-2c179c25637f | -8.10501 | -43.12259 | 2025-04-25 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3c227e7b-b97f-3039-8057-5a14db3519a2 | -9.61928 | -37.03102 | 2025-04-25 04:27:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 00c7ef06-c744-3bbf-89aa-41aa9e5e5198 | -7.43767 | -45.42183 | 2025-04-25 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37768cf8-c67b-3d2a-974b-433102cb8358 | -11.39802 | -52.95484 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 269415ed-1614-3580-a408-96d9141a8586 | -8.17585 | -46.7052 | 2025-04-25 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dba2a7a0-cec9-392a-be11-5c6f10543838 | -11.4086 | -52.94882 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a27c9e4-2c2b-3f78-b857-049eb8e9bb68 | -11.40168 | -52.93967 | 2025-04-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8960e66d-70d9-30fc-94f3-b3d16e2aa99e | -9.61825 | -37.03872 | 2025-04-25 04:27:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 30a39eb7-175a-36d4-9984-5d2f73b7c317 | -14.08897 | -48.11412 | 2025-04-25 04:29:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b903bf90-8f38-381c-a26d-c752f7641741 | -17.88688 | -43.76904 | 2025-04-25 04:29:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb8ed462-6ff8-39b6-ac25-fa000e2ef324 | -17.88332 | -43.76481 | 2025-04-25 04:29:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b466b941-cf4b-34ae-afe6-74bf945baef3 | -17.65678 | -42.26528 | 2025-04-25 04:29:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e72db41-9e07-3e55-8da7-9164dddf0162 | -14.46478 | -45.2766 | 2025-04-25 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25d8b1b6-87d2-3535-aaba-670cbf3d4d8a | -16.67947 | -43.88436 | 2025-04-25 04:29:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb427cb4-f7d7-30b7-979d-c895fab94473 | -16.70251 | -42.34718 | 2025-04-25 04:29:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e272ba32-8028-327d-ba1a-ad56eb704e21 | -17.88283 | -43.76851 | 2025-04-25 04:29:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fbfedaa-97aa-3a5c-aff5-1327a24fef56 | -6.2224 | -43.3693 | 2025-04-25 04:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| d1ba8e09-e19e-3855-82e0-d3cf1696499e | -26.33424 | -53.18898 | 2025-04-25 04:32:00 | NPP-375D | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a723ec17-1bb3-3ea0-9cab-6b115ed9e8b7 | -30.1513 | -52.02386 | 2025-04-25 04:34:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |


[Clique aqui para ver as próximas entradas](README3.md)
