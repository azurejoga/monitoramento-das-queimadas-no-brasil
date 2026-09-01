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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53fb94de-23ae-305f-a9e9-4b786e3be8c6 | -11.25853 | -45.11991 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 206ad6ff-4bab-3abd-84d3-3d38fef1a4b2 | -4.9483 | -47.65868 | 2026-09-01 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7b8e773-a894-3fbf-86a9-787f06310e5b | -10.80719 | -50.70824 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec32e438-b0e7-3160-8129-7c5d88288a97 | -11.20338 | -46.08007 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e6e8987-fc43-3e89-a976-ce6c6ccdff94 | -6.65439 | -59.43245 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebe2de6e-d131-399a-8af8-1b8532cd32b9 | -6.67759 | -52.87202 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1b9e0cc1-1577-38fc-921c-cdb8aaee0a3f | -10.21166 | -50.31905 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b31f6092-dafc-3e7c-8f89-1d9591cda034 | -8.59441 | -54.75647 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4f16e75-1b3d-32db-981f-1dff8d749428 | -11.27602 | -50.57963 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c75ffe87-0f22-355b-a41d-789be009a43f | -11.19305 | -45.0393 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 522be2f0-40cd-3092-8216-d5da23d1dbd9 | -11.33626 | -45.15403 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6f419f4-65c3-37c7-9fe9-878cf9ad14b8 | -11.90791 | -45.07523 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebed9b4e-94d6-3fce-a521-aa5e41a3563a | -6.35975 | -51.7555 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18608df8-dc06-3209-b883-5b45a4cecc5b | -11.68469 | -47.15681 | 2026-09-01 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c5be85e-c074-3b81-b4a4-0ca74a925a3c | -10.06802 | -48.70749 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32ef970a-f3d8-3970-9a8e-eb7440443e15 | -6.11006 | -57.86734 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4a9e32d-f7c4-3779-af7c-e31478d2b6a2 | -7.81472 | -50.76886 | 2026-09-01 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f3be526-9121-3e0e-9d0c-2b8f6a2b3533 | -11.31033 | -45.18895 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f59db08-529e-3527-8e76-77eacc3ab708 | -8.12731 | -54.96473 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba20297f-8c77-34f8-8e4c-de2dc1d30208 | -10.0314 | -44.69345 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fbc80893-cf96-3eb6-b59b-446d26379247 | -7.34017 | -60.58564 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 81938139-9d4f-398c-9a23-df4c616d9c7f | -7.0549 | -52.71772 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e53fac7-bc2e-3e8c-8f91-929cb51bae92 | -6.59687 | -58.59307 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30b2aa69-798e-3adb-8d32-41137ce72fed | -10.73011 | -47.95872 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b3932bdd-8f88-37dc-af9e-2f4b1ed6547c | -6.31096 | -53.54841 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8b64530-295b-3eb8-9dfb-3af417898c9e | -4.94886 | -47.65502 | 2026-09-01 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| defc667f-f80b-3fcf-bcd9-21e311cc2ccb | -6.16111 | -57.77891 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a2205c0-8f76-30b4-b085-5a6d76a27b74 | -7.35479 | -60.59573 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 306bb176-3291-348e-a1e5-3c6898a6b87b | -7.52034 | -47.33284 | 2026-09-01 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29411e13-a165-3d74-892a-69b5e8cd647a | -7.3476 | -60.57812 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7e5af540-db5a-3fc3-b4d1-3d45cd0f6751 | -9.14779 | -59.5348 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3768ce1-811f-3507-b472-2fd36925bbc2 | -7.41817 | -49.74001 | 2026-09-01 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04c59425-34fb-366b-a6cb-044868e8dc8e | -4.85457 | -55.83208 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1d59bf4-dff6-32a1-a3ef-a1ec911149ee | -6.79707 | -59.39676 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cc07810c-09aa-3bfa-95ab-90f5979dddba | -8.50366 | -55.3056 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1599c186-8858-3878-a5bc-9f934583f0d2 | -7.57033 | -61.37291 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 639c4dbc-b522-3d30-a274-02cd252239ba | -7.28718 | -49.83934 | 2026-09-01 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee5b3f7e-3de7-37b0-aeb5-28ae3b9cee99 | -6.96319 | -56.43382 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c5eeddf-9682-37bb-ab51-1272bcfd1424 | -10.39494 | -48.23677 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29cd5b4a-347a-3153-8eda-18511c5a1af8 | -4.15759 | -60.7274 | 2026-09-01 04:40:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 766e09e2-0963-389f-9016-6dfb436a7ec7 | -11.21824 | -46.08778 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f346271-6bd0-381e-b637-f484e2775f9c | -7.21385 | -42.74049 | 2026-09-01 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fd86aa7c-d4ac-3d91-b755-1f683289bb52 | -9.20589 | -59.4178 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e89e063-ae11-30dc-a7ef-3da34ad722ab | -6.81118 | -59.09331 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5783c8b8-2fb5-3eb8-b779-2230b7791087 | -11.32697 | -45.15999 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79ad58d0-9169-31a2-90f4-03c278dbf30b | -4.15846 | -60.72242 | 2026-09-01 04:40:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb0f5898-b2b9-3558-a29c-3c6b33ebcaa7 | -6.2508 | -55.48391 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7db7736-8405-3b95-bd99-ab6d1ae01c24 | -6.31172 | -53.54382 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c2f5464-6020-3d17-9c5a-26d3ae28bfc3 | -6.48637 | -49.89341 | 2026-09-01 04:40:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c075749-7df6-33cf-bf64-c0331cc33e74 | -9.44524 | -45.68153 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac27dd86-13a3-3d2f-b82f-8a1e174a97fc | -5.80962 | -43.6432 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b947a5c3-4fdd-3574-b475-6dc9d54449ca | -11.2661 | -50.57804 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db20d94d-0f73-3cf9-a366-8a34d90fd983 | -6.25658 | -55.42322 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f945d990-1878-35dd-9165-b9a1f2ad781c | -6.56422 | -58.56378 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a404cdf6-f247-38b0-9c29-3ec85aa4d09c | -10.35484 | -50.00908 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0a320e32-c704-3be4-8dfa-32c3e1c23ed5 | -8.94115 | -62.36827 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 316378f9-67c0-3960-aa21-de437e8bedd0 | -6.59161 | -58.59221 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4fea54ea-d799-3527-a8ce-d9011fd0a369 | -6.69455 | -55.4016 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 465c9fc6-a869-37d0-8f64-93f3fe520da1 | -6.10555 | -57.86338 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc6b1aa9-fb8a-3ed7-943a-d46783b1d922 | -9.20765 | -59.55691 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf64cdf2-c20d-3daa-bfd9-1dacf39d3f06 | -6.59105 | -58.59547 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b03d880-5cbf-33b7-85c2-1532c94921ba | -6.80595 | -59.56774 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0774e6be-b4f7-3434-bfe1-2629c44d056b | -10.45631 | -46.73909 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2a1c7ae6-795b-3fbb-9c0d-949f87f49f56 | -7.18984 | -60.68753 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 31bad565-aa12-3eda-ab4b-b26aaf4cfea2 | -3.54705 | -54.71979 | 2026-09-01 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9509ac1-1d86-3cc3-9524-fa4b472ca3c5 | -6.90646 | -59.48515 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c08a6cab-b3b8-3d23-87c7-9f996dfd324d | -10.32344 | -50.03592 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d929d1de-8f22-3086-8398-c4657abc9d2a | -7.3465 | -55.19903 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3feda3a-b46c-3186-b2a1-9a8329d64415 | -5.85339 | -57.55682 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b8c74e6c-c0fd-3c01-b707-cb95e17340bb | -11.20819 | -45.11602 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 333b10e1-8a25-3932-9194-4a077d78377f | -8.93904 | -62.37168 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbe30f3c-92d2-39a8-a976-96438545d47c | -10.67273 | -46.27423 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04dfd076-0b3d-357e-b7d1-50b4cc37ab15 | -7.52594 | -61.37695 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b799d1f8-c18d-3edb-987f-cfa1ea386ce8 | -9.41275 | -51.67602 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7a055e5-b9f8-383e-964e-aecfe1ea0298 | -8.76873 | -46.44849 | 2026-09-01 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 171ac22a-02bd-3f2c-9143-98d40b1e54c2 | -3.61771 | -59.07 | 2026-09-01 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5f49715d-e868-3f59-aa19-9c4bad992ce4 | -7.35201 | -60.58748 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ae073247-2f4d-354d-b515-0e15ec6a61ba | -11.31607 | -45.1778 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b4d7b0c1-e166-3e93-ac7f-ee34451ddd06 | -9.16684 | -59.36893 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab081dd1-0beb-3015-b013-5638ac61c9d3 | -8.1307 | -54.96897 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cfcc7e58-32f1-3f97-b221-6ee601c2f7c4 | -11.26442 | -50.56702 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcb618a3-7135-338f-88b7-835465836050 | -7.62017 | -55.29231 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a113ad2f-05e6-3731-914c-08e69bb4b8fc | -9.4803 | -57.02192 | 2026-09-01 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59671a1f-3978-3418-a6d8-c572637231c8 | -10.85473 | -45.30241 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8061c22e-b893-361c-b08e-7329d8d05f06 | -11.28871 | -50.58524 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| a3a3c109-b07d-3c5e-9617-97df831dcf05 | -5.89374 | -47.73066 | 2026-09-01 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5857206-c0e4-3443-b748-3d020e1304fa | -7.35128 | -55.19582 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 308118c3-9cca-3253-a99b-2fdf5d502d81 | -9.67079 | -50.84071 | 2026-09-01 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74df2686-3b52-33c7-b73e-f68730d00b5f | -7.28495 | -49.8319 | 2026-09-01 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 84b11b73-6db2-33fd-bc76-6f866ba41446 | -10.51126 | -57.44041 | 2026-09-01 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 77e5b792-32e1-312f-92f6-07c8ee4325d2 | -6.02886 | -57.67822 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06d04e1a-ee2d-3682-9a9d-4fbed21a162b | -11.31766 | -45.16613 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05531a89-af81-332b-828a-3f3f07682e5c | -11.3114 | -45.18111 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 82e0bb35-ac38-3dda-9a31-ea4558451bed | -6.42082 | -55.52929 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d76f9679-b15b-3eba-a6a1-49d13286f070 | -11.66409 | -47.60864 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1dd3cf6f-207b-3144-8641-e8a21d856ce0 | -11.79796 | -47.67286 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9aa16955-a44c-3de5-b5f4-80b99a115e5f | -6.93697 | -55.63647 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c875f8a-e9ba-3c0d-b269-46b8add259e3 | -10.69006 | -46.26212 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ebfd095-2770-37c2-8339-33d41653102f | -5.53856 | -46.59861 | 2026-09-01 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfadbb1a-fc3a-3dc4-aec7-6b375517c204 | -8.90438 | -50.56665 | 2026-09-01 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README37.md)
