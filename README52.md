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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7a45344-85c3-33a1-aaed-b6097c99697e | -2.01832 | -54.31548 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d680ccde-4bbd-32fd-b139-4fd3097dd317 | -3.09534 | -53.72713 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b18b59b-16ce-351f-95aa-bc228a076ba0 | -3.35302 | -49.56336 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e0b2c1f-1e3c-35a4-b398-3808197ae951 | -2.79 | -54.10566 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 699a6b53-917a-38f1-aacf-734d284c3b1d | -2.87494 | -53.94268 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b97c7174-a174-3ede-9e1e-2b6502e7f0da | -2.90667 | -51.58121 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1712f0f-70d6-3a4e-a63a-e3413a6f5571 | -2.04626 | -54.66434 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 303aa43d-2f4c-35ea-bc7f-eccb611c7551 | -1.57037 | -51.19987 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb004778-52f3-3575-a5fc-cac288440199 | 1.13741 | -55.98463 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59c389ed-3a67-34fa-abdf-4b3b30dbdc11 | -2.97971 | -53.90053 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76282a97-190f-3e59-b686-64d74a92085b | -3.54957 | -50.19728 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03a0d916-b125-3f0c-b5e0-32526929e30b | -3.2682 | -53.63218 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0984ea08-cbd3-346c-9681-71ffcc1ea3db | -3.29142 | -52.07164 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3f2c8957-c78e-327b-9012-eb44746efabe | -2.13021 | -51.00854 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ede626e4-1c5e-3794-a00c-6bface4d9fa4 | -2.6048 | -54.36132 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07724a5e-d0ae-3050-82dd-51d598b6a809 | -3.707 | -51.06887 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad2eab51-e2e4-339f-90a9-2186398a2ec7 | -3.49387 | -50.32621 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89ece779-164d-34f5-8d4d-137951a7897f | -2.8638 | -48.55708 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1750189-8102-3880-801c-f3f09806f3e3 | -4.03865 | -48.33586 | 2024-12-02 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0a26f4d9-a161-3be1-897a-d0e1697e4013 | -1.07004 | -53.62931 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0915611e-0fc7-3abe-a1e5-617cc999f361 | -4.54684 | -43.30215 | 2024-12-02 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69e5a95c-e983-3d2d-a6dd-8d3a73fbc0c7 | -2.37274 | -53.66186 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbe14ba6-1863-346a-bde8-2ef6ab1bd30b | -3.28882 | -46.04248 | 2024-12-02 04:48:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59592cdd-08e5-3091-b10d-fd323d31d538 | -4.05111 | -46.99266 | 2024-12-02 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42162993-d5f5-31c4-af00-63f1b5ede8bc | -3.50297 | -53.83156 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c150669c-a071-3584-8dea-d552b2be0827 | -1.4036 | -53.64955 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 70a643e5-9dc3-392e-aa79-9f889b4dd717 | -3.02847 | -54.18459 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc447bc0-c210-303f-981a-22e4c9a1ba26 | -2.87049 | -53.99251 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c5e34b9-f81b-309b-8281-1c66efcb3902 | -1.08602 | -53.40052 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dcbd341-b3d7-372b-8439-5c114636df4e | 2.4266 | -60.65962 | 2024-12-02 04:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06aa7edf-1648-31bd-bb39-cf9819efc92e | -4.19641 | -50.67499 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 750c0936-8f0a-3887-9ce5-91e7d79bf5a9 | -3.39107 | -50.3103 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d17d2157-6b83-3e8b-8be9-b7735374f7f9 | -4.03454 | -50.56286 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62b33e64-71f4-35ba-afa6-33debda84ca1 | -3.48106 | -46.0857 | 2024-12-02 04:48:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6f73a72e-20ba-3310-8be8-cd473ed420cb | -3.10068 | -54.02346 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a4fe269-f40b-3886-9a03-d8e64d36b22a | -3.30737 | -53.86984 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9dde616-f37a-35db-8b81-3dfc596a28e2 | -2.45279 | -52.21863 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e0a192c-3689-393e-b8fb-66dce5606d6d | -2.46507 | -46.5808 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1ac6d9b-e344-3085-b71f-7e73422f476e | -3.26527 | -54.19736 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ea51d1a-d65e-360c-b0c7-5a79643faa8f | -3.2902 | -53.66968 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 539a42af-1ad1-3a7d-8dc7-2aff0bf5fa67 | -3.25515 | -53.62637 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 95811f6b-1831-3f40-8a91-89540d37550a | -2.52742 | -53.9868 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50f05706-2b4b-3b7e-8d12-075433068b2f | -3.43395 | -53.88964 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bb6ca0fe-f126-32a9-b410-0b971934a166 | -2.68079 | -46.61272 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c85ca398-9ac3-3dd0-a4ac-d38cffddb5be | -2.82505 | -51.83999 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f93c510f-b3fd-3923-aebe-01dc471ff623 | -2.86825 | -53.98435 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 970b96ff-39fc-3349-a0ea-ea3b9a05ce59 | -3.3114 | -53.86665 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aac9920-9a91-3ff4-a747-da05a87f7172 | -3.85441 | -46.53138 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52b548b3-478f-3b93-96bd-7bdc6238fcd2 | -3.2138 | -54.17373 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf3192e4-01e5-3adc-8d00-0c379a2e9c3a | -1.78536 | -52.7452 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72220f54-11b6-3d56-b99a-948b48a8b713 | -2.30398 | -51.26544 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 802496e1-c2ef-3c77-b95f-2d44a1a115d8 | -2.71392 | -52.00545 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b0b7528-9e6f-3aeb-a294-f16d48e6e945 | -3.22006 | -53.42698 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f646965-f015-3993-9abd-7861ba1c5dab | -2.58889 | -54.21363 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e492f8d5-2439-3e27-add0-dcc39a85cb9d | -3.3695 | -49.86586 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e063d4a-4606-36d9-a1d8-3d67f48db25d | -2.54525 | -53.4161 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e955f230-1cde-3f76-8c2d-1ff76d3d4585 | -2.85308 | -54.19043 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ef5b7de-906f-3ee1-9f60-c72ec37a3e7f | -1.60641 | -52.28576 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b2f4050-45f4-3c4c-9975-bce5807b5a5a | -1.11396 | -53.10971 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e884b09-3d2e-341e-9bfe-687b286aa90a | -2.84581 | -54.03551 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b8c10ee-98f4-30d3-9b0b-77c43551a135 | -3.25747 | -53.3438 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f07ae67-460a-3d7b-b32a-7719ad303326 | -2.7911 | -51.9051 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc5bbab3-de8b-310d-838b-6f5886d2d3cf | -2.82645 | -54.03279 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 362dbf86-c5c7-345e-97e6-5ff8e6d65d4d | -1.18168 | -51.76877 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77ad1b3f-1f7f-3343-8129-5a2b46e503e2 | -3.42189 | -50.65496 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ad63d8e-521d-3ad4-bb61-1acfde7cc9bb | -3.99127 | -47.91603 | 2024-12-02 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9f6abcb-b42c-3bbc-8690-2a8e9397b71a | -3.28486 | -50.79226 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de5423d5-4e33-3daa-9d45-5f53a4f46564 | -1.07 | -53.39037 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 018737f2-4413-3402-bb53-8d086809c990 | -2.47021 | -46.57438 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1691c4f-320a-3141-8979-543ee27422a3 | -2.97218 | -48.0481 | 2024-12-02 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67305628-b26f-3cf2-a1d8-29969a58b99b | -4.91189 | -41.34865 | 2024-12-02 04:48:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7fc76689-89c3-3e3e-bb43-a5f52f6d12ad | -4.77324 | -46.42928 | 2024-12-02 04:48:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b28c6de6-b42f-3c88-a4f2-e21794e3690d | -2.4445 | -50.51883 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61b73db0-b652-31fc-8e6f-54b175f22f3a | -1.61783 | -52.69051 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95727805-1b2f-3534-a640-e3443b1cd6f1 | -4.08979 | -51.11742 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f515ce9-60b3-3f8b-9428-6922df9a7b87 | -2.05992 | -47.73526 | 2024-12-02 04:48:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bad96a9f-1c1e-3ced-8ec5-f81fbc0e0906 | -1.1674 | -53.41655 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d3ac76e-bfa2-3907-a84b-4582f1d1eb93 | -5.58195 | -45.20535 | 2024-12-02 04:48:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed3bfce1-e927-305f-a2ec-216b8ad50b48 | -3.08921 | -54.29749 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f68cefc-ce9a-3948-8c37-1e4cd7248495 | -1.68096 | -52.52247 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c923c863-cb5c-3af3-971f-81323b4ad811 | -2.92445 | -54.17711 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b915e542-a48d-33b2-9100-6977ee862a5e | -3.33807 | -50.25039 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f06f1b78-a392-3171-bc6d-ea12b0d8e9fd | -5.12367 | -43.20618 | 2024-12-02 04:48:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 33e75ece-4a7d-3ca4-9d81-ec39af782c3d | -2.88193 | -54.0099 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e468251-9339-359f-8f6c-d487c248f44c | -1.29224 | -51.36731 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dd02f72-83be-3631-9827-57745b34b5c9 | -3.70367 | -51.06836 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 765119d5-6d19-31f6-bfce-21b07de43e6f | -1.52678 | -52.66518 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3dcd6d9-9c7f-37cd-b65e-6c6a950a48ef | -2.43325 | -54.11986 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10d8f9c2-4d32-38e8-bd78-d05a6051ba9b | -2.49985 | -49.01646 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3334b56-7de7-3fff-af04-d141898c0af3 | -2.84228 | -54.10168 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba9dc794-306f-37fd-8db4-d682d77d219a | -2.86234 | -53.99903 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b5a1c15-38a5-3193-94c9-435d02a61756 | -2.88539 | -54.01044 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b32318c-8e4f-3fbe-b552-1e5b7d3c5693 | -3.98825 | -49.87401 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4f15d6c-d8b4-3f54-b07d-9f141fd74502 | -4.05202 | -46.81895 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3dd34b30-d03f-3569-b5b8-a8daca87d8d4 | -4.28823 | -49.94869 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c182176b-fc6e-3314-9362-f83f5229adaa | -2.45859 | -53.71718 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ec7caa6-fcd3-3d65-9814-b5ef126db864 | -3.11091 | -54.04837 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aaa0f743-9cfd-39a8-82e5-3559f7fbfb53 | -1.36331 | -51.3922 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc3d0109-565a-31f4-b270-47574a467036 | -3.74234 | -51.29896 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0597795-b3d8-3711-b757-458bfbb0030a | -2.98661 | -53.90156 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README53.md)
