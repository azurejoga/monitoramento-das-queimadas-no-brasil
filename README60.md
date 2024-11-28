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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc953598-3049-3402-bd4a-5ec08eeeb6ba | -4.1753 | -48.62848 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2824478-21a7-3fb2-85fc-64ea76617b5a | -3.68733 | -54.20832 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bb5563f-2701-3255-a364-49b9c2e28b68 | -4.06446 | -48.83829 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 457872de-370f-3d0c-ad85-05664fde4e90 | -3.47319 | -45.04335 | 2024-11-28 04:25:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 857ca484-44bf-33d6-bcf5-f6af5f306aa0 | -2.46201 | -48.57772 | 2024-11-28 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22b695c9-d462-3c7b-94ad-dae32147ee8b | -2.8235 | -46.84171 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89672485-92c5-39a5-aac9-1281ea9fa62f | -3.71332 | -47.13829 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e667086e-3083-3b82-af19-cb33aaacc266 | -1.62167 | -53.87521 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f37eb38-ad53-38b8-b7a1-c3f1a19f19dd | -3.26154 | -50.43531 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a1e76ed-bf9c-31ea-9b26-90878c561025 | -4.04636 | -46.8357 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 734322e2-b22d-3415-af73-20d750e3c7c7 | -2.91642 | -48.32522 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fde10b3f-c602-375c-a982-9479ee969152 | -3.09476 | -53.81459 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db5537c2-b5cb-32b4-9b63-33873d3fa184 | -3.31271 | -50.50111 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c524c65-6912-3da5-9818-8b23ed286173 | -3.3335 | -53.54708 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a629c320-7441-37a6-b39e-bd90cc01b8c6 | -4.36317 | -48.69806 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 108ca0c1-578f-32af-a76d-30f9849989b4 | -2.11581 | -50.34948 | 2024-11-28 04:25:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7f064b3-7491-3def-a56f-24f6c647c27e | -2.84966 | -46.88235 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80997cc8-5f51-3c3d-8f29-c9d21835e70d | -4.2159 | -50.89876 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a40b5f90-f549-3af3-8f68-756919dc33bd | -3.55641 | -51.03636 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be3fa7cc-7b05-3e80-9b1d-bc720565d5ec | -3.78059 | -50.13599 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1b268da-4d90-3ce5-83c2-aa49f377f43d | -3.39054 | -50.11232 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 6a06cf1d-eac1-3457-a104-f630a1436ff2 | -3.63474 | -44.94381 | 2024-11-28 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c3e66cd-636a-307e-8772-8906de298469 | -5.19504 | -44.24799 | 2024-11-28 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31cec29f-09a6-33c0-9f43-54d06e2d03ca | -2.60863 | -47.73359 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acf21b2c-f5ab-3f03-b54d-a02fed32ff73 | -3.9518 | -46.91874 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d91133a5-2243-393e-9335-ec5ed5f151bc | -3.94483 | -46.72544 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56ba70dc-6a57-3984-9d70-0343d3f502ce | -3.29019 | -51.15831 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df426783-bd08-3ed7-97fe-328c0d2d4a03 | -2.43473 | -50.41473 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fc45f06-f6eb-32d2-b1f0-42e4b8866274 | -1.63742 | -55.23147 | 2024-11-28 04:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7348fe51-189f-319a-9dc8-d3bcfcdf555a | -2.65641 | -48.5044 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7b8f689-9514-3757-ad7b-e97fe8e4cbd6 | -2.24699 | -51.87552 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79ccc4ba-6081-388e-9175-1b5dba9b013c | -3.17342 | -50.28514 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aabd2919-7541-39a8-927f-e867734e4ccb | -2.81733 | -46.83706 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ef97306-6b28-3804-9953-080254910ce0 | -2.86544 | -46.8701 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24b0704f-6f05-3e93-b83a-e02c25e51e3c | -1.56519 | -55.78544 | 2024-11-28 04:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 550deffa-288b-35f9-afcf-7fe786e4c8b1 | -3.2629 | -46.4428 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c81988a5-8ee8-3e2e-b7ac-7c2d75956573 | -2.85475 | -46.87212 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a83780d4-c966-3469-a367-611d593591aa | -3.57844 | -50.33796 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c922002-d5da-3b6f-a8ba-44f7e24ab84c | -2.63122 | -51.7763 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc714a14-ba6a-3261-a727-b85565b2c7bd | -2.59861 | -54.21883 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79becc1e-ac95-3c7b-a89b-aa53065764f3 | -3.96548 | -50.18575 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c22e88c5-38b9-348c-92c7-bf483c31ae23 | -2.82899 | -46.83865 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 871d85e7-4711-3a89-9338-2ff7b0c5f955 | -3.3969 | -50.70448 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a5f0361-f46b-3715-b225-1723c657fd75 | -3.71516 | -50.54118 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2388cf46-7ea2-39c1-862b-ccab2e2848e1 | -16.44381 | -47.04438 | 2024-11-28 04:25:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c63455a-28e1-3e1b-9626-a2a1e73467ea | -4.31592 | -48.08781 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cd8ce55-61c7-3835-9bf5-d4272eca1803 | -6.01328 | -38.65779 | 2024-11-28 04:25:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0790675d-2afe-3ce8-80f1-a374f6342b07 | -4.47172 | -46.36106 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e9876a9-dc2f-3dde-9f67-ac0bf4b52dfe | -2.75413 | -54.12619 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8d54268c-94f1-3eb8-8640-ab0400c22dc4 | -3.39101 | -50.11047 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 81da6d53-036f-3800-ae72-87f3b9cc962b | -2.61822 | -49.07292 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3891348-6bdd-328d-8fe7-fdcd8f7aef46 | -4.11962 | -48.8173 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 141d2872-2522-31f2-a53c-45b8557bb2d4 | -2.59976 | -51.82946 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4a2ca78-9c3d-3052-8294-53ddd60962b4 | -3.16838 | -48.58382 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15f3cdf7-8835-367a-9dfa-9bcaf02e52d1 | -3.09694 | -53.26034 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 431e12c2-2dce-376c-8935-0f546e8b59aa | -4.22172 | -50.88858 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2a54d84-65a5-3726-bf67-7cd851dd20e6 | -2.31346 | -51.96267 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86b4e865-f50e-356c-a53b-287c4bf93354 | -3.78528 | -50.13168 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1207fdb8-32b6-38a6-a8f4-4285f7efb8c9 | -4.65518 | -49.5188 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76528d90-3c42-3a67-bc4a-d7275fd11dc6 | -4.04915 | -46.83976 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82130746-ec14-3b49-8286-6c06e036d5b5 | -3.77391 | -46.69115 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5063cabd-1cc9-310e-b220-111f088b1095 | -3.2286 | -45.38928 | 2024-11-28 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50f067c5-dc61-33a2-90d0-371f85080928 | -2.83659 | -54.11879 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f3812512-e003-3bce-8bee-ec462e350af0 | -3.54104 | -50.40298 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fe844b7-2a40-339f-82f1-4b910ad12bf3 | -3.46776 | -50.25868 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32b7f2de-e3aa-304c-892b-ac3a897faf91 | -3.61231 | -40.8119 | 2024-11-28 04:25:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| be62ff19-95a8-3157-ab5f-dc051d8a9602 | -2.85595 | -46.84286 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d0f2073-8525-3438-88df-7cada474a41b | -4.178 | -48.62809 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7aac11fd-c4e4-3004-b828-32222df8fe6b | -3.23844 | -53.93455 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 834c6595-39ee-3ed1-aefd-158f68b498ba | -2.88788 | -51.58356 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 761841ca-83e6-3a7e-9569-298054831c40 | -3.8184 | -46.60451 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d892eb84-6803-3bd4-baa1-e04234c307e0 | -3.11404 | -53.26445 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c76bfe8-6e14-331d-bc80-801619e92bfa | -2.97076 | -48.00698 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14bfeccc-5f3e-381f-956e-b8251ae503f0 | -4.21707 | -50.89156 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ea1c718-ee53-3fe7-99eb-cbdda7dd0a01 | -3.0319 | -48.50378 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd479009-a4db-3f74-99fb-9c72ea828e64 | -4.05723 | -48.83717 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76acbc49-7f42-337c-831d-4119284b871e | -2.91169 | -51.7146 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ca8d24a9-d2f2-323b-a728-881533dd7ae1 | -3.34102 | -53.28836 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b717d452-9b04-381c-8bc1-eccdba76d808 | -2.25193 | -53.74954 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eeadd518-c006-3f0c-a91e-4a17e6d94c42 | -4.65895 | -44.04085 | 2024-11-28 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4dd0f9a-a1a3-387d-9cf4-d7db43f04092 | -4.67486 | -44.61368 | 2024-11-28 04:25:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7372297-5a89-3a4b-9b83-367a846dd4f5 | -3.95548 | -46.124 | 2024-11-28 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95524d3a-2390-3fec-9e46-a7d824dd58c4 | -3.70144 | -50.87943 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71c12ca7-1fe4-339a-9f48-61390b2a1b47 | -3.95907 | -46.91626 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 162ab281-7226-336a-980f-b0e1c85b3cb2 | -10.46606 | -49.65002 | 2024-11-28 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 352450fb-7f39-3087-a995-38fc9047b825 | -1.83809 | -55.5707 | 2024-11-28 04:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 377a4704-193e-33ac-8833-3f64fd756543 | -4.39138 | -45.90291 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 035a0522-28fe-308b-8dba-dfbfb921ed2c | -2.94537 | -53.72113 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 639e45a9-700a-393e-a2d6-9896688c5792 | -4.17432 | -48.45098 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80b6a7b4-36c0-3a6a-9e47-5353d38ac59a | -3.32491 | -52.76479 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4cd4c99e-9e33-3109-8ea4-66a5abed82d4 | -3.71104 | -51.81863 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b455b85-5748-31c9-9b8c-c411e4fd89eb | -3.24775 | -50.62146 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ac400a23-c4ef-3143-9383-bd2cb3d193e0 | -2.72216 | -48.89623 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fde3db9-77b3-3a8f-a771-1f3d405d3b2d | -3.97712 | -46.73773 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75141ef9-063f-3ec9-a70f-f6cca6d5ce31 | -3.27836 | -50.56065 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd4bbd4b-20d9-3739-a87e-8d2d0a0914b4 | -3.0492 | -48.51075 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57af4cfd-8110-3cc0-9792-10c95c8cb5e0 | -2.24846 | -53.46345 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16f2eb45-a788-3199-b1a4-7a5e67279a28 | -2.25346 | -53.4643 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb394465-8df2-3000-8e21-c5854e7684a5 | -1.89684 | -53.0349 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 912673cf-0606-309a-a90b-250b3d430612 | -3.1049 | -53.81614 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README61.md)
