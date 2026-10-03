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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1965c90-745e-3902-af86-adbfb0f922d5 | -12.13797 | -63.1754 | 2026-10-03 05:38:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 834e3ead-8b27-3396-8759-452290b496c9 | -12.13134 | -63.17432 | 2026-10-03 05:38:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c896292-8f3c-3cb7-859b-12d9087c066c | -9.89289 | -60.29312 | 2026-10-03 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98bfb4ae-3055-3cc0-aa23-fc8beb03e613 | -9.11397 | -65.3967 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fc9e154-f591-3d1f-9e38-477c959de4a4 | -7.9829 | -67.15674 | 2026-10-03 05:38:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4083865b-e944-3cbe-a523-b6ceff4b1eac | -8.70655 | -66.73143 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b70b4e7-cf03-3339-867d-759e0abb545f | -7.97902 | -67.15607 | 2026-10-03 05:38:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e8fa1c8c-5f2f-3962-bb63-bb60e7554662 | -9.29186 | -60.53998 | 2026-10-03 05:38:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aec6d0d-533a-3779-96b2-ce4f6cc744d1 | -9.1074 | -68.25595 | 2026-10-03 05:38:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6c8196e-85f2-390e-ad44-4ee22478fd07 | -10.9949 | -59.13805 | 2026-10-03 05:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 08217a94-b10b-3650-a975-128925cc7aba | -11.03728 | -62.57169 | 2026-10-03 05:38:00 | NOAA-20 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a852c46-2d51-3d0c-a6de-d024c37ff89f | -9.90697 | -65.03828 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82078635-02e9-3d6e-9b76-039e4be3153d | -10.49782 | -63.3024 | 2026-10-03 05:38:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 732fdba6-4213-359d-8494-fdd21a8c0605 | -9.48492 | -67.15633 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f28f1de-cbf4-3b3d-93c6-713ef72a0d7a | -12.145 | -61.1745 | 2026-10-03 05:38:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a05bcb3c-d341-3164-97ca-f17b5cee735f | -10.9956 | -59.13322 | 2026-10-03 05:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| baed16e8-6c39-32f0-aa79-f195413fe248 | -9.56265 | -62.72982 | 2026-10-03 05:38:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 846572db-e701-3211-a5b1-c7b960b5686f | -9.38015 | -65.47148 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f2c70ea-43ff-3af7-8957-aa4f7b034321 | -11.199 | -61.52528 | 2026-10-03 05:38:00 | NOAA-20 | MINISTRO ANDREAZZA | RONDÔNIA | Brasil | 1101203 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04aea5b6-b538-322f-b8a0-ae925b00427f | -9.91867 | -65.05117 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36953437-ceae-358b-ab30-f2557f6191ea | -8.85691 | -66.78604 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7474a06-3045-382c-9c3e-081c31b0fa0f | -9.17374 | -59.69503 | 2026-10-03 05:38:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3b042dc-a92d-3f18-b150-eb14c6e1250a | -9.17012 | -59.69447 | 2026-10-03 05:38:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df040d78-552c-33cd-abea-cfede04cc98b | -9.62281 | -65.73737 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd0fa26f-352f-39d3-8616-d0f5d8fccc36 | -9.72416 | -66.34324 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a055b26-fbf5-3ddf-bc65-626903088e49 | -8.85513 | -66.79224 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7eef657-a2bc-39f1-a6e0-086eef5f64d7 | -11.04448 | -62.56925 | 2026-10-03 05:38:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 849d741d-5d0f-3682-b48e-d2021068e330 | -12.14128 | -63.17594 | 2026-10-03 05:38:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 57e27cea-4beb-34b9-a208-86cbaf081a9d | -10.99107 | -59.13751 | 2026-10-03 05:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b95c2a60-f3ab-364c-8149-4df42cb29a10 | -8.85588 | -66.78766 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7591609a-39df-36e9-bd29-7d9b85ef0124 | -7.7025 | -67.08338 | 2026-10-03 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fd90603-4efa-3792-a78c-1fc024912926 | -9.88788 | -65.1416 | 2026-10-03 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc7a3d9f-2082-3c72-a154-385d1337f4c7 | -8.85645 | -66.78576 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ae2418c-f6cd-3b0c-89f4-caca6eb11227 | -8.70372 | -66.72958 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03917d28-2ee2-3580-a410-131e884173f1 | -9.37442 | -65.47174 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 335d7a5e-5d8d-376b-9b41-2cb877dcae85 | -9.13679 | -68.24887 | 2026-10-03 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b60328b-914a-3876-9bad-b1edee38c6bd | -9.37811 | -65.47118 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2140e2eb-4bcb-37c1-a88c-58a67e7f01e8 | -9.45177 | -68.94481 | 2026-10-03 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad21f5cd-5d98-3baf-a3e4-ddb7b1b827ad | -8.85561 | -66.79205 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 731e070c-f0cf-34c1-914b-abe027be8399 | -9.13414 | -68.24589 | 2026-10-03 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51428f61-eeb3-304c-aff5-e1144dce96c7 | -8.89222 | -66.8866 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fca47ef-269d-3498-812f-52d7f7d0c8d1 | -9.62354 | -65.73839 | 2026-10-03 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 112964b5-392a-3d4f-88d9-ea2de8c26258 | -8.70331 | -66.73276 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8b09f76-e721-3122-8568-7eaa6e6f53ea | -7.70289 | -67.08047 | 2026-10-03 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb9674a7-9f4c-3ccb-bc8e-542a635f95fc | -9.13348 | -68.25093 | 2026-10-03 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f266951-f675-3d21-a576-07533f322a7c | -10.72887 | -69.41347 | 2026-10-03 06:22:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b39edc83-4211-3c9f-918e-3bf114a773a8 | -9.31022 | -65.77291 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e3f1f11-3f6a-3338-9ab4-b5d44b41f595 | -8.6587 | -66.93441 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0be73bd2-8cf5-34b2-9025-61602ef77aee | -8.70851 | -66.73351 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f219eba7-1f53-3b4d-b1ef-e535cc4d7776 | -9.13208 | -68.24818 | 2026-10-03 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96d50ff5-4118-3044-9965-2359a4890dee | -8.86164 | -66.78651 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2a9ae04-f648-3ded-87b3-01a7bb1f7776 | -9.55264 | -65.98505 | 2026-10-03 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 363af4d0-d98f-347d-9717-ae754eb377cc | -9.62303 | -65.74235 | 2026-10-03 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db500dfd-3d64-3637-b394-3a82d9780735 | -8.05675 | -69.95791 | 2026-10-03 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecd01888-89f5-3e79-90f2-386cb97471da | -8.86079 | -66.79279 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03821306-feea-3b2d-9c52-5da901a6bb63 | -9.882 | -65.14085 | 2026-10-03 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a9f16dd-09a8-34dd-8ec3-570278ea1459 | -8.89738 | -66.88731 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d647ab5-ad19-377e-b5c0-5703c3099984 | -9.38013 | -65.47253 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 558aa0be-c69f-3004-a054-9cf9b1ccb197 | -8.86121 | -66.78965 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c1bc1e4-0ec8-3e47-a59c-cfaafe790001 | -8.68275 | -66.80989 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77549efb-4ba5-3d90-9f4b-d208c38602a8 | -10.72827 | -69.41803 | 2026-10-03 06:22:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a063e0ad-d045-33c8-a313-d89869644fd7 | -8.89262 | -66.88348 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 410f402f-cd62-399f-adee-f4271689878b | -12.13225 | -63.17396 | 2026-10-03 06:22:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07d668b6-6655-3789-8c19-7437b94a61c4 | -12.13905 | -63.17485 | 2026-10-03 06:22:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9259ee15-cab8-3d3e-bcb3-0fa0208ed5d9 | -8.85602 | -66.78892 | 2026-10-03 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c11e63e-5e55-31a9-9a20-b154fd62039d | -9.87973 | -65.13488 | 2026-10-03 08:05:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c24a88fc-744e-3bce-9c56-57dbad777e79 | -9.54387 | -68.52563 | 2026-10-03 08:05:00 | AQUA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a72b381a-4ac8-3d52-b563-2684dcc9978c | -8.85759 | -66.78883 | 2026-10-03 08:05:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b7fa11a7-a28b-3d9c-9e27-01748ab4ccc0 | -9.1695 | -61.403 | 2026-10-03 08:05:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 98adcc84-f18b-3045-bad8-d2602596e046 | -3.70458 | -50.65349 | 2026-10-03 12:19:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| dc7705a2-3320-32c3-8021-32494f8492df | 1.7993 | -55.56688 | 2026-10-03 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cdd10250-d9bb-3725-a626-d18464fdea22 | 1.90411 | -55.78048 | 2026-10-03 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7f839059-2c4a-3220-91de-520d423fc2b3 | -3.64596 | -55.50568 | 2026-10-03 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 06603955-305d-37b5-9acc-1ce461a6dffc | -4.12021 | -55.01894 | 2026-10-03 12:19:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e51dacd1-75d6-395a-acf4-40072f210a44 | 1.9117 | -55.77039 | 2026-10-03 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 966852b2-9670-3ff8-902b-06e86dab2222 | -4.53915 | -50.76772 | 2026-10-03 12:19:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 08202ff8-37e2-3db5-9c0c-44342171521f | -3.85745 | -55.96593 | 2026-10-03 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 43ee5d3e-2689-349f-8c5f-014d031efd6c | -3.84865 | -55.9647 | 2026-10-03 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bdecbb13-6172-349c-bb5e-b840c786b7ea | -3.12935 | -53.75165 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 7998d37a-2793-3020-8b52-68f7e0d19d1a | -3.0089 | -53.88182 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 59014882-191c-3385-8bd1-f957963a1a06 | -3.85061 | -55.80692 | 2026-10-03 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2d8dd378-a5ce-3d62-a479-70f66b5f7752 | -3.22392 | -54.31536 | 2026-10-03 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a9def697-4750-3667-8f62-7de2df251ee5 | 1.9193 | -55.8237 | 2026-10-03 12:19:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f26d0f27-bda3-3a51-8587-4f66662cdb7e | -2.25117 | -51.93062 | 2026-10-03 12:19:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| eb76faf7-0fee-3327-b405-76c92f04de04 | -1.27111 | -54.5564 | 2026-10-03 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6c6f796a-7fda-3abc-b3c0-27734ea777ee | -2.26168 | -51.93199 | 2026-10-03 12:19:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8beabff7-d417-3dce-a22f-0a0d1db4d769 | -3.28402 | -53.82599 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 5c7a2d32-0643-314b-9420-47594535d8b6 | 0.43474 | -50.7562 | 2026-10-03 12:19:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 16.5 |
| afca4e91-3017-35a8-8494-a14a86ebd307 | 1.91803 | -55.81481 | 2026-10-03 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| e0ea85c4-7e1d-316c-a614-9bd06b06a4d9 | -2.77869 | -57.68711 | 2026-10-03 12:19:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| db720f3d-6380-371b-9e70-0340c664b5c6 | -2.63227 | -56.58266 | 2026-10-03 12:19:00 | TERRA_M-T | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 14ee5eff-d30f-36cb-adb7-be287bc97f65 | -1.08477 | -54.11091 | 2026-10-03 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c307f6ff-2594-3e9a-bf10-f6abfad9d999 | -6.00772 | -53.53029 | 2026-10-03 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 96fff9ba-8691-3652-8a22-2134fced6200 | -1.88239 | -50.63419 | 2026-10-03 12:19:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c79d4cda-b8b1-3bb5-b4d1-aacf6093e7e2 | -3.22529 | -54.30578 | 2026-10-03 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d9c18a51-a238-381a-bf6c-3b72391fb11b | -4.54472 | -50.7743 | 2026-10-03 12:19:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f639f223-64a0-3109-89a3-a788d515b1d2 | -6.01812 | -53.53794 | 2026-10-03 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| b905a474-3fad-369b-aeba-eddec28fb94e | 0.44575 | -50.75469 | 2026-10-03 12:19:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 70f186ed-e595-3ca2-9344-6d15f4e9b90c | -3.15542 | -48.73272 | 2026-10-03 12:19:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8c3029a0-031d-350c-932a-84731dd098ff | -2.97379 | -53.27398 | 2026-10-03 12:19:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README47.md)
