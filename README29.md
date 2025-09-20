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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ce24858-6b98-38b0-8ae0-52407316c09d | -23.96101 | -49.76703 | 2025-09-20 05:21:00 | NOAA-20 | WENCESLAU BRAZ | PARANÁ | Brasil | 4128500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| f94abd1a-bac6-3ebe-9224-ba79efa483de | -19.61694 | -57.74377 | 2025-09-20 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 79dc4f36-efdb-3a29-bf4e-45a23634ac94 | -20.6 | -56.73088 | 2025-09-20 05:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db36898e-b145-3d5d-8202-40d6e4ca78d2 | -19.54326 | -48.04842 | 2025-09-20 05:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 54d94165-1438-3ad7-a09d-ce237efa7b94 | -20.32407 | -49.204 | 2025-09-20 05:21:00 | NOAA-20 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce046979-a192-3bc0-869c-4f0c9bbbd655 | -20.35518 | -48.78673 | 2025-09-20 05:21:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8567958-566f-3a10-b183-866a2639bdbb | -20.60049 | -56.72703 | 2025-09-20 05:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b61674e6-1a63-3154-a84f-b7176473d1bb | -2.69322 | -59.42112 | 2025-09-20 06:05:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fb19020-adb0-3144-a695-1051fa99c58d | -2.69147 | -59.4217 | 2025-09-20 06:05:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ae6ea38-7340-3b0e-84b5-a434a7b7f596 | -2.69696 | -59.42772 | 2025-09-20 06:05:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 094ba5a3-828a-39ca-aa83-14ee3b245bda | -2.69248 | -59.42601 | 2025-09-20 06:05:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70be4fc1-8262-3fd1-b1bc-5cc6672ce365 | -2.69767 | -59.4228 | 2025-09-20 06:05:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cedbff16-56b3-340c-b9a3-3fe1af876f6b | -9.43451 | -67.89082 | 2025-09-20 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e75900f7-cf4d-38b2-b669-d875cddd6586 | -10.09148 | -68.83002 | 2025-09-20 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1429c619-14ee-3aa0-9673-4980aabf36f9 | -9.41428 | -63.69087 | 2025-09-20 06:08:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75892db3-3de8-3bf2-95d5-dbf4e44c81a0 | -9.60375 | -64.03833 | 2025-09-20 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64de2db8-b69b-3e6d-9599-d089e1443a1b | -8.80426 | -69.04136 | 2025-09-20 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbe4355a-d9ea-3c1d-9254-2be8c6b0d25a | -9.42 | -68.87302 | 2025-09-20 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75faf049-3df3-3a15-bac9-6914c3292fd1 | -7.97978 | -71.33965 | 2025-09-20 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d755d8d9-42d7-34f7-a5b5-e1dfa482bb8f | -9.41385 | -63.69416 | 2025-09-20 06:08:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0df969b0-53a4-314c-b099-adaf2f9652ed | -8.85173 | -69.1797 | 2025-09-20 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 926d2f0f-081a-332e-8dab-0e195f8c4bbe | -9.41343 | -63.69738 | 2025-09-20 06:08:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acb3b958-79e0-374e-b3c9-b2db93157e98 | -9.55397 | -68.57842 | 2025-09-20 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff007113-c8ce-384b-bcb2-b19178f56037 | -9.55855 | -67.47292 | 2025-09-20 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0146a94e-8bd2-34ce-adac-a6e715dde05d | -9.18767 | -62.61684 | 2025-09-20 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ea1029a-c3ff-38ee-bf0a-f5b9b158ee93 | -8.66336 | -63.85223 | 2025-09-20 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0c3aa95-3eef-38ed-a74d-a5a712a15f81 | -7.1937 | -72.68944 | 2025-09-20 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2526206a-1160-315e-a910-84aeb74102a0 | -9.98599 | -67.56683 | 2025-09-20 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d42c239c-d3ef-3326-aa83-02718739f125 | -9.531 | -63.57707 | 2025-09-20 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de7b3ece-e56d-383a-9920-d3c39cdc64d7 | -9.41945 | -63.69164 | 2025-09-20 06:08:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8202e748-10bb-3921-8229-9fd8abc2bc32 | -9.47135 | -67.88863 | 2025-09-20 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e98d22b-2540-3ab4-b1f6-09d7cef7ed35 | -9.94986 | -66.75014 | 2025-09-20 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11e8fd50-4c58-34e1-a5d2-886b1a4a0fd1 | -9.18787 | -62.61725 | 2025-09-20 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c1b8311-b349-34b1-8764-4450c4269781 | -22.487 | -47.538 | 2025-09-20 06:10:00 | GOES-19 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.3 |
| 6a337292-689b-3229-9edd-2e666671ba19 | -10.66475 | -69.10378 | 2025-09-20 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 194affe5-9d46-351a-bc1a-1d7512fd2d5c | -14.8454 | -60.25847 | 2025-09-20 06:10:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a4bc75a-4859-36a9-a7ac-6a20bf95cefb | -14.8386 | -60.25682 | 2025-09-20 06:10:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 892a8b30-d21a-390c-81b9-fd7d9285575d | -10.6658 | -69.10192 | 2025-09-20 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abf0dd88-55c7-3f0b-a914-eaa66c849f0a | -22.8109 | -45.2767 | 2025-09-20 06:20:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.0 |
| 36fc786a-1d10-3449-8ce1-056342095383 | -22.5079 | -47.5325 | 2025-09-20 06:20:00 | GOES-19 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.5 |
| 2bc29f23-2a6f-389f-8ba8-2d9e56421d4d | -22.487 | -47.538 | 2025-09-20 06:20:00 | GOES-19 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.7 |
| b7720ce7-116d-36cd-bcc2-100ee6bb9306 | -2.78564 | -47.14599 | 2025-09-20 06:20:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| b3f713cd-b7bb-36b1-8417-e275663bd5f7 | -2.43238 | -49.33521 | 2025-09-20 06:20:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 369c583a-dc38-3070-af71-b265c2cc43f2 | -10.32878 | -45.21606 | 2025-09-20 06:22:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| fdbc95fe-83ef-3540-8aad-00ddc11149d0 | -3.4576 | -51.20818 | 2025-09-20 06:22:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| a37d51bd-d529-3567-be76-6d68b57c0ec8 | -5.75923 | -53.41602 | 2025-09-20 06:22:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2376d9d8-c48a-3c06-a510-0ee256ef9ba7 | -10.3253 | -45.22342 | 2025-09-20 06:22:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 712ae0fb-8183-3926-8fe2-2f744b434587 | -9.35491 | -54.52135 | 2025-09-20 06:22:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6f305e2d-6c4f-37d0-9174-bc6f7e5fce8e | -3.98005 | -51.05251 | 2025-09-20 06:22:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a58fdd79-b6eb-3dd7-83e4-ec24fe5ae14a | -3.51365 | -49.44273 | 2025-09-20 06:22:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 15a97060-6cda-3bf5-a9af-b2a63ec11ae4 | -9.40372 | -54.68353 | 2025-09-20 06:22:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 521c928f-be62-37e0-8a3f-34a3db7a1f83 | -3.51351 | -52.74874 | 2025-09-20 06:22:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c1e271c2-02fe-3433-8b83-ed77b2acc5ac | -9.39482 | -54.68219 | 2025-09-20 06:22:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fb27f8c1-1619-34de-aca2-528c5a11f056 | -10.34049 | -45.22581 | 2025-09-20 06:22:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 3b3220a7-4112-30e9-8373-051346a9d46d | -3.45624 | -51.21727 | 2025-09-20 06:22:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f7b9299d-7304-3465-ba1d-28243405da14 | -7.38081 | -47.03905 | 2025-09-20 06:22:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 9c74d205-e9de-3c7b-9457-467e9a76e981 | -12.85317 | -52.99174 | 2025-09-20 06:25:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 88e62d41-a41b-3ced-806f-599dffafd66d | -19.60851 | -57.73891 | 2025-09-20 06:25:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 6cea5caa-2b5f-3cfc-9270-4760a54965b3 | -15.30574 | -56.81359 | 2025-09-20 06:25:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| acd08081-04a0-3321-aeaa-a63acac54caf | -15.91098 | -59.45205 | 2025-09-20 06:25:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 196eacab-d897-3426-8188-d475178899e8 | -15.27199 | -56.84879 | 2025-09-20 06:25:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8031aa4b-c877-3ee4-bc8e-ae8e7e99127e | -10.8763 | -53.74286 | 2025-09-20 06:25:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7161fa5e-45cc-3d63-a791-3b2acffa7e46 | -12.85182 | -53.00118 | 2025-09-20 06:25:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| c88a8e2c-7f0d-38db-8f55-cc672c9c3fe5 | -15.31488 | -56.81519 | 2025-09-20 06:25:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1bd03595-d648-3d79-80d0-dbd4c071ed0b | -19.61475 | -57.74661 | 2025-09-20 06:25:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2a01a54f-3aed-35c8-bcaf-4ea7c7924ce1 | -16.11127 | -53.8082 | 2025-09-20 06:25:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c5ffbfd0-5fc1-3082-800c-5e209bcb264c | -22.49158 | -47.54091 | 2025-09-20 06:27:00 | AQUA_M-M | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 171.3 |
| c775b9d0-bcbe-3555-8a73-50201592c103 | -22.19344 | -49.65242 | 2025-09-20 06:27:00 | AQUA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.6 |
| e07010c9-f935-3480-a3e0-9a14042af1c6 | -22.99546 | -50.40517 | 2025-09-20 06:27:00 | AQUA_M-M | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 61f8b0e8-d3b9-34ad-9556-88f84316645c | -22.47814 | -47.53505 | 2025-09-20 06:27:00 | AQUA_M-M | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.0 |
| bb9b5e70-8559-3c99-966e-73a6fb195ac7 | -22.4934 | -47.53638 | 2025-09-20 06:27:00 | AQUA_M-M | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.4 |
| 3ddd6eab-231b-39d2-b5c5-7ee39c81327e | -7.19204 | -72.69128 | 2025-09-20 06:35:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 133e4d27-37a9-3302-99dd-0591d629ce5d | -12.8587 | -53.002 | 2025-09-20 06:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d66e49af-4fad-3f53-80b7-ea7540e6b6a9 | -18.3222 | -55.0452 | 2025-09-20 07:10:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f6d5c917-d8f3-30cc-b87c-e96178ef71b6 | -9.184 | -44.6251 | 2025-09-20 10:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 155.7 |
| aabf856e-8d07-3cdb-9933-29ab72381370 | -9.1079 | -44.657 | 2025-09-20 10:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 23850a08-8b65-35fd-afd8-83e3ab2b63ff | -9.1268 | -44.6548 | 2025-09-20 10:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| c89b995e-199d-3192-a39e-272133c4c452 | -7.7336 | -44.3902 | 2025-09-20 11:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 168.0 |
| e4cf07c1-745f-368a-b66f-7db312497e0a | -7.7336 | -44.3902 | 2025-09-20 11:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 8104e9d0-336f-3225-84f3-1490a73be225 | -6.07562 | -41.02468 | 2025-09-20 11:17:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 934.7 |
| 10fa6b32-d2da-3c95-9e46-fdcad9e38c3e | -6.08883 | -40.98703 | 2025-09-20 11:17:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 348.9 |
| 38d52cfa-2daa-30cc-8239-57e7c83414c0 | -6.08365 | -41.02028 | 2025-09-20 11:17:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1122.3 |
| 87db426c-b447-3497-9d14-83ac32778f85 | -6.08106 | -40.99144 | 2025-09-20 11:17:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 595.8 |
| 0fff8741-0e22-3089-8282-5349e5d3be9f | -6.0676 | -41.01741 | 2025-09-20 11:17:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| eedc22b7-aeaf-383a-a7a8-ad096a419cd6 | -11.10274 | -41.29399 | 2025-09-20 11:19:00 | TERRA_M-M | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 43.6 |
| e00bd8f0-7ba9-35cc-a187-08c834be2a11 | -7.83346 | -37.39659 | 2025-09-20 11:19:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 26.0 |
| fec3daa3-d6ff-36b9-ab33-b56671ea9817 | -7.7336 | -44.3902 | 2025-09-20 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 219.9 |
| 2dc11ce9-d7d3-3aaf-9bba-7bfda14bb016 | -7.7336 | -44.3902 | 2025-09-20 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 195.9 |
| e3f4e66b-0ff1-39ce-b713-73de1e701f87 | -6.0069 | -44.3354 | 2025-09-20 11:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 3f65f36b-512b-31f2-a5a9-64dc1c2723bd | -7.7145 | -44.4151 | 2025-09-20 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 0759abdf-6921-3fa4-97d5-7e962e19e0ed | -7.7336 | -44.3902 | 2025-09-20 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 912f477f-ec79-3579-9b14-5f1bd7b5b654 | -7.7145 | -44.4151 | 2025-09-20 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 5a803aa0-6910-3cc4-984c-c0f8a19217ad | -6.0071 | -44.3124 | 2025-09-20 11:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e819682b-1af8-396b-99f2-2226e1f65a0e | -6.0069 | -44.3354 | 2025-09-20 11:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 53faf400-1346-3b66-b2ff-5fa4de2a5e90 | -7.7145 | -44.4151 | 2025-09-20 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 884b8f0b-9dfc-36f0-92de-4e703a740e46 | -7.7336 | -44.3902 | 2025-09-20 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 5bd434eb-7bf6-358e-82e3-f7b6e6ee4000 | -6.0069 | -44.3354 | 2025-09-20 11:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 136.4 |
| cb24c306-302e-3ff2-9f86-6a155ef6cb19 | -7.7336 | -44.3902 | 2025-09-20 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 184.0 |
| acd3b141-7c07-3bae-89bf-7dcddf3df942 | -7.7145 | -44.4151 | 2025-09-20 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 97c58df2-716e-3935-984c-cb88a4b429e1 | -7.3554 | -44.5645 | 2025-09-20 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |


[Clique aqui para ver as próximas entradas](README30.md)
