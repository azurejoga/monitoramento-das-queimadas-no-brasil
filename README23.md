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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fed550f-04c3-3774-af7b-d4c77d28f047 | -3.09075 | -54.01578 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edd999a2-885d-3c24-9554-55871d10fe5f | 1.67578 | -50.66564 | 2024-12-01 04:21:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2402b71-b418-3480-8bf9-7dbda93c7fe7 | -2.80637 | -53.04452 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6de9cc0c-53c4-3e20-ba94-2ebe5e0a5ef6 | -3.36834 | -51.53642 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74066596-a001-3033-b48e-cd3acfdc50d6 | -3.14776 | -45.37208 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| f97c86ac-7991-3e22-b05b-3c113726b541 | -4.10093 | -47.80903 | 2024-12-01 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ac07674-5662-3009-81a1-db775ac01d78 | -4.53739 | -45.7017 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9878165f-d337-38b5-8d0c-e4b8ae30641c | -4.87057 | -43.01732 | 2024-12-01 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b74d92ed-19f6-32dd-8266-b516174ac2f9 | -2.73516 | -54.03884 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4b45618b-367a-3459-9e61-f2b2cbf27de4 | -1.6976 | -52.467 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d57cb8d3-55e5-3273-b470-d1d3636b960f | -3.85722 | -47.0478 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae33d2d2-780b-37b5-8d43-8e1b989745ad | -3.30348 | -51.1058 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b544b43-9757-3949-9ca1-13fbd319b258 | -2.69079 | -48.65625 | 2024-12-01 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe24ea3c-28df-37fa-89fa-ab87b973971b | -3.89334 | -46.68272 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 585b01b8-9685-3139-8ffa-1610e5537a05 | -4.35941 | -43.31266 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 715b2244-c30f-3175-b505-5961bf3de35f | -1.70001 | -52.4656 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 862e248a-93e2-3e38-b968-ae4b6cb86bbf | -2.62435 | -46.95647 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91f319a1-a6a9-37af-823f-f8a16ff49b7c | -3.53919 | -50.17854 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b029044d-12bf-39bd-9c16-f04fed6528e6 | -2.65527 | -46.58152 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ab335f8-139a-35bd-b994-de0ee445aa8c | -3.60474 | -49.98721 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51e61253-9fba-3f77-8635-4b711dc44939 | -2.97674 | -53.29135 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ef7cc03-ca53-3e5b-8d4e-e0769ddb7eed | -2.12277 | -46.57685 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 080f83fb-8029-31bb-9233-389e04a579df | -4.75141 | -41.10765 | 2024-12-01 04:21:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aaf49c3b-3328-35ed-86fe-6fb36a24a8ed | -3.54345 | -50.17922 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bdab6e2-b272-3082-9ec8-3f923aaac689 | -2.60794 | -46.57867 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c63e1ac6-c54a-3784-b5e8-8850c070de25 | -2.97509 | -53.29149 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8b852d7-0446-3df8-b5a6-e32340ef61fd | 1.1599 | -55.97456 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37a17d23-be1d-3469-831e-1d07b0223917 | -3.06724 | -53.81802 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2df09467-2c0c-3a3e-9a1b-7f1de3469540 | -1.20158 | -51.74251 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ec7f690-2d5e-37ea-b4b2-649d923efa92 | -2.99904 | -51.07012 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 019dba5f-bf6a-35d6-ae6d-286f8b8e4664 | -4.6986 | -42.39976 | 2024-12-01 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ef748d5-dca7-3842-b324-78e3fd435aef | -2.88246 | -53.33146 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e8596594-1118-31f4-9e6b-123f2322684f | -0.96525 | -51.65012 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c09a8248-616b-380c-bf39-5e2ea27ea77a | -1.95681 | -46.25195 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef942496-c721-3803-8d85-f73e050c1b69 | -1.34442 | -52.1303 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3aaabcb4-18dd-3ebd-9126-aac1535751ab | -4.89843 | -41.32578 | 2024-12-01 04:21:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 04440fcb-904a-30ef-96a9-5865620867ba | -3.32844 | -52.60009 | 2024-12-01 04:21:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de5896e1-bc2b-3ba2-9fd0-75c4137e2484 | -2.47533 | -46.57019 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69965c99-d28d-3790-84a4-b0e6b2684af3 | -1.43981 | -55.24848 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da9061b5-e561-31f7-981b-6384ada43080 | -3.354 | -50.51304 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d8f9e0fd-5dbf-3a85-98bc-8ac4026a78c8 | 0.9431 | -50.74772 | 2024-12-01 04:21:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 57de3b79-91fe-3113-9568-8c5aa87d77ee | -4.56607 | -43.9559 | 2024-12-01 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a74d2c23-5f6c-35c0-ad38-03a1fd538f25 | -3.06966 | -53.80334 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5e432a5-4af1-3c5d-81da-ba645893c267 | -0.96435 | -51.65561 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0dcc257b-6510-396f-8074-2e30da36fed8 | -2.10137 | -47.62907 | 2024-12-01 04:21:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 305811af-0a72-3aaa-87c2-ba875650fc9f | -1.52056 | -45.90357 | 2024-12-01 04:21:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4295e206-384b-346c-8ec6-b022880559b5 | -3.03752 | -50.24338 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ec30475-0075-33ef-957d-d1e2cb824822 | -3.59427 | -50.37011 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93110262-713a-3e65-ba40-4c4df45dc2fd | -3.09383 | -51.40823 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e5be698-3bc4-3e21-b613-b8feb5cc4556 | -4.01716 | -47.0022 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4543020f-ab34-39b5-8d1d-0d69f2154d2d | -3.30258 | -50.7985 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 470710cf-13b8-3921-bf7e-b08de36453df | -3.56095 | -48.67363 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ac6da031-813e-3fde-9cb0-c2e955170b91 | -2.60566 | -46.57037 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71541153-3843-31c1-b557-aa80be4e871f | -3.15014 | -53.83126 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 071a42dd-acaf-39db-8122-5edb7370b457 | -3.99967 | -44.75285 | 2024-12-01 04:21:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83b05b6a-5148-3572-b49d-a0a8704fc256 | -1.24477 | -51.78915 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 951d4240-e70c-3349-a90e-075301aa8115 | -4.53404 | -45.70118 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 08ba7f37-1ec7-3884-9454-54c594f77014 | -2.63629 | -46.19623 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4733fdd0-f66d-3b0a-9b4b-56b7905d739e | -3.21314 | -53.12775 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5dba1416-5a02-3ce1-9184-8f1906e82dc4 | 1.17149 | -55.96062 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0734cb8-6e14-3e15-b225-72dbd2098603 | -3.47609 | -47.68319 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6dc4434-672f-3735-8ae3-cccb7ac75c25 | -2.52296 | -54.07259 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db21aa46-27ba-3f2b-81d1-7a6281d9571f | -4.8918 | -41.32051 | 2024-12-01 04:21:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8795c47d-b053-3715-b1d3-a175e6045527 | -3.10473 | -50.3215 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61c275e3-3d64-3139-bc3e-467145e38da5 | -2.80002 | -53.05016 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 697ea672-b1ad-3f37-835e-d1f7ba2d7600 | -3.01109 | -51.79249 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ca7113b0-6d4d-3177-9e87-be53458e9623 | -0.83488 | -51.81463 | 2024-12-01 04:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ac6d542-b1f1-3d8d-80f2-58d09c88461c | -3.34765 | -50.74659 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 542292d3-a489-378d-9916-cd1d10eac6c2 | -3.36277 | -50.51434 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c4addaf-684f-31a0-a3a6-80dd780fb4e5 | -2.97161 | -48.04264 | 2024-12-01 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fb7b9d8-25cb-3810-b57f-887b12735a8d | 0.9427 | -50.74984 | 2024-12-01 04:21:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 90da4a63-cec3-3aca-b08e-c93e9c0f7c4d | -1.00383 | -51.72425 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 23b302de-a3ec-3c47-a814-6a615ad227f2 | -3.84505 | -46.52339 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 429e811a-3ca1-370e-a3b9-328bbf5a2bbd | -2.87716 | -46.80338 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f9ae168d-779d-3a95-bf78-b627483d7720 | -3.76159 | -46.51463 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 222a1b09-24ca-3ee0-9905-54fef0b79ceb | -2.72734 | -46.24089 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 61fa4115-cf12-31fc-8afb-8f5bfd8beabb | -2.69331 | -46.86498 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60f9741e-d90d-34d4-a316-f1680b5107c3 | -2.68354 | -46.14226 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c93703cf-d25a-3959-94e1-50a0b01af6d9 | -3.5149 | -50.21998 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39cbd13f-3c87-326f-9542-d83ee329fb64 | -3.11127 | -53.76031 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46bebd9c-c705-3093-99d0-20f026c6e814 | -2.89175 | -54.16096 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da50de42-c4dd-305c-9511-6fd17ab70f74 | -3.13762 | -45.97745 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b80f43b-a3f9-3eaa-9ddb-322385734149 | -2.9149 | -51.71782 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08e339ef-7b0b-3678-ae21-decebbd842f8 | -4.04811 | -46.83156 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e022a732-d5fb-38fd-ac88-fc87feeabff7 | -1.3449 | -52.12737 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 468a064a-6194-353c-8ee6-af03216f89ba | -4.55864 | -43.30328 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 656e36a5-e95b-3ca1-8a1a-c6a57406f3e7 | -1.66506 | -53.77742 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 41b097ac-5085-35b0-9351-1d1761b93881 | -2.56021 | -46.5633 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47ad8409-c591-33e5-9605-a1f673553916 | -3.42129 | -50.4292 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bcfe71b0-4104-369d-af4a-389eea1dcfee | -2.46298 | -46.58024 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3f0ebd5-f203-30d9-a4c4-88cd62fbae3f | -2.11698 | -46.24109 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4eb7cf8-f481-3d97-be9a-1fddff410f88 | -2.8454 | -49.88186 | 2024-12-01 04:21:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3fe76f6d-4817-331a-bb21-a952de782ed7 | -2.79678 | -51.89795 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d9e9204-8115-308b-8935-565cd5bc8d6b | -1.70702 | -46.14813 | 2024-12-01 04:21:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9774144f-3840-3c01-84a4-774660fa780d | -1.18811 | -51.76319 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c69fefbe-93cd-3a50-81a9-5e56f4ab7633 | -3.28438 | -50.16879 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9989c8f0-a20b-303c-9629-e588a5045ae5 | -3.82566 | -46.60197 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcd9f5aa-65af-39a4-8fbd-df468355b12f | -2.63711 | -46.57531 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96cdda63-f279-30e6-998c-ccc57fff79dd | -1.27072 | -54.55216 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b112c34-b35c-3f14-95e1-5157d89c0f8e | -1.52653 | -52.66482 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README24.md)
