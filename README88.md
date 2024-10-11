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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb882c49-e9d2-3117-af58-ad4b85417fed | -9.51764 | -62.93105 | 2024-10-11 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b2516be-d49c-319a-bb29-71acfd1ee292 | -9.5141 | -63.48895 | 2024-10-11 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87a719b7-30c2-3893-9852-4dedc4af6e1e | -9.51402 | -62.93045 | 2024-10-11 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdd96eb1-1a5d-39b3-9187-87b46c145cd0 | -9.51333 | -63.49351 | 2024-10-11 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36ea462e-c7fd-3ab0-96e9-34d883b05872 | -9.46665 | -63.14677 | 2024-10-11 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b256a30b-bdbd-31f2-a0a8-287ab18145a4 | -9.46592 | -63.1511 | 2024-10-11 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce3091cf-7a5d-3ee2-9580-30ad36841e3a | -9.463 | -63.14613 | 2024-10-11 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df2cb23f-b27c-3cce-b166-87c913d8761c | -10.26783 | -63.34347 | 2024-10-11 05:18:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2895c972-76b2-3974-a58b-44bcccde0a7d | -10.26736 | -63.34623 | 2024-10-11 05:18:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4968933-250a-3d91-aa53-64ae8e054d44 | -10.26712 | -63.34782 | 2024-10-11 05:18:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 374732a0-7c4f-322a-9ffa-81620dd0242d | -10.26445 | -63.34127 | 2024-10-11 05:18:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d23b4cb-c23c-3f95-b857-5cdab70f1829 | -10.26418 | -63.34285 | 2024-10-11 05:18:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d73c2b0-9ae4-3c04-9f9d-28c6fd64e3d7 | -10.2637 | -63.34563 | 2024-10-11 05:18:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74218b51-5765-3006-b54b-d9747e7b7903 | -10.05387 | -63.2518 | 2024-10-11 05:18:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2af19c95-2e57-3786-aec8-92712f7cf410 | -7.35324 | -64.67094 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8908166c-bb53-3d7a-970f-a9ef30e6c74d | -7.34975 | -64.66649 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e5b6fbf-3c8d-3443-b3e8-0299a5609906 | -7.34588 | -64.68909 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 999a0532-83c3-31b9-9c8f-19cdacaff460 | -7.30961 | -64.66379 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fec747c-8430-3d3a-b93e-af08ecae872f | -7.30772 | -64.67512 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b8735ec7-d1a6-3f11-a503-131b41ed11c2 | -7.30709 | -64.67889 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b00cb4bc-b542-3618-880d-efe8e9133ee5 | -7.30358 | -64.67442 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20d69d87-76d4-3442-8efe-e357224146b7 | -7.30295 | -64.6782 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f7f5abd-16be-34a6-84b3-70ac430132fc | -7.29495 | -64.64971 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b327cc3f-aa08-374b-9a1d-5e86285c6373 | -7.29116 | -64.67234 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d2f5bea-1277-3c84-9263-c9f645202073 | -9.44976 | -64.45728 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c24588b-5e12-3a45-8c6a-c8831a966a64 | -9.39778 | -64.45687 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02f993d5-b7de-338f-ac67-29413ffb2454 | -9.35132 | -64.34925 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46583892-b098-3dab-9cf1-3f305c296449 | -9.35045 | -64.35429 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ec95f9b-9e4e-36e9-8ccf-0521c53c5095 | -8.65884 | -64.29845 | 2024-10-11 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 831fdfba-7704-30e5-b339-5ccf26e80913 | -9.96121 | -64.71982 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6123a505-cc3a-346e-bf12-bb46fdc2917f | -9.96061 | -64.72334 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da9b0a1c-a372-3ddf-8e3c-de4e5bbeafcd | -9.95724 | -64.71912 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b18161e5-1259-3eff-a272-c7722afff5a9 | -9.95663 | -64.72261 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 995a726c-9cbf-3760-bfcf-7529a2c31d8d | -9.893 | -64.79458 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35e3ce2d-c57d-37a9-9528-ffe025e2065b | -9.8924 | -64.7981 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dafb786a-847d-378a-83c9-870e096c8f32 | -9.88839 | -64.79743 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05167eff-4c8f-3fbf-a94c-bd8ad9895a07 | -9.88686 | -65.00387 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f98f85d-68ef-39ab-8d3f-ed93eff069c4 | -9.75191 | -64.88665 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c8a33d5-9f3b-3524-8e50-c41bb93c3d72 | -9.7513 | -64.89022 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1767d2d6-26fe-3c0f-a58e-1210fbae5a9c | -9.74789 | -64.88589 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c738e53d-0104-3780-84cd-07d436cfa370 | -9.65234 | -64.95535 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d96bcddd-c3ee-395c-96f4-eae83ac68298 | -9.65172 | -64.95898 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e98c78d2-661c-34f4-97f7-e038cfff94e7 | -9.6511 | -64.96262 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0f1e1df9-1b49-304a-8270-6221ed5628b5 | -9.65048 | -64.96627 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a813665-9248-36d5-a6e4-e386fa7ed6c2 | -9.64987 | -64.96992 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81fac3f3-079b-3d6b-8c83-058854da9420 | -9.64828 | -64.95464 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a93b192a-5fe9-3593-8dd0-00c9abbdfd17 | -9.64766 | -64.95829 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 658d7e64-976f-3ef6-9b69-e7871bb94fda | -9.64704 | -64.96195 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4d108b10-63b4-366c-a54a-1ea686260d47 | -9.64642 | -64.9656 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ece63e70-a8ca-3efc-a9e6-e219fae43622 | -9.64359 | -64.9576 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bc5b36b2-cd52-3e1d-896c-fa296ce8e074 | -9.64297 | -64.96124 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0c9c42be-24d8-30f6-8fd4-29d8b82feced | -9.56714 | -64.62144 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b6326db-d3dc-3e76-b361-294dbf814758 | -9.56656 | -64.62489 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb7f3465-9b80-33fa-bd22-b81dd1757c67 | -9.56316 | -64.62077 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 627ed58b-6e24-3338-93a0-3cf20c88e599 | -9.56257 | -64.62421 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bad47fe8-b3ca-3142-aaec-f142f711562e | -8.61077 | -69.73457 | 2024-10-11 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b82ce807-dd39-3ff1-ada3-7766219c52bf | -8.3364 | -49.96893 | 2024-10-11 05:18:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8279ef9d-a8d1-37d1-aba4-1db2290ee1ec | -8.70412 | -67.00111 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38fef133-078f-314b-9646-91f0fdf52564 | -8.69938 | -67.00026 | 2024-10-11 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a91db290-4257-345c-a2b1-965757eb1a14 | -6.96187 | -45.29267 | 2024-10-11 05:18:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cb8c69e8-be4f-3c50-a508-ab5488841a7b | -6.95942 | -45.28402 | 2024-10-11 05:18:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| de4b81d8-5fb4-3859-b392-d5de6d185fbb | -6.95851 | -45.29123 | 2024-10-11 05:18:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 2cb34209-be04-3248-bb04-1145a336a08c | -6.95541 | -45.28672 | 2024-10-11 05:18:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a46763b1-9ee0-306d-82f4-d9461adae6f6 | -6.95451 | -45.29352 | 2024-10-11 05:18:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 48226152-2b2c-3b95-a335-35314d930327 | -6.951 | -46.12885 | 2024-10-11 05:18:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| afb6bdf6-cf1f-3b8a-a26e-75fdc717f171 | -11.39477 | -47.19021 | 2024-10-11 05:18:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d60ac77b-4584-3f6a-8f2c-a3caa98f57ac | -12.29953 | -47.20723 | 2024-10-11 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8e376a1-544c-3c95-96f4-0f69b32d78e0 | -8.12921 | -48.04235 | 2024-10-11 05:18:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16814ce2-36ed-34d4-b3b6-fa39794ae191 | -8.1286 | -48.04702 | 2024-10-11 05:18:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 907c8333-6079-3143-be0b-3c2a829178e6 | -9.87418 | -48.27517 | 2024-10-11 05:18:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f0ec40b-738a-3161-8df4-1e0f8aa74b80 | -9.8682 | -48.27642 | 2024-10-11 05:18:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8507770f-dc38-3f24-96ac-747582e9d50f | -9.86754 | -48.27807 | 2024-10-11 05:18:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6cc26d2-5d20-3b6f-8a08-9c1b9b83a802 | -10.01069 | -48.84922 | 2024-10-11 05:18:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 702d5f7b-be00-3502-905c-48e889d57be5 | -10.0076 | -48.84805 | 2024-10-11 05:18:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 95699227-5114-3468-a968-00eaa14ac2a3 | -10.00474 | -48.84819 | 2024-10-11 05:18:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad3fb3fc-009d-36d9-81a2-7f678937ea3a | -7.69131 | -49.82733 | 2024-10-11 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0f375da-8831-3ef3-b164-1ccc5d48dc96 | -7.68989 | -49.83775 | 2024-10-11 05:18:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 439dbfe9-d1b0-3bca-9b56-eae3209e133a | -7.68588 | -49.82658 | 2024-10-11 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd0092ed-0650-3966-b9cf-e621389c36cd | -7.68541 | -49.83006 | 2024-10-11 05:18:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1641ff84-554e-3846-9a0f-402486d83050 | -7.68447 | -49.83699 | 2024-10-11 05:18:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd5843c9-ac01-3fa6-814b-272e4876668b | -8.8361 | -50.06825 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3922f1e5-cda4-3930-8e9a-3ec31f70a191 | -8.78838 | -49.78954 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 319c0d97-e558-34b5-99d6-d4616a4d0934 | -8.7879 | -49.7932 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fec92ee4-773d-39e9-86f3-21b249d11f47 | -8.70797 | -49.97597 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9df10210-a95a-3731-a01f-8796c5ff77e4 | -8.70751 | -49.97949 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d9a29499-be49-392c-b2fe-afaacfc60c7f | -8.70705 | -49.98306 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5844ae21-3bd2-32c9-90a0-570014f486eb | -8.69385 | -49.99935 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5b9044b-3fa6-34ad-b2de-d644f76c3fd9 | -8.77498 | -48.85873 | 2024-10-11 05:18:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92f87417-3c04-39f7-a965-cb0b53cbb5ab | -8.77444 | -48.86293 | 2024-10-11 05:18:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7e5aac7-2575-355c-aff4-8eaa48e7dbed | -8.4349 | -48.65948 | 2024-10-11 05:18:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2aaa578-a4bb-3668-8856-756900881051 | -8.43434 | -48.66362 | 2024-10-11 05:18:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd207b35-957b-3776-ad3e-4241ebc37406 | -10.47819 | -49.98041 | 2024-10-11 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e004bdfc-7f01-3fac-a2d4-8007782d74cb | -10.47771 | -49.98417 | 2024-10-11 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0933552c-007b-30b2-858a-189b623b0a1c | -10.47701 | -49.98164 | 2024-10-11 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9369b62c-94b6-3a80-a473-ecafa30707ec | -10.47213 | -49.98341 | 2024-10-11 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42204859-b0a9-321b-981f-b39f30a241ac | -10.47165 | -49.98717 | 2024-10-11 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 13a40d87-eec8-39d3-9bec-e9c77a3f58f0 | -9.67718 | -48.91908 | 2024-10-11 05:18:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b01aa95-56ff-33e6-9c7c-140e809cc65f | -9.67339 | -48.91723 | 2024-10-11 05:18:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 717f3306-06f2-3585-97e5-aadc916b928b | -9.67132 | -48.91786 | 2024-10-11 05:18:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1f2ddc9-7cca-3f4f-ba34-86f39fcd1402 | -9.62235 | -48.98748 | 2024-10-11 05:18:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README89.md)
