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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c39bc0b4-4c4c-3436-80f5-e9ffe64d5f3c | -4.12018 | -50.68947 | 2025-12-04 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a027d32b-c195-3666-8785-9261e7219ff0 | -4.82684 | -43.20138 | 2025-12-04 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98f64b3a-7d3d-31aa-ba4e-3723a0f1de92 | -4.22009 | -46.44996 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 766c1d29-664c-3313-b03b-8cadedf25440 | -4.69279 | -46.43758 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbbb4398-ff26-3fc2-bade-3f1c4847e2f4 | -4.38906 | -43.13033 | 2025-12-04 04:21:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 11cf623e-9882-31c8-905b-62ba4e5c793a | -4.74814 | -45.89084 | 2025-12-04 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42a1e28e-230c-39cd-a08d-884a0ed89be0 | -4.34654 | -46.1427 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d42ed60-e218-33bf-905c-6bb9694cb3c0 | -4.08113 | -47.04464 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53aa552a-b191-3e51-a4e8-968355c1bd41 | -2.42398 | -45.8005 | 2025-12-04 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7d4c82b6-ea6b-3237-8f68-8fd4acf7a59d | -4.21663 | -46.44941 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4442a81-6a44-3040-8b85-913643cd8b95 | -3.93649 | -47.20678 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1934f1a-e7ba-3d5d-a235-27d70554f4f7 | -6.43349 | -44.78513 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31b0ddc3-76c0-3620-aad9-2238415721c5 | -2.63407 | -48.03165 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62626d82-37d5-3f87-9e3e-839ef533a641 | -3.04621 | -48.41723 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 84b7399f-7f80-3309-ad91-cbf8a66b8457 | -2.94527 | -48.59639 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 094b9c22-4438-3a0d-bb97-bfcba4e92370 | -5.02885 | -41.01529 | 2025-12-04 04:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5d957bb3-8a6f-3a9e-b22c-eaf5fe6bec42 | -7.2186 | -45.04783 | 2025-12-04 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27434302-bf10-3b14-8013-f381e595f85c | -2.34933 | -46.91648 | 2025-12-04 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d85fc67-9472-3fb9-ba2f-0ee277e9ff8a | -2.79629 | -48.90454 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74a727f7-a5d8-3b69-95a3-1670879c367f | -2.14649 | -47.87958 | 2025-12-04 04:21:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 611d4b0a-a21d-3344-9990-9fc7ebb26837 | -5.85838 | -39.93224 | 2025-12-04 04:21:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c0edf9c3-08b5-34a1-8ea1-65c2190c8e8a | -4.67127 | -46.30727 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f4a6285-b4b2-358e-bbee-a9f401e21bd4 | -3.33673 | -42.1036 | 2025-12-04 04:21:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a0256fd8-20ce-36f7-b227-6ca85bea73fc | -5.98738 | -44.59444 | 2025-12-04 04:21:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfa6510a-a502-3a7c-a0a7-1b17260375cd | -2.43667 | -50.27031 | 2025-12-04 04:21:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65b151e2-3d37-3db7-a2c1-be67cec233c0 | -6.54454 | -41.50961 | 2025-12-04 04:21:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4afc9a32-becf-33ad-af68-e3bfd031ddf5 | -2.5923 | -46.80597 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec9e64c6-3ae3-3330-b81b-6184d9f4900a | -2.32928 | -49.084 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41d7178c-5236-35aa-a11e-8cca0dc661b5 | -3.34866 | -40.42217 | 2025-12-04 04:21:00 | NOAA-21 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ab708a5f-7a80-3609-9e63-b15d85d8e0f4 | -7.56629 | -46.47869 | 2025-12-04 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ccf8041-1d61-31f5-846a-4ae4c250a14e | -5.99376 | -40.3793 | 2025-12-04 04:21:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 20ad702f-7c96-3172-8eb9-ff837b08a202 | -3.91236 | -47.71373 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48f61e43-b680-3e08-bf77-a00d36083387 | -3.84656 | -47.83834 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ccc8ef6-4e5a-3143-a45f-1e063e4e6c2b | -5.03336 | -43.97326 | 2025-12-04 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55692038-2d76-3b2c-a652-1e65f6942a44 | -7.86726 | -38.72989 | 2025-12-04 04:21:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b9d998ba-393a-333b-a052-6f47d3bd6270 | -4.80618 | -43.07503 | 2025-12-04 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07116f42-57b9-32ae-8ce4-c56af2616b25 | -2.02412 | -47.00153 | 2025-12-04 04:21:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1657710-e405-31bf-a410-dc97ddc8aca7 | -2.35123 | -46.91788 | 2025-12-04 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da049c17-27b5-345f-905f-9eaa8318744a | -4.73023 | -45.6999 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bfc7110-b175-31a2-a7e6-4b0b71f5ddb8 | -5.02674 | -43.97223 | 2025-12-04 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8762f231-b156-3b3d-9064-a198b20fa636 | -2.07651 | -48.36893 | 2025-12-04 04:21:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a41adb8-d205-3ac3-809c-b4f215480223 | -5.47847 | -45.40504 | 2025-12-04 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ca8bdd5-4d0b-324f-b471-5864ab611cc7 | -3.2271 | -46.85534 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c485a14d-82c9-3888-b9e3-b125b03d9c1a | -3.19121 | -41.36779 | 2025-12-04 04:21:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db32512e-a7aa-32f1-95cb-8746e0bfd0b1 | -3.39084 | -47.2739 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2698d4d-d54c-3736-bcda-196d0f86f885 | -3.9434 | -47.02414 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81ed2f65-c578-38e4-8c0f-7c503ca9f23f | -3.93714 | -47.20267 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f26ef35-9923-39f1-b885-ac2691bb6493 | -4.46017 | -44.13759 | 2025-12-04 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ad3a215-a927-3595-887c-45077c4035f6 | -2.87978 | -46.80324 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 726d0ca5-a092-3b99-a5c3-20458c17848c | -5.36219 | -43.0322 | 2025-12-04 04:21:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1624b80f-fa69-388d-94db-ec3224c1d73f | -4.53533 | -44.26572 | 2025-12-04 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e408e88-d4fb-3fac-bcd8-88eefdc0914a | -1.96984 | -46.05097 | 2025-12-04 04:21:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1de208f6-6d44-3c12-9920-bddde4b688a3 | -2.41977 | -48.59059 | 2025-12-04 04:21:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 336e4d43-b557-3424-90eb-67e7b6da18cb | -4.55777 | -45.80584 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e93f7b27-c32b-3ff3-9cea-0c96ecebccdb | -6.58457 | -44.66723 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ca9a297-a73e-378e-b1fd-0270934113c6 | -4.97835 | -37.47765 | 2025-12-04 04:21:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 31d5dd5c-58d0-388d-afae-6763d79a38a2 | -4.13067 | -42.93462 | 2025-12-04 04:21:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25c817d2-ab8e-3059-add5-ad2fcdefd844 | -6.4258 | -44.791 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14fe2802-3770-3e81-b548-b9c899391696 | -2.94514 | -48.59427 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1be0c6b1-b508-3910-b326-89063dde7c61 | -2.56566 | -49.06951 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a01af255-e9a1-3554-b079-b23f87ceb0de | -6.00699 | -42.3243 | 2025-12-04 04:21:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9b287c3d-b4e3-3895-b517-2b6b8a9859d8 | -4.25679 | -44.1546 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f65f743-f226-31cc-ab85-0a0a6711d746 | -5.00722 | -42.93786 | 2025-12-04 04:21:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2448ff1-9d45-300a-a486-50dd4bab438d | -4.34312 | -46.14217 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2d2df39-951b-3d52-9ef6-947e66bf4354 | -4.38798 | -46.67204 | 2025-12-04 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 034e64fa-e367-3d54-aca2-23324663066c | -3.76912 | -51.19689 | 2025-12-04 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 470e8b6d-21e4-3d99-b55b-3ad09fb4bc84 | -4.93078 | -41.14425 | 2025-12-04 04:21:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1b696122-2622-3f85-87f5-f9a34c6704e5 | -2.49228 | -47.82816 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1d32e35-54b3-3e12-8453-a1d6bfa97a01 | -3.32702 | -44.37845 | 2025-12-04 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea1780f2-8383-35f5-8a84-387943936576 | -4.50101 | -45.77117 | 2025-12-04 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67f559ae-2738-37ce-9a95-179723b71316 | -6.42471 | -44.79791 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bb36d1f-ef53-38a4-9e65-2aaf10f87a65 | -5.82911 | -43.00362 | 2025-12-04 04:21:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8da29864-33a2-34a0-8ca6-8a6ba1b774dd | -4.73301 | -45.70402 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feabc9d1-0447-3092-87b8-e31b2904b2fa | -7.56967 | -46.47923 | 2025-12-04 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e49c98da-b98b-31be-99bf-8cd49bf54bce | -4.45791 | -38.38439 | 2025-12-04 04:21:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0c50b2c6-64ed-34d5-bc00-37d72c0ec751 | -3.76275 | -42.50095 | 2025-12-04 04:21:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0825a331-0fe9-3b37-bef3-fed648501145 | -4.83074 | -43.19836 | 2025-12-04 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63215af9-5974-3df4-bd22-d8df5c69fa18 | -2.92339 | -45.5097 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e2c0c5f-ae89-36b1-b118-11a2e43e78d1 | -4.4318 | -43.86091 | 2025-12-04 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 07ebad19-a616-3444-93d6-3bd7abb88a16 | -2.44568 | -46.31316 | 2025-12-04 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5dda070-cae0-3585-9853-781190915554 | -4.21088 | -44.25317 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7df9734-72a8-3344-9fdf-fe0e53f0b4a6 | -2.92011 | -48.23064 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d32a4ed1-fee5-3841-844d-e2d0adf9e876 | -3.64036 | -42.22844 | 2025-12-04 04:21:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f8bad813-b899-388d-881c-378fa3543ee8 | -3.68863 | -41.8653 | 2025-12-04 04:21:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ad7bbc6d-46b3-3e1d-9520-eb7669cdaded | -3.04154 | -48.4215 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79f39dbb-2f16-32ce-8682-e863fd48cce5 | -2.59164 | -46.81002 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3519ce5-5d5a-37aa-b8bd-f4c2a079443a | -2.64711 | -51.62164 | 2025-12-04 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8dee86a-e312-33fc-8dab-bf62cc18ae59 | -2.42872 | -50.2915 | 2025-12-04 04:21:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b45249c-6d09-3bd9-8eae-f6d1e6577f94 | -4.0344 | -46.97622 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aaaa9df3-3cf2-3211-9d0f-ebe5d485c34b | -4.55497 | -45.80168 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 749bbfbd-2510-3308-8839-a818dce78516 | -4.70087 | -46.43108 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77177adf-a652-399e-a21e-d53403814a82 | -2.24541 | -47.98917 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62fa85ab-181f-3af1-8a72-afecc3d016bd | -6.59389 | -39.5386 | 2025-12-04 04:21:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8d4371f2-2bc6-3861-85a6-7040a7583161 | -2.54338 | -47.80125 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d05dfa83-8077-3312-8f0b-6b9668c6b7ce | -4.50358 | -40.50508 | 2025-12-04 04:21:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e3cf7b0-fe26-3d8f-9faa-65735cb4492a | -2.14193 | -47.88369 | 2025-12-04 04:21:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c622eaad-2737-36bd-9109-1f1b8a1b4efc | -8.16294 | -43.17225 | 2025-12-04 04:21:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ffc83cf5-2f35-3765-a89d-ca325ceb6850 | -3.23429 | -46.85208 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b53a0e4-20ef-38b0-9e4a-97d905fb5623 | -4.25631 | -49.25022 | 2025-12-04 04:21:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d751030c-f2fe-366b-a110-9730b682283c | -4.05034 | -46.60792 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README11.md)
