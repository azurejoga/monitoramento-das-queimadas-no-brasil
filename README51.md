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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51092314-5bca-3eb0-ac93-a30f0828ae1c | -3.46482 | -54.6388 | 2025-11-18 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21225c22-7ac3-3003-bd2f-7c93e9480eba | -3.5244 | -50.34408 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 161d4eed-5435-3fbb-8bc4-1e86abc1cdf9 | -9.39809 | -48.44368 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af8c9946-4ac0-3688-bc61-c701e8b81584 | -8.46995 | -47.98681 | 2025-11-18 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c0f485d-3b0a-3067-b0cd-a7b704aaff7a | -3.02817 | -47.84322 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64118423-97b3-3fcb-89fb-f30c7272fd24 | -4.17708 | -44.23573 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e89d6d33-5fee-318d-970f-78f6fe2f2f2b | -3.30131 | -50.07195 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adb645fa-8ffb-34ec-8fc3-e8294c26e150 | -4.64804 | -47.95083 | 2025-11-18 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9efe0901-a859-3c15-bbc7-2af3d920e847 | -3.17369 | -48.61361 | 2025-11-18 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17e0d9cd-3c0c-3ff2-a90e-1af6c7e85d68 | -4.65053 | -46.54658 | 2025-11-18 05:10:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7941cfa8-12de-3833-afad-ee055e9a12fb | -3.23339 | -50.50861 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05e5f2d3-9f68-3749-9af7-73ba70ab4338 | -2.45308 | -48.90599 | 2025-11-18 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79994b27-c34f-30d4-a8d9-d192f156ed30 | -2.8289 | -45.41713 | 2025-11-18 05:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 754fb6b2-f425-3d27-aa83-391af7edb8c7 | -4.18119 | -44.23268 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 195cc1fd-46c0-3cef-83f4-9e0379a1fabc | -2.89202 | -53.28534 | 2025-11-18 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5510bed6-5b3f-3b68-8aa5-a541a76edd9b | -1.87049 | -50.96173 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02f051f0-63fd-3ff1-9465-2139abda9ce4 | -7.43207 | -48.93972 | 2025-11-18 05:10:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 714bde6e-2a9f-3523-8f4d-f3ad5fccab04 | -2.716 | -59.43018 | 2025-11-18 05:10:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edf20bd0-01b3-3e72-aa41-bb75f76c3771 | -3.46384 | -54.64231 | 2025-11-18 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af84146f-b192-39b8-8c50-4824ae26cc8d | -8.12198 | -55.30395 | 2025-11-18 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 045436ad-c054-3aab-9c8b-be8a0ad496c3 | -3.18006 | -50.65275 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cacbba8b-cacb-3a9a-8359-49bb14a30fbe | -5.12961 | -55.94718 | 2025-11-18 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e51e4701-2135-385c-b9b3-844544a68a50 | -1.36762 | -55.46012 | 2025-11-18 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 554165de-1a05-3355-bdb5-21ddac954e1b | -3.04455 | -51.14612 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58aa1264-1bad-303a-9917-187b37740365 | -3.98871 | -50.51684 | 2025-11-18 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdef32aa-a812-3cd3-a953-0e61f82c17b5 | -3.07314 | -50.23323 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ed6116a7-34b7-3f20-8f99-c7284511e8d8 | -3.38292 | -51.02328 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f960a9f-3251-30d9-a89d-decdbe6671d8 | -3.32707 | -51.5091 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e12610c2-d70e-3a24-9a37-f320eea8a0f0 | -2.47805 | -50.2422 | 2025-11-18 05:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2d66db31-db13-3f3c-9100-6cd5dc49cbed | -8.47092 | -47.97947 | 2025-11-18 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4c68b81-54d0-3e97-8389-dd5436c117e9 | -3.25415 | -43.04022 | 2025-11-18 05:10:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9ec91ccc-e494-3888-8a7e-a4d592c33263 | -2.51719 | -47.81149 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5e259540-079d-3fec-b02b-55d865f2a52b | -4.13405 | -52.11362 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e947fda5-98e0-34db-86f3-3adbb92ac9e3 | -2.5313 | -58.02811 | 2025-11-18 05:10:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db0c2492-f7dc-3540-aed7-1e4050ba22e7 | -5.09568 | -56.16531 | 2025-11-18 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc24f986-9f0c-327e-bd7c-02af1fca7ba6 | -1.46278 | -55.52505 | 2025-11-18 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db7d280d-3071-3e30-9564-f2bed248a332 | -6.31852 | -55.16201 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30183f39-c19a-3216-8f28-9b3d5663a08f | -3.1748 | -46.60374 | 2025-11-18 05:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2739d3b-c3a9-305a-88bd-063d98006099 | -2.33326 | -55.909 | 2025-11-18 05:10:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51eb84b9-589f-3382-90ab-fb6481810694 | -3.24032 | -50.50001 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6cf3a1a-d3b7-3a77-9d54-d590466b8c8c | -7.35368 | -46.21123 | 2025-11-18 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2e7224a-9497-3f78-9d95-e01854d2a874 | -3.17792 | -48.03103 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 477c7d08-3aa8-3f0c-9e2e-bedfd58b493f | -7.35989 | -46.21192 | 2025-11-18 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b47651ff-e120-30a2-a68d-3260965b591b | -7.43744 | -45.19377 | 2025-11-18 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8edd954-2346-36ff-870c-c6277b84ba54 | -3.01034 | -51.34593 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bf8b14d-93c8-3583-b6ce-dfd16d9cd9de | -3.07774 | -50.35305 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fedd6b32-f6ae-351e-a512-0b43a15f2735 | -6.1494 | -57.84568 | 2025-11-18 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05da2097-8883-34ba-b046-9be9574366cd | -3.16053 | -50.16622 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b823bdc7-97f6-3151-baff-59f962064374 | -3.47585 | -46.07068 | 2025-11-18 05:10:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54e4b2f2-942c-35a5-8c29-4396cdecd457 | -3.76967 | -52.39723 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2878c9ef-b0aa-3e1b-bff8-79b637940155 | -3.93908 | -52.1833 | 2025-11-18 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d508faf-d8cb-3f9a-8b1a-f2f79443aba5 | -3.08156 | -48.13392 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7701447-c2f7-3f1c-9c7a-99f8d22a6f89 | -8.2141 | -48.3054 | 2025-11-18 05:10:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44e2e5bf-c4d8-35c5-ac9e-15513b7ea93a | -3.67468 | -50.80878 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e8b548e-0079-3186-a50c-2e574275f05e | -3.22968 | -50.50378 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 234a054a-c342-359c-80a5-51682bd44017 | -3.50349 | -51.60852 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0146a8be-3c79-330c-a3f4-88ed43fc7fc8 | -2.5285 | -58.02398 | 2025-11-18 05:10:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5848ff45-4879-33f6-bc2e-4b4dedf8c26d | -3.34542 | -53.76288 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00a5b7b7-d794-330c-aa06-b40993decde0 | -3.49279 | -50.34371 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68db0236-9fb8-3454-ae09-fa523c6f1df3 | -3.13717 | -49.89622 | 2025-11-18 05:10:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82d8b130-15e4-34c8-a63a-ce5be14d70f9 | -8.33327 | -45.36505 | 2025-11-18 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6a41cd2-dcee-3b0e-aee1-257b8a19753c | -2.68709 | -49.16631 | 2025-11-18 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d03e6095-e0c3-36c4-9a05-c8576ca8a25c | -8.33981 | -45.36636 | 2025-11-18 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34071785-7742-376f-a697-662edc23f128 | -3.29837 | -53.85493 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92476767-8ca0-372e-85c6-bbf38c2deaf7 | -3.02343 | -47.83921 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1a46957-fdce-3502-aadc-43386c9081bd | -3.51582 | -50.28035 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7196838-57e4-3989-b288-e99303e6b83d | -8.38041 | -44.07043 | 2025-11-18 05:10:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5114120-e88b-3e38-80d7-b7e29b315df6 | -4.18376 | -44.23681 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| df6b86b5-5d5e-3ad7-bdc4-69d0f7f0be47 | -3.47414 | -46.06965 | 2025-11-18 05:10:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6b70c4e-3c7b-3f5e-b602-a567c5768a05 | -5.47503 | -44.69351 | 2025-11-18 05:10:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbbd2f7b-3803-3ea8-8097-f49deab04ce9 | -6.44241 | -43.82182 | 2025-11-18 05:10:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fb07556a-1dc4-384d-bb87-e1db6a429eba | -7.8662 | -46.87086 | 2025-11-18 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2f7fa81-4564-3411-af22-cb399fac905d | -3.33138 | -50.2827 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bb3cf62-3d23-3ffb-a6b7-7235f6a118e6 | -3.26127 | -50.09334 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39a14c43-5328-3019-bcfb-d118320a3138 | -8.21956 | -48.30616 | 2025-11-18 05:10:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a4cfd3a-1ec8-3f6b-9970-233162283784 | -4.18785 | -44.23385 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1c714a3c-391a-3ef2-8e56-f3093912fba4 | -8.5718 | -46.4889 | 2025-11-18 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25b1a394-6c82-39e2-98eb-23a1756264f7 | -5.2135 | -50.17763 | 2025-11-18 05:10:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfc0ade7-b337-3d3e-9d8d-e604d23ad5ac | -4.27052 | -44.2516 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54589b3a-ab75-3acb-bad4-5d10a32f1426 | -2.82826 | -45.41949 | 2025-11-18 05:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43421c7d-883a-3950-ad6a-5e5b3762aa1f | -2.40203 | -55.96955 | 2025-11-18 05:10:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8ed7267-86d4-3b51-ac4e-7dcd34aa39f6 | -2.53188 | -58.02451 | 2025-11-18 05:10:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 181c8b5f-8051-3d77-be04-5a2e009b704a | -4.22883 | -46.34616 | 2025-11-18 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4362177-dd5a-3a90-bc0a-4d8e39a67ca7 | -2.91422 | -47.85075 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c101dbf5-6eb7-3241-9877-1f685e0ac34c | -3.18437 | -50.65338 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1ab76c2-7464-363f-8f66-d20dec3bf619 | -4.19372 | -44.24062 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58cbf87f-35ed-3421-9540-d37d2335f897 | -3.83299 | -52.29671 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a93b845b-1f97-33f1-9bf8-224c0c1b6571 | -2.49476 | -49.3383 | 2025-11-18 05:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a2c8708-0c4e-3bde-b574-65b4ac88009e | -2.96152 | -51.03701 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f334892-797c-3f99-a378-9399820007ca | -2.89136 | -53.28955 | 2025-11-18 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32d88b09-2d3b-39bd-a5f7-4f01f32c21b6 | -9.39212 | -48.44645 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 71c0dd0d-64fd-3bed-ab02-33a72ed4ea4d | -4.1325 | -52.12376 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8169401-8775-319a-9d72-65b9e89c06cf | -3.34185 | -53.76232 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 626daa01-72e4-3759-a8d4-3b63368c3c05 | -8.54185 | -46.04816 | 2025-11-18 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af8768b4-801f-3800-8919-d2a0224fc7d4 | -1.38515 | -55.43471 | 2025-11-18 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45935ce8-dcd7-38bc-9600-036e65cdff52 | -4.71535 | -50.95284 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f94a12f9-166a-32e8-9ebe-3214bb6acd1a | -1.41126 | -55.74368 | 2025-11-18 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0831010-1cf5-3018-b166-90801a2b320e | -3.29993 | -50.08083 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a931605-af57-3022-b74e-c92ddbe4263b | -7.07937 | -52.61825 | 2025-11-18 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 266b34ef-ebc2-3871-83ae-a293be40bef1 | -4.64369 | -47.9435 | 2025-11-18 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |


[Clique aqui para ver as próximas entradas](README52.md)
