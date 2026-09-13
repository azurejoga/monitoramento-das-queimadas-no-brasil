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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 066fc47e-d31b-3208-b7a2-63597fea2e5d | -6.28574 | -59.92615 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2a5de6c-0f15-3e24-9964-a374ea1e016a | -9.38001 | -50.12017 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fface4b8-1d63-34b8-89de-b8a6a4f7c7e9 | -4.86414 | -55.99902 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81eb0db5-6365-3bc1-bc0f-4d4e466583c3 | -5.48501 | -57.23257 | 2026-09-13 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc96a536-100d-3bd8-ab67-dcc85db6646d | -2.71719 | -57.60213 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38b98138-2c46-30b2-9d48-8e8338c95821 | -7.46662 | -46.14343 | 2026-09-13 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77f6a7ae-9538-3f17-8f52-05846ec0a9f0 | -8.09929 | -54.8605 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31390c8f-23c2-3005-8f11-4b889b44c644 | -3.44158 | -57.87105 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1bbbcf7-6655-32a4-9cff-8936bb94d082 | -3.76987 | -58.8458 | 2026-09-13 05:10:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9994399f-4c5f-3e00-b3bf-a32fe8bfe653 | -3.07729 | -61.01032 | 2026-09-13 05:10:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c91c6c1-d946-36bc-b4e2-fe9ca8510cfb | -3.49933 | -53.73591 | 2026-09-13 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9840fc3d-912c-3405-b32c-92bac018d396 | -4.53383 | -55.61798 | 2026-09-13 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8040afc0-6101-3fa8-b5b0-7aecffd1c774 | -6.68019 | -58.87598 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 492a2d1a-891d-3acc-9d46-efdf5e347df4 | -2.95813 | -50.40141 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b553f7b8-f1d9-3de8-b96f-a3f46ef175c1 | -6.23831 | -51.70115 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51cf03e9-082c-3298-a1dd-be9881c4f3c3 | -4.53484 | -54.92479 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd9a51e5-f408-3c82-9cf6-7e5acc141f3b | -2.67906 | -57.5411 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5ae4f53b-d83a-3485-acd4-52dd8cdc8170 | -8.11283 | -54.7955 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14ec89d2-f309-3233-a6e1-e4cf0a2c08d8 | -8.0379 | -54.85458 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fd1f8a6-74de-3ebf-a616-30e4f11bbe19 | -6.27366 | -59.92889 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9878bad6-1845-33d8-9951-5572859b4109 | -4.86745 | -55.99955 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d58d17d-3014-3ec3-a438-5a78afcf22b9 | -6.64493 | -58.82481 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff294b4d-8d28-349f-a7dc-4098e8704bb4 | -7.96796 | -43.99286 | 2026-09-13 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7ed75e0-d5e6-343a-bb89-2d21fbe1aede | -6.11083 | -57.63309 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e86e2be2-503c-3d11-9e73-4a8469d8e0ab | -6.60029 | -58.85532 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26e6f7ed-2093-3ca4-8381-ef24d4be51ad | -8.04804 | -54.85617 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a7fec97-1c97-3273-b4d8-06b36a70c950 | -3.33851 | -53.26452 | 2026-09-13 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c3a61dd-e2d4-3517-9ddd-a82ee454e094 | -3.64011 | -58.63077 | 2026-09-13 05:10:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7caf75a3-c9e2-3129-87ac-f5158b21b020 | -6.06693 | -57.73133 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13d23e7a-64e6-3756-9bf7-afe6fc01591b | -7.86332 | -54.71303 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8ca8a5e-f3da-32fe-80d4-7d79444310e8 | -4.45664 | -50.16684 | 2026-09-13 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05755573-f0a9-38db-b37e-254d4e2e8cee | -6.59451 | -58.8461 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f00e3774-3307-32bf-bc8b-52a781e80e4b | -8.6095 | -55.22724 | 2026-09-13 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46e92edf-b4d7-31b1-9292-8de8a54c9db3 | -3.30514 | -57.88339 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 431f72af-c84e-3f43-a146-8869dbd5cb1b | -6.28499 | -59.9307 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20880667-77ce-3284-aaf1-d99c71c1183c | -2.94252 | -50.40717 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 666080ad-2f5a-3f32-b4e7-096b410d3568 | -3.64375 | -58.63134 | 2026-09-13 05:10:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 000ae46b-ca0a-37c6-a96f-3a3110d0a9dc | -5.97294 | -57.77021 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31acaaf4-4478-3b36-b125-f69151c0e957 | -6.36768 | -57.86685 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 962c8b21-b88a-35a7-af16-378787b2b6d8 | -6.16637 | -57.7247 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 99a1f73d-c426-3498-b329-0039cbfe74d9 | -3.3863 | -50.75269 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 581371ca-6fd4-36d2-98a7-608c1d438207 | -8.05142 | -54.85669 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a72e608a-c276-36f1-a176-d08bba0599ea | -5.89175 | -52.25772 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0e006e4-f0ee-32ff-ae7d-e3a02fc352af | -5.98097 | -57.76396 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16e46ea7-33be-39e2-9ad9-5fbbde5fa0f2 | -2.96852 | -50.41347 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd562580-74c1-34d3-885e-c57a9bee9875 | -1.71745 | -54.95446 | 2026-09-13 05:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d63eeee-1813-3de5-ba0d-329471333e19 | -6.30533 | -59.9955 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9389fe3-f7a4-31eb-a540-b4be4f0743c0 | -2.74477 | -60.2375 | 2026-09-13 05:10:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8beeafd7-0c9f-37c4-9ade-3b90d55e69a4 | -6.6972 | -59.14151 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 193a4ba3-3c28-38a3-ac09-a8dac545d8db | -4.7996 | -42.89437 | 2026-09-13 05:10:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 045e5e66-3d6a-31c5-b73e-b87bce7a8d13 | -6.28046 | -59.93466 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e97415b-c842-35a2-a90c-1624b0af378f | -8.01575 | -54.85581 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cd64222-1f2d-312c-a21e-ec007d99b003 | -2.8298 | -49.23269 | 2026-09-13 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e88635e1-9261-30d1-a9ae-81a1c1895b6f | -7.37077 | -45.3707 | 2026-09-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43c01f30-ff03-315b-b460-1f118d5b9cc5 | -6.37734 | -58.28598 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6da77d0-3291-3872-b010-10e40ae54c14 | -2.66246 | -57.51086 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd8ccd04-b7be-3000-b040-af32d2ad61a1 | -6.23272 | -51.68574 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac2eb634-ba8d-38f3-9f5b-38d04662b04e | -2.63519 | -54.75768 | 2026-09-13 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04c34aa5-6f77-3903-9d16-1dd092d7ba9f | -6.68204 | -45.4799 | 2026-09-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4376133-a793-3eaf-a8c3-860dc069c478 | -3.87598 | -51.19419 | 2026-09-13 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d849ffed-b15c-3b9c-a5cd-4a70f525d353 | -3.04861 | -51.26608 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cdb933d-efbe-3fb0-b5c9-884f192d474a | -8.05874 | -54.85413 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7cd9b98d-664b-34fc-b450-c15c982c0856 | -7.87123 | -54.70676 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af95807f-8710-3097-b3de-09b4f05f5133 | -1.46167 | -52.96575 | 2026-09-13 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6ec3d802-a715-3c02-b944-d52887c0aea0 | -8.05647 | -54.84633 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dff52fc4-b00e-3669-8a3d-f5d462edd5f3 | -6.22748 | -51.69469 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4bbc565f-8c2b-3848-baef-50397056485c | -6.23902 | -51.69637 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6800c6fd-b3ba-3592-afee-2b46e55d961c | -6.66888 | -58.87825 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f0bbfbc-786b-327d-8534-05b3486c159a | -3.3324 | -42.30586 | 2026-09-13 05:10:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8fcfc433-af2e-3f65-9fbd-57bd86c4cee7 | -1.65436 | -55.18036 | 2026-09-13 05:10:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a1791dd8-76a9-3b88-b006-51d010507259 | -5.10219 | -56.12575 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fc4dfe6-fbd6-3f35-b851-8d279e7ccb43 | -2.95524 | -50.4039 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16869352-31ef-330f-be28-4657796290b5 | -3.16807 | -58.65339 | 2026-09-13 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5c46f6e-4004-3254-b603-8e20f6b7ea82 | -3.32762 | -42.30067 | 2026-09-13 05:10:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3f510431-b76d-3830-8de1-83cb7ad6e03e | -6.60384 | -58.8559 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84c0267a-d3b0-3a43-8b1e-cd4d5c9b6ee6 | -6.0881 | -57.86008 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9928be7d-b954-3df9-b565-25e448597e57 | -8.31938 | -49.68777 | 2026-09-13 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10637144-d901-32f5-baeb-3ae805a2156a | -6.66533 | -58.87766 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b64b2abb-c45d-36f2-a571-d6f593bdebdb | -3.727 | -61.75116 | 2026-09-13 05:10:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bc5f1db-dcdc-340d-a560-6417887daebc | -6.72236 | -50.4715 | 2026-09-13 05:10:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 455b46ad-9872-3ea9-b20a-afd17178a5ae | -6.03265 | -57.79136 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6312d88-35af-3168-875f-dc68f4ed80ca | -2.9621 | -50.40202 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3db83239-86af-3388-8390-196a3a9a58e1 | -8.0548 | -54.85722 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d8f5a08-0471-3c75-801a-29bed50c1b8b | -6.2302 | -51.68762 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3369ce45-192d-336a-95ad-cae3ea89843f | -6.7955 | -58.79096 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31f3ab02-0196-3fa6-9b08-d46cc1f674e7 | -9.38447 | -50.12081 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5187b8e6-dae7-36c7-b103-323381b26a15 | -6.11572 | -57.66759 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 49ba8226-4589-3640-90c1-77936345de58 | -2.97314 | -57.21381 | 2026-09-13 05:10:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 757f1196-4c50-3ddf-8cf4-c67c3cfffe0f | -6.37958 | -58.29422 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 619197bd-ee3e-3e14-a24f-c7ec022e389d | -8.53588 | -54.71001 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f46416c3-1391-310e-a6c2-bd491249c10b | -4.66693 | -55.99997 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3195c20c-6b96-3b79-af08-a46294821548 | -5.18679 | -49.27788 | 2026-09-13 05:10:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3421bd5e-1cb6-3844-9a4e-d86a205bc0b5 | -2.96082 | -50.39427 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b8244894-f872-3e85-9af7-64a696fe0dc6 | -2.7813 | -51.36513 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f01eaaae-5968-3f7e-b3dc-bce9d7f6bd19 | -7.42488 | -55.52799 | 2026-09-13 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d12628d6-52cc-36c1-8855-2152cec5c7f8 | -3.52207 | -54.47725 | 2026-09-13 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d577323-5df4-33c7-9d19-f731ce238ff9 | -6.9602 | -59.74506 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a41938a4-8cc1-33ab-8e6f-f09c80019d93 | -8.02983 | -54.85428 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e115b5aa-977a-3468-aa7c-7ff805db80f1 | -7.37309 | -45.35315 | 2026-09-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3f01140e-4a00-339c-88e5-bbcfdd0782b5 | -3.39964 | -61.30963 | 2026-09-13 05:10:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README51.md)
