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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0c15996-80a9-33a1-8cab-b342362d95a2 | -13.08928 | -47.30918 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62f882b5-601c-31f3-9ae3-beb7cb5401b7 | -11.99955 | -46.96832 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b2d3578-4937-390b-b69a-82780e0e79d4 | -10.44365 | -49.34703 | 2025-07-29 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50d6f8ef-9904-388d-88f5-d86734b513b2 | -8.70156 | -50.04663 | 2025-07-29 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27d4139f-7db6-3616-8d89-639ae04beaf4 | -11.99898 | -46.95413 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dd41898-a98b-3ed7-9874-9b03e3290dda | -13.48595 | -45.59529 | 2025-07-29 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b4104d34-cdd8-31c5-bb28-72ac77a4e8a0 | -9.46046 | -57.84991 | 2025-07-29 04:49:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cd0172c6-1867-3aa8-b904-0617d06a04fa | -11.74852 | -48.18324 | 2025-07-29 04:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f300f251-cd7c-3c48-832e-ffe89161039e | -10.16343 | -51.21704 | 2025-07-29 04:49:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42bd3cd8-29be-35c3-bc11-4ae3cae7b82f | -9.45686 | -57.84493 | 2025-07-29 04:49:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 197a31aa-88b1-3477-8312-c9c71e765478 | -6.49956 | -56.20496 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9ec495a-4dc5-3507-8ada-c795633d96f6 | -9.46121 | -57.84566 | 2025-07-29 04:49:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 270e3849-56bd-3c0f-a55d-d18640cf0f7d | -7.80471 | -46.57115 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c056b7a-3db0-3726-af0e-a160dca3431d | -8.88899 | -47.34196 | 2025-07-29 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 934530b5-6b79-3f8e-bd59-0743b1b5b76f | -8.13868 | -49.51064 | 2025-07-29 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5398c9c5-51aa-3968-b9a1-7dbfaf9cf816 | -6.49077 | -56.20723 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f3bc253-6cb1-3c96-be19-a96e577049ad | -11.69128 | -47.43237 | 2025-07-29 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5006ccf1-400f-3ad9-9524-d95a46a08b3c | -6.50182 | -56.21653 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f052769f-083c-33f0-abb9-4c463a7d6b41 | -12.00308 | -46.95469 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 620bab77-4e2a-37b6-ae27-2898e6e5d346 | -11.98825 | -46.69893 | 2025-07-29 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a4f5fe1-65f4-35d2-8cbe-bcb019ecadc8 | -11.4201 | -45.1181 | 2025-07-29 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| bdcb4b0e-39fa-347a-9a1f-78d745a94bd2 | -2.9106 | -48.2971 | 2025-07-29 04:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 09d0ee57-79a9-3436-9ba1-b46f6c3c3ab7 | -14.3604 | -59.3349 | 2025-07-29 04:50:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| cedf3f85-cd87-3b1f-8f00-29c7843c8914 | -11.4389 | -45.1385 | 2025-07-29 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| a8ee84dc-1945-3484-9b67-176c51d42270 | -11.4393 | -45.1154 | 2025-07-29 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 4b24ca2b-488b-3e99-bd30-bda0d9cc05a7 | -2.8921 | -48.2977 | 2025-07-29 04:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0835bbae-5418-3e9f-9a7b-7e892dc1cc1c | -14.36459 | -59.33716 | 2025-07-29 04:51:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3035b367-0685-3adc-b629-44002ead5c01 | -15.12439 | -45.33006 | 2025-07-29 04:51:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ade7ee6a-9932-35d2-b93c-ae92f6de18ed | -14.74222 | -46.30302 | 2025-07-29 04:51:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dea76486-6291-3769-bb5b-0ad16f9b405a | -18.43759 | -54.66187 | 2025-07-29 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2aaccba-3d33-3c98-8241-10575232e74f | -14.34957 | -47.09901 | 2025-07-29 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a134f2c-8833-36dc-8fbe-cddb5593a3a5 | -14.34945 | -47.10046 | 2025-07-29 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 463beac9-4b35-326b-9d67-b47d75a1beb4 | -16.03192 | -51.39238 | 2025-07-29 04:51:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 499c1f62-7f6e-3eed-9036-7ddd761aa225 | -14.35662 | -59.33109 | 2025-07-29 04:51:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0faac250-2f0f-35bd-a8a0-d1992a00d8cf | -19.94834 | -54.38885 | 2025-07-29 04:51:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8139c109-953f-369d-9014-202b3bf06fcd | -18.35367 | -49.38058 | 2025-07-29 04:51:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 525638d2-3d67-389e-9534-695a7477baed | -18.43485 | -54.6576 | 2025-07-29 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed841111-6d46-36ea-aa2d-fb4d966391ba | -14.5054 | -46.54374 | 2025-07-29 04:51:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3f95701-d672-3982-88da-432b58ae71b5 | -17.04523 | -43.77679 | 2025-07-29 04:51:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93f8b25e-d58e-3276-b72a-b38b2229fcb2 | -18.43639 | -54.66924 | 2025-07-29 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6d3d4c0-1589-33f5-92f6-159bf26decb9 | -14.361 | -59.332 | 2025-07-29 04:51:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2c39dfa7-f725-3e81-977e-b7998be7d39c | -18.44034 | -54.66615 | 2025-07-29 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd74e710-0835-3087-b1d4-6e155b5c974e | -18.43914 | -54.67351 | 2025-07-29 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18a3ec17-8945-3801-9267-b7346b0ac962 | -18.43699 | -54.66556 | 2025-07-29 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58adcc5b-6152-3806-bf2e-13e5991d62bf | -14.36019 | -59.3363 | 2025-07-29 04:51:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ac2edc1-0c1b-3e85-8871-6f168a0d9692 | -15.82003 | -41.89312 | 2025-07-29 04:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cc18a69-277d-3f25-8fe0-268daf7bcba2 | -20.14337 | -52.83899 | 2025-07-29 04:51:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db336fb1-baf0-38b8-964b-cfd9053ba44c | -14.12613 | -45.28754 | 2025-07-29 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76bbe699-839b-373a-a5e2-79d92ee74cd6 | -14.50597 | -46.53944 | 2025-07-29 04:51:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca41ecb3-a766-39c4-814b-06d2fd9ab028 | -14.36539 | -59.3329 | 2025-07-29 04:51:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f0cb9dd0-5331-325f-b2f5-86eb8d929fa7 | -15.8678 | -52.40944 | 2025-07-29 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 373a2a3d-fcd6-3373-bc93-5ddc7f6b9dbc | -15.86836 | -52.40582 | 2025-07-29 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7962d9c8-4579-3ad2-8d25-f3c4b7cb529d | -15.1496 | -53.51278 | 2025-07-29 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f50f74c8-c85e-3665-af46-d3dac0fc0d19 | -14.36181 | -59.3277 | 2025-07-29 04:51:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ab0940d-d3ce-3cf7-b134-0d7b1cca7cf3 | -15.8717 | -52.40636 | 2025-07-29 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9f8b7fb-6c1b-3f0d-920e-c3f2b18296b7 | -18.34852 | -49.38984 | 2025-07-29 04:51:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79eb9cdb-3983-3f40-b493-905fedfbdc84 | -14.50976 | -46.54439 | 2025-07-29 04:51:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d987b52-c21a-3e26-8800-37bcaab048ce | -15.12981 | -45.32539 | 2025-07-29 04:51:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 401fdd30-a08c-3f58-8b16-02547bd2c293 | -16.95028 | -51.77512 | 2025-07-29 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd436640-4aff-3a2b-962b-2a0740084cb4 | -14.46108 | -47.88155 | 2025-07-29 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2df49fac-1cfe-31dc-87a1-82c2cfa916fe | -18.43425 | -54.66128 | 2025-07-29 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82626f5e-4b87-31b0-a1d0-2d14bd7feac1 | -15.82052 | -41.88865 | 2025-07-29 04:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4813db8b-ffec-3416-be43-9e5de38de32e | -13.7665 | -56.12463 | 2025-07-29 04:51:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 074e7848-2923-3bde-8836-9207dc8ab6f5 | -13.09054 | -52.13676 | 2025-07-29 04:51:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b162f3cf-6619-392d-8d4e-82d998073488 | -19.94776 | -54.39253 | 2025-07-29 04:51:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2be6fe1-1b09-32fa-a552-b69be5f225ad | -18.35302 | -49.38548 | 2025-07-29 04:51:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b75aff4-bfe1-32ef-b745-8b7749378cab | -14.35429 | -47.09563 | 2025-07-29 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2b389b4-41bd-386e-81ef-761a039dfc75 | -14.48817 | -50.29327 | 2025-07-29 04:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15ba45c7-7d72-3404-abe8-2827452d944e | -21.44616 | -45.76726 | 2025-07-29 04:51:00 | NPP-375D | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 81d20a5d-759c-3e8b-9ddb-b50e1adffb20 | -21.44729 | -45.76767 | 2025-07-29 04:51:00 | NPP-375D | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4a478e5a-01cb-381c-8d29-136a622f04e0 | -14.2255 | -43.94919 | 2025-07-29 04:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffc9bc58-34dc-36bf-9f9a-5d361da2f220 | -14.22587 | -43.94601 | 2025-07-29 04:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efe28fa9-e85a-35b1-bdef-8cd5acd484f9 | -17.59962 | -48.42513 | 2025-07-29 04:51:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb615b39-e089-3c2b-80cd-65c86aff94d8 | -20.29513 | -54.07517 | 2025-07-29 04:51:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6a8836d-d259-3cfd-b4aa-a1d4c35b6136 | -18.43579 | -54.67291 | 2025-07-29 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e03c5eaf-28a1-3e24-9750-4e68286edeaa | -15.12917 | -45.3307 | 2025-07-29 04:51:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8985f15d-60c4-3f4f-a74c-f47cb9c8321f | -14.34999 | -47.09648 | 2025-07-29 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bff98661-346f-33c8-8be7-765759418b4d | -14.48466 | -50.29274 | 2025-07-29 04:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ba0436c-6d39-3fbe-b15a-04432194360c | -14.37518 | -50.326 | 2025-07-29 04:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2bd5f21-1db5-3442-8d7f-81262b660cbf | -15.82121 | -41.88964 | 2025-07-29 04:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 229844b9-576b-3418-96c4-5ba7a8e76d4d | -17.66928 | -44.12508 | 2025-07-29 04:51:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d62a91ab-05fb-381f-a424-b8bf700db3a0 | -14.48524 | -50.28874 | 2025-07-29 04:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6630656f-6d2d-3c0f-b5a1-dfbf059e016f | -14.13086 | -45.28816 | 2025-07-29 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46eb012a-9541-3092-835f-9c99d4c9fd1b | -14.3746 | -50.32996 | 2025-07-29 04:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f31d076-0eb0-3b62-bb1c-fd5a4dacac0e | -14.45954 | -47.8843 | 2025-07-29 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c0d52b6-4c67-34e5-8160-49d7ebe5e1a1 | -14.74282 | -46.29847 | 2025-07-29 04:51:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5329819-f1e5-3907-9cc9-07f94974c280 | -14.36619 | -59.32862 | 2025-07-29 04:51:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81e8da8f-4e94-3263-aaa7-5dde32cf9ba0 | -14.35009 | -47.09503 | 2025-07-29 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 965c67dc-842b-32f3-97f5-b057d312653b | -18.43974 | -54.66983 | 2025-07-29 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f84123c-d56e-3500-9c73-4343b703c748 | -14.50161 | -46.53876 | 2025-07-29 04:51:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ee1f4ac-e0ef-3cfc-90c8-fd4989b0b590 | -14.57799 | -52.87872 | 2025-07-29 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6a4a49a-01a9-39a9-a82c-656fc42cea80 | -14.48173 | -50.28821 | 2025-07-29 04:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0edaf88b-2fe8-3e30-b00e-042970ab5f5f | -15.93183 | -48.39606 | 2025-07-29 04:51:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c41a3433-5d84-345d-a160-8131ba98ebfc | -21.33444 | -55.63103 | 2025-07-29 04:53:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5415ef63-9017-349b-b1d3-e38b9500507c | -22.53234 | -43.55361 | 2025-07-29 04:53:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| a1cef3b2-1ec0-31b8-92e4-9923eec2fa05 | -21.77549 | -52.75095 | 2025-07-29 04:53:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 183ef263-4c1e-3ba1-8d9f-bb15b8947c3e | -22.53265 | -43.55013 | 2025-07-29 04:53:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7d7929cd-104a-38ee-bf6e-be30abf7266d | -22.53199 | -43.55767 | 2025-07-29 04:53:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 1158ef68-5091-3c14-853c-ccdbabf0ff7b | -22.52582 | -43.56028 | 2025-07-29 04:53:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 4f2711e2-4864-3c87-baa1-184a2560f2f2 | -21.3378 | -55.63167 | 2025-07-29 04:53:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README20.md)
