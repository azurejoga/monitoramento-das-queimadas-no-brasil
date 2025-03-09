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
| 3388acf0-1ea3-34ac-a64d-c797f015d5d6 | -20.988 | -43.3281 | 2025-03-09 00:00:00 | GOES-16 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| e0650921-2c24-3cff-b07f-aa4fe182500f | -20.9672 | -43.3341 | 2025-03-09 00:00:00 | GOES-16 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| 1ef071d4-d359-3046-b40d-41edfdab80b8 | -11.9686 | -41.423 | 2025-03-09 00:06:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c5096406-fe53-3a71-9922-fff58f903ba5 | -15.5639 | -42.674 | 2025-03-09 00:06:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e4663f7-7c3d-3508-8691-ebd2f2a12af2 | -7.0451 | -44.400799 | 2025-03-09 00:06:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c8510fd-94ba-303c-9830-5bd6bb9a7f2f | -15.5757 | -42.681599 | 2025-03-09 00:06:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79d6c3dc-f130-3388-bfe0-b33e9ed0bf2a | -9.971 | -37.256599 | 2025-03-09 00:06:00 | METOP-C | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| 7eedc4f2-38e0-3f5f-8b88-18d79a74b532 | -20.970501 | -43.327099 | 2025-03-09 00:06:00 | METOP-C | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9d0a16c-6604-3419-bfb7-cb5bcce97478 | -15.5679 | -42.6931 | 2025-03-09 00:06:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ddcf9559-a00f-3eaa-b434-3d677a21c333 | -11.6449 | -37.790798 | 2025-03-09 00:06:00 | METOP-C | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd0dd4eb-29e7-3175-9cc0-75689d3845d8 | -9.9808 | -37.254299 | 2025-03-09 00:06:00 | METOP-C | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| 3723cb0e-9df4-3fc4-82cb-3cff3687b623 | -20.972799 | -43.339699 | 2025-03-09 00:06:00 | METOP-C | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 263f13ab-ca44-3bc2-a665-be93160d68e0 | -15.5659 | -42.683601 | 2025-03-09 00:06:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0bd9edb4-4afb-3ab3-b019-3e0b667edd6c | -15.5737 | -42.672001 | 2025-03-09 00:06:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a043c900-924f-38a5-881a-1ac42ef5153b | -18.815201 | -51.620899 | 2025-03-09 00:57:00 | METOP-B | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 144d8e34-dcae-3543-9efc-d21fbb040d98 | -27.686501 | -50.798698 | 2025-03-09 00:57:00 | METOP-B | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 10600e8e-10dd-33a5-850f-cab0bb43aae2 | -18.8132 | -51.612499 | 2025-03-09 00:57:00 | METOP-B | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fed56176-469d-3cf2-a8a9-4f88b67e58f7 | -22.1283 | -51.456402 | 2025-03-09 00:57:00 | METOP-B | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b0e5929-7c15-3c18-8ca8-9cc5c378af32 | -22.1264 | -51.448299 | 2025-03-09 00:57:00 | METOP-B | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a336a6cf-cc05-3f38-9aea-0835428b8579 | -8.0742 | -34.97612 | 2025-03-09 03:42:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9590736b-97a4-3bc3-bcf2-f3012846437c | -7.37761 | -34.88427 | 2025-03-09 03:42:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ad1c986a-772a-3f14-8d04-fc57dfc10597 | -8.41951 | -38.70903 | 2025-03-09 03:42:00 | NOAA-21 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd645277-1ff8-3ae8-b4a0-55cef818cfc3 | -8.57512 | -36.31929 | 2025-03-09 03:42:00 | NOAA-21 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 11084a27-e3bd-32de-9afd-c24666f11255 | -7.04774 | -44.40535 | 2025-03-09 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86c0f8eb-baad-3f22-951b-bce473e3eec5 | -9.91539 | -37.17716 | 2025-03-09 03:45:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06efd6c1-e1a0-38df-8ffe-e17347c0c642 | -13.91264 | -46.11389 | 2025-03-09 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2744954c-2709-3d4b-bfb6-2f0d0a879432 | -11.64231 | -37.78934 | 2025-03-09 03:45:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9e2a556a-dc49-38ad-acdf-f76364d9a27d | -12.49546 | -45.52778 | 2025-03-09 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9294ff0a-517a-36c7-b299-a71f0c53ac22 | -13.08323 | -44.20995 | 2025-03-09 03:45:00 | NOAA-21 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28e3dd8b-a2ef-33e5-934f-97e5f2bd14fb | -12.40929 | -38.41562 | 2025-03-09 03:45:00 | NOAA-21 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 47f3aac8-26e1-3827-8326-423e1088ceb2 | -13.90872 | -46.10632 | 2025-03-09 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d703fbf-1179-332a-8bc3-5e10052c8c52 | -11.96341 | -41.42511 | 2025-03-09 03:45:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2556d167-5b18-314f-b2e9-c5f9a70a3f16 | -12.50063 | -45.52871 | 2025-03-09 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82241e49-0776-32f4-9116-792e794dea53 | -12.14794 | -38.36044 | 2025-03-09 03:45:00 | NOAA-21 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 76cfb6a7-0eb6-3a9f-b12b-c2a33ed239ef | -12.14454 | -38.35987 | 2025-03-09 03:45:00 | NOAA-21 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 82fbc6c5-8750-3468-a5db-e63877689a73 | -15.61943 | -43.25501 | 2025-03-09 03:45:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| af1c3086-638e-347c-8869-b2011dd04b61 | -10.50642 | -42.40687 | 2025-03-09 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 130a93bc-9183-35a9-a88a-bd5bcfc6541a | -15.94212 | -38.97663 | 2025-03-09 03:45:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1f4d1fe7-f28f-372c-a3e9-a3d295b78a55 | -13.90808 | -46.10957 | 2025-03-09 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1da7a529-b943-3dfb-bc5d-593e0c086b2a | -13.90744 | -46.11281 | 2025-03-09 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02dd839d-b636-3d80-9e21-e468099afc34 | -9.97029 | -37.26331 | 2025-03-09 03:45:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5c0c0ac1-581c-3bd5-bfd6-dab33266acef | -13.08417 | -44.20495 | 2025-03-09 03:45:00 | NOAA-21 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e01b302-5a90-30a7-97f5-9f0e63316c45 | -9.15681 | -43.12247 | 2025-03-09 03:45:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 51d44dfe-2f31-3bbe-bbb6-23f33349516b | -22.61083 | -47.46633 | 2025-03-09 03:47:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89883c3e-de1f-3b5a-a953-dfce48a36c1c | -17.09644 | -43.80522 | 2025-03-09 03:47:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 373efe6b-8420-3085-baca-87bfc7a6221c | -28.65365 | -49.45992 | 2025-03-09 03:47:00 | NOAA-21 | NOVA VENEZA | SANTA CATARINA | Brasil | 4211603 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 212cf55f-f0f8-3c74-81db-818d44bebe75 | -19.10839 | -46.91671 | 2025-03-09 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 970d94f2-aad0-3910-ad9c-49ab71e4a54f | -19.83264 | -40.11346 | 2025-03-09 03:47:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 3b0c61d8-a01f-3a60-839c-deae0bc71b93 | -21.20795 | -48.55643 | 2025-03-09 03:47:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6496e4e0-dc64-3986-9ad3-c7fe433d5434 | -21.62633 | -43.46604 | 2025-03-09 03:47:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ab485fb0-06e4-35ad-a91e-adae3f410b53 | -22.71795 | -46.12472 | 2025-03-09 03:47:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.6 |
| 57c9f3ac-ce5b-37ee-b5d2-06e0d0ceee7b | -23.34066 | -46.7741 | 2025-03-09 03:47:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 52fc7e2d-33f1-37d9-a659-40414de54364 | -22.71892 | -46.12611 | 2025-03-09 03:47:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| 71b66142-544c-3ec4-87dc-a2e78205f26e | -22.78674 | -43.75857 | 2025-03-09 03:47:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2f6edbd9-a871-321d-93c4-53e188bcd60c | -19.7188 | -40.35382 | 2025-03-09 03:47:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4036e7df-905a-3500-a537-b9b14360cb98 | -19.83776 | -40.08263 | 2025-03-09 03:47:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 67e545b0-68fc-349f-b054-761a65726067 | -17.59576 | -43.19841 | 2025-03-09 03:47:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a518366-1669-3f6d-a344-0cba39e0bdb5 | -20.31229 | -45.58519 | 2025-03-09 03:47:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66648138-3c55-32ab-b778-847886fc50a3 | -22.71989 | -46.12119 | 2025-03-09 03:47:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| 902f79bb-6907-31f8-8e46-23f622812782 | -20.8999 | -43.8197 | 2025-03-09 03:47:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 16983275-0dd8-3f84-ae18-38839af1a2b8 | -16.68116 | -43.88197 | 2025-03-09 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d67b338c-06e8-33c2-a5b0-08b54d2de78c | -22.11921 | -51.46355 | 2025-03-09 03:47:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5838efc3-bfa5-34e6-b7b3-586b74c2a31b | -22.71451 | -46.12508 | 2025-03-09 03:47:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0c7d8d8b-1725-3da4-bdf1-7885a548aefa | -19.10336 | -46.91587 | 2025-03-09 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65528ae8-5311-335e-b3c9-7a9fe81662f8 | -22.71546 | -46.12031 | 2025-03-09 03:47:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bb428529-f97a-35ca-8c64-30bc8235a8f3 | -21.18104 | -43.97993 | 2025-03-09 03:47:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2b8cf983-5078-3ba4-8b51-f044e44147c5 | -22.71895 | -46.11992 | 2025-03-09 03:47:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| f20d3de7-9848-3f6a-bb74-8654853a0bd9 | -16.34847 | -43.69738 | 2025-03-09 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d11b6f46-9b63-3310-a991-9787956f6d43 | -22.69881 | -43.34819 | 2025-03-09 03:47:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a793e42c-609a-356b-aa93-f1d707c73254 | -25.56898 | -49.36667 | 2025-03-09 03:47:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 38937b74-796b-3e86-92a3-81bed5bbd25c | -23.03459 | -43.49628 | 2025-03-09 03:47:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7931151c-fac0-3c0a-9cb5-3ab15758b0ab | -20.41556 | -43.55436 | 2025-03-09 03:47:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c282de30-09d1-344c-8630-0710817c3daa | -16.68042 | -43.88595 | 2025-03-09 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ffe9b13-ef32-32d8-9ca9-3a356610ad0f | -20.44011 | -41.60588 | 2025-03-09 03:47:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 729f0383-8d3f-31a4-b4a3-74ff136d1516 | -23.40545 | -46.55497 | 2025-03-09 03:47:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 38537e49-548b-3f87-8c85-e592ae59fa77 | -22.11794 | -51.46886 | 2025-03-09 03:47:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7a482399-ae8b-3bd2-9e1b-2a1bc5d54db7 | -16.80435 | -43.96065 | 2025-03-09 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dba3a8c-645f-3b33-b8f9-75b214701ffd | -19.32896 | -43.70191 | 2025-03-09 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39702eab-91c1-3858-90d3-34bdb79ffdf8 | -19.3249 | -43.70114 | 2025-03-09 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8489b79c-71c1-3b1f-9e27-c3525f1678dc | -19.10402 | -46.91269 | 2025-03-09 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f64f9cab-a4f2-388f-b7df-86ad4f76fe89 | -20.76187 | -46.77054 | 2025-03-09 03:47:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4dc6c655-fd7d-38fa-b3a7-4005c06a737f | -28.6523 | -49.46598 | 2025-03-09 03:47:00 | NOAA-21 | NOVA VENEZA | SANTA CATARINA | Brasil | 4211603 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f53d3f85-ef7e-35cd-94e0-1ae39b9724dd | -20.67068 | -43.31475 | 2025-03-09 03:47:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 652ce411-724f-38d2-851c-61dd3aed8540 | -23.54168 | -48.236 | 2025-03-09 03:49:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c170392-586b-3433-85c9-f811e5ed048d | -23.98534 | -48.91877 | 2025-03-09 03:49:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 076498ae-15c5-3a06-a431-3303725cf94c | -10.55634 | -46.42308 | 2025-03-09 04:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 028f3434-3b41-35f8-be5e-1d0da5d48b67 | -7.04775 | -44.40542 | 2025-03-09 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27b000d5-bb74-3e1e-bbd1-8b7f2fadce43 | -12.1468 | -38.36089 | 2025-03-09 04:08:00 | NPP-375D | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ccb07129-fa7d-3459-a2ae-23a7fa3b00d6 | -8.4181 | -38.70911 | 2025-03-09 04:08:00 | NPP-375D | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9b21d2b0-9154-3ad4-94ed-7551060df14e | -11.96609 | -41.42467 | 2025-03-09 04:08:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa13d1d0-6706-3c89-9668-d0b5702dae79 | -9.96711 | -37.26199 | 2025-03-09 04:08:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b1c44026-37b2-32f4-b02d-1d7763101f23 | -10.50493 | -42.40634 | 2025-03-09 04:08:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7afaf1de-d9a8-37bc-8a30-b9e0b4e81e16 | -6.20441 | -44.83263 | 2025-03-09 04:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c274ce69-227d-3f54-840f-50298dc67b26 | -7.04422 | -44.40476 | 2025-03-09 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8ff478c-c778-33e7-a40e-3ecb90b79f28 | -9.15649 | -43.12273 | 2025-03-09 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b3fcdaf9-2889-39c9-85b9-373eba201493 | -9.15593 | -43.12627 | 2025-03-09 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e3f18b4d-c171-3a52-b650-4b7ea0e87767 | -12.14714 | -38.36266 | 2025-03-09 04:08:00 | NPP-375D | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 184d7560-3b31-34ca-a51d-c4b54be4dd2c | -10.88194 | -44.17164 | 2025-03-09 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1a4d21b0-f1df-33cb-8b45-1de8643d7b1e | -9.97115 | -37.26266 | 2025-03-09 04:08:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9aed7d7f-4db7-3b0b-abe1-b649918896d5 | -12.14783 | -38.35764 | 2025-03-09 04:08:00 | NPP-375D | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README2.md)
