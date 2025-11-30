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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24d85b47-7743-3b0d-96b0-3d1383921086 | -2.38463 | -47.60944 | 2025-11-30 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ceb4b36-dff1-3405-9e1b-8055d0d028a4 | -3.23062 | -45.52901 | 2025-11-30 03:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b29ce623-5668-3ca6-b16b-1c1620d69cf7 | -2.51473 | -49.10019 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bf32cdea-9aea-3d2c-8246-cdf36debf84e | -6.68524 | -39.69563 | 2025-11-30 03:53:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b2ea96d2-08f7-3dd9-a5a5-3bde4aa74d13 | -5.23424 | -41.24113 | 2025-11-30 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05517aa4-54fb-3add-a8e9-51ad7dbc94f8 | -5.50833 | -42.58352 | 2025-11-30 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3703e950-ce16-3425-8f65-b7fd343e634c | -3.43955 | -41.50099 | 2025-11-30 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7cca8369-436c-3273-a028-ea6b9e1b6eef | -5.74591 | -40.8171 | 2025-11-30 03:53:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0789218e-c096-3f13-a868-031fa54a9b63 | -6.80859 | -42.23332 | 2025-11-30 03:53:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3f168015-305a-334a-a164-ad36b14bdfda | -4.77313 | -38.55963 | 2025-11-30 03:53:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f8a56b66-26ab-3fc4-8675-98f4c5fbba15 | -5.53552 | -40.70522 | 2025-11-30 03:53:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3855e092-5861-303d-ac09-839d92f8815b | -5.73143 | -39.83604 | 2025-11-30 03:53:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 39c5c88b-fdb2-359f-9569-c3cbd08398df | -4.35675 | -43.16584 | 2025-11-30 03:53:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35e5d187-6d2b-3c84-a0ea-7f563299d89e | -2.44289 | -47.08307 | 2025-11-30 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2eb93e4-4198-3e8a-bdcc-efbe395773ba | -4.54551 | -40.47313 | 2025-11-30 03:53:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9246027f-f447-30e2-9840-df3a64eb693a | -7.35893 | -39.39693 | 2025-11-30 03:53:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 540d4a03-6e70-35a7-bdc4-bcb97c55498a | -5.54708 | -39.66938 | 2025-11-30 03:53:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 820c5e84-602f-3948-93c8-96b7e4316ea8 | -5.05459 | -41.51542 | 2025-11-30 03:53:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8592025f-073e-3aee-a12d-8a56c4f82ad0 | -6.7005 | -41.26331 | 2025-11-30 03:53:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 487a0f7f-9c46-34bf-85f7-386dd9f90189 | -2.6411 | -45.91889 | 2025-11-30 03:53:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4eb9a52e-10df-3a88-87b5-cb827df4807a | -5.36688 | -43.02517 | 2025-11-30 03:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e5f29a3-a556-3fe1-8ee5-4c632d28c3bd | -6.40414 | -39.69126 | 2025-11-30 03:53:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3429c365-bca2-3faf-8ab0-64b0da1f950a | -3.58694 | -41.66682 | 2025-11-30 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8008d8f6-15ef-3ee7-8071-791f639baa55 | -7.04601 | -37.24057 | 2025-11-30 03:53:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b2e6f7fa-4e30-3248-b9f3-144e53cf19d6 | -2.70368 | -48.34958 | 2025-11-30 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5134ae3d-13b6-369f-8a11-2e1a16c2a403 | -4.48313 | -37.80721 | 2025-11-30 03:53:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f2be469b-4fb1-3ddb-871e-f883df1d8696 | -4.60774 | -45.2049 | 2025-11-30 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ca60fca-3711-37e7-bebf-175033840c32 | -2.63944 | -48.54986 | 2025-11-30 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f07ae66-c5fb-30f7-8786-a5fec78dde2e | -2.50971 | -49.10708 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 657cccfb-bbcb-3cf5-b571-1c858f9d155a | -2.17496 | -48.41935 | 2025-11-30 03:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ba3bc576-d20a-3c6c-a6f5-4ee306a5427b | -3.94755 | -42.03233 | 2025-11-30 03:53:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8aa0664f-8337-3c77-a825-5e45c2bd7266 | -2.38967 | -47.61444 | 2025-11-30 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a15cdb8-21dc-3fb8-87cc-417935c72ff8 | -5.31396 | -40.88536 | 2025-11-30 03:53:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fae14fd2-963f-3b49-8076-530be7940138 | -2.6859 | -47.36394 | 2025-11-30 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bb77ae1-b9ea-3e8d-9a2d-139b7d5e652c | -3.58767 | -41.66222 | 2025-11-30 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e41ab4c7-56dc-3c81-9a27-ed9b55ccbfbf | -7.22408 | -40.27875 | 2025-11-30 03:53:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6b111a50-83ad-3184-b8d6-9c86b8a84da0 | -4.07668 | -39.95355 | 2025-11-30 03:53:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 309977ec-5223-3b1e-8d43-b9035717239b | -3.4376 | -41.31131 | 2025-11-30 03:53:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f1a43e19-b0e4-3959-b621-f137b4465b64 | -7.49304 | -37.43014 | 2025-11-30 03:53:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 325c07b7-cb27-3ab5-9a9c-3aed8addeb42 | -5.98084 | -39.48428 | 2025-11-30 03:53:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 82b79e6e-3dc0-3846-bf84-e7d1696e1225 | -6.67171 | -40.12745 | 2025-11-30 03:53:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| daeb3771-234c-33bc-98cd-0b61f8cde0e4 | -5.11291 | -43.29368 | 2025-11-30 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a14456f-45ec-3bf7-9109-3aa25951dcc5 | -5.74941 | -40.81774 | 2025-11-30 03:53:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 38330a13-dfec-3db9-b60a-9e0a71715f06 | -7.49638 | -37.43066 | 2025-11-30 03:53:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 20.6 |
| c744686d-5b32-39c4-b9fc-c9794f5dca10 | -2.60379 | -47.3392 | 2025-11-30 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5cd23591-4ff5-3653-bc2a-1a5852e3acec | -3.59521 | -41.66344 | 2025-11-30 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c66c0abc-8137-3776-bd3c-fbd4b68ac18d | -6.25401 | -41.44786 | 2025-11-30 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ddf1593f-ec79-3595-ab64-90b737924820 | -2.51678 | -49.10319 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72205650-7eda-37d5-95b0-b06f2aeeeba1 | -5.15491 | -36.59451 | 2025-11-30 03:53:00 | NOAA-21 | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d48dc9d3-7345-3fad-84bf-2785a55138aa | -4.5517 | -43.22415 | 2025-11-30 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5b6229d-482d-355b-b46a-49837cc52c8a | -7.3295 | -38.76403 | 2025-11-30 03:53:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a8808c7e-8484-3b35-9789-c37bdd6b26d8 | -2.90203 | -45.26247 | 2025-11-30 03:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3040f93f-5d6b-363a-90b1-baaff61ab7a5 | -7.07263 | -39.25065 | 2025-11-30 03:53:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6d2ef078-a833-374b-ab7c-6501d8b3327b | -6.6886 | -39.69613 | 2025-11-30 03:53:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a2dabccf-348c-374a-8b27-7e2592d0d637 | -2.44348 | -47.07947 | 2025-11-30 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c026371c-15ff-3c57-8fd6-780dafd420c8 | -6.86521 | -39.3574 | 2025-11-30 03:53:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cca7499e-ef84-3f3c-8297-9ff0bf8464d2 | -3.59449 | -41.66801 | 2025-11-30 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cae2aa96-9aba-3ce1-8f92-06af9cf31409 | -5.414 | -40.8719 | 2025-11-30 03:53:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9edf021f-35aa-309d-aebc-d2fdf72cfe3b | -4.02921 | -38.72396 | 2025-11-30 03:53:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 73972a35-99b6-30a4-83e5-fe8db224bbc7 | -4.42668 | -43.30593 | 2025-11-30 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9d358a7-f9a9-3f9b-868c-f4c5267a947a | -2.64473 | -48.55537 | 2025-11-30 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1a3cf0cd-ac04-3cb4-9df7-da2be14f340d | -2.30345 | -47.73848 | 2025-11-30 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32600db3-48f9-3b71-93fe-5c836add7814 | -7.83816 | -35.46661 | 2025-11-30 03:53:00 | NOAA-21 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ed6abb16-f790-34ee-ad13-059718b2fc39 | -3.19622 | -43.96693 | 2025-11-30 03:53:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 41cf5e05-451a-3088-818f-7174e3d3839d | -6.69985 | -41.26728 | 2025-11-30 03:53:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cb830bf9-9f32-3cc5-a684-74ad44b4fd08 | -5.05428 | -41.51462 | 2025-11-30 03:53:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7061bb1d-9af5-39f7-957a-f828453ac203 | -2.64019 | -48.54539 | 2025-11-30 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e68cdc98-d962-3305-867a-ff6c0ce82d0d | -5.73483 | -39.83654 | 2025-11-30 03:53:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b26ba4a5-d86a-3e9f-9d8e-bceab291476f | -3.37525 | -40.60154 | 2025-11-30 03:53:00 | NOAA-21 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 636cdb3b-dff4-31c8-84d6-b113cc2a205d | -2.6334 | -48.54884 | 2025-11-30 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8b4e380-ed48-344d-8fd8-04a55ca2c0fc | -4.36084 | -43.1665 | 2025-11-30 03:53:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb15f019-37d1-315a-983d-3098022e9dae | -4.81321 | -43.08549 | 2025-11-30 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f97e8d68-52ad-3912-89ee-bb2ab40b2585 | -2.60097 | -49.2606 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 787cbcef-d596-3fac-b3a3-669a3cc55f1a | -6.95813 | -39.0711 | 2025-11-30 03:53:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1813b8e4-1202-3a37-a1b7-76b61205d342 | -5.42459 | -41.38563 | 2025-11-30 03:53:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c87a1a1-07ca-31aa-9342-6296c7ae1e55 | -4.81666 | -43.08975 | 2025-11-30 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a47d2550-0d0e-31ac-9881-e32de8d7cfca | -7.49583 | -37.43422 | 2025-11-30 03:53:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b42d273b-59c0-3e52-b40d-dd87038646e0 | -3.5839 | -41.66161 | 2025-11-30 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 300e0f99-8f23-3c5b-a6a3-998012166b0e | -3.62204 | -42.75519 | 2025-11-30 03:53:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46642db4-ef03-3a1c-b355-2c917e971a1b | -6.44699 | -39.6944 | 2025-11-30 03:53:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8708c243-488b-33a9-abee-994510cdbe4b | -5.23784 | -41.24171 | 2025-11-30 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7523d22f-d7bc-3ef1-9ef9-d07bdb4b5422 | -2.44841 | -47.08391 | 2025-11-30 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4ddcf830-2ac3-38da-89cd-3fb803fb3faf | -2.69591 | -47.39801 | 2025-11-30 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b95aa792-6ceb-3121-b30a-4e4bbef8d76b | -4.35614 | -43.16946 | 2025-11-30 03:53:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0805047e-445e-3ef3-b68a-bcc852b8c4cb | -4.42195 | -43.309 | 2025-11-30 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89d3a151-4b4b-373f-b3c9-afc5260498f5 | -3.97731 | -42.52186 | 2025-11-30 03:53:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1277f460-0ba3-3a3f-a098-9c65183ce5a0 | -5.50523 | -42.57809 | 2025-11-30 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 47c96d6e-9d01-3fd5-b33a-5188d1fa8c65 | -4.26433 | -38.05143 | 2025-11-30 03:53:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d65fb6e2-bd25-3301-9f7f-f3bf9e9edee2 | -2.16742 | -48.42755 | 2025-11-30 03:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cc5a464-0a50-346c-8d88-bcb6e86a0b19 | -3.23461 | -45.53532 | 2025-11-30 03:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f915a739-8a12-3eac-8f5c-ec328fee955d | -2.51596 | -49.10822 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c45994cb-ad59-3276-ac34-36101e613f42 | -5.24213 | -41.2381 | 2025-11-30 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf86456d-f9bc-38fe-9eef-6bc16c0c2418 | -4.99698 | -40.73574 | 2025-11-30 03:53:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 33044b9f-6e41-38d1-9d9b-b6a9f058acc8 | -7.33333 | -35.06785 | 2025-11-30 03:53:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6cdcfe68-7b46-32ce-aeb8-52251dc4479c | -2.29766 | -47.73762 | 2025-11-30 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c04a6a20-3536-346d-bc71-65e7b74a4b8f | -2.92605 | -48.2291 | 2025-11-30 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b6f6d577-2bf2-3f62-97b4-899e026b1eb1 | -5.74529 | -40.82095 | 2025-11-30 03:53:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 25451c54-abff-3199-b23d-8ad56249296b | -4.52355 | -44.75182 | 2025-11-30 03:53:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51be5e3c-2a48-3e0a-8980-ea8a90d1e7d7 | -2.50762 | -49.10409 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 806aa9e8-4588-33e7-bdc1-235c6c64382f | -2.92676 | -48.22485 | 2025-11-30 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README8.md)
