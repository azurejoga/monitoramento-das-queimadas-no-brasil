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
| dc5630c6-735c-3449-a3ed-10f68bc727e7 | -19.7334 | -55.399899 | 2025-01-01 00:35:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e92cb13b-b8f2-348f-8473-e8ece719807c | -12.2198 | -49.323898 | 2025-01-01 00:35:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74aa7f04-28e2-3119-b5a3-9bcb69959dab | -12.2181 | -49.316601 | 2025-01-01 00:35:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb7b7d6d-a17d-3fb5-a2c9-ea54113aee33 | -19.731001 | -55.386799 | 2025-01-01 00:35:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5bf6daca-b4bf-3aea-ac83-01715532beb8 | -15.2145 | -60.173901 | 2025-01-01 00:38:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76a6d214-702e-3d29-9315-a5c33fa5ce23 | -15.209 | -60.198799 | 2025-01-01 00:38:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27218493-f7ae-3500-b51e-cab52e4c35b0 | -12.2099 | -49.326199 | 2025-01-01 00:38:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efa4e37d-11b7-347a-8086-596eb0bff731 | -12.2082 | -49.318901 | 2025-01-01 00:38:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db79d61f-e253-3486-855c-5251d061a01b | -15.2187 | -60.196999 | 2025-01-01 00:38:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4210d1e6-95b1-3886-a3cd-fca1ac433aef | -19.721201 | -55.388802 | 2025-01-01 00:38:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e5d1d582-7c97-3ce0-9780-668a6e706b92 | -19.7236 | -55.401798 | 2025-01-01 00:38:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ad5c4f45-c1a1-34a4-a121-2c22dcdad3bb | -11.7592 | -49.339699 | 2025-01-01 00:38:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e31e38e-d60d-3441-95db-3c2dcdfa09d3 | -15.2048 | -60.175701 | 2025-01-01 00:38:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da30218f-a831-3b70-86d6-8e52d9794771 | -23.0883 | -55.49762 | 2025-01-01 01:24:00 | TERRA_M-M | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| c6d9b630-767d-3af4-8500-67aacb16514b | -19.76626 | -55.39889 | 2025-01-01 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 784654f3-f2a8-3a88-9d67-3ba2b26f5d6c | -19.76756 | -55.40836 | 2025-01-01 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 32e63ff6-e765-36bb-934a-e1144bb1d8e5 | -15.16664 | -56.47333 | 2025-01-01 01:26:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aeadfe43-a7fb-3de7-a491-e6eb22085ff5 | -14.70648 | -56.81359 | 2025-01-01 01:26:00 | TERRA_M-M | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7af484c6-1c7c-38e4-a0a7-06700c4aefee | -15.39117 | -59.88623 | 2025-01-01 01:26:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 835e067e-6964-3214-8dfb-ea892e2a8ec8 | -15.16539 | -56.46412 | 2025-01-01 01:26:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 216bd961-473d-34d6-b374-0b42a379a94d | -19.8172 | -57.466801 | 2025-01-01 01:36:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 20607054-3e5a-3570-8d88-bb96c1bc7258 | -15.2405 | -60.205399 | 2025-01-01 01:36:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 540bf125-1abf-3746-a3b1-f99c7248a3eb | -15.2421 | -60.212399 | 2025-01-01 01:36:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1fbd369-9e18-32bf-847a-7d2110e742c7 | -15.3737 | -59.882599 | 2025-01-01 01:36:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32e1e7be-5b5e-3ec1-9f64-be5b001e8ab7 | -15.2437 | -60.219501 | 2025-01-01 01:36:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db9e8f34-37d5-34c5-90a6-db180904e01f | -11.9759 | -63.964699 | 2025-01-01 01:36:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 87f9b343-c9b8-3146-9585-d36b19d64daa | -9.2149 | -60.3368 | 2025-01-01 01:36:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e44b2da4-6348-35a2-8459-c5c30f2c77e9 | -9.2165 | -60.344002 | 2025-01-01 01:36:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10f8dc16-53f4-3a4c-b33a-ac3a363db516 | -23.0709 | -55.499001 | 2025-01-01 01:36:00 | METOP-C | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 153743cc-4881-3d4a-b409-8cc779a1f321 | -14.6867 | -56.819302 | 2025-01-01 01:36:00 | METOP-C | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f60a17c8-ceb9-3793-b0df-c72542398c6d | -15.3655 | -59.892101 | 2025-01-01 01:36:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a5180a4-84e4-3c30-8eb2-cbb180d41e8b | -15.2519 | -60.210098 | 2025-01-01 01:36:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4321dc36-b773-3e6e-9208-47706304662f | -19.751301 | -55.4081 | 2025-01-01 01:36:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dada040c-db7d-31ea-b34a-f183bc627f13 | -15.3753 | -59.889702 | 2025-01-01 01:36:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47502e64-bec7-323a-8bea-c38e2b08a1d8 | -11.9776 | -63.972698 | 2025-01-01 01:36:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 924b1459-0daa-3af6-95f3-d004a39fd514 | -6.02204 | -38.04951 | 2025-01-01 02:57:00 | NOAA-21 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eb445baa-9166-37d1-a20b-2a28bfb17081 | -6.02325 | -38.04303 | 2025-01-01 02:57:00 | NOAA-21 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3e6aef86-3865-34eb-8bb2-1d9069e41e6f | -6.01855 | -38.04906 | 2025-01-01 02:57:00 | NOAA-21 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4ba59fe2-1ed1-3592-a921-bee4c8c9db19 | -10.29931 | -37.53892 | 2025-01-01 03:00:00 | NOAA-21 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a31e5a12-a1c1-3ff4-b54e-0f9e08e74f53 | -8.02585 | -35.06974 | 2025-01-01 03:00:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 78cc181c-a8a2-3cb8-abf2-fbc2d16466bf | -8.02507 | -35.07385 | 2025-01-01 03:00:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9174030b-6eba-31f5-9c18-97d04d00b08e | -8.81294 | -35.12532 | 2025-01-01 03:00:00 | NOAA-21 | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 127bb6c9-5fbf-33d0-b59f-dd6041687a84 | -10.29284 | -37.53773 | 2025-01-01 03:00:00 | NOAA-21 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 40da4177-0e8f-3258-a274-47235481e4f5 | -8.20753 | -35.4758 | 2025-01-01 03:00:00 | NOAA-21 | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 814163c7-7439-30b5-bc1c-d50e3c857d25 | -12.30884 | -37.88919 | 2025-01-01 03:00:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 136e10a7-8a12-38a5-b02a-56f9cfd0ac65 | -12.30992 | -37.88391 | 2025-01-01 03:00:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9b5d02d7-5eaf-35ff-ad28-af5dc5c3123a | -8.81223 | -35.12908 | 2025-01-01 03:00:00 | NOAA-21 | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 6edf071d-7baa-3854-9b82-81db20452805 | -8.02482 | -35.07248 | 2025-01-01 03:00:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fdefd04e-7403-37b5-a0fd-980dbd12b542 | -5.18693 | -37.63774 | 2025-01-01 03:21:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e2ddad7a-5d0d-3f83-b760-ce0ae0b56b9f | -5.10517 | -38.02562 | 2025-01-01 03:21:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 675bc4af-f6b2-3316-8cf7-18e3c445220b | -3.82089 | -38.47887 | 2025-01-01 03:21:00 | NPP-375D | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0e04c499-c5ad-3bd7-9ffc-efc87e7ad98b | -3.82139 | -38.47586 | 2025-01-01 03:21:00 | NPP-375D | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f3a0f371-af0c-3bb5-ab42-9ac4f91557a7 | -5.10791 | -38.02441 | 2025-01-01 03:21:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f747bd3-7aee-367b-ad61-cdad4dfff9e8 | -4.37375 | -39.05716 | 2025-01-01 03:21:00 | NPP-375D | ARATUBA | CEARÁ | Brasil | 2301406 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 465e9e63-ddd9-3fef-943e-1725ee29ac2d | -4.3744 | -39.05329 | 2025-01-01 03:21:00 | NPP-375D | ARATUBA | CEARÁ | Brasil | 2301406 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ce3500fb-21d7-37e8-a310-b24ef353bf40 | -6.81806 | -34.91558 | 2025-01-01 03:23:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d0b47418-f947-3adf-9621-4e9cd600b66b | -9.87745 | -40.29245 | 2025-01-01 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ec14a4a7-3be3-36c3-8764-669ef445debc | -6.81667 | -34.91835 | 2025-01-01 03:23:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| febf7628-97eb-3f38-865f-5abe64087754 | -6.01846 | -38.04509 | 2025-01-01 03:23:00 | NPP-375D | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4aa21b1d-3e1c-3e6c-91a0-900802a4d42d | -8.81273 | -35.13062 | 2025-01-01 03:23:00 | NPP-375D | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e1c20225-554c-36b5-aac3-acddab7fcc8e | -10.29644 | -37.54002 | 2025-01-01 03:23:00 | NPP-375D | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cfcf2bbc-a29d-3cdb-b216-a74b1dfd6de3 | -6.81281 | -34.91771 | 2025-01-01 03:23:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| deb2c26d-a8d6-346d-83ac-5a78e80f9f1b | -7.5399 | -35.31693 | 2025-01-01 03:23:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ed88d42-15d8-3b57-af79-fbc8ab2cddc4 | -8.36047 | -35.19945 | 2025-01-01 03:23:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 57e029d7-f53d-3dc8-b83e-4d4140707b74 | -7.37649 | -34.88549 | 2025-01-01 03:23:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e23b42dc-a50d-3d20-859e-050365a0f087 | -8.81349 | -35.12602 | 2025-01-01 03:23:00 | NPP-375D | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fee0e84d-055f-39e0-ac5d-907a6d5171ca | -9.28784 | -40.44586 | 2025-01-01 03:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 95117254-7659-35cd-9f36-4265cc7f7ada | -5.60703 | -35.63861 | 2025-01-01 03:23:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e3c04c13-aa2d-3f39-8e44-9fa4328db33a | -10.74947 | -37.20568 | 2025-01-01 03:23:00 | NPP-375D | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 29a33946-d35b-38ac-a61c-2535cb0a9879 | -8.21021 | -35.4777 | 2025-01-01 03:23:00 | NPP-375D | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f07113c5-2563-3e87-b945-9dbd68718c3c | -10.80224 | -36.91056 | 2025-01-01 03:23:00 | NPP-375D | BARRA DOS COQUEIROS | SERGIPE | Brasil | 2800605 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 06871a39-e1c0-38c1-ade1-18d0290a81ec | -6.75544 | -39.13791 | 2025-01-01 03:23:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 15097445-b10d-3fa9-a20d-290f2d9554bd | -9.29317 | -40.44685 | 2025-01-01 03:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 94f6bce1-03d1-3de4-a8e5-3d3114e156e7 | -8.21104 | -35.47272 | 2025-01-01 03:23:00 | NPP-375D | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8aee8b29-bef1-3ea1-9ae3-c8881fe6697c | -6.75491 | -39.14089 | 2025-01-01 03:23:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7dfdebe8-a25b-38c6-a289-ebb75a13e6aa | -8.8097 | -35.12537 | 2025-01-01 03:23:00 | NPP-375D | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c4600d10-d98b-389a-b59d-e00918301409 | -6.81421 | -34.91494 | 2025-01-01 03:23:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 98beebc7-c6a2-36dc-8621-c72031cfa12e | -10.29718 | -37.5359 | 2025-01-01 03:23:00 | NPP-375D | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6ff7b85f-8aad-38ff-b17e-faba5393e0cf | -8.0258 | -35.07198 | 2025-01-01 03:23:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c7a76e2e-7416-3647-bde1-2adb6fa622c0 | -6.76053 | -39.13886 | 2025-01-01 03:23:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 88ac1b00-0c7f-3cbd-b4ce-000aee25f6d3 | -6.0233 | -38.0457 | 2025-01-01 03:23:00 | NPP-375D | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9d2f43bd-b886-3132-9a0a-cd30fc72d252 | -9.29098 | -40.44501 | 2025-01-01 03:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 85663207-e4c7-3af4-a5a9-826ae26e73e9 | -9.29037 | -40.44837 | 2025-01-01 03:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c8de4c8f-e872-313d-9dd0-172c539b3e62 | -5.60532 | -35.6375 | 2025-01-01 03:23:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 95b0e4c8-9a6d-351c-9d4f-3166fd408660 | -11.96934 | -41.33546 | 2025-01-01 03:25:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fc19796f-33e9-3804-af84-c24c168b2a36 | -10.60736 | -44.32645 | 2025-01-01 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ec6c842-8a11-376e-9989-c2f4ccc594a8 | -10.6128 | -44.33382 | 2025-01-01 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b3b2e39-573b-3370-b1c1-c8c3f85c75ae | -10.61149 | -44.32312 | 2025-01-01 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2818fb35-dca8-315d-9d32-f89dd386641a | -10.6062 | -44.33234 | 2025-01-01 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f7d2a0a-5dd6-39ed-a5ef-5351631cfcfe | -10.61395 | -44.32795 | 2025-01-01 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 794af284-4747-3b39-b078-dfd9e1818773 | -10.6103 | -44.32895 | 2025-01-01 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f954916c-62d1-3970-9a4d-cc0cda5de220 | -11.96463 | -41.3309 | 2025-01-01 03:25:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7e189920-473a-3f35-80e7-80ed609d0919 | -10.60911 | -44.33484 | 2025-01-01 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 818e7be1-e02e-32c8-9ee6-78763885a571 | -15.77949 | -38.95957 | 2025-01-01 03:46:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2855d560-b1e7-3024-8313-375638a26373 | -3.55574 | -40.84174 | 2025-01-01 03:46:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 54d332b0-f1cb-3ee9-a6c9-2c791e3b1708 | -6.23712 | -39.62178 | 2025-01-01 03:46:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d3367c27-70c3-36b6-a713-1149ccb12a8d | -7.91495 | -38.47624 | 2025-01-01 03:46:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| de51a3fc-4a28-3883-bb5f-68b06ff1d706 | -11.95326 | -38.96971 | 2025-01-01 03:46:00 | NOAA-20 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e2be799b-3ee7-36c6-b23a-c73493130a0e | -3.97636 | -40.85413 | 2025-01-01 03:46:00 | NOAA-20 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72391b93-43ce-39f7-8d12-6cb6f011c89b | -3.89883 | -38.35232 | 2025-01-01 03:46:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README2.md)
