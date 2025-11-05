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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a254eed5-4621-3366-bcf9-d07b83292380 | -4.50877 | -45.43754 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d9f412c-d0b2-3a3a-8a98-bc65441665a0 | -6.55481 | -44.47448 | 2025-11-05 03:51:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0bb7c09a-a865-3e81-8386-628037f0b747 | -8.93567 | -40.87414 | 2025-11-05 03:51:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b806cfbf-b468-36d2-9942-b2c2708b9d44 | -8.50694 | -44.17126 | 2025-11-05 03:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 502270d5-7104-30d9-9649-97f3bd474ce5 | -4.86511 | -44.61667 | 2025-11-05 03:51:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b8e8cbd-21eb-3f56-89a4-8f86bfc953e4 | -5.78718 | -40.81995 | 2025-11-05 03:51:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 89ce20a4-7afd-35f8-b35c-bc04276c6f88 | -5.23578 | -48.50595 | 2025-11-05 03:51:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f2bb7cf2-2f81-3a8c-9608-6344a83fa9cc | -6.4599 | -39.85601 | 2025-11-05 03:51:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4bc84f34-df5c-3f91-b3cf-29a697181f0e | -9.77767 | -43.61496 | 2025-11-05 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9617c3e3-e93e-3281-a9a2-e72d3d6806b3 | -5.03175 | -43.61969 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 98d2ad3b-99de-3f35-823d-7d207ca3f174 | -7.12892 | -41.33249 | 2025-11-05 03:51:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26a01926-9165-3e6d-99df-6ca80f3565e2 | -6.34687 | -40.63577 | 2025-11-05 03:51:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a5beb2e6-c176-3ccb-8ebe-f257f7786878 | -4.11136 | -43.88216 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af567edf-da46-3b7d-8810-c667498ea112 | -6.0992 | -41.70379 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3a018b4d-fd74-3d1c-87f7-7c6cf0477684 | -3.4976 | -43.62933 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0ac0c011-3095-3611-9a4d-e88496ae24b0 | -5.34277 | -45.1708 | 2025-11-05 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b224f35-e296-3600-91f3-61e78ad4533d | -3.07347 | -47.77707 | 2025-11-05 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f93d488-0ab4-38ac-9701-4cdd36a0e938 | -3.23451 | -43.44412 | 2025-11-05 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 75b84969-a8b4-39c9-a1d4-76c1aa100087 | -4.91955 | -47.33033 | 2025-11-05 03:51:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 811cd84f-357f-34bf-8232-cc5ffe4140e6 | -4.38305 | -46.27338 | 2025-11-05 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1cd06e6-228f-30ae-9b1a-8c635c40deb2 | -3.23349 | -43.44717 | 2025-11-05 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| be915fe2-aa6f-3c96-b472-4365238c03a2 | -6.70462 | -40.83195 | 2025-11-05 03:51:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ee6dcb65-2d78-3afd-98fd-fd2fbfb8c801 | -4.58896 | -43.33562 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cb9c5af-fc69-36ab-953d-4707aad65a60 | -2.97603 | -48.70591 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f653637f-9d1b-3a0f-aaa5-ba0f0cd3246c | -4.50606 | -45.43833 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5703752e-6a9c-37a6-ae1a-e99a7f837af8 | -5.14863 | -41.22179 | 2025-11-05 03:51:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 307a8606-dbd3-3d26-b5f1-2ab1a43195b8 | -2.82534 | -45.14806 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 507f7e72-1bc4-3645-8fb7-0b35d7f9427e | -4.52704 | -40.3508 | 2025-11-05 03:51:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 12f23629-11cf-3166-a89c-eb5ff994e768 | -5.31946 | -37.576 | 2025-11-05 03:51:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb353a43-7feb-3f8c-9f83-e7a5cbc2b8c7 | -7.04778 | -39.28676 | 2025-11-05 03:51:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2b387c6-ec14-37dc-90a1-26bc5b27a392 | -4.10853 | -48.02533 | 2025-11-05 03:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5e063abd-4fb2-3881-87b8-2b5ba6eef5a6 | -4.28708 | -47.17554 | 2025-11-05 03:51:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bf1fe96-fdc4-3d32-a74f-288bc609b086 | -7.9021 | -45.56862 | 2025-11-05 03:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10e54914-3e83-3ebf-9609-6307fd93e69c | -6.09456 | -41.70688 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2fc6cbc3-51ac-3c6e-a327-b364cc8f5267 | -6.21315 | -43.26885 | 2025-11-05 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 823b8a25-6ce9-3895-a4d4-d2dd5182a66c | -2.64996 | -48.50957 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 34e45378-dd5e-3c39-8d55-a3327cc9521e | -9.78108 | -43.61316 | 2025-11-05 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb6b4e83-ad6d-3b1b-bbe9-c7eae715bfa2 | -5.24309 | -48.50192 | 2025-11-05 03:51:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 949e5b9c-a999-34f9-9d7f-27b6b24841b3 | -7.32935 | -47.2515 | 2025-11-05 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42cd8cc3-a7c9-390f-9455-282e377deea9 | -4.61343 | -45.35349 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a72d0e58-6cb4-30ba-b334-4806e0fe6e26 | -6.70919 | -40.82788 | 2025-11-05 03:51:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 904b2937-2550-3d8d-a2b8-4bc8bc71b3f6 | -5.11361 | -46.22466 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6353fc96-c1a7-318c-8afb-0f3a6f28a225 | -7.2874 | -45.45261 | 2025-11-05 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af2a9853-d419-3d54-a67e-8366f7c9e3ab | -2.73225 | -47.39048 | 2025-11-05 03:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24b7e592-2bcf-3522-a14e-37416d512867 | -7.32861 | -47.25552 | 2025-11-05 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3b57e69-435b-3549-a3ed-be5cc2362c64 | -6.10042 | -41.70045 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8202b48f-b406-377e-857a-ab52b8f4dc3d | -5.2843 | -43.62782 | 2025-11-05 03:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa662303-d953-39a6-9c9c-31447d4bd103 | -3.79962 | -44.04185 | 2025-11-05 03:51:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56365d73-f20c-3798-8068-b5b9d5da1465 | -7.16241 | -40.10172 | 2025-11-05 03:51:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 758dc348-c6e5-385f-bd67-3e9533c40228 | -7.33546 | -38.8552 | 2025-11-05 03:51:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dd273bb9-19e5-3430-b540-a1bf21dbe564 | -3.47674 | -43.63653 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31ba030d-04d6-3bbb-8015-901f71f87517 | -5.04025 | -43.62602 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 007eb499-ce2a-376a-a51a-68368ea23422 | -2.81997 | -45.14716 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 942372be-4e22-3d18-b5ed-dd37ef37d2a3 | -6.10074 | -41.72285 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a3eec01b-1799-3602-ac06-2dfbda60615c | -6.37536 | -42.41538 | 2025-11-05 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 28ef1aa8-89e5-3508-b578-0e59e76a4934 | -8.05323 | -49.63129 | 2025-11-05 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f0378845-3956-3174-9ee1-3e112bfe7a72 | -3.23378 | -46.87541 | 2025-11-05 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 62e1f866-47df-352e-bdb5-11322b1731b9 | -5.99224 | -42.95385 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f7cfb560-1f3a-38f8-b70b-cfb67ce623c6 | -4.5007 | -45.43764 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cbef8aa-c611-3c5a-8f09-deb053f434dd | -4.41955 | -48.95079 | 2025-11-05 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7b6c8462-c64a-344c-bf9c-fb6bff4b606e | -4.50983 | -45.43116 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1913457d-fba4-3b33-99c1-cc4f5214f0c6 | -5.47557 | -43.57553 | 2025-11-05 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b1d503ef-cbae-3aa9-894c-ad978cd6082f | -4.91637 | -47.32718 | 2025-11-05 03:51:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2150306c-cbb3-3c98-a8d5-5bf2304eaba6 | -4.61216 | -45.3538 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65526068-2c00-3f81-b0c9-45df2e0fc951 | -5.43061 | -44.66232 | 2025-11-05 03:51:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ff8259fa-942d-3d39-a661-4c87729004a1 | -3.64573 | -44.4374 | 2025-11-05 03:51:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9eb5578-d9ea-306a-aba1-5c1bbddae103 | -4.60744 | -43.89466 | 2025-11-05 03:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 471c7a09-979c-3a6a-8602-7b68b0f442f4 | -3.48323 | -43.62699 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9134df21-b3d3-32c2-a6bc-2e46860c53b4 | -7.2336 | -45.7006 | 2025-11-05 03:51:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0973693-72a2-3c07-91d0-b2e8be969817 | -3.66096 | -44.79741 | 2025-11-05 03:51:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 433415e3-6add-3933-8f99-d2341658931e | -8.05212 | -49.63704 | 2025-11-05 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6bf64e92-bd0a-3f78-b580-4a5291a37566 | -5.37582 | -44.74094 | 2025-11-05 03:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8c3c3c3-66a7-323b-87f7-8643aa87817b | -6.13865 | -41.64571 | 2025-11-05 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2ac54e69-93f0-3fcf-95f0-00c2fea7f954 | -8.85912 | -49.88086 | 2025-11-05 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a408e43-abad-34d7-94cb-fbae245b604f | -4.92233 | -47.32833 | 2025-11-05 03:51:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a43e06cb-5ae7-3700-9c76-69522fe40120 | -7.03905 | -41.46334 | 2025-11-05 03:51:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b6fa3825-28ee-36e0-b239-5fa32fb94489 | -4.65933 | -44.52711 | 2025-11-05 03:51:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f39ddab-7b3c-3597-8d90-e442756a4ade | -3.28851 | -42.18227 | 2025-11-05 03:51:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67cf8a65-b8ac-3288-b80b-f2814ab5c89d | -3.23309 | -46.87947 | 2025-11-05 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 48cfa41c-1411-3192-b3e0-fd2c68a14f9e | -5.47127 | -43.58301 | 2025-11-05 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d2652d5-c509-3537-b213-1b1b2f70f182 | -4.11704 | -43.87775 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8783ef7c-e43e-3343-b13a-2ac14b3a70c5 | -7.42667 | -47.1361 | 2025-11-05 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e99e27c2-66b2-3e92-90e4-e26118a1fb75 | -5.92971 | -41.29401 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 47c49a30-96c8-377e-8f82-c9c0ef4cc1ee | -8.50435 | -39.93538 | 2025-11-05 03:51:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5fe0e942-b9cd-30f7-9ca7-6f1d63fc2552 | -6.43334 | -45.66379 | 2025-11-05 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b39b60fd-4b94-3de7-9c95-bc5b8b3594ae | -7.54622 | -45.84756 | 2025-11-05 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbbc2995-eb7a-3409-9c61-fcc71e419c74 | -3.48407 | -43.62189 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c7222331-a917-304a-b849-ed3f014cd508 | -4.28556 | -45.66361 | 2025-11-05 03:51:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fe04f94-e40b-359c-a32d-a173091496d9 | -5.26679 | -44.13734 | 2025-11-05 03:51:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ee01ae2-d5bd-3107-94c4-28de6e4cb159 | -5.62348 | -41.08701 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0b66146c-f5ca-3e88-87d0-5e436ecabde1 | -8.79746 | -40.60059 | 2025-11-05 03:51:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3a40880-54f7-3e01-8ba4-1c82e3500815 | -8.3028 | -49.65496 | 2025-11-05 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2109050-0fbe-3e19-9b91-b7e81d4d1ae9 | -8.2319 | -49.98946 | 2025-11-05 03:51:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cba6760-a02b-32e5-b038-e5f6a0aa03d4 | -6.97092 | -38.08538 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5de720c2-f75b-3f77-aba7-cc08c343d47f | -7.24244 | -45.26389 | 2025-11-05 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8abb01a8-5eb7-3a1d-9c8f-f7e4034f7811 | -4.15572 | -46.79198 | 2025-11-05 03:51:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ce46c00-628c-388b-879e-0cbddeb2dee6 | -7.24193 | -45.26677 | 2025-11-05 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e7db2af-de76-3f97-a8f9-935d1a7718db | -4.76184 | -42.64972 | 2025-11-05 03:51:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 9f07c911-d8bb-39d3-933c-cb32dff4497a | -4.56972 | -43.33729 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b37a28b-b372-3e14-ba7f-9f6131376a72 | -2.84869 | -49.41819 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README11.md)
