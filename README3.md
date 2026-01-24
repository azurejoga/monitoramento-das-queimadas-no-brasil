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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5563c62e-2a9b-3e77-9532-b5b4e2ccd0e1 | -7.62515 | -35.09216 | 2026-01-24 03:53:00 | NPP-375D | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0683f4b5-fb10-3b6f-94f5-0030aa6965ab | -7.02036 | -40.14264 | 2026-01-24 03:53:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 880db7ab-41e2-38c1-910e-5cc19b93cde2 | -7.62226 | -35.08784 | 2026-01-24 03:53:00 | NPP-375D | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5bb9d02a-22cd-345d-aa84-75c7366775ec | -6.5471 | -35.19164 | 2026-01-24 03:53:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 75737908-8484-30c6-8a68-00d1b47eb6d2 | -6.08554 | -37.31669 | 2026-01-24 03:53:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f45423af-3e85-3160-b87b-480ea345818d | -15.55009 | -39.03785 | 2026-01-24 03:55:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 713e000b-2534-36b4-900c-2e2c2c79b745 | -9.81312 | -38.1079 | 2026-01-24 03:55:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c0436d80-f7fa-3a7a-b609-8d0a584b0159 | -10.11141 | -36.18326 | 2026-01-24 03:55:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 883ec588-f26c-300e-91cb-32f9cb436434 | -12.21874 | -38.94715 | 2026-01-24 03:55:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f2c8b51a-33e9-3bb4-92c9-c85692b69277 | -10.14784 | -36.40211 | 2026-01-24 03:55:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a8a07e43-916b-3d51-952c-fa7bdc991d80 | -12.6365 | -40.1777 | 2026-01-24 03:55:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4d732fd0-5a12-3a07-af50-ee18dc3be71c | -12.00638 | -38.4605 | 2026-01-24 03:55:00 | NPP-375D | ARAMARI | BAHIA | Brasil | 2902203 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6ac6dbbe-625c-3e12-ac67-8039a543ef1c | -11.98952 | -37.751 | 2026-01-24 03:55:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bcf43707-be93-39f1-af60-4ff89d6f65c1 | -16.72729 | -39.61303 | 2026-01-24 03:55:00 | NPP-375D | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9159d411-1cb6-3b4d-8464-811a3df16a89 | -11.56254 | -37.82375 | 2026-01-24 03:55:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| acb2ad20-cba0-384c-9b6b-6e324cb223d2 | -9.81368 | -38.1044 | 2026-01-24 03:55:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 88db5ce7-e3c5-31d4-aa88-70e6747f026e | -17.07955 | -39.46422 | 2026-01-24 03:55:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d00757dc-0348-321e-8a58-c25cc6dc6061 | -13.46626 | -41.33264 | 2026-01-24 03:55:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e94cf16-3103-33eb-949e-66cc2d9e7c4f | -12.03231 | -37.67425 | 2026-01-24 03:55:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 412e7634-c815-3e80-ad96-c93f8d4a312b | -19.5588 | -54.44422 | 2026-01-24 03:57:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4fbd711-55e7-3897-bc08-b2ad727fe4ab | -20.73449 | -48.81691 | 2026-01-24 03:57:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1a3d0dd3-e66e-3adb-add7-56fc12678ca5 | -20.4578 | -48.67882 | 2026-01-24 03:57:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 10ccab78-7a5c-3e7b-acb7-3d3f90a85307 | -18.25031 | -51.27691 | 2026-01-24 03:57:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fc5cd7ab-ad4c-3e0f-b01e-778408022142 | -19.56562 | -54.4465 | 2026-01-24 03:57:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7449619b-b754-3faa-b680-528ab6f60ba2 | -19.29379 | -53.17628 | 2026-01-24 03:57:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fcd90f5-645b-33f2-bb28-c90b1eec72ce | -20.72957 | -48.81582 | 2026-01-24 03:57:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fd3c72dd-e3bf-3238-95da-05cfc7b8d68c | -21.13766 | -48.66837 | 2026-01-24 03:57:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d2f2374e-50b3-3c34-a573-bf6404c51d5c | -18.24928 | -51.28148 | 2026-01-24 03:57:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a330b492-4d8d-32f0-82a1-5a95d2d0ccd1 | -19.56281 | -54.43977 | 2026-01-24 03:57:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ef4d241-a81c-3835-9022-2a70a81358c6 | -18.81329 | -51.60348 | 2026-01-24 03:57:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c059218-e383-3b9f-8b4e-f4fa5ced3b25 | -19.56119 | -54.44651 | 2026-01-24 03:57:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14780046-a60e-3719-9b36-816919287a68 | -22.03837 | -49.50418 | 2026-01-24 03:57:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6a5ab800-97df-3d76-a9c0-5e42c7fb8011 | -20.45173 | -48.68332 | 2026-01-24 03:57:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87741417-cf21-304e-bf75-8a04964114e2 | -18.81327 | -51.60146 | 2026-01-24 03:57:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4aa4c200-adfb-3f2d-9441-98d0e9cff7aa | -20.45661 | -48.68452 | 2026-01-24 03:57:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 15.7 |
| afe37b65-3960-3a19-9775-2a16eb53c645 | -18.81934 | -51.60273 | 2026-01-24 03:57:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9370d81-b739-374f-9c13-5ebc53ff5fd1 | -18.81434 | -51.59884 | 2026-01-24 03:57:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e81b4765-4207-3219-a631-3c3443f80441 | -22.83689 | -48.65402 | 2026-01-24 03:57:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5ac718b-b79d-3e47-b79f-7375a3c803fd | -19.30021 | -53.17836 | 2026-01-24 03:57:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2366d92-8106-352e-9dfa-02fca88dd4fb | -19.29854 | -53.176 | 2026-01-24 03:57:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5d2b9a04-0461-3569-b93d-55c3cea4eb6b | -23.00584 | -52.38733 | 2026-01-24 03:59:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d4bfed4d-807d-346d-83b0-95e61a59d64a | -23.6052 | -48.26509 | 2026-01-24 03:59:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d304663c-8f0a-371f-b01b-cee4920f0b3a | -23.60619 | -48.2603 | 2026-01-24 03:59:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d549e63-41ae-3eec-bac3-ec460d9d1a86 | -29.12179 | -51.18426 | 2026-01-24 03:59:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 49e699df-1595-3912-a099-bedbdf7af112 | -29.11699 | -51.18312 | 2026-01-24 03:59:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 87edb05e-7380-37a5-b66f-f93394de38cd | -27.09495 | -50.529 | 2026-01-24 03:59:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0d82e9af-7acf-379e-a838-6099de19200b | -23.00693 | -52.38274 | 2026-01-24 03:59:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cd0e3d22-bd9c-3ec4-88de-48954889c891 | -30.0497 | -50.75469 | 2026-01-24 04:01:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| 059123d5-06d5-3a86-ad3e-5077a6dc9c85 | -30.05424 | -50.756 | 2026-01-24 04:01:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| 2d9f7622-1f4a-3c62-abd2-5c5848645eaa | -30.09216 | -50.79713 | 2026-01-24 04:01:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| ce297916-68d1-3471-84cd-301bdc887fc7 | -30.05545 | -50.75055 | 2026-01-24 04:01:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| a7a9fd22-3606-3f94-83a1-49c7f33f5f03 | -3.07028 | -40.11097 | 2026-01-24 04:14:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 365b2391-6802-3635-a3d8-1c6fd6ee8069 | -6.31065 | -35.22978 | 2026-01-24 04:14:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| daf5b187-4bf5-30ae-87f6-347a9d696fe3 | -3.06739 | -40.1066 | 2026-01-24 04:14:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| db53c6b9-5008-37ab-8753-42b462c12a40 | -6.25301 | -42.58646 | 2026-01-24 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cc0c77f3-f427-313d-93bf-71cfebd0087a | -4.14848 | -38.48086 | 2026-01-24 04:14:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c7ed61ce-bbe6-3d2a-b5e1-22efac13134a | -7.28893 | -39.05981 | 2026-01-24 04:14:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 37a7ec00-cb60-306c-88e9-01db2b46af60 | -3.07435 | -40.10766 | 2026-01-24 04:14:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fa5eb8e8-2718-39de-ad73-c7ca4fb8b838 | -7.62275 | -35.08722 | 2026-01-24 04:14:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 72ed5c9a-b970-3bd2-acf7-68e9e28be126 | -7.62233 | -35.09029 | 2026-01-24 04:14:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 44e190b5-90b0-3a69-9700-41f432d9611f | -4.92386 | -37.88408 | 2026-01-24 04:14:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6a941dd6-9603-3262-a90b-afd7aac0a997 | -3.07146 | -40.1033 | 2026-01-24 04:14:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9cf52b38-b3c7-3e58-b242-9cc695ff63c1 | -4.60809 | -38.4733 | 2026-01-24 04:14:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5b31bc93-be29-3e90-bfe1-dc1f19abcceb | -3.06798 | -40.10276 | 2026-01-24 04:14:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0a610034-960d-3460-9fa4-a93398fb0b0c | -3.06679 | -40.11043 | 2026-01-24 04:14:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 781dad9f-aa51-3729-856a-5fedf9e61e0a | -5.86157 | -39.6329 | 2026-01-24 04:14:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fa83d940-1c1e-3784-83cd-805565ceeda9 | -6.16728 | -40.35978 | 2026-01-24 04:14:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d561cfb7-9dd6-3430-8584-5d89a10f738a | -6.99341 | -42.86693 | 2026-01-24 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4e0492d3-b470-30ff-8c6b-e08e0f86c957 | -4.15233 | -38.48138 | 2026-01-24 04:14:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fa97c67f-02e8-3339-bf8f-38da29b45f8f | -5.77428 | -38.68776 | 2026-01-24 04:14:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 41c2f089-aedc-3081-8646-a9c488a83991 | -7.62191 | -35.09333 | 2026-01-24 04:14:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| c1487ab6-ca2b-365f-8d68-105dc90535af | -6.99395 | -42.86345 | 2026-01-24 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 092f24df-d810-3470-9b2a-5e5f553c1660 | -7.62701 | -35.0939 | 2026-01-24 04:14:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 6b265b70-d87f-3fa5-9725-5793777a0466 | -6.99727 | -42.86396 | 2026-01-24 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1adf06fd-a71e-3d06-947e-0e072184d1ca | -5.26312 | -37.72577 | 2026-01-24 04:14:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| afdf99a0-a4c5-358c-9857-17223aca3b4c | -4.78331 | -39.64635 | 2026-01-24 04:14:00 | NOAA-20 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 77100b18-446e-3074-9e36-16b3adbac588 | -4.92438 | -37.88055 | 2026-01-24 04:14:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c75fdc9f-d997-3ac2-8add-5ee5ed73a431 | -3.07087 | -40.10713 | 2026-01-24 04:14:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5dbc7d0c-5340-3332-9900-7431fa9130e3 | -5.09543 | -37.59697 | 2026-01-24 04:14:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 86b7d50e-bc6c-3eeb-ae20-73c637caf8e2 | -7.27988 | -37.23208 | 2026-01-24 04:14:00 | NOAA-20 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cb5e157d-af72-3b21-b94e-93271bb110e2 | -4.86543 | -39.00339 | 2026-01-24 04:14:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 043f7d45-68b8-3c86-ab62-151fc251cf55 | -7.62743 | -35.09088 | 2026-01-24 04:14:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| ce843a8e-0b65-3fe7-a3b6-37e94ac2ee01 | -3.4181 | -39.28313 | 2026-01-24 04:14:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a51bed5f-8c9d-36a8-a430-1dfe43dbe64d | -7.62784 | -35.0879 | 2026-01-24 04:14:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 85a57171-4e41-3ffa-a24b-860431a86e7f | -6.25356 | -42.58297 | 2026-01-24 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 358623ec-c9ab-3aaf-816a-d8e307119e74 | -5.26721 | -37.72639 | 2026-01-24 04:14:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 23f2ae96-25f9-33b2-b06b-552de1ed5826 | -8.45618 | -35.59182 | 2026-01-24 04:16:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7f7e1197-229c-3732-92d8-6c63f1412d64 | -9.33778 | -40.5631 | 2026-01-24 04:16:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7bcb9000-d400-3995-8c74-be762ca47f89 | -7.95485 | -37.49839 | 2026-01-24 04:16:00 | NOAA-20 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e9006076-0448-38c3-a53f-f30efe8483c0 | -10.14771 | -36.40229 | 2026-01-24 04:16:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4251c218-f65b-3926-a1a3-c6d98900aba7 | -12.21666 | -38.94704 | 2026-01-24 04:16:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 586bfc30-cb17-309b-b87b-609e2bc19a77 | -9.81223 | -38.10678 | 2026-01-24 04:16:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f1eaddbb-74eb-3fbd-86fa-492872490808 | -10.09177 | -36.15218 | 2026-01-24 04:16:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0965d803-12b4-34d9-aa9f-13b8e4c151e9 | -7.864 | -39.09626 | 2026-01-24 04:16:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 87b4d373-a5c6-3809-99ca-b965cf27658f | -12.2036 | -43.69719 | 2026-01-24 04:16:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3486054-311f-3d5f-8399-446c58cfc04c | -7.86527 | -39.09393 | 2026-01-24 04:16:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1ed6f2ba-423e-3741-b11d-5d0a891a2fce | -7.95844 | -41.54057 | 2026-01-24 04:16:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f4d18626-0a82-3f97-ad95-f6d57f013455 | -10.08957 | -36.15203 | 2026-01-24 04:16:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fd73060c-249d-303c-9d02-7e990fef101c | -16.44462 | -58.17226 | 2026-01-24 04:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d0f609a4-499e-3622-848e-891bf9e8799e | -19.29676 | -53.17708 | 2026-01-24 04:18:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README4.md)
