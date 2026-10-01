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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3093f833-186f-3842-b4d9-beede674370e | -5.91121 | -53.49887 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59433d04-6a28-3598-b02c-36c485178371 | -10.825 | -57.20673 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aedc7a77-7bb7-3af1-9af6-b9cfdb64cfd6 | -6.34396 | -55.32933 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b0bd71f-cb16-3178-b312-a1271a9a3b62 | -10.53369 | -57.77945 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7bfbf9a-90a0-3f46-81c4-13014346ca63 | -8.1555 | -54.80947 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27aade98-38af-3405-aab5-7d0555099bc2 | -9.00097 | -65.7025 | 2026-10-01 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a81bc5e8-b456-3940-a41f-473c30bfe4eb | -5.37219 | -56.0574 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4de3972d-d334-3e03-9b73-785bdb6158b8 | -10.536 | -57.764 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a6b87c8-f027-3b8c-b49a-a8dceb6d7837 | -6.24537 | -57.75853 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fc8f96f-5fdf-3665-8483-c9f04f689df0 | -6.10418 | -53.09138 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4128888e-d48a-31d4-beff-cc5d6b5682a7 | -6.11201 | -55.70364 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c8dde5a-cfc5-3e0f-b378-9cb77321d1d9 | -10.05348 | -53.1228 | 2026-10-01 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b39dc7ea-53e1-392d-9835-197985e8214a | -9.545 | -56.16368 | 2026-10-01 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24f92a60-f5f9-341c-8cd7-a8d196ea1b58 | -5.88517 | -53.67937 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c210ec58-32ed-35b8-92f5-a8b0a9ced99e | -11.29258 | -50.96521 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e91c9887-9809-34f9-8a54-67054460e0bc | -7.4938 | -54.9813 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ec44149-ae39-32b5-9e5f-40705a77f530 | -9.06799 | -49.87421 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0d96001-0490-31ec-a5d3-8a4629ea672e | -5.12984 | -56.00703 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b542ea2e-9d7c-3779-bf37-c2b605ec9a9c | -6.85161 | -59.36029 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38d68ae8-a8c1-36ab-981a-68f7dd71a99a | -7.46101 | -55.00474 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a13b507-8bc9-3f2d-a5d9-b1e2224129e8 | -10.82795 | -57.21144 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a20b5da-0769-36c9-b41e-9dfcd0abf757 | -11.33587 | -50.96766 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a19534b5-a2c3-3220-9fc6-c6749d82f50f | -8.38779 | -46.29353 | 2026-10-01 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a152437-cfc6-3b7d-9635-e54fb12ea0b3 | -10.506 | -57.77516 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b984fc04-103b-3227-8936-4875dc4fc20e | -7.46246 | -54.9949 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 897db627-bc39-33ba-9880-689fa526de69 | -5.86502 | -57.7592 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c03d9e54-f094-32a4-8e54-26b186fa64e0 | -5.97794 | -55.37207 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37bbca7f-e059-3860-bfe7-46f90ea974cf | -9.314 | -57.7093 | 2026-10-01 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8633b198-be2b-3220-832c-a042ade80441 | -6.07694 | -53.30904 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d3fa6ed-8226-38f1-a328-54a40e171ef7 | -6.14005 | -53.29034 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c21e4543-1acc-3381-907a-d4bbd8757c9b | -6.05896 | -59.91999 | 2026-10-01 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 160b6299-f36f-391c-942f-b4f5b571e27c | -9.02541 | -60.55231 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c39db073-113a-3dde-b986-b4876c519dd5 | -6.90439 | -58.93022 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 82c32cb4-61a3-347f-9dca-82f11db59e46 | -7.5952 | -55.07064 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c02aaa2-8041-3b2a-b346-086561946628 | -6.67862 | -58.87325 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2602fc97-1ac7-3cf0-b7a2-99f9f6e2f1b2 | -9.54563 | -56.15927 | 2026-10-01 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1e76880-e995-3bab-b3e8-dfafbb03877f | -7.49335 | -54.99962 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7a3fb0e-bad3-3e18-b005-7eea50d959e4 | -7.5014 | -45.79544 | 2026-10-01 05:18:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94130056-cbb0-3adf-baa6-a3c9f336bfaa | -10.52903 | -55.01139 | 2026-10-01 05:18:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c4b67e0-c134-3fca-a07d-18574f91990e | -6.84501 | -59.35925 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15624f26-36f2-3d11-a6da-06c26d3a2fab | -8.16806 | -54.80215 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cff6feab-400d-33c1-9446-cb55210c334d | -10.53163 | -59.62528 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9218f7f1-bf87-3cc7-ba48-8689dbc58033 | -10.60398 | -53.97393 | 2026-10-01 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c79831c0-2917-3f23-8286-7f94590e43a5 | -8.84888 | -49.709 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd0bee0e-5569-3c6d-bde1-008975c3a246 | -7.33973 | -55.59503 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7518bc38-5a41-368d-8730-2aeee95e03f2 | -16.43025 | -47.18195 | 2026-10-01 05:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85e7d8e6-45c3-3d32-b0e1-321ee54b47fd | -14.39968 | -51.26293 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7217792d-3f63-33e0-90b6-f0b926a00168 | -14.44043 | -51.25519 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5eebf9c5-a5e7-3269-99e0-ca53e596ca33 | -12.77431 | -54.02117 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8df2b2d-f91a-3cdc-ba63-f5be68d6cc6e | -14.15524 | -51.14775 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17513eed-f54c-3c75-9ed5-f4599bedf7b6 | -14.42987 | -51.2501 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12df8e2f-39e8-35eb-9122-c91aee1c8727 | -14.39504 | -51.25493 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9ca4b821-1273-3c3b-a086-6eedd07d1df4 | -14.37911 | -51.29714 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0c162a86-7f1a-382a-8486-7102ada48ab4 | -13.6509 | -53.93251 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 72835cfb-6842-3a4c-8668-21904344db99 | -14.89247 | -51.88343 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6542db52-3d9b-343e-99f5-8133e6c697a0 | -11.18637 | -58.17156 | 2026-10-01 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8e0612e-6308-37fc-9fb3-37cbcb48604b | -14.39296 | -51.27312 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1ba61215-07c5-3f10-b984-9909924b29d6 | -14.48993 | -48.30602 | 2026-10-01 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ae7f2cb5-7fd0-3c4f-9ee5-3a6b992fee86 | -11.11872 | -59.12384 | 2026-10-01 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 082938b4-1929-3d63-b2ed-a9b132ff6af5 | -12.64093 | -47.64027 | 2026-10-01 05:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cdb29fc-c412-3d16-ad12-223bf0ff6a88 | -14.14506 | -51.13895 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b7002d9b-3110-38db-90f3-9be1a7b125c8 | -14.15855 | -51.11826 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55d2482a-49cf-38a4-9580-99b57f6971af | -14.86483 | -51.85163 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 22c3f10f-cfc2-3ef6-a0d6-ef8f1b887ee3 | -14.40389 | -51.27456 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2ae88570-7666-3a04-b57c-ef4f033522a5 | -14.87013 | -51.85231 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ddb52dca-1e22-32cd-9583-524d47b2f2db | -14.38874 | -51.26149 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 22a1145d-91f4-3750-b9ef-d76a9df8763f | -11.18405 | -58.16351 | 2026-10-01 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9951b1ce-d3e1-3d9c-9b8d-0872b5b8259a | -14.89304 | -51.88604 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f5d8ba1-483d-3bf3-b24c-03b72c408979 | -12.70037 | -54.06954 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac3c1e12-b35b-3997-b71d-47ef5e65cff2 | -13.65873 | -53.94318 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20481b34-2420-37c4-b9eb-614eaa6e5df1 | -14.86444 | -51.855 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fe8c15c1-364f-399b-827b-3466172fdbe6 | -14.40473 | -51.26728 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8fb9e860-f14c-3171-970f-c93427c475af | -14.89343 | -51.88268 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 976d3f21-4729-3289-a884-ad06d30390b4 | -12.77489 | -54.01669 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c2b830a-6f51-3a30-b0f1-ddef456b6522 | -14.40431 | -51.27092 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca0a0053-c8af-3dc9-a0a2-f88843746163 | -14.3904 | -51.24694 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b85a539-577a-35e5-84da-c5cdc06de5c7 | -14.37953 | -51.2935 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a0bb753c-1cc5-34b8-a6ea-90612cb8568f | -12.25331 | -50.29821 | 2026-10-01 05:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75744580-987b-38f2-87c3-754a629360e2 | -12.09452 | -50.68952 | 2026-10-01 05:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d382d4a8-753c-3ef5-ad08-bccea2693b6d | -13.65541 | -53.93325 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2ad44daa-848e-33fc-be56-da64aed766e3 | -14.39337 | -51.26948 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 32bef4b7-b6aa-3eec-a688-61cb310c4b24 | -14.3879 | -51.26877 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e23b3b95-633b-31fd-a702-8ef9164843e6 | -14.43928 | -51.25696 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73a570eb-4b1a-31db-9d5d-b0d5739836cc | -12.77607 | -54.00771 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24ca006c-1950-3598-9719-97bc49685a06 | -14.14547 | -51.13527 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 495bf43e-c8d0-3aa5-b848-953d6fb9e464 | -12.71 | -54.06904 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32dc3385-f6f0-3e63-ae51-083f85af7fed | -13.66326 | -53.94379 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5287dda-e9ea-31c7-9302-999cf98db285 | -14.39926 | -51.26656 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 670288cc-afaf-3532-bdb6-ece808a999c7 | -12.26196 | -53.99575 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d8024f7-77f2-3e82-b7f3-e03d0c1115b1 | -11.71918 | -59.35295 | 2026-10-01 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 985e0a57-98ed-31c2-bfc4-b13589e65946 | -14.14491 | -51.13713 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 72a2e85e-0768-33b8-8fbf-c7a0c5bd5a5b | -11.18461 | -58.1597 | 2026-10-01 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f1b8724-7e79-3675-b6b1-0f5d2e74e228 | -14.15565 | -51.14407 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 011b2bbc-ec64-3901-a3c6-fa397ad0c0be | -12.08857 | -50.69245 | 2026-10-01 05:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9dcf60dd-f138-30cb-9d11-a2bc31ccf745 | -13.66266 | -53.94836 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37677bb8-7a30-38a6-8759-8ccba7069067 | -11.18692 | -58.16779 | 2026-10-01 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6c06c65-1577-3ad7-978b-ee963f1ece1a | -14.38957 | -51.25422 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f5f11109-12a7-347f-a367-99d28e2fe500 | -14.87052 | -51.84896 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 211448a7-6bda-3a2f-b022-a3cc21632f4d | -11.18805 | -58.16019 | 2026-10-01 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aca78b73-cd3d-307b-b6de-d5f20d4c0ac5 | -12.39245 | -54.095 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README84.md)
