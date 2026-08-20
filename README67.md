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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3b6fc23-30c8-3c1e-a32a-aa32b52fca17 | -6.80361 | -59.01704 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a6e3f57-3d89-3567-9b2b-1f5601d4aef1 | -7.82942 | -61.61631 | 2026-08-20 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bb4f073-f0b5-326b-b8a9-9354cf966e5e | -6.71367 | -59.09732 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a875aa0-6f7e-3871-a9b3-20d0057fc3b2 | -5.49409 | -60.13059 | 2026-08-20 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1948f38-dd21-3f28-97f4-3120014f163c | -3.10224 | -61.22245 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a286538f-9acc-38ec-b02c-74e39a906490 | -6.9252 | -59.35015 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da06bb98-5b73-3047-ada8-6bdc324d8f93 | -6.86886 | -59.02932 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de850728-c848-3e8d-9237-b68108a1a867 | -7.42859 | -59.79008 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a60605ab-f0cc-3653-a90c-7562453674bb | -7.54491 | -55.59756 | 2026-08-20 05:59:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c426e07-ab99-3848-acb8-b352869611b4 | -5.80204 | -55.73435 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07bdcc11-cc33-34e9-8965-f27cbbdb72f0 | -6.70762 | -59.10028 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e3a40bc-101e-37f6-9b34-4e68159dc195 | -6.84858 | -59.0198 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f1c93b0-b887-38c4-961a-7d07185f06f7 | -5.80965 | -55.7291 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4790219-c06e-3ff3-a991-07f0c91125b3 | -6.38049 | -54.94108 | 2026-08-20 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2534a9cd-09ff-32f5-a5af-699dfe8bfb9f | -6.8031 | -59.02072 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46cb5d92-11d4-3fc7-b4d8-c435d352371f | -3.09772 | -61.22179 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 412eed21-aa0b-3103-9e21-272f1e3eda7e | -6.86373 | -59.03289 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4213e4d9-1214-3f17-a79a-deb676f6791c | -3.10054 | -61.20362 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1973973-9ddf-3dd3-9103-c8df4be6c82b | -6.71419 | -59.09363 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77ec0b0b-455d-36f4-bc8b-8cce94691673 | -7.54928 | -55.56482 | 2026-08-20 05:59:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b27fff4-ec33-33be-a66b-c9e98183d2ab | -6.95604 | -59.04934 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f179f579-0906-3471-b2ba-28efb69e1ef4 | -6.74983 | -59.16227 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f08cd38-99e6-3204-ac61-fc1242b7edd1 | -6.08973 | -57.92537 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc59f90c-a19b-3820-9d93-8b607ca5fb88 | -6.37957 | -54.94801 | 2026-08-20 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1b04b26-c3e7-331d-9b0b-c84a9c63d39f | -3.10365 | -61.21337 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f940823-f280-3057-a11e-95688019f51b | -7.83012 | -61.61131 | 2026-08-20 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cc92da3-bbe1-398b-8452-880e3c04faca | -5.79612 | -55.72747 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7187d70-25df-3b14-85c3-c760637be441 | -7.04671 | -59.84668 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c75f4daf-9f14-3c47-8a59-e810b7a267d0 | -5.80453 | -55.71648 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1dd210a-3e6e-36b4-beff-bf64c52759cf | -6.84352 | -59.0155 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53a9f854-0747-3b60-997b-03758a31d871 | -6.74357 | -59.04231 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77aad90b-2f9c-3a6b-a91c-f35fd68af2b1 | -6.97673 | -59.58615 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 973e4872-8bb5-31d6-a8d9-20bf4904701d | -6.70108 | -59.1068 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20d8f7a2-159b-3ef2-9a09-754cb5c20e3f | -6.09092 | -57.91681 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b8473bf-7d03-3ce8-9420-cc8414f646ab | -6.71471 | -59.08989 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 672b3792-8f26-3afd-b3fb-96a0ea374c23 | -3.1008 | -61.21067 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b803424a-4989-3f8c-9a7e-f8b6793cd440 | -7.55625 | -55.56574 | 2026-08-20 05:59:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fcaf6e5-e7e2-3759-9853-f0bd6e088e8d | -3.09878 | -61.22433 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 743f193c-f5cd-3824-a8e8-8f8de80e73ce | -7.53365 | -55.5759 | 2026-08-20 05:59:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7406306d-e6d0-3b24-91c4-585ae4002d2c | -6.91576 | -59.34938 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2c69b37-f450-36df-95b1-14a957c680ad | -3.90059 | -55.88122 | 2026-08-20 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4fb4f6f2-45ff-36e7-b388-8149b8295e01 | -6.95554 | -59.05307 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2acb9435-9c8c-3e0c-92b0-2658b530cecf | -6.69463 | -58.9497 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54d048b3-557a-33f4-8991-0ca608672313 | -6.70159 | -59.10315 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c2017ba-bc16-3ea6-af84-834946372be4 | -5.79994 | -55.71642 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d48ddbc-2a7b-39e3-ae52-0cc65708a9aa | -6.74934 | -59.16589 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7cd1000-d009-3566-ad81-b66a4f17d489 | -6.08378 | -57.92481 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fbe7229-fd75-3e4f-8443-ea3224f16a62 | -7.05201 | -59.84727 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4aae2319-f1ed-32b3-9e9a-403798188b8a | -6.80471 | -59.58124 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 03549c1a-7a42-3554-8eda-c3d63f2ab752 | -6.08438 | -57.9205 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8afce24b-b879-3e0a-ac3c-742425a27a3f | -4.38474 | -55.47647 | 2026-08-20 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c5d772-b008-31cd-9432-f898eb3864f7 | -3.25714 | -61.16585 | 2026-08-20 05:59:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20153fb5-ec91-3418-baff-b3934ac8c683 | -6.70178 | -58.93912 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09fb77ec-401f-3241-959c-56ec5b7ef19a | -6.7066 | -59.1075 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b805cdf-953a-396d-8483-6b7f3959712f | -6.14737 | -57.85882 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65856806-ed9b-3d57-b268-f287af2d156f | -6.8623 | -59.03593 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35644c64-ceb8-35df-8dc1-609d94a41ef3 | -6.70864 | -59.09297 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0237bd98-ad4c-3a0a-a2cf-02ef89f5c33e | -6.69655 | -59.09891 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37310769-b46c-360d-9e4e-8edd24e08a48 | -6.59126 | -58.96732 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 904680d2-474b-38d0-b475-de6825c9aa22 | -6.86981 | -59.03 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f15b33a-ea17-33bd-953a-3b560d2b88e2 | -6.70258 | -59.09603 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de08e61f-1a0e-3332-a675-08dca9f17b80 | -6.92168 | -59.34665 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef3c0a38-c243-3243-adf3-50ffd6ce2c53 | -7.8723 | -61.58628 | 2026-08-20 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbb78806-dd52-3efb-9c41-c30327ed6e28 | -6.13784 | -57.8835 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c19de492-7053-39e6-94ef-2f50b2b185f1 | -6.58267 | -58.98842 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7047d101-2aca-3b5f-9ee3-b78291ef588e | -5.49238 | -60.14232 | 2026-08-20 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf330702-90e6-3db2-9968-c5fd4bea5a93 | -6.73851 | -59.0379 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e48290e-3ba0-325d-b9d3-82ac7dc3b430 | -6.84804 | -59.01556 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56b520eb-f66e-3ee4-9fee-f846f8ab6024 | -7.0573 | -59.84788 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94f24815-1784-3dd3-8402-c45fa74d4781 | -6.70074 | -58.94663 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61b32ecc-bac9-30ec-8510-ac2b00042f81 | -7.53876 | -55.58348 | 2026-08-20 05:59:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad5a073f-7075-3284-b2ec-46edd4bc3e76 | -7.5397 | -55.58357 | 2026-08-20 05:59:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8550bb7-0734-36c5-8f66-714a6d33a172 | -6.74788 | -59.17657 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c6ca485-c128-3580-b882-5cb871b28f10 | -7.42773 | -60.03047 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17e33472-a3d9-3108-9398-ac37caaac016 | -6.85265 | -59.02347 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcb8c2e9-1d28-34a0-86ff-e67a8b3bb9b6 | -6.7031 | -59.09234 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d2bc6f9-17df-3b59-8845-46710d903bf8 | -7.44705 | -60.00705 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4d1a0eb9-946d-3dcf-a55f-23e21ff3b26f | -6.38397 | -54.94166 | 2026-08-20 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 864417e5-20ff-3d27-9067-a7081b590780 | -6.7023 | -58.93528 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7644d1f2-6720-3f27-bdce-594e144dbc9f | -7.44181 | -60.00626 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8894f206-b145-35a8-8aa8-2ca1fddbb1da | -7.0574 | -59.84394 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 460b5287-0970-3266-a856-686b7184ea48 | -7.01078 | -59.59809 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c017640-347d-3dc3-8114-220c7f89b88c | -6.70208 | -59.09961 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8059c008-ffa1-32ab-b4bd-ce2988dd3ef9 | -6.7521 | -59.46712 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a372a259-dbce-36f2-ad78-c32a7abd7ebb | -6.91926 | -59.35291 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b99d212b-6ea3-396f-8e01-56ae9c5b49d4 | -6.9212 | -59.35021 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 27793714-76b2-366c-a00e-fef01fcddcea | -6.70125 | -58.94289 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69de7671-8014-35df-868a-850e9d36ae18 | -6.59026 | -58.97458 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5677928-b83c-3f2c-bf92-72c4f8edd8e5 | -6.96131 | -59.05729 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36fd58a8-c01a-37f4-b1bd-201f80c95e78 | -5.7953 | -55.73343 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cac30a2-b932-3017-9be2-cc3a036a3afb | -6.9568 | -59.04914 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f82d87c-5357-37a4-a19a-8347f51ba52f | -4.78695 | -62.92324 | 2026-08-20 05:59:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f946ff18-d7de-3075-83d8-2e283f950acf | -6.58318 | -58.98479 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0553ba9a-923b-3eac-86a6-9df576f21e81 | -6.79309 | -59.58639 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1ded7a8-0b9d-3665-a859-b5c61b9ea5e4 | -3.10533 | -61.21132 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6813826a-7311-3968-a8e0-f78bc73bd3d9 | -6.91876 | -59.35642 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d70e438f-4f3d-34dd-b65b-4ef1d03bda2f | -6.38671 | -54.94878 | 2026-08-20 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d5bbd13-38ff-39aa-bcf5-48829728b724 | -6.69758 | -59.09159 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0fd689d-cc01-3516-b819-296c8ba258f6 | -7.53182 | -55.58237 | 2026-08-20 05:59:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74c20300-1068-3a4e-a0bc-9ec8894dd0c4 | -4.78918 | -62.92031 | 2026-08-20 05:59:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README68.md)
