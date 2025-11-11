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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a575f0c-f353-383f-a02b-d451bd333b87 | -5.33043 | -35.55782 | 2025-11-11 03:59:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7c40f31f-20c0-3b33-bb28-ed9b2074e732 | -3.85311 | -41.58205 | 2025-11-11 03:59:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e41d30dc-2919-3416-8f3a-a0bb086c1ba4 | -6.54964 | -44.46939 | 2025-11-11 03:59:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03f254d9-bdd8-35ba-b8fe-6fab0633c5c4 | -5.12621 | -45.59968 | 2025-11-11 03:59:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32f62264-41b1-34d6-9c0b-af5fe186ed92 | -3.85434 | -41.57444 | 2025-11-11 03:59:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 43e80e1c-638f-3e21-9e7d-d4f2686cdc1b | -6.37255 | -41.07469 | 2025-11-11 03:59:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bdaca8fd-112d-304a-b84c-2a9b81451072 | -5.30062 | -41.41719 | 2025-11-11 03:59:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3d8b3e76-fe54-3aa7-a02e-0f5646d256df | -4.86803 | -46.69247 | 2025-11-11 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6af1cbb7-85dc-3e04-ba58-2a78ec08437b | -6.08711 | -41.56417 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c734ea69-77d4-3ced-91b0-a2cf86295ca9 | -5.37896 | -44.72253 | 2025-11-11 03:59:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82da4b52-0049-3bfa-9206-705fdf870d96 | -5.70557 | -40.63231 | 2025-11-11 03:59:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b42a3fd0-90c6-3778-bea7-12d5b5707cca | -4.20514 | -50.63789 | 2025-11-11 03:59:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f5dc7fe-1a99-32fc-86fd-fd927308b173 | -4.27315 | -50.54171 | 2025-11-11 03:59:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aad776f-b394-3494-af50-74fbc98d97ca | -5.60824 | -47.28195 | 2025-11-11 03:59:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f1352d6-1f0b-32e9-a078-8eac7dd95426 | -3.42737 | -42.42382 | 2025-11-11 03:59:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3c1f65f2-2b60-3798-9c70-e9541bfbf3d1 | -0.909 | -47.5541 | 2025-11-11 03:59:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 483129d4-c6a4-3d2b-be9c-2421a3a08a8e | -4.73764 | -49.52931 | 2025-11-11 03:59:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9f2cac1-e17a-395d-b65c-1d1e88dfe526 | -4.99864 | -46.87293 | 2025-11-11 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 188c69ae-4f73-372e-92fb-b33daff2c606 | -7.06623 | -39.67751 | 2025-11-11 03:59:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2024dddd-564c-3de3-992f-d531656e585f | -7.03769 | -39.75113 | 2025-11-11 03:59:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 97764d2c-d75b-32be-9c4b-1d03db9fcf7a | -4.27198 | -50.54028 | 2025-11-11 03:59:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62c2ccee-bcfa-3776-a733-88b4beaf26f5 | -3.90968 | -42.8726 | 2025-11-11 03:59:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b1c51999-eb4f-3f71-b59a-ac3f0f03812a | -7.67743 | -38.64788 | 2025-11-11 03:59:00 | NOAA-20 | SANTA INÊS | PARAÍBA | Brasil | 2513356 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dbb647c1-f776-30fa-9226-17e6dabfa389 | -6.09227 | -41.55369 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4156b5cc-715e-32da-acab-5a26179e1042 | -6.06862 | -45.80804 | 2025-11-11 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6b93933-8827-3fd0-93e8-52958b117d76 | -4.14007 | -50.65065 | 2025-11-11 03:59:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c0f549d-d86f-35ac-8667-0e90c4d8f6e5 | -4.02488 | -42.06499 | 2025-11-11 03:59:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 57019611-6e82-3b28-aa4a-fdaadb0bb743 | -5.61474 | -41.0739 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7ec8c09b-c81c-3aa0-9f3f-13388fef66d1 | -4.86419 | -46.68707 | 2025-11-11 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 438199fc-c81d-3e6b-93d5-32407aef92a4 | -5.77802 | -44.02607 | 2025-11-11 03:59:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 05388e8c-bdec-3606-bb3a-71b6d89a1527 | -6.36388 | -44.71883 | 2025-11-11 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a30bb1c6-33bb-36a7-bd7d-6a94a9cb07aa | -6.09331 | -41.56897 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f06df52b-97ce-3dbd-8fde-fa9e6bd56c38 | -5.40008 | -46.00492 | 2025-11-11 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91393b30-c2d4-3381-ae03-17dbcff12a3b | -5.42253 | -44.83942 | 2025-11-11 03:59:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9144d268-cce8-37a1-a5fd-24872ad776bf | -4.67993 | -43.24807 | 2025-11-11 03:59:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d6df8b2-313e-369b-8af5-2c9be0e34eb3 | -6.26425 | -43.68829 | 2025-11-11 03:59:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e696bc47-9b3a-3ed3-ace5-d159560862a3 | -5.12386 | -45.59686 | 2025-11-11 03:59:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cd4f72b-1a68-35ce-988c-edb16b861b63 | -7.69335 | -35.0958 | 2025-11-11 03:59:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 10d9c788-199b-3970-985c-d7a511cc7902 | -6.36235 | -44.7201 | 2025-11-11 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8bdfab4-0082-309a-b6f3-b8de473666ce | -6.71711 | -39.99751 | 2025-11-11 03:59:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0b2c8052-fd8d-3ec5-8a65-f3cef14af9d2 | -4.9133 | -44.32392 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f332b5cf-e788-3811-9635-62baf2230972 | -7.10518 | -39.77595 | 2025-11-11 03:59:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a1f74844-4c94-3321-8f94-2be1d606290d | -5.61139 | -41.07337 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fcdda65c-9314-3e5d-97b5-5a4245961565 | -7.18822 | -38.7904 | 2025-11-11 03:59:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 48bcce88-e9be-3a56-8dc0-0d00a721267e | -6.07082 | -45.81126 | 2025-11-11 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff564594-ce91-3d79-abfc-c5cb9d8516ff | -7.6893 | -35.0952 | 2025-11-11 03:59:00 | NOAA-20 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 018bf0a1-c5a0-33a4-b98b-f06af7f67d4a | -6.68693 | -40.82808 | 2025-11-11 03:59:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 34a70d6e-d4fd-32da-9038-a2671385dc8a | -5.88834 | -43.96859 | 2025-11-11 03:59:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 264fea05-e0fe-32a1-8484-08e7c82dd706 | -1.48057 | -45.62346 | 2025-11-11 03:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8e15af5-ff9f-3fad-95b4-5e1c2533682f | -1.6432 | -52.05685 | 2025-11-11 03:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 35dce645-5475-3982-a3ef-5a11d9a7bb8f | -3.47534 | -42.87207 | 2025-11-11 03:59:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a7b8c93-1392-398c-9a95-ccd1591d0003 | -5.90983 | -46.24725 | 2025-11-11 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1cdcccae-3122-3480-b823-9b5bc1f21233 | -5.46061 | -41.29361 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38416442-acba-35ee-8b71-0684a280f761 | -4.45118 | -38.39316 | 2025-11-11 03:59:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 64944857-0c63-36bc-bf6a-7a5fbf6e1d25 | -5.79011 | -43.74058 | 2025-11-11 03:59:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f58d70f-e002-3945-a3f3-1715244f96d7 | -3.73231 | -47.65353 | 2025-11-11 03:59:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45ebd35c-cb45-3155-aa5c-e2d449445520 | -5.63768 | -41.08116 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2bf24f2d-0927-34fd-857b-b063f8d14824 | -2.43926 | -46.31304 | 2025-11-11 03:59:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3237ff25-5254-347d-a6fb-8a71f28a8271 | -7.13199 | -41.25757 | 2025-11-11 03:59:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fb584478-8d3a-3473-9edf-aa05a169b1f8 | -4.74 | -44.59973 | 2025-11-11 03:59:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa181d74-880d-3305-95b0-dd891d14b046 | -4.27352 | -50.53127 | 2025-11-11 03:59:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52926515-2d5a-34fb-9aea-9f496061d1ea | -5.42217 | -44.643 | 2025-11-11 03:59:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e803d4e5-4df3-37aa-852b-332e56c12462 | -4.45786 | -38.39419 | 2025-11-11 03:59:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bbaab780-a893-341e-8d06-af83c15020f6 | -5.60411 | -41.07586 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 470d14dd-3625-3103-a409-80dcdfea36c6 | -4.74057 | -44.59623 | 2025-11-11 03:59:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce61f7ba-9e1d-3bcb-9929-7375c9510291 | -3.91335 | -42.8732 | 2025-11-11 03:59:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 901dfb82-8f6d-3fde-9c7f-a54c4617d77a | -5.6416 | -41.07812 | 2025-11-11 03:59:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7867f984-6855-36dd-a296-2f0955e66fc3 | -5.75269 | -40.80557 | 2025-11-11 03:59:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d7b38df-55de-39ff-8201-b46cdc20b84c | -8.23848 | -34.94172 | 2025-11-11 03:59:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a1628b2f-6e01-34f5-b8f5-942395c319a2 | -5.05555 | -44.11385 | 2025-11-11 03:59:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b65aa2f-ff0e-31e6-9481-17482af364f7 | -5.60804 | -41.77384 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3b9a33fe-ef7f-3f24-a145-357e5687e925 | -6.64608 | -40.9763 | 2025-11-11 03:59:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 607db8bd-6ca6-3b62-b65a-df8d0fe0bfbe | -6.08829 | -41.55682 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 304574f7-0874-3313-a204-995200fd6471 | -6.36633 | -44.72065 | 2025-11-11 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f20c4d72-40d1-33fe-b19f-d05374da35be | -1.63633 | -52.05556 | 2025-11-11 03:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2a98a3ed-238e-381e-9321-b586cfcfc09e | -5.09652 | -43.78518 | 2025-11-11 03:59:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4d62633-e70b-3be6-965d-edc4ffde7b0e | -5.60738 | -47.28714 | 2025-11-11 03:59:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53e2884f-48d0-314d-9479-4dc19d1f40c7 | -4.31344 | -43.20548 | 2025-11-11 03:59:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 148c52ed-990c-38f4-bd74-c01f41c2075f | -3.89048 | -39.92815 | 2025-11-11 03:59:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1b2cb579-667f-380f-bc8d-f15180858c67 | -7.07411 | -39.67169 | 2025-11-11 03:59:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 51b4a706-3a47-394f-abd7-b1c5531cee54 | -6.83237 | -38.35171 | 2025-11-11 03:59:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a1d5bd5d-994e-33bd-a810-c8401ce5ba82 | -5.425 | -44.65064 | 2025-11-11 03:59:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6578a8e5-1fdb-317a-8b0b-2defedc1aa12 | -5.41848 | -44.83876 | 2025-11-11 03:59:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85d5168c-4b66-35e5-a991-ba451f056bc2 | -5.42658 | -44.84012 | 2025-11-11 03:59:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f254ef96-4dc7-3095-b231-0662a05fede5 | -4.74461 | -44.59687 | 2025-11-11 03:59:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e88afd8-9f70-309d-8804-c4bd7eeea7ae | -4.86885 | -46.68766 | 2025-11-11 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 135c6d19-0ad4-33c9-b360-461c529a8579 | -5.37984 | -46.36616 | 2025-11-11 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdcd6321-2379-39b5-9b90-3ecff8654a6b | -5.19214 | -40.76002 | 2025-11-11 03:59:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 92975b8a-63ed-3790-b675-311b5b145a6f | -5.00784 | -44.87528 | 2025-11-11 03:59:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88544341-119d-36f1-9ddc-32cc4c18bbbd | -5.65385 | -41.05826 | 2025-11-11 03:59:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b097a34-5d1a-30d1-a15d-a92e9ec95b1c | -4.75791 | -42.65917 | 2025-11-11 03:59:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ea943fd1-e0b1-360b-a30d-f9677566ba76 | -7.11179 | -39.77699 | 2025-11-11 03:59:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0432c6b1-bdc7-3123-90ea-96ed25049940 | -5.75364 | -42.73344 | 2025-11-11 03:59:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c36306b3-44a5-365e-909d-742ea5ea618d | -5.51159 | -44.3987 | 2025-11-11 03:59:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c30a5c69-7a6e-335a-8373-53976e6ae7c9 | -4.67178 | -43.25121 | 2025-11-11 03:59:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edf99fdf-d26c-31af-8f2c-e6ceb81eb2aa | -6.26499 | -43.68375 | 2025-11-11 03:59:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e23745e0-0862-3773-868b-82ba09d9f31b | -4.68126 | -45.84959 | 2025-11-11 03:59:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7290be5-012f-3bb6-bdef-7bb38aabfa0e | -3.85249 | -41.58585 | 2025-11-11 03:59:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d89e508c-b9bc-3871-855b-2bfd03e87c44 | -5.60803 | -41.07282 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 92541abd-dd6c-3232-a43a-3c4d2fc8e784 | -3.20831 | -43.32916 | 2025-11-11 03:59:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README13.md)
