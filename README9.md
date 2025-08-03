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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 884f22da-744e-3bf6-89ef-54a918f674ec | -11.78293 | -45.01402 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70a058d8-5990-3e72-8051-5843f63ace1c | -11.77518 | -44.99471 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec831e19-4f5b-3fa1-bca6-7f359773f1e8 | -8.01383 | -43.13805 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60331e31-a12f-3f35-9e58-514ec8efc9c8 | -8.01874 | -43.14447 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| eeeecce6-7fc0-3b9b-b044-4693b6e67ca7 | -8.00245 | -43.17022 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 41ac1fae-7f57-384c-a6ec-31638ea1520e | -8.00532 | -43.18427 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 72561e91-380c-3a21-b17e-5f3a3f95e547 | -7.99939 | -43.19251 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| bec39b81-375d-3714-b49c-2da226fb2e71 | -8.02162 | -43.12811 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f259549e-8939-379b-9f5b-0a89687de934 | -7.96006 | -45.11131 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1f8e36d-45bd-37dc-8d94-4660c8b29d2d | -9.39842 | -45.50565 | 2025-08-03 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a085acf-eea2-3dee-bbd3-98e2ae10f691 | -8.93549 | -46.74675 | 2025-08-03 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3bde27d8-04f0-38c5-85da-0f6ddfb63394 | -8.01485 | -43.16208 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 6a5e5d28-9487-3b08-a2df-82d48f7dbeb2 | -8.02962 | -43.14087 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4a522caf-c1e9-3ef4-8ed4-da14d83e6831 | -7.11392 | -43.48716 | 2025-08-03 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5d7639ad-e3ae-32c1-9ee2-15bb4853b9a4 | -7.12006 | -43.48443 | 2025-08-03 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa033bd3-9a98-3d30-943c-7a4a0baf1785 | -8.00293 | -43.17248 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2b4a7628-a29e-3893-97d9-410c98cb3002 | -8.01115 | -43.1567 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| cca0a2fa-89b3-3c4d-b3f3-c51040d31223 | -8.00528 | -43.15914 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 8b4ca81d-8433-3889-a5cb-2779554fac38 | -7.88079 | -45.53817 | 2025-08-03 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57b07950-7a78-352a-80cc-c72d3b1cbea6 | -7.95844 | -45.12015 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6149d39-87a5-3f96-9296-608af078dd48 | -7.9994 | -43.18678 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 146c90bb-7720-3f7c-9166-55d417f0d364 | -7.87553 | -45.53239 | 2025-08-03 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd64be51-f942-3cdf-aad2-1294d883f66a | -8.00705 | -43.14911 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 352c0fdf-6295-3eb4-b1ec-57972796f27f | -8.02104 | -43.13138 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 02e16c6c-8a8e-3a3d-85f7-4d72c6e9dc7d | -8.00588 | -43.18664 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 714820c2-b443-3eb7-883f-65fba1283c2a | -7.96689 | -45.10778 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70d753b2-ed12-35bb-8daf-dc77b5ca9446 | -8.00285 | -43.19765 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8f277373-1a60-3382-96d0-914e09d7b677 | -8.01423 | -43.16544 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2f5b6eea-8e13-3d91-bdc6-a13befb09bf7 | -8.01081 | -43.15441 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 5b1e4b91-7e38-3ee4-b96d-951a2ddb842e | -11.75762 | -44.97356 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b1f5973-8ed8-35d4-ba22-731da6537ceb | -8.0041 | -43.16586 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3e003e31-a50b-39de-9f98-e99c83123b5f | -8.93352 | -46.75298 | 2025-08-03 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0470359d-151d-31c1-99b2-3e3c94499d1d | -8.00471 | -43.18758 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 74351260-9e20-3276-ac26-791b177aeba0 | -8.00713 | -43.17441 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 6bffcefd-94b4-329f-890c-be31533197fb | -8.0152 | -43.13371 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7883b86e-5f2b-3a4d-abe6-b4800e4f0576 | -7.11526 | -43.47976 | 2025-08-03 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6c26723c-e378-3d38-963a-45d513f596b9 | -8.01405 | -43.14024 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db432706-c035-3d74-a28e-4c5877a1f285 | -7.99879 | -43.19587 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d079645e-1a83-31da-9ad7-33762c490949 | -6.20055 | -46.34714 | 2025-08-03 03:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcfac282-0abb-34d7-9801-27f6555d45f0 | -10.47658 | -46.9615 | 2025-08-03 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 535b8af5-0284-38d5-9075-d22b8bedc07f | -12.77916 | -38.49544 | 2025-08-03 03:36:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 217e7947-abce-3f15-8748-800ee7e70180 | -8.01361 | -43.16881 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 493f3054-a5d7-3ad6-9d5d-f009a4c695f6 | -8.00588 | -43.15574 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.7 |
| f74d0bef-a043-31c5-846f-817599413c68 | -7.88374 | -45.52711 | 2025-08-03 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aa1ed7dc-1577-311d-bb53-5f2be2e76ee7 | -9.38813 | -45.50551 | 2025-08-03 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48467931-4154-3c9e-93db-d7061df2718a | -8.93459 | -46.74755 | 2025-08-03 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0077a9d3-6d52-3824-b6d2-1a61fa86fe6c | -8.00307 | -43.1669 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 487b94d2-cdd4-3db7-9436-73ce6e1177a0 | -8.013 | -43.17215 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 89149bdf-c30b-38d1-842c-4ea95162c55b | -12.03555 | -44.02416 | 2025-08-03 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d11eaff0-0f06-3855-b07c-f2a608421f05 | -8.02149 | -43.12594 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eccd498e-5b45-375c-a9e9-af8b64f1be94 | -8.04667 | -43.10696 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9168e311-7831-35a5-9fd0-84c685d566ff | -11.76732 | -44.98309 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10e74963-90da-38dd-a17c-6c01bc5f5f8e | -8.00234 | -43.17576 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| bd920f70-51ea-3b29-ab86-89a5c43c48db | -8.00001 | -43.18344 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 9276d510-accd-3998-9328-3a8a2b3955fa | -8.00555 | -43.15345 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| bd62f039-44af-3d31-8f16-ac503c32c811 | -7.99586 | -43.18163 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| f9ee6c0c-f25d-301e-950b-6b29fe1f55a7 | -7.10849 | -43.48599 | 2025-08-03 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 81960258-5abe-33f5-b3a5-97a501fee15d | -8.01464 | -43.16781 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f422b811-23d4-3678-b9ab-27b94038108d | -8.04084 | -43.10923 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 290afc5b-59a9-361e-94cc-e4faf39d7a6c | -6.67385 | -44.36247 | 2025-08-03 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f405dd9c-2e80-3233-8eef-a201bdf84242 | -12.03611 | -44.02121 | 2025-08-03 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6f319ba-8ea1-3b51-97bf-831294b0b8a1 | -8.00646 | -43.18332 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 6ec5fda2-5cfb-3b8b-b1b9-badd3204e782 | -10.34274 | -44.90985 | 2025-08-03 03:36:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b23e515-e00b-3523-b4ff-80a3f66bbe8a | -8.01056 | -43.16006 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c3b066a3-46a0-3755-92b8-162471878d74 | -7.95324 | -45.12615 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4457896a-fb44-3ce6-9f0c-0ccaa45a242e | -7.97035 | -45.10136 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4cd65d3-5d99-3316-88ec-926497b90000 | -8.02089 | -43.12918 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cbe97fad-5cb9-311a-aa54-9a291eb39945 | -7.75715 | -45.11359 | 2025-08-03 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f32aa9f7-5ddd-3209-9df9-3023771d4fed | -7.75848 | -45.11622 | 2025-08-03 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 47ccef4c-eb99-3090-a1f0-21086210c345 | -8.00879 | -43.17014 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| bb0205c9-a7c4-373a-a899-8b7f4e977b6a | -10.47126 | -46.95473 | 2025-08-03 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a659e16-b09f-3d5c-98e6-d762e0b2df40 | -7.99754 | -43.19685 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c8c951d2-c3a9-3f09-8789-4284396e3721 | -12.77842 | -38.49976 | 2025-08-03 03:36:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fba98b63-9b7a-3c4a-9751-ca638b5be654 | -8.01608 | -43.15539 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 709d7c04-68f1-3090-815c-18ab630adc0c | -7.88201 | -45.53655 | 2025-08-03 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3bfd4c22-66dd-3041-ba80-4650c4b65faa | -8.01583 | -43.16106 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| b1b12157-984b-33b7-bde1-ef9e5af3662a | -8.04549 | -43.11344 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fc9d37fc-2b41-3d76-bb49-9da975515715 | -7.96171 | -45.10228 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 966deae1-3598-3642-ac47-1522442cfa54 | -8.00763 | -43.14583 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 53ca9254-7c03-3b52-94cc-03c58c734a70 | -8.01232 | -43.15007 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 9566c16b-6e60-3c91-b80b-bf7d188cdb26 | -6.49531 | -42.8164 | 2025-08-03 03:36:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1134c36b-6405-381d-91ba-3a61476a420d | -7.12073 | -43.48077 | 2025-08-03 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8aef406c-0935-37a7-9890-61ee25ee3f79 | -8.00063 | -43.1801 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| b35f3a2d-306c-327b-ac6a-67e9aacb0ff0 | -8.00368 | -43.16359 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ac78e827-3b3e-35b4-8dc2-35751ae65f58 | -6.5292 | -44.53639 | 2025-08-03 03:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e77c3fc-2cab-38d7-9d12-9012c6ee0240 | -8.01669 | -43.15208 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| b7df9398-4eb3-3cf7-9a06-1afbf2394518 | -8.00409 | -43.19092 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a9327ace-1cf5-3621-8218-b4f664c9a85d | -6.67466 | -44.35796 | 2025-08-03 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 741d76af-ad47-36c7-9caf-480ddca1c721 | -8.01524 | -43.16443 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 53f4cbfc-7ddb-3e10-af29-549067d0b87f | -8.94008 | -46.75394 | 2025-08-03 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e7e1ea3-347b-3d66-90d2-eabaf40bdd75 | -11.80447 | -44.93382 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b7fae4c-5eb3-30a1-bb7f-40ce08ae079a | -7.96525 | -45.11673 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f234a1f-e574-3d16-87bc-8f80d6b2c503 | -8.02902 | -43.14415 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a63f8ac5-f519-376b-8e02-5cc70689b126 | -9.39161 | -45.50889 | 2025-08-03 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dea2a751-0209-36ba-92ef-5c48a81b0e06 | -11.75226 | -45.00154 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c981bee-a06f-35a7-825e-fce0cd433f16 | -8.02794 | -43.12036 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 629e87d9-3fcc-3f2b-8d81-a799d95a4423 | -8.00896 | -43.16448 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b05f999c-9d59-3886-b9fc-fbe9ef3e2297 | -8.0199 | -43.13791 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4f781b63-f635-3a3b-8c92-e3d7e5b4d981 | -8.01817 | -43.14775 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| fc08a318-2e79-33b3-bba1-846cf9c08f06 | -8.00351 | -43.16917 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |


[Clique aqui para ver as próximas entradas](README10.md)
