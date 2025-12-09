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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b55e83a8-4628-3ea1-8807-0d70347203e3 | -5.5182 | -39.00953 | 2025-12-09 03:36:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49e135e0-fbeb-33cb-94e2-0e8c617c53f6 | -8.98297 | -35.2425 | 2025-12-09 03:36:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 653242e4-cf78-3f9b-a26c-fdecdfbb10c7 | -6.74703 | -39.67319 | 2025-12-09 03:36:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63f91060-0b5c-3020-b2ea-7af1bd0726ed | -3.60841 | -40.41405 | 2025-12-09 03:36:00 | NOAA-20 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a20c8ba2-7844-3f0b-a3bf-4e40ad63e803 | -5.22117 | -39.2564 | 2025-12-09 03:36:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 599a4827-d0ca-3d75-9ca1-d33e28c8d596 | -3.43463 | -41.65329 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cdb453ec-b964-31c8-a045-d124df98c55a | -4.92726 | -38.75249 | 2025-12-09 03:36:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf00f7ef-a930-3bea-a5b1-755bf825ccf4 | -8.31273 | -36.43159 | 2025-12-09 03:36:00 | NOAA-20 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1db4d1a4-c383-36ac-a168-d03751ae4831 | -2.05652 | -46.50296 | 2025-12-09 03:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 30fb95f6-76fb-3093-af85-41c35a9504bd | -5.22138 | -39.2519 | 2025-12-09 03:36:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 47370c7e-ec93-3d60-92f1-778fe4459a7b | -5.70483 | -42.07351 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1b7ed2a3-f6ec-3ad9-90cc-3ebc36fbf2fe | -8.98354 | -35.23896 | 2025-12-09 03:36:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 543d7c4c-fd01-3508-9103-d5dd132f46bb | -5.70947 | -42.06104 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e355cce3-c004-3dfe-82f5-e4a13ad676f6 | -3.33463 | -42.84083 | 2025-12-09 03:36:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db17e8de-6c43-3c76-b9a4-f9ab9315f057 | -3.87623 | -42.51795 | 2025-12-09 03:36:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a685cae9-baf2-3785-85b4-4b55a18fdb4b | -5.22563 | -39.25253 | 2025-12-09 03:36:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 41bf5102-a0e1-337b-8c3e-3ffdeff30dfd | -5.71048 | -42.07134 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 59aa357c-8ae7-398e-b1a5-558d8636f4a0 | -3.32905 | -42.83991 | 2025-12-09 03:36:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9b8bd1e-4cc9-3b07-be99-6a5cd3c1338c | -7.86533 | -38.7308 | 2025-12-09 03:36:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0a5e0fe2-7bcf-37c5-9e07-f5d69dc9ceaf | -3.42895 | -41.65552 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 693a5072-429a-3697-b8b5-fb01d151ce8e | -5.70537 | -42.07048 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 52de54a1-a85c-30a7-a493-5c4c1056d17b | -3.60501 | -40.41381 | 2025-12-09 03:36:00 | NOAA-20 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fa621b07-215e-3de5-b69e-87f4a8c23d87 | -5.99357 | -38.93906 | 2025-12-09 03:36:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da155338-ca84-3b7e-b683-c6c6a27b5f0b | -2.93954 | -40.12872 | 2025-12-09 03:36:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0c763954-41ba-3ad3-beb3-332bd6132e68 | -5.67528 | -39.60157 | 2025-12-09 03:36:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 38f6bec6-61e7-3d16-9992-59da0215385a | -5.04132 | -43.60513 | 2025-12-09 03:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2f0ee15-cfef-3261-8f43-f5cbce25d9b4 | -8.8633 | -38.75369 | 2025-12-09 03:38:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aff1dec4-01c5-3fc0-b64d-5de19bec94b3 | -8.48561 | -40.50267 | 2025-12-09 03:38:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2daa2883-4823-342c-a4c8-ce642c6ae259 | -13.45455 | -38.95708 | 2025-12-09 03:38:00 | NOAA-20 | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c7b22d48-f8c6-3120-b100-d3d8dbb4fb84 | -3.4451 | -41.6413 | 2025-12-09 03:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| c6be2116-1f95-32ac-b015-cede6d35ddeb | -3.4449 | -41.6653 | 2025-12-09 03:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| b95fe6a3-3bcc-3bb9-b24b-177e222d23a0 | -3.0909 | -45.2074 | 2025-12-09 03:40:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| cf24f633-7610-30bb-b12d-73afe315cf87 | -3.4262 | -41.6662 | 2025-12-09 03:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| a5893a93-7aff-3617-8790-f49b9f137133 | -22.8939 | -43.65722 | 2025-12-09 03:40:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 34b10287-805f-3c1a-addf-e28f04b1674e | -18.88753 | -41.94781 | 2025-12-09 03:40:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9c5e647e-88a0-3f66-8ac2-468e665d7758 | -3.4264 | -41.6423 | 2025-12-09 03:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 68a36368-1b86-34fd-976f-8890d0b2e406 | -3.4262 | -41.6662 | 2025-12-09 03:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| cc2198d5-c1ff-39fc-98ee-cd835b703d6d | -3.4262 | -41.6662 | 2025-12-09 04:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 156b6a48-57ad-3665-a269-4893ac9bd24a | -3.4449 | -41.6653 | 2025-12-09 04:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 6f0129d2-34d4-393e-81c9-ee42ca983d1a | -3.4262 | -41.6662 | 2025-12-09 04:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 77dff3ad-6442-3b91-af63-404822263f76 | -3.4449 | -41.6653 | 2025-12-09 04:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 48.0 |
| e163cdd3-3d3d-3ca9-b241-500fdf1ac5eb | -3.4262 | -41.6662 | 2025-12-09 04:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 55.3 |
| 37407d38-c1fd-39db-b9dc-386fed0fdefd | -3.4264 | -41.6423 | 2025-12-09 04:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 44.8 |
| 0db3a215-b337-3ed6-bb7c-dd5794e1eb75 | 3.39612 | -51.25143 | 2025-12-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dabb1b5d-13a9-3b53-b331-9b53a26ee676 | 3.40004 | -51.2459 | 2025-12-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae56054e-e8b4-3df9-b16a-cd399d4c1199 | 3.41943 | -51.24806 | 2025-12-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b87d522-6330-3c8b-9a2e-b9a62a25a54c | 1.57276 | -55.99259 | 2025-12-09 04:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3d24c3e-8a1b-3b42-80c9-448bf16ed1e5 | 3.39146 | -51.25211 | 2025-12-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbe90cd8-c8f6-378e-ba49-3bda403e4fc1 | 2.01927 | -55.67408 | 2025-12-09 04:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3dcbde9-b635-341b-b2db-863c559f8e35 | 1.11092 | -51.32851 | 2025-12-09 04:23:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9d2887a-13d9-3bfa-a6d1-3c8848f755c2 | 1.57177 | -55.99561 | 2025-12-09 04:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ff9e144-293a-34fa-931b-a9a98241f2cc | 2.01963 | -55.67646 | 2025-12-09 04:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b49dbd52-319e-3226-8380-c42b916160d9 | 3.42409 | -51.24738 | 2025-12-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a22043d8-4a94-36de-a12d-2a5d1efb139a | 2.01894 | -55.67194 | 2025-12-09 04:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eb51f37-5916-3cda-b4d6-118054fd20ad | 1.57104 | -55.99076 | 2025-12-09 04:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b67ad960-1c11-39af-afab-aeecfb06faef | 3.39538 | -51.24657 | 2025-12-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2a9b163-0c3a-39e9-8305-ce3638bf1510 | -2.26515 | -46.06794 | 2025-12-09 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 551d9c3b-fbeb-36e1-b73b-d900fd1d88e3 | -3.39852 | -42.10751 | 2025-12-09 04:25:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 395ee462-0ccb-3927-9baa-3ed587a41f21 | -5.00396 | -42.60207 | 2025-12-09 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 54f6cf12-002c-3233-9c5d-60b5c406fe21 | -1.72589 | -46.18683 | 2025-12-09 04:25:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 786373fc-d424-323e-a140-80372cfd3dcd | -5.08436 | -37.54731 | 2025-12-09 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c5f7c323-4c82-3190-9ef1-6fb86d9ff4a3 | -1.33731 | -45.78022 | 2025-12-09 04:25:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34d72f6f-78b3-3bc9-a85c-29ac2cdf4ec4 | -2.06094 | -46.50171 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17b0717c-5a9e-3e76-ab1e-8da353806184 | -2.10782 | -45.35858 | 2025-12-09 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01f54beb-dcde-3273-aba6-922973f9e4c3 | -3.19911 | -43.16797 | 2025-12-09 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b466d16-9be2-301d-971b-a194d04ccb47 | -4.82151 | -42.98162 | 2025-12-09 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8973079b-2df1-33e7-9b0d-18a0dde25ae9 | -3.43656 | -41.65858 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 0f6441b7-2b89-34cd-81f0-a8c0131df6e8 | -3.44034 | -41.65916 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 51ccf10b-a34f-3016-b165-ef573d3390c7 | -4.40461 | -44.31821 | 2025-12-09 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08566881-8a7d-3902-9793-fec5b49327ad | -4.04856 | -45.64997 | 2025-12-09 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2c6486b-da4e-35e2-b9c4-db806215260c | -3.43965 | -41.66372 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7292aefd-6b75-364c-9d9c-72e66be5bf05 | -1.95757 | -46.4454 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c459265-a7ff-3155-af99-8a59b2c108c5 | -5.87076 | -41.32232 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6f9b7f8f-d510-3701-adb1-b3bc345f2c78 | -3.00657 | -41.75786 | 2025-12-09 04:25:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e4e41493-dffb-3a73-ad52-78c897f8e9a0 | -3.44103 | -41.65459 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 284b236d-5dd5-3ac0-8e07-8b0583c65096 | -2.91504 | -45.91545 | 2025-12-09 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57b15b47-4929-306d-b691-3d5bce5fd6d7 | -2.25722 | -46.4635 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb1cee13-2c4c-3c97-91e4-01ec2eb928e1 | -3.33648 | -42.83918 | 2025-12-09 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d0ce64cb-e2b1-33f4-bcea-950ed62b1e70 | -3.20105 | -44.19696 | 2025-12-09 04:25:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba4c9516-1d74-3541-b23e-0f0d865bea83 | -3.73729 | -44.54847 | 2025-12-09 04:25:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f753152e-74ac-3e93-97b9-9aa6a2c9939f | -2.91227 | -45.9115 | 2025-12-09 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d627c2b-e534-37b8-ab0e-d8111106bf91 | -5.14641 | -43.86793 | 2025-12-09 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28cc058b-9121-3052-80d4-7f6fe8bdc35e | -5.0034 | -41.30305 | 2025-12-09 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d2c9b99f-b710-3b6d-8baa-86ab1eeca9c3 | -1.76865 | -46.19701 | 2025-12-09 04:25:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecfeb8e7-1082-3412-9344-51cefd9b5079 | -5.70947 | -42.07317 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b3501420-4793-3599-9c51-f4131d2b73d7 | -2.22545 | -45.21584 | 2025-12-09 04:25:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0e9353f-8af6-34c0-ae44-2da4db001e38 | -3.00284 | -41.75727 | 2025-12-09 04:25:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 12d27cf3-7c32-3bac-8a53-36d2213346ef | -2.785 | -42.49286 | 2025-12-09 04:25:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdb7443d-8f0c-3c99-b990-92931ca96e2e | -2.26237 | -46.06396 | 2025-12-09 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b54bdb0a-b237-3250-a943-b08e5f4c8ec1 | -6.87112 | -39.13114 | 2025-12-09 04:25:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d854c308-bc14-3fea-8945-e5f2ef3c6461 | -4.40123 | -44.31769 | 2025-12-09 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2997f223-df07-338b-8b0a-29dfcb85bd09 | -5.2226 | -39.25321 | 2025-12-09 04:25:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1ed7d03f-4512-3d77-8812-34c153b1a886 | -6.60255 | -39.53307 | 2025-12-09 04:25:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6105ec2f-1208-3c5e-bcad-1fe7a0fefc9f | -3.44172 | -41.65003 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1d20722b-2c51-3c94-87b8-97044dcaeb60 | -0.30103 | -51.68436 | 2025-12-09 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ff3b2f8-a3f2-3a2e-8c25-20be72b2abec | -2.81473 | -40.41942 | 2025-12-09 04:25:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f0b323ca-efdb-33fb-a07d-a3b46c7337ce | -4.0491 | -45.64653 | 2025-12-09 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68f2e217-3a91-3535-a8d0-d69f2bbcc963 | -5.72575 | -42.04538 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f8cc1ec2-aad1-3ca3-b7d3-5ddf7f65beac | -2.26569 | -46.06448 | 2025-12-09 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9952cd39-881e-3a17-abef-5c1105b75ed5 | -2.79162 | -45.35706 | 2025-12-09 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
