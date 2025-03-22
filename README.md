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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49f102dd-4974-3367-8d98-724363f7debc | -20.22178 | -46.68554 | 2025-03-22 00:20:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 667ba965-df9c-31b3-8112-35102d1ef08a | -19.65187 | -40.18789 | 2025-03-22 00:20:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| ef407c50-f505-323b-bb48-6a62f8ed18a2 | -14.15298 | -42.85152 | 2025-03-22 00:20:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| ee5d4910-d77a-381f-a343-4dc74933f725 | -16.03787 | -40.80593 | 2025-03-22 00:20:00 | TERRA_M-M | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| b1bc374a-047a-3d94-9d67-035f923f1a14 | -20.21931 | -46.66105 | 2025-03-22 00:20:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 28463758-98e9-3efd-b975-ae81744c2582 | -14.6892 | -40.50784 | 2025-03-22 00:20:00 | TERRA_M-M | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a5ccc6f1-da65-36c4-b54b-d0a2f1fe7b5e | -13.13559 | -40.20951 | 2025-03-22 00:20:00 | TERRA_M-M | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| d91526b4-e5b3-3aed-b8dd-d5826010139a | -9.71654 | -37.83704 | 2025-03-22 00:22:00 | TERRA_M-M | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 10.6 |
| dcaad232-f1d8-346f-bc6f-8f8b9d908922 | -12.36744 | -41.42657 | 2025-03-22 00:22:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b81dccb5-f9f9-3cdf-9815-585e6459ee59 | -11.91785 | -41.23249 | 2025-03-22 00:22:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5dfafa81-b04f-3ca8-9805-ac8ce92aeb1f | -8.27115 | -39.12647 | 2025-03-22 00:22:00 | TERRA_M-M | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 16.6 |
| e507d009-7ec9-36c1-a27c-ccfeb16ed1a1 | -8.26121 | -39.12796 | 2025-03-22 00:22:00 | TERRA_M-M | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c735e1ee-8927-34a3-8364-32985e9e89df | -7.06652 | -35.06477 | 2025-03-22 00:22:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 97.6 |
| 287c6bdb-12a4-339a-99fb-a789515eb0dc | -7.06272 | -35.04071 | 2025-03-22 00:22:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 33.3 |
| ab14dfac-748a-3292-8227-ac10151a7490 | -12.3687 | -41.43557 | 2025-03-22 00:22:00 | TERRA_M-M | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 3f6657c2-8474-3920-9ca6-e4baa4e3df63 | -12.41195 | -39.15636 | 2025-03-22 00:22:00 | TERRA_M-M | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| a7f39637-4877-3c62-b31e-b0b623364e79 | -14.1607 | -42.844799 | 2025-03-22 00:37:00 | METOP-C | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 74fb3c5e-d0a2-30d6-84f6-289a6bebb920 | -20.1404 | -50.714802 | 2025-03-22 00:37:00 | METOP-C | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31711fc0-695a-3cf3-8c04-a4bc0d3d399e | -20.2183 | -46.680302 | 2025-03-22 00:37:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 31dd6a30-8074-35ae-bb3b-255af99ed258 | -21.1731 | -53.0653 | 2025-03-22 00:37:00 | METOP-C | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 02de6d27-aeeb-3959-8230-3c067e35cd74 | -20.224899 | -46.662899 | 2025-03-22 00:37:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 054b4f12-b0db-326f-ae36-f12a9983df81 | -20.2265 | -46.670502 | 2025-03-22 00:37:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c85aa3e0-0347-32df-94dd-beda59a713db | -12.3732 | -41.423801 | 2025-03-22 00:37:00 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a1931f48-d933-3e68-b6d3-4546c70538f7 | -20.180799 | -46.696999 | 2025-03-22 00:37:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 68f0fd9c-a747-3e8a-9193-f3d6216d9d28 | -20.1824 | -46.704498 | 2025-03-22 00:37:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3ab03df6-8e7b-3ee4-b1b8-b17172419c8f | -20.2167 | -46.672798 | 2025-03-22 00:37:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 38d36e5e-061a-3186-ba69-f131a28f5210 | -22.719299 | -55.5751 | 2025-03-22 00:37:00 | METOP-C | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0ff4b76-826e-357b-8662-3795cdf38825 | -20.1425 | -50.7262 | 2025-03-22 00:37:00 | METOP-C | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 12c6a8c6-a49d-372e-a9e1-a9ad359bd6a5 | -22.715401 | -55.5495 | 2025-03-22 00:37:00 | METOP-C | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8d3c2a05-04cc-35a2-b473-f68342812a8a | -20.2199 | -46.687801 | 2025-03-22 00:37:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f5b8bbbc-a438-3255-95b9-27194b8931c4 | -22.7356 | -55.571201 | 2025-03-22 01:27:00 | METOP-B | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2e4bcde2-30c8-3df5-b59b-e8db08b17c66 | -22.732401 | -55.558498 | 2025-03-22 01:27:00 | METOP-B | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e1485dd5-df02-3e7d-9e3d-4fd5ad70d275 | -9.71516 | -37.83771 | 2025-03-22 02:58:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0aaf6ed3-f750-3e00-b595-a4c8aae8cd5e | -8.39002 | -35.02814 | 2025-03-22 02:58:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5cf21400-0402-3647-98ac-767ac3921887 | -4.90391 | -37.4296 | 2025-03-22 03:21:00 | NPP-375D | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e768c7d2-93fe-3954-985f-89adeb6ecc69 | -4.67232 | -38.06152 | 2025-03-22 03:21:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e37488f9-3bcc-39e1-9641-bda99c9fbbfa | -4.67274 | -38.0606 | 2025-03-22 03:21:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 681e6884-3a8f-357b-88a6-e4c086913cf8 | -9.71338 | -37.8372 | 2025-03-22 03:23:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0fb44af5-7f66-307b-9245-d8dda97e6f01 | -8.90963 | -37.84242 | 2025-03-22 03:23:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2bd9052d-ad29-3706-94d4-47e18be94b0c | -7.47547 | -34.84296 | 2025-03-22 03:23:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 95a018d1-6e15-3f34-8102-3bf0ef595fbe | -8.81415 | -38.92472 | 2025-03-22 03:23:00 | NPP-375D | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fec48d47-ffcf-36ea-8c9a-929bad86cf67 | -11.62145 | -38.05244 | 2025-03-22 03:23:00 | NPP-375D | ACAJUTIBA | BAHIA | Brasil | 2900306 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a1fb445-c898-34f2-ab6d-fbc35b99cd06 | -8.81322 | -38.9283 | 2025-03-22 03:23:00 | NPP-375D | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5a220e89-3196-33bf-b6f1-5c7edfa6dcf2 | -7.22215 | -35.61341 | 2025-03-22 03:23:00 | NPP-375D | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| be24ac97-dbc8-3fa3-bc18-d57794b6feea | -8.07358 | -34.97641 | 2025-03-22 03:23:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 270bedc6-56a1-3f51-8d2b-9047f0ef039a | -12.3622 | -41.42542 | 2025-03-22 03:25:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fc059aab-4807-3f9c-a793-3d887d7e1577 | -13.24945 | -41.33088 | 2025-03-22 03:25:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4a167544-bbb7-36e1-a676-a62a748a852c | -19.83172 | -40.11261 | 2025-03-22 03:25:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0d0986b8-059b-3f55-b626-beaa55c16dac | -13.28913 | -39.1688 | 2025-03-22 03:25:00 | NPP-375D | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99d86001-e56b-375d-b6d9-6520c86332ee | -13.25482 | -41.33185 | 2025-03-22 03:25:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| b179152b-97f7-3777-b34e-e4413589a348 | -12.35672 | -41.42436 | 2025-03-22 03:25:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d39cf4e8-1c6a-3fb4-9bff-f9e5c59bc761 | -13.25416 | -41.33514 | 2025-03-22 03:25:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 8b780221-f82c-397c-9726-e68e53e51d3f | -15.42988 | -39.47642 | 2025-03-22 03:25:00 | NPP-375D | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f8235c21-ed93-32d7-b765-e4c620b76d19 | -13.25349 | -41.33854 | 2025-03-22 03:25:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 66ae5a29-cfc4-3469-9096-d5f4d6696d50 | -13.24878 | -41.33426 | 2025-03-22 03:25:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 95a98122-b273-3748-a30c-24b662b8a6c9 | -20.21924 | -46.68063 | 2025-03-22 03:28:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9eccc5f-5669-3ecd-b858-863c0481d27d | -20.22541 | -46.68341 | 2025-03-22 03:28:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc4f1fe5-ef3b-3bd1-8657-1c20bcacd34e | -20.22074 | -46.67432 | 2025-03-22 03:28:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb45488e-6329-326c-88ec-8b1da45b2810 | -20.22679 | -46.6776 | 2025-03-22 03:28:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4db23e8-ffe8-362f-a69e-1699fe2f523f | -27.74045 | -50.42524 | 2025-03-22 03:30:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 964391eb-00e5-38c1-ac95-7187b70ddceb | -27.73933 | -50.42554 | 2025-03-22 03:30:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0892eff5-0600-36ef-b221-621d57322082 | -28.93899 | -51.40213 | 2025-03-22 03:30:00 | NPP-375D | NOVA ROMA DO SUL | RIO GRANDE DO SUL | Brasil | 4313359 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8f22de32-ef20-32c5-a46f-c591fed020db | -29.52114 | -50.68064 | 2025-03-22 03:30:00 | NPP-375D | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 49049368-9e96-3964-852f-073a39c8915e | -27.73385 | -50.4228 | 2025-03-22 03:30:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| acd6cc6d-4beb-3d0d-b6b2-d901d662258d | -29.51792 | -50.6782 | 2025-03-22 03:30:00 | NPP-375D | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 92558486-e5c7-3085-9acf-f4e3c083f3c1 | -27.73274 | -50.42309 | 2025-03-22 03:30:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a892f598-0818-3649-b3ba-227e11b2eaea | -8.81208 | -38.92518 | 2025-03-22 03:47:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| d3db532b-abed-3426-83e9-69a2838d3fcc | -8.07242 | -34.97601 | 2025-03-22 03:47:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ecd4449-d6b4-39b9-8192-5ac929106cd6 | -8.81149 | -38.92886 | 2025-03-22 03:47:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 93f867ec-128e-3a4b-98df-0eaae727277f | -9.78302 | -37.0123 | 2025-03-22 03:47:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f198991a-d31d-3868-9a6c-a53f21594f01 | -4.90581 | -37.42855 | 2025-03-22 03:47:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 47a40f22-256f-3ccc-987d-a854c10aa738 | -9.7108 | -37.83688 | 2025-03-22 03:47:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cfd8d53-a29c-3b27-9c80-b73fd512246f | -9.78578 | -37.01632 | 2025-03-22 03:47:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 792f900b-a588-3cd9-8c03-40d9b004ef6e | -8.39098 | -35.02304 | 2025-03-22 03:47:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 18c8cc05-e3db-3ac6-a41a-c653891e8c48 | -8.87684 | -36.52927 | 2025-03-22 03:47:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e3fa8298-9b9d-3d5a-b566-9f4833fe8e64 | -8.17004 | -34.97916 | 2025-03-22 03:47:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7a136810-eff4-3a2a-8c7c-35c94d30af64 | -7.47653 | -34.84147 | 2025-03-22 03:47:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 48b10502-efb0-33a1-bd51-70c3ed58f913 | -7.22724 | -35.7816 | 2025-03-22 03:47:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84309c9b-11be-3059-94fc-2099c9065d27 | -4.67166 | -38.05851 | 2025-03-22 03:47:00 | NOAA-20 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| be824eb2-5a8d-3ac2-92fe-fb28eb8ed7e7 | -9.71411 | -37.83741 | 2025-03-22 03:47:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 442cab3d-3f44-3dbf-ba33-d5b56ca1d0a1 | -10.41265 | -36.82798 | 2025-03-22 03:47:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f83008d6-fcc4-3e4a-8dcd-0f10d8d14540 | -13.25527 | -41.33698 | 2025-03-22 03:47:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 593905bc-6ca0-345b-80c7-ad6ca648c336 | -13.25239 | -41.33219 | 2025-03-22 03:47:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| ae5c4f31-2b71-3464-89ec-4e2368e4435a | -16.03563 | -40.80644 | 2025-03-22 03:47:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2907941f-0169-362b-b109-779cdf9c1572 | -14.11789 | -41.67751 | 2025-03-22 03:47:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 327094eb-3351-3303-bfe8-8c24f4a2296d | -14.13383 | -41.69291 | 2025-03-22 03:47:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 91806799-dc2e-39a9-8afc-afced092c325 | -15.42991 | -39.47522 | 2025-03-22 03:47:00 | NOAA-20 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8292f2d0-d258-3715-950d-1fdd30bb172c | -13.25169 | -41.33636 | 2025-03-22 03:47:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 24fa1cf5-c90b-3a21-8832-ab0bacb3f3a8 | -13.28703 | -39.17093 | 2025-03-22 03:47:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e6b3e125-b582-31ff-aaa4-8ece2fd3dc55 | -13.25597 | -41.33284 | 2025-03-22 03:47:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 3f6a27a7-bb6c-3683-8ef9-675c714b78b1 | -13.20481 | -40.49178 | 2025-03-22 03:47:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9de15e04-ad7e-3d27-b732-0f7279375020 | -12.8041 | -40.39054 | 2025-03-22 03:47:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d7d385dd-5651-35dd-bef4-9dd9074fccaf | -15.36647 | -39.49016 | 2025-03-22 03:47:00 | NOAA-20 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a027a79d-147c-376a-9e2a-e5f146180ca4 | -13.28761 | -39.16735 | 2025-03-22 03:47:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d4ee565e-cd59-3bb7-b298-a4fbe7c6ddee | -12.29979 | -41.31235 | 2025-03-22 03:49:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 44279985-8bb4-3f30-a37e-636f056e9c3c | -11.62056 | -38.04944 | 2025-03-22 03:49:00 | NOAA-20 | ACAJUTIBA | BAHIA | Brasil | 2900306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 516280b5-2ecd-32d9-aa11-4de11d8ff49d | -12.36506 | -41.43433 | 2025-03-22 03:49:00 | NOAA-20 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eb5de290-8295-3aa1-b229-70815a433f68 | -12.41598 | -39.15581 | 2025-03-22 03:49:00 | NOAA-20 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0f371e1d-51af-3f22-9826-f58720ed6378 | -12.35923 | -41.42439 | 2025-03-22 03:49:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1c05d9e2-6ded-3008-a42c-cf0198546eb1 | -12.36869 | -41.43505 | 2025-03-22 03:49:00 | NOAA-20 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
