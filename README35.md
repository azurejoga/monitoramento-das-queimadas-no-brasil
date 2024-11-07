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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba2cc1ca-a693-380c-b2a3-e4b25deb4e2d | -2.80955 | -51.4929 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbd6b0d7-5d69-3ba8-807b-459c0c20a8c2 | -2.65085 | -49.89177 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6b00f6c7-5dfa-3967-bb00-949ac8b83f2d | -5.58952 | -45.21007 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 71d6ba31-a693-3250-a83f-84348659ac45 | -4.99577 | -46.90178 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc68eba0-cca7-3d9f-97ef-b48a55e811c5 | -2.60466 | -51.30371 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b60c81e-f155-3e5d-84e2-4a8c268a31f0 | -7.37031 | -42.95697 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d176479-7070-3437-b1e9-99e04e14592b | -3.17481 | -50.59886 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 598912a9-5a1d-3906-bf74-c54dbbbd4350 | -2.81646 | -52.96594 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3dafa28-0b03-3486-bf80-28c1486debc5 | -2.42915 | -53.66801 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 117de9ef-f508-3ccf-89c4-c9b44379db48 | -4.24191 | -48.53825 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b15e7c4c-2053-3290-90bf-9159146266b6 | -6.13578 | -43.96078 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4be22a2-06d1-3d0c-96c5-2e9fca284877 | -3.70585 | -48.99871 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a466a3d-c941-331f-b12e-0a28b4dda9d1 | -2.95455 | -49.57148 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dd99d00-cfe0-32f9-b2b4-bba63ad62525 | -7.01104 | -45.00971 | 2024-11-07 04:18:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5993d101-85ba-3f27-b482-a3bb1050dffb | -3.34839 | -50.25952 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f996b3a-3bb0-37f4-8636-a388293e3fb9 | -3.04026 | -53.28157 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3ee6265-e438-32a6-94a1-ea5ddc89f628 | -4.80666 | -50.82697 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 981b4e03-099c-3414-9048-6dfd5720c724 | -3.51949 | -50.34324 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2c95605-395f-3ed2-ba2f-6d97f106dc50 | -1.52657 | -52.49646 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10bb5a38-0319-3d26-a3e3-40122b54e4ab | -3.70642 | -48.99522 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95c768bf-8fac-3e11-aa97-0a6b3aaf4f0e | -5.84916 | -41.49643 | 2024-11-07 04:18:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9d40bde3-4b82-3c64-9cc5-f8fbfa920cb3 | -3.01693 | -53.42511 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39096dc6-72b1-3e6c-88e7-64b5d0d82025 | -4.07544 | -48.31385 | 2024-11-07 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 402da6c4-09ff-37ee-8151-fdb9a09fe215 | -5.98392 | -45.35864 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 98065106-d3e5-3186-9838-3482d2e2cb8f | -5.37462 | -46.26797 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62fd87ff-c23f-39b3-8b12-d96d4e6c5540 | -2.19467 | -48.37791 | 2024-11-07 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3dd2936b-f4e8-3ed3-bb7f-aa4645942d4f | -6.0825 | -44.71434 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0e60cb47-cf94-3fb3-b0fc-8955ae107e0f | -4.67234 | -46.34024 | 2024-11-07 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0870d172-bde3-3072-8732-0f89862f48f3 | -3.43438 | -50.25963 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 965c1d7a-5586-3060-901f-f1cf21c387ba | -3.21948 | -50.38472 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 87cdb80d-9aa6-3194-9ead-89f6f6ec362f | -3.18003 | -50.59512 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25effeeb-1168-320d-a828-64a87a1c0a13 | -3.04082 | -53.27816 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b935ab0-e4d7-3ad0-b8fd-88dbdefbf243 | -1.32894 | -54.63931 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 094a30eb-c086-3c7e-92d7-131910f6b9c8 | -3.29198 | -50.0804 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e1a038d-2f85-3df2-adaa-a8a274fd78df | -5.9795 | -45.36508 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3d92e9b8-74b7-3c47-9d9e-c6025acd38df | -3.18526 | -50.59137 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e7111d9-a44f-3007-9649-250f1ab46e70 | -3.36621 | -49.75883 | 2024-11-07 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13ec5f63-0ada-3f88-8eed-1a561864f529 | -5.11396 | -46.08046 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e03cbd76-3c67-360a-8113-42b78143a1d5 | -4.67524 | -49.62889 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3752617a-c677-3a51-9cb7-6b0703a0bcfe | -3.18452 | -50.59584 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bbf0af3-6de5-37e4-9728-256948db1e94 | -1.21975 | -54.54093 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a09ee8df-128d-313e-bbd8-26921565b2e6 | -5.37122 | -46.26741 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bb05dcb-4e52-341f-bd3c-22106584747d | -5.07558 | -45.51287 | 2024-11-07 04:18:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dd63253-dece-300d-a52a-0f4546b20d5b | -2.93475 | -52.53959 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39015297-7883-3171-9740-24843049bd70 | -6.48695 | -44.68944 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 570ae6a2-c96c-36e8-b805-ccf55deffa50 | -2.65783 | -49.87616 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c9c51613-e636-3515-afc6-534545422e70 | -4.6695 | -46.336 | 2024-11-07 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5147cd67-14f2-3c5a-9d37-5ea4fdf58bf7 | -4.99989 | -46.89843 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7640e82b-9a70-3280-8113-5e602fd6491d | -5.20512 | -47.46445 | 2024-11-07 04:18:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bba7114-50c1-3637-8be4-dfac52a4114a | -8.6683 | -36.21239 | 2024-11-07 04:18:00 | NOAA-20 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 037314fe-8622-3162-af6b-f23772b966f8 | -3.18078 | -50.59064 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93f3c546-2b82-34a4-95b1-581cd33234f8 | -5.20545 | -46.18846 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96f68928-b3a0-365c-bda1-06caf538ac87 | -5.98282 | -45.3656 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| cc5590f7-95ed-3af3-a9c4-7dd5dc0a2d56 | -4.11288 | -48.86516 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d7ef0ab0-049b-3192-8d4e-2046ebb91d69 | -5.79188 | -35.38499 | 2024-11-07 04:18:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4ec63dc4-5f5a-32d2-a62e-11b8a6c74d8b | -2.61617 | -51.2976 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b5c15616-289e-39af-a30e-ceabb5924501 | -5.81383 | -45.95765 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| feef07b8-add0-375a-bb4d-45377ae8fc04 | -6.64601 | -43.4079 | 2024-11-07 04:18:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36bbd130-a23c-3343-a809-98a6e0161f81 | -8.34824 | -43.59349 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31bf8e82-6c93-3b63-a04c-ccb2824216b8 | -2.76304 | -53.22073 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08d999a9-91b3-39b0-9336-7923d870206f | -3.23972 | -50.45519 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4b1541cd-0faf-383f-bf12-0fb717aaf321 | -2.70634 | -46.6727 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a838ae14-6e14-30ae-b9a4-f537c3158faf | -4.76779 | -45.74118 | 2024-11-07 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1755ea6b-6cc5-3621-87f3-f3f6d3dc80e4 | -5.06809 | -44.22963 | 2024-11-07 04:18:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc8a6f64-359c-3969-807c-988800bba6cb | -2.15333 | -53.65429 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2ca08d3-b770-3f2c-90ed-a0feea92ef18 | -3.24221 | -50.01936 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7713b210-ec31-3d2e-88ba-b9128c4800fb | -1.1583 | -53.7253 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce3d51f0-f0b6-33d7-bf0d-fd160d4ad4a5 | -2.20845 | -53.72569 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3a2aa004-adea-3208-914b-ebd76fe6a91f | -2.93421 | -52.5429 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64aca20e-a91f-3bf0-a22e-b9783955e8c0 | -2.72755 | -54.14433 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5914ae2-136c-30b7-b41c-67c07b1c3494 | -2.72025 | -51.71076 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| deaa47f0-b528-3132-a186-7a5133dd49b9 | -2.9769 | -50.29729 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41fbaa93-ddfb-3555-8271-2939022c9b0f | -6.23097 | -45.32242 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eda2bb38-d92f-3baa-899a-394f769b428c | -3.65396 | -52.34284 | 2024-11-07 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f940fef5-eb89-304c-b605-8411f5097d30 | -4.93728 | -43.63156 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43281df9-2177-3913-b914-d2d985e4d14c | -5.04021 | -44.75095 | 2024-11-07 04:18:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 131805df-0ec3-3f8b-b0d2-d124bdd3f341 | -3.17929 | -50.59959 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa3ea204-825e-346a-8615-4ebe0a935a66 | -3.56576 | -52.69747 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37aa8999-3834-38d9-89d7-02931e3e47df | -5.97839 | -45.35063 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc28f879-1010-3ebb-8ebb-859cdb4e3d22 | -5.95897 | -44.26693 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1bd6651-c8b6-3b15-8cb5-8db0f860e1ef | -2.82634 | -52.90638 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6074ba5f-1a91-361c-807d-7fc9f805c016 | -3.5159 | -50.47346 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c8149761-1023-37e5-990f-5237cc29af51 | -2.84656 | -49.81324 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6bc7fe9c-0071-3172-876e-f5e780ef1ad7 | -2.81133 | -52.93123 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d444508-674d-3ddd-a3d2-25e10d64f8a0 | -1.28991 | -54.56644 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4943ec7c-c300-38c5-ac15-19b549b82c9a | -3.30791 | -50.09155 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7ffb10e4-19e9-3942-be9b-a1862c0d83c0 | -3.13527 | -49.22699 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3565e04f-f12c-3757-8a24-8f12bbf4fb59 | -2.75102 | -53.2262 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e1bf6cc-d8de-3229-ba0d-b49179cb63ae | -6.29636 | -43.84682 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 50e6c458-70bf-3431-a07e-bbda6f986b9e | -5.25425 | -46.66951 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dd738e6-bf6d-339a-a79b-50c39e8e3fc4 | -6.13469 | -43.96775 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ff8be6e-0da2-3f7b-8b75-1b888f10e125 | -6.07535 | -44.71675 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cac3b811-8e00-3431-921b-babb0b451e0b | -1.38629 | -52.2047 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d9ae94d-c61c-3c37-92b6-f87af946ef8e | -5.16577 | -44.12483 | 2024-11-07 04:18:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d3cf59e-f689-3ab8-83ba-69e2b1a694fb | -3.48555 | -50.38599 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1ea4a1a3-97ae-35a8-a2e5-802da8229832 | -1.93013 | -48.94277 | 2024-11-07 04:18:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8610383e-7160-3f37-b8b9-85b525012260 | -5.71705 | -46.5185 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35880ca6-2138-3cab-9ed5-2678b89b5d08 | -3.7641 | -50.0038 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef09f858-e841-34fe-b764-05ca417be7df | -5.02676 | -46.84274 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 838b8475-e669-3845-ba3a-5fee78c5adb9 | -5.01627 | -44.36223 | 2024-11-07 04:18:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README36.md)
