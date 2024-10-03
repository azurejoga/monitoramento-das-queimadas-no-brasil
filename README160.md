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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e505f98-0a33-3f04-9a73-15a58a27cd03 | -13.52543 | -51.14051 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1564aca-e922-3fc9-934b-2d8dc04b629f | -13.52459 | -51.14739 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 76420205-beaf-30e8-bf51-6ba691c83287 | -13.52326 | -51.20282 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f151716c-fa2e-3e1a-9a8b-cd56697c308c | -13.52284 | -51.20622 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dae34b0d-5d00-3c65-8a3b-c067e999cddf | -13.52242 | -51.20963 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02e09a0e-0eac-370f-a31b-775a2c3609fb | -13.52048 | -51.1364 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4437c70-3751-33b2-9528-56a42ad7a4fb | -13.52007 | -51.13984 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f1b8cd5-7437-3f9c-9d64-e9e8214c8509 | -13.51595 | -51.12885 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b17dc57d-1775-3b64-94cf-49bc58c0885f | -13.51512 | -51.13572 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e40c8a68-5fe7-3466-84a8-7e3d4ecf0852 | -13.21052 | -51.18744 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 474d1485-b749-38af-8142-53a4cc1f7827 | -13.21011 | -51.19082 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 24ef513a-2177-331e-b54b-9eaeefdc912b | -13.19779 | -51.20301 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 758f7c27-c69c-3c6b-8531-461d34628633 | -13.19289 | -51.19896 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e7db44c-426b-38c8-b8c6-0113c019f876 | -13.13398 | -51.19486 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 788f4e30-d15b-3e58-82c4-d0e7ab4f818d | -13.12866 | -51.19419 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca804a14-7e6a-3c71-9e5c-96920c432887 | -13.12485 | -51.19375 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2589dc91-964f-3ca1-b60b-0806f7dfe695 | -13.12334 | -51.19352 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e3a1376-3283-37e3-ae01-d62378030be8 | -7.78615 | -50.2269 | 2024-10-03 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29bce22a-612c-3361-8dd8-97ad11012e63 | -7.78579 | -50.22797 | 2024-10-03 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 440b5f6f-84ac-3dae-b734-0bc37018d32c | -7.78569 | -50.23013 | 2024-10-03 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b88cf01-bc2e-370d-8b47-ff562d9bf81f | -7.78537 | -50.2312 | 2024-10-03 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 44bd6ca1-41e2-39e2-aa8f-030075a0dd7d | -9.11425 | -51.52061 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d003d18-aee5-3ad7-90dc-1b4d8eee0c0f | -9.11235 | -51.51828 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e69fcbd3-01b7-3d58-884a-82b3ee6e5fed | -9.11155 | -51.52406 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0485d799-1374-305d-868e-9db269794cf1 | -9.10859 | -51.52563 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| acc0a1ad-a719-3a69-a2ed-c7574f4d4852 | -9.10667 | -51.52317 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ddc26f6-b157-3cd0-bc14-5c6d2c5783b4 | -8.52366 | -50.97504 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 359fd644-8ff1-33ff-9c76-23d83de8476f | -8.52326 | -50.97798 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a29f8f3-45de-3817-9795-3a2b09e57e35 | -8.39957 | -50.75751 | 2024-10-03 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40f4f3d6-53d9-3b4a-9611-5760021ad4b1 | -8.3992 | -50.76026 | 2024-10-03 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70a4367c-c002-391f-b4a2-b2b96fcfced0 | -8.17951 | -50.486 | 2024-10-03 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20eff6fa-7a71-30a6-b6ec-b16885befcd4 | -8.1791 | -50.48918 | 2024-10-03 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45a815d6-afc7-33ae-bcb2-edce50c244ca | -8.17859 | -50.4846 | 2024-10-03 05:16:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e04b9b1-f57a-38d6-9f86-b42977722ace | -8.17815 | -50.48777 | 2024-10-03 05:16:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6cbdae8-f37f-3c55-b16d-64320da2f05d | -8.17771 | -50.49096 | 2024-10-03 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6857b447-736a-3c39-95d2-f254c0085d72 | -8.07641 | -51.1441 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7344c5c0-80ba-3f81-bcb7-fdfae67ddc36 | -8.07068 | -51.1489 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f65ad1b-0761-3c45-b1c3-2dd44b55508a | -8.06988 | -51.15465 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdb34ae4-0f96-3852-a0e7-ab1351cd0051 | -8.06485 | -51.1544 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 246d3eef-8cb9-3286-88df-8fd17c2f2b8c | -8.06412 | -51.15963 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 205eddc8-176f-3773-a21b-1a59461386af | -8.05916 | -51.15892 | 2024-10-03 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ebe86b4-dcd7-3e56-b680-929c866efaef | -10.6304 | -51.11367 | 2024-10-03 05:16:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad51bd4d-8200-3515-b0f0-78e4574b433e | -10.49656 | -51.12004 | 2024-10-03 05:16:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92792845-452a-39dd-83ec-2c6b32879309 | -13.25846 | -51.22683 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1203ccbe-2254-3069-9762-9b62a40f6139 | -13.25765 | -51.23355 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1f47924b-891a-3889-9e98-fbdbcb2a19f6 | -13.25725 | -51.23691 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e71bf219-0caf-3e44-ad5c-eee0962a68e1 | -13.18958 | -51.22586 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7630e575-b65d-3333-a348-db68fe227d53 | -13.18917 | -51.22922 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cbbaf6a-e13b-35d6-88df-b5de0f5f0872 | -13.13357 | -51.19825 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| adfec03b-8c76-3bf7-8c86-457f94150958 | -13.13317 | -51.20162 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92fd8172-e8fa-358f-a2a8-f7f54cb17dbb | -13.12826 | -51.19756 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd641989-21ed-372a-b02b-74cb078035a3 | -13.12443 | -51.19711 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b7ca0cb-b237-3a63-81c3-203dc167eeb7 | -12.89943 | -51.32932 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54bbbe6e-b60e-34fc-928d-76b14a8267e4 | -12.89904 | -51.33259 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c90e82a4-0eff-359c-9b76-919375275bbe | -12.89562 | -51.31868 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 255de8f4-22ed-3891-b65a-2697eb9c0878 | -12.89535 | -51.31883 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 713abaaa-f415-3a87-bfd1-cb93e1356444 | -13.80653 | -52.44175 | 2024-10-03 05:16:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f9b3d84-723c-3b5a-818e-eaa43fc64334 | -9.06873 | -53.26181 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4e0d581-4aa7-37ac-b97e-268bee16be6a | -9.06437 | -53.26124 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a34a877-6c87-35c9-b8ab-034b66bff6dc | -8.96236 | -52.80006 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8541ec79-cda4-3e36-aa5f-6d8f6cb9c13e | -8.96175 | -52.80455 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b966843-14cc-387c-a492-fed998d5749c | -8.95067 | -52.12761 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ee7ae23-60f9-327e-9ae0-c82048471cd2 | -8.93594 | -52.77526 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90a671d9-a21d-32f1-a314-87a41cd9c64c | -8.9353 | -52.7798 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8b6ba7e-89b2-3378-87bb-00e896a4df96 | -8.93088 | -52.77868 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fd22b9d-4b8c-3370-a513-d5942c570ce8 | -10.91125 | -52.41633 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c538087c-a3ca-3c80-9722-9d76a884c546 | -10.91055 | -52.42151 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d757a881-75b5-3b9d-932c-047d4c6477f4 | -10.90986 | -52.42659 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98d3ff5a-8b4c-364b-a122-3dccd6130936 | -10.9079 | -52.40534 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfffe7bf-e703-3fdd-8ca5-327748fefd34 | -10.9072 | -52.41054 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f2b63e8-3e4d-39ad-acd5-5ead504ebf15 | -10.90581 | -52.42086 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46dcf3cc-6961-36f4-9d15-6c32b368cc6a | -10.90513 | -52.42591 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6beec7a9-1ada-3e23-beb2-4ea55537a168 | -10.90445 | -52.43094 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cec8822d-8a23-34f3-b686-1c961adafe08 | -9.61105 | -53.20435 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1054a047-2a92-3625-a94b-591794542c1f | -9.61044 | -53.20869 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83d50b5b-a8f6-372a-a828-d0b8517ccbf7 | -10.02156 | -53.4124 | 2024-10-03 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 51888ed2-caf5-34a6-9ac9-349a12bbc6a7 | -10.02095 | -53.41671 | 2024-10-03 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ad6e678-6def-3d2d-9012-2286862f9abb | -10.66089 | -53.69386 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00c6dd07-874f-33d3-8ac4-8a3170d80661 | -10.65711 | -53.68914 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b32a1b4c-419b-3553-929b-53724d9cba68 | -10.65655 | -53.69331 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69e54aeb-35e2-3aff-9c0c-fe4478aea3c5 | -10.65591 | -53.68631 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7821635e-68d2-3bd4-bb44-5ec3b84d5b3d | -10.65333 | -53.68441 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82066764-11b4-3ad8-b6d8-ba5baca77d76 | -10.65277 | -53.68859 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 654a3c8c-2059-3678-bd00-b1fcdedab4d2 | -10.65222 | -53.69275 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 026b613b-323d-3310-9d76-03f1437c3fbb | -10.65216 | -53.68159 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e134aa3-235c-3054-8c73-0c486da451b4 | -10.65157 | -53.68578 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 288bebbb-f2c4-3cad-a2d0-4894831664be | -10.65099 | -53.68993 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3346c552-656f-3c33-883f-9ccbca9bcb98 | -10.6504 | -53.69407 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6eccca1-1fc9-30dc-899c-08f663c2f645 | -10.64955 | -53.6797 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9f9ca20-f170-357f-b04f-4a15ea780a77 | -10.64899 | -53.68388 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f7770cc-5156-3bc7-9b26-07f85184e579 | -10.64788 | -53.69219 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9df7a20c-8658-39a6-8c59-b6705c301f03 | -10.64782 | -53.68108 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72309f1b-c54f-387e-ab22-40adfcb1f707 | -10.64723 | -53.68524 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f01f576-a606-32a2-90dc-b5050dea460b | -10.64665 | -53.68939 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a725d760-9aa0-3e9b-b485-401728c01fa4 | -10.64607 | -53.69351 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a910028-2d45-3d39-98f7-4a204a5b0fd3 | -10.64465 | -53.68333 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f6b1797-a088-381b-919d-543cfd0ea36f | -10.6441 | -53.68749 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af0a9a78-14ca-31a9-998f-04c1de5b9e64 | -10.64355 | -53.69161 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d0190e3-7565-3c0c-bb00-6180dfb0e086 | -10.64348 | -53.68053 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b553ba00-4545-3d84-a0b5-eeefa17b7413 | -10.64289 | -53.68468 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README161.md)
