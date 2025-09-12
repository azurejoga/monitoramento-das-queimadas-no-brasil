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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d3e2285-ab58-34a9-ae69-483c2f212556 | -17.35347 | -46.68627 | 2025-09-12 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 2fe051ff-1c02-350d-be03-af94f89e5e5e | -22.87159 | -46.55956 | 2025-09-12 00:09:00 | TERRA_M-M | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| 206fe18c-07a0-3033-8f2a-7ddb949178b5 | -14.12151 | -44.31604 | 2025-09-12 00:09:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 38f84f59-37d2-3ff6-92ca-81def23ba7fe | -22.48421 | -46.59305 | 2025-09-12 00:09:00 | TERRA_M-M | ÁGUAS DE LINDÓIA | SÃO PAULO | Brasil | 3500501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| cbe23a88-19b7-3856-a6c6-5d39f71b483d | -17.91495 | -45.91127 | 2025-09-12 00:09:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2856bd85-70bc-3b73-a334-aee0cb2d33c6 | -15.53029 | -41.43405 | 2025-09-12 00:09:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 3f84bec0-82e7-35ee-8a83-0d8889fec67a | -21.17236 | -45.12349 | 2025-09-12 00:09:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 0cb4602b-d99f-349b-8a91-a5331f9e2a05 | -13.90715 | -48.23911 | 2025-09-12 00:09:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b9e17d53-ec4e-3a48-9dbe-5d77d15266c6 | -16.60138 | -49.81095 | 2025-09-12 00:09:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 05269630-de03-35e4-b723-3bef92371259 | -14.18249 | -46.17181 | 2025-09-12 00:09:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 6fea07b6-6a84-3a12-b82d-1bcf5e425d7a | -15.50673 | -40.75365 | 2025-09-12 00:09:00 | TERRA_M-M | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 9e68288d-fe34-373d-a8cf-a9f891ea2ee5 | -15.6944 | -47.03603 | 2025-09-12 00:09:00 | TERRA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 30439649-c587-3d69-9e43-8c6d4b23663a | -18.59467 | -47.18373 | 2025-09-12 00:09:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2cfe65ee-9d44-3cfe-934b-f569402aa9c5 | -17.8002 | -42.56942 | 2025-09-12 00:09:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 4ef48c35-9f38-39fb-bd4d-ce32629d79b9 | -15.78707 | -43.40665 | 2025-09-12 00:09:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b1693689-8a0c-320d-81ad-5978221a304f | -21.13847 | -44.44884 | 2025-09-12 00:09:00 | TERRA_M-M | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 8a569f88-da47-32b6-8055-be51727b5a61 | -18.5968 | -47.20331 | 2025-09-12 00:09:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| bec1ad62-e805-302a-96ff-55c6fa184567 | -14.74651 | -46.28885 | 2025-09-12 00:09:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4a61a2c6-3357-39b4-a792-0198fb31ed61 | -14.45478 | -47.30431 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 7811f5fe-92d4-3b6f-b3e1-de35e10ed731 | -21.95539 | -47.54688 | 2025-09-12 00:09:00 | TERRA_M-M | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 356.0 |
| 0914c087-2a7b-3e80-81da-c91e0be50824 | -15.09431 | -48.01074 | 2025-09-12 00:09:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 67bd7a62-6d04-392c-b799-535b2ac26211 | -14.49603 | -43.8063 | 2025-09-12 00:09:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a59248c4-0049-386a-807e-b3ea5d538e14 | -15.24314 | -44.05 | 2025-09-12 00:09:00 | TERRA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 25334951-4bda-307d-8f7c-557e0c228a56 | -14.12409 | -45.37913 | 2025-09-12 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1428c7a7-0bbe-31f1-9b42-469842bfe416 | -15.48856 | -47.35204 | 2025-09-12 00:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d0070200-dcda-34fc-a814-e337f64a0cd5 | -17.59157 | -42.17255 | 2025-09-12 00:09:00 | TERRA_M-M | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| fb925360-c4ab-3076-89d4-c9415b953239 | -14.44945 | -47.3251 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| e6fddb43-5f4f-3ff2-82f5-919dd2d09123 | -20.27779 | -42.11068 | 2025-09-12 00:09:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 182a8d45-6b95-38ba-a13f-de5486914ba3 | -17.34176 | -46.68771 | 2025-09-12 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| af4eafb0-a836-3f79-b332-4d821540ef5b | -13.36661 | -41.92122 | 2025-09-12 00:09:00 | TERRA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 438799be-b77d-3afb-8d90-24c7862f66cf | -13.25109 | -43.77515 | 2025-09-12 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 545fc863-25d2-3ae6-8654-734e32f7d08b | -19.17436 | -48.01219 | 2025-09-12 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 39.7 |
| f86e645b-d5bf-3318-b19a-c66f7067db1c | -16.60123 | -49.81765 | 2025-09-12 00:09:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 94202953-0a50-32d5-b38f-72d635089a8d | -12.10194 | -37.97539 | 2025-09-12 00:09:00 | TERRA_M-M | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 3989e426-7e40-3dc1-87c5-ce5923625244 | -14.15011 | -44.4624 | 2025-09-12 00:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f8978f8e-ea4f-3df8-ab4b-6e2d628c8382 | -19.66385 | -44.90554 | 2025-09-12 00:09:00 | TERRA_M-M | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 7fed1b47-e94d-36d0-8d78-79bb0720ba12 | -20.16112 | -43.68002 | 2025-09-12 00:09:00 | TERRA_M-M | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 35ad9881-c5f0-3729-b36e-e4ace8ade7e1 | -21.3207 | -45.01493 | 2025-09-12 00:09:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 78d875e7-9a36-3345-9d95-5ce0d9857093 | -13.24196 | -43.77644 | 2025-09-12 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 268d1882-a17b-38d3-b42f-50242d5f9321 | -20.39965 | -42.19764 | 2025-09-12 00:09:00 | TERRA_M-M | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 78b3fac3-453c-33a1-83a2-4a299324e005 | -22.85901 | -46.56124 | 2025-09-12 00:09:00 | TERRA_M-M | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.7 |
| cfa400ca-0f6a-32b3-9399-c655724a7858 | -19.99517 | -47.64394 | 2025-09-12 00:09:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 35.7 |
| edf4bbe1-5f5f-3c81-ac9a-61da0d2b5cdf | -18.05303 | -45.43992 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| a44a421a-8fb2-3503-a1e3-83566143cd3e | -21.12798 | -44.45002 | 2025-09-12 00:09:00 | TERRA_M-M | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| d1faf420-a605-3b23-8de7-ad46db366bd3 | -15.83593 | -42.6003 | 2025-09-12 00:09:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a2042dcc-d6f9-3a84-ac3a-5a5f011eaf13 | -14.0441 | -42.15575 | 2025-09-12 00:09:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| f134074b-5292-30ac-8447-cca9633f3795 | -19.24353 | -48.02723 | 2025-09-12 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 8306372a-f43c-3357-a559-7610db727672 | -13.3189 | -44.09052 | 2025-09-12 00:09:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 248.1 |
| 910823e8-a4b2-35e8-9e59-41a0b2c27b5f | -16.59829 | -49.78905 | 2025-09-12 00:09:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| b15286f6-b0c6-33dc-8cd8-2f0a007878a7 | -22.61064 | -46.42402 | 2025-09-12 00:09:00 | TERRA_M-M | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| 22ccbcc9-fc4b-370c-8d06-1f85b0627022 | -15.68821 | -47.01482 | 2025-09-12 00:09:00 | TERRA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| fe2094db-1427-33db-b5ab-93e790577708 | -19.48765 | -42.32336 | 2025-09-12 00:09:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| f06d609c-7a0e-325b-a76a-334bc4334b80 | -21.65442 | -50.11685 | 2025-09-12 00:09:00 | TERRA_M-M | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.5 |
| 9aed3b28-fc26-32c3-9cc1-e58570539f71 | -15.1069 | -48.00949 | 2025-09-12 00:09:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| cb6b71e3-d3ee-3b6f-9e42-8f71b37cef1b | -19.88297 | -41.41826 | 2025-09-12 00:09:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 96a2a897-1cc2-3b3d-bc93-1e28bcbd1187 | -19.82092 | -45.00532 | 2025-09-12 00:09:00 | TERRA_M-M | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 83bba83d-ec10-30c1-a4fb-85387ab5864d | -18.12257 | -51.72926 | 2025-09-12 00:09:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 8c516e94-b15d-366c-9080-3e4738023f9f | -20.27904 | -42.1203 | 2025-09-12 00:09:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| dd76f7f5-4fcc-34d2-85ba-45c88c1af623 | -20.40106 | -42.20825 | 2025-09-12 00:09:00 | TERRA_M-M | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| fb29617b-0073-3989-91af-5de955d5f66b | -16.42444 | -45.69032 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 6d554c31-1bc0-33a7-a85b-55a111c26447 | -18.61777 | -48.25625 | 2025-09-12 00:09:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| faf9199a-37f7-3420-a47d-913f26c819f6 | -22.78774 | -47.80396 | 2025-09-12 00:09:00 | TERRA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 9fcb23ed-9a06-3832-890c-8d5f10a69091 | -20.41641 | -41.62823 | 2025-09-12 00:09:00 | TERRA_M-M | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 21c41a80-f37c-336d-aac7-93cfc1b832f0 | -20.39746 | -49.13987 | 2025-09-12 00:09:00 | TERRA_M-M | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 06f242b4-fc14-354b-af66-8cf0af839e31 | -17.33984 | -46.67076 | 2025-09-12 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d9b9121e-e56e-36ee-8481-4790feb25999 | -14.18583 | -46.19898 | 2025-09-12 00:09:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| bd5d6a4b-914f-3463-9899-5269c3ef5968 | -13.3202 | -44.10052 | 2025-09-12 00:09:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| f5ccae29-44ea-3666-a200-e09534b528ed | -20.39484 | -49.11119 | 2025-09-12 00:09:00 | TERRA_M-M | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.5 |
| 3c9874de-c9d3-3a2d-bc23-230559c8af25 | -16.437 | -49.05547 | 2025-09-12 00:09:00 | TERRA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 319f273a-f918-31b0-9fb5-a9be22309c6d | -23.10895 | -47.52066 | 2025-09-12 00:09:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| a787bff3-24ca-3a8c-8bee-b920ca6ecea7 | -15.69248 | -47.01991 | 2025-09-12 00:09:00 | TERRA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 78882635-dc24-3b8b-a05b-e53f79094f12 | -15.56067 | -41.79781 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 472d5576-b3cb-33aa-a24b-ea22234b440a | -18.0581 | -45.44812 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 75b4a8cc-e5e9-3e8d-aea1-efbb5b3d95a2 | -23.11422 | -47.4889 | 2025-09-12 00:09:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| ec9fb224-cb14-3daa-bbe2-78ad701325f8 | -16.41209 | -45.67797 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6db0d165-c307-37a9-b3d0-8fe26ecdfe3e | -14.17505 | -46.19998 | 2025-09-12 00:09:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4894ee48-f3c8-36fa-8ec1-53692d2bac94 | -20.86596 | -46.51043 | 2025-09-12 00:09:00 | TERRA_M-M | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 31.7 |
| cb65def1-742f-30e8-a89a-802189fccc79 | -13.89473 | -48.24177 | 2025-09-12 00:09:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 527a4975-6829-3dba-aebc-099fea76a3d7 | -17.94082 | -46.92982 | 2025-09-12 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e28286c0-eefe-3351-90c3-31a6ff0939e5 | -19.99861 | -46.9205 | 2025-09-12 00:09:00 | TERRA_M-M | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 8e2f7594-a0b8-34b3-abbd-0edf57609d05 | -18.13838 | -51.7326 | 2025-09-12 00:09:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 2abf0ae3-5dd6-33cd-8905-53f9f95e6e5c | -15.69004 | -47.03117 | 2025-09-12 00:09:00 | TERRA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 39.3 |
| ab54c80e-7cc0-3064-8f92-db14981a4df3 | -15.69185 | -47.04734 | 2025-09-12 00:09:00 | TERRA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 37bb2edf-984c-3379-bb74-f61a1721b9e2 | -14.37337 | -47.28639 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f85f0d0e-3ace-3b6b-895c-0cfba2b1b3e7 | -22.79616 | -47.82174 | 2025-09-12 00:09:00 | TERRA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 88.6 |
| d908e162-5bdf-3a1f-b9b5-9875cea7884b | -14.04285 | -42.14671 | 2025-09-12 00:09:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 30425441-b7f8-37f8-9108-ad6fd3176992 | -15.67898 | -40.98836 | 2025-09-12 00:09:00 | TERRA_M-M | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| e5dc728c-6d8f-3d94-b75a-13dba46ce3cc | -16.42884 | -49.03567 | 2025-09-12 00:09:00 | TERRA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| d2b777da-34a4-30fb-a420-92b229990b7b | -14.41235 | -47.3142 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 72cffeeb-2e3a-3f9f-8f53-2327619243f1 | -15.1091 | -48.02912 | 2025-09-12 00:09:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| f5716983-e6e6-318b-aca7-64320b40becb | -13.25893 | -43.76417 | 2025-09-12 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ba0069ae-a5a0-3a13-a362-a16cc2da524b | -21.64656 | -50.12279 | 2025-09-12 00:09:00 | TERRA_M-M | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.5 |
| 25c4247a-286a-3656-84b9-ff5bff313a7b | -21.32238 | -45.0302 | 2025-09-12 00:09:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 7ca9911d-938f-3306-8211-e87785dc4016 | -14.44473 | -47.32077 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fa63ac8f-abdb-335e-8eab-3be1a9db78c8 | -15.87973 | -48.17169 | 2025-09-12 00:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 20f32939-1587-3c2e-825b-51fefcf6061f | -19.16099 | -48.01372 | 2025-09-12 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 3900d592-e3b1-3614-9525-cb15353b97c9 | -13.95876 | -48.22662 | 2025-09-12 00:09:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6072543d-fb19-315e-818d-6b73899c1ceb | -20.27072 | -45.53616 | 2025-09-12 00:09:00 | TERRA_M-M | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 3c02ec75-0d52-39e0-a3d6-540c03c0798e | -18.65959 | -47.66538 | 2025-09-12 00:09:00 | TERRA_M-M | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 9069d8de-20fa-32e2-97ef-e9e5b03b1379 | -19.63783 | -41.58116 | 2025-09-12 00:09:00 | TERRA_M-M | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |


[Clique aqui para ver as próximas entradas](README3.md)
