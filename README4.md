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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c319ac8-1ae4-346e-a288-995171452334 | -12.84818 | -38.24342 | 2025-02-15 04:23:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 99f4b330-69c0-31ad-874f-aa93bc636a16 | -10.78366 | -40.3105 | 2025-02-15 04:23:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7cacae8-c162-3e9e-8222-1c3e290fec34 | -8.72024 | -44.00674 | 2025-02-15 04:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4d3ee937-9ed2-3806-b287-cc3aa2ed1f02 | -10.609 | -45.10482 | 2025-02-15 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 718f07c7-b51b-3ca6-8afa-e0619cc4ebc3 | -10.54778 | -45.2216 | 2025-02-15 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 37dd16b8-2e96-3199-a4f5-280640945986 | -10.61179 | -45.10889 | 2025-02-15 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ecc95d83-397b-398b-af3c-dcbdc205e0c3 | -15.46777 | -42.14516 | 2025-02-15 04:23:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b243faac-cb60-3236-b1c1-9b09bef7a3e0 | -14.28043 | -47.41265 | 2025-02-15 04:23:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f510a71e-5525-3fef-a393-b9f7bb47c7b2 | -22.67399 | -42.85675 | 2025-02-15 04:23:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b45498ec-2644-3139-b252-0be728ad38b9 | -16.58566 | -46.78738 | 2025-02-15 04:25:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f304a77-3dcc-35e0-8129-859a8546f737 | -18.04511 | -43.23487 | 2025-02-15 04:25:00 | NPP-375D | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f09af9ba-8e7b-3052-9576-908b1208d6d6 | -21.78933 | -57.48713 | 2025-02-15 04:25:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77e2166a-e3bc-3dbe-b689-0f00469a9749 | -21.07412 | -56.38951 | 2025-02-15 04:25:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a23144e-20ae-385f-9fbc-e5f435cb1db9 | -25.2082 | -50.581 | 2025-02-15 04:25:00 | NPP-375D | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5fadef56-cf57-38ce-8605-94781c812a87 | -21.07891 | -56.3905 | 2025-02-15 04:25:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd2f5004-89fe-3390-b972-46cbd5d37f66 | -18.35864 | -44.99308 | 2025-02-15 04:25:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd138aab-c533-3961-bf0d-f988b083c084 | -16.68702 | -43.00846 | 2025-02-15 04:25:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd958aec-aecc-342e-96b6-cf692369a951 | -23.63357 | -46.28757 | 2025-02-15 04:25:00 | NPP-375D | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7e16e6c0-537e-3c39-bfe1-25e8a394a35b | -16.99431 | -42.82947 | 2025-02-15 04:25:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a71a3953-4cdd-35d9-8f04-4118d4e1f7b7 | -24.22595 | -50.90702 | 2025-02-15 04:25:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| be67946b-f26d-3552-b156-f074c17846d8 | -21.79437 | -57.48831 | 2025-02-15 04:25:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7634fbd-b104-3712-a17c-029afcf8b8a9 | -16.99045 | -42.82883 | 2025-02-15 04:25:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f347abd-c0aa-300d-8b97-f2025715910f | -23.40505 | -46.55554 | 2025-02-15 04:25:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0c38a286-9c7a-3a8d-865e-8486a0d0d45f | -16.34925 | -43.69469 | 2025-02-15 04:25:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5747e0b-8651-38ff-80d1-f986024f1285 | -22.90093 | -43.75256 | 2025-02-15 04:25:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4bd482aa-6bbe-3c60-b8b3-9eed4561ac4e | -17.09452 | -43.80372 | 2025-02-15 04:25:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1add690-dbae-350e-b787-7205bfb44989 | -9.90299 | -38.10215 | 2025-02-15 04:44:00 | AQUA_M-M | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| cde41af8-c88d-391f-a8c4-ca4583db2965 | -8.131 | -43.14073 | 2025-02-15 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 507853a2-6b88-3d40-8f63-6f82033816d4 | -11.69323 | -43.92609 | 2025-02-15 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8eb7cc14-0cee-321a-a498-0f4d26ba2d9e | -11.69788 | -43.92973 | 2025-02-15 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb034639-f390-3aca-a1d3-ea5d8c803f31 | -8.13155 | -43.14289 | 2025-02-15 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa113ac6-f173-3d33-b670-b5569e68f340 | -10.54664 | -45.21816 | 2025-02-15 04:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9c30325-9da5-31dd-b95d-49a9d849590b | -11.57744 | -47.64312 | 2025-02-15 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcd43edf-a8d8-37ec-a988-6a73073c6705 | -11.69286 | -43.92904 | 2025-02-15 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc5d5469-cf1a-33ec-8636-8f2cb3474b32 | -9.98365 | -48.08542 | 2025-02-15 04:44:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7214ecd5-eb9e-307c-b055-fcceb44b1a82 | -10.54602 | -45.22282 | 2025-02-15 04:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1569626-f3b0-3aa7-ad59-0dbff7e9d413 | -9.90806 | -38.10587 | 2025-02-15 04:44:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7fe18e40-8e25-39a7-81f6-563ad966bc7a | -8.12651 | -43.14224 | 2025-02-15 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e98a52cb-97b8-3764-8db1-4b6323bc0a6a | -9.90725 | -38.11269 | 2025-02-15 04:44:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ba6e7507-0894-34a2-b3e0-411743f72e64 | -10.55054 | -45.22351 | 2025-02-15 04:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93e55df7-c21b-3be8-ae96-065224b10d0a | -8.1306 | -43.14373 | 2025-02-15 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ce3a9b34-b813-381c-af00-e9a25558663e | -12.35209 | -47.99437 | 2025-02-15 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7726d5a-68f4-3ba1-b211-b69e65d78e6a | -12.34472 | -52.47611 | 2025-02-15 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3713cfa8-ef80-3016-af01-18d21d523a8a | -12.34361 | -52.48314 | 2025-02-15 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cd494de-8f48-3152-98e1-c85767d29a22 | -14.47626 | -45.82539 | 2025-02-15 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46ad01a5-b34e-3a85-908e-87cc5c32269e | -18.35787 | -44.99117 | 2025-02-15 04:46:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d3a15b72-22c7-360b-a947-951299c5040b | -15.23368 | -51.45844 | 2025-02-15 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32ed2cae-bfec-3eb8-8e52-809bf978eaeb | -14.00441 | -52.15359 | 2025-02-15 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87adae50-979c-309f-89d8-79f817d44675 | -18.35751 | -44.9943 | 2025-02-15 04:46:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8a135fc7-1b4e-35fd-8650-f732d204dc50 | -18.90559 | -45.0412 | 2025-02-15 04:46:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01638b3b-946f-3522-a79a-fc14ca254f25 | -12.34692 | -52.48368 | 2025-02-15 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 967cd7a5-7db6-3eae-9b9a-0cbe638dc3a0 | -12.3403 | -52.4826 | 2025-02-15 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d5469ec-68ec-3870-927e-e12ef6f27a6f | -15.23707 | -51.45898 | 2025-02-15 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d5c93ee-521c-335e-aba8-1c498ec0b869 | -12.33313 | -52.48503 | 2025-02-15 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1adb012c-f7fb-31f9-aa88-4bc356b2108e | -12.34417 | -52.47962 | 2025-02-15 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 095d13f5-1476-3f55-b92c-6153666a2c6e | -16.34848 | -43.69611 | 2025-02-15 04:46:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ff100a9-d5e9-3a07-8c90-da89b2ad5ee1 | -12.33258 | -52.48855 | 2025-02-15 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d008d334-4411-3bd6-b86d-7a25605c80f1 | -13.48231 | -44.02081 | 2025-02-15 04:46:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4ebb828-6193-33cb-b2f4-973ce54efca4 | -12.34086 | -52.47908 | 2025-02-15 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07924617-eb00-3a08-82c9-6715ffa3d264 | -21.10592 | -56.00224 | 2025-02-15 04:48:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ea9f4dc4-65a9-32ab-bdc3-83686c5a963f | -21.62437 | -55.97046 | 2025-02-15 04:48:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e47e3c42-5ad0-3314-a90e-fe50076cd56c | -21.07627 | -56.38787 | 2025-02-15 04:48:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d96bf60-f2e8-3157-9170-e7093d089399 | -19.50086 | -55.44797 | 2025-02-15 04:48:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.2 |
| 911af07e-587d-351e-a6d0-ddd64ad85662 | -21.22348 | -55.86625 | 2025-02-15 04:48:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ed959ce-1938-359b-8ebe-d98b3e2b9b0f | -21.011 | -55.85535 | 2025-02-15 04:48:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ac36ee74-6022-36d8-b974-5cd0748cf52a | -21.07534 | -55.80093 | 2025-02-15 04:48:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab37153c-5f48-3271-9eca-d922c414e804 | -19.50024 | -55.45173 | 2025-02-15 04:48:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.2 |
| 0544c1bc-eab9-35b3-8a62-3ebbde313e0b | -21.7927 | -57.48761 | 2025-02-15 04:48:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bf356c70-20e4-3141-a840-e63fd07f0823 | -21.84766 | -55.99978 | 2025-02-15 04:48:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a19c8a47-b894-3bc5-862a-5003d7a6c16c | -25.20547 | -50.58106 | 2025-02-15 04:48:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5a660aa4-15e8-37b3-bd76-1d7da95f63c5 | -23.40643 | -46.55952 | 2025-02-15 04:48:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 294c38ec-e18a-32da-9b69-962199c4cf06 | -20.99576 | -51.79379 | 2025-02-15 04:48:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d54170dc-330e-38a0-b579-f4250815ad65 | -21.88398 | -56.27067 | 2025-02-15 05:40:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b49ea897-8467-37fe-a922-eac04f42b684 | -21.79401 | -57.48736 | 2025-02-15 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b64da63e-715f-34b2-a9a3-66caeb0d00a4 | -21.87854 | -56.26593 | 2025-02-15 05:40:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49fb7b3c-b76a-3616-9a21-721a5fa285b4 | -21.79141 | -57.48679 | 2025-02-15 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75b55150-2b59-3807-a005-42aacdde6d09 | -14.1049 | -45.6634 | 2025-02-15 11:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 3d11d17c-0fe9-35cd-ac27-70f2fd2c98f5 | -14.1049 | -45.6634 | 2025-02-15 11:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5aef2f81-ef0f-30c0-99d4-47663e391c7e | -14.1239 | -45.6832 | 2025-02-15 11:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 342e0949-5487-3384-bb30-9faaa461c3b8 | -14.1239 | -45.6832 | 2025-02-15 11:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 9e711812-db00-35ce-90d3-d5baf77d6401 | -14.1239 | -45.6832 | 2025-02-15 11:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| cabe60b5-526e-373e-a61b-0e8fca62e9cc | -14.1239 | -45.6832 | 2025-02-15 12:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 80be96b3-abb3-3628-8133-08aaf58cfd4d | -10.59697 | -43.67055 | 2025-02-15 12:33:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3dadc3c6-ddb1-3f73-8a6d-b97b725ba21a | -9.22177 | -40.00231 | 2025-02-15 12:33:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| b84acbf1-f778-3d9d-8473-ab6ccabbb352 | -9.21546 | -40.00716 | 2025-02-15 12:33:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 6e0ac22d-d7f2-3282-87c4-563ebb8ec709 | -10.59448 | -43.66331 | 2025-02-15 12:33:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| a5f9eda6-39ef-3456-8639-2c7c8dadc1f0 | -9.92298 | -49.9155 | 2025-02-15 12:33:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 69d40e7e-39ed-3d63-b1e5-ef1f3f6b7edb | -10.59868 | -43.65797 | 2025-02-15 12:33:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 6fcaf3ab-fd2b-3acb-998e-01fe2b2177ac | -12.60312 | -45.066 | 2025-02-15 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 83a879a1-4850-3f1f-9239-9e51ae247223 | -12.32202 | -39.17209 | 2025-02-15 12:36:00 | TERRA_M-T | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 45.5 |
| 151d994a-d927-32e6-9cc8-d9e7738cd780 | -12.6046 | -45.05503 | 2025-02-15 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a233df4a-c81d-3b02-8eb3-ad00ba8424d7 | -14.47484 | -45.82008 | 2025-02-15 12:36:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| a08f9350-811e-3fe8-917b-3038b73ab21e | -12.59339 | -45.06462 | 2025-02-15 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a8b47ce8-22b1-3f5a-b8f4-1e2bb419cea7 | -12.59487 | -45.05364 | 2025-02-15 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 442ea5d2-4cfb-399e-a363-b1e59c382ded | -14.48437 | -45.82136 | 2025-02-15 12:36:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 589c44fe-b6a5-320b-ab83-6279b9d650e4 | -12.87888 | -43.97421 | 2025-02-15 12:36:00 | TERRA_M-T | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f5b0ece5-3951-3220-b3a8-d83edf9741a2 | -14.11418 | -50.27113 | 2025-02-15 12:36:00 | TERRA_M-T | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bcf3bec0-9792-35d4-91ed-bb170322110a | -19.00212 | -46.30114 | 2025-02-15 12:38:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c399f521-0129-3986-8570-cb049bd5839e | -15.73667 | -47.03775 | 2025-02-15 12:38:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 45e76f0b-c38c-39a5-bb3c-84ddc0137864 | -21.05242 | -52.33992 | 2025-02-15 12:38:00 | TERRA_M-T | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |


[Clique aqui para ver as próximas entradas](README5.md)
