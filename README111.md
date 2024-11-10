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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd147665-2fce-3296-8212-05b7cb66742c | -5.41637 | -47.56981 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f93b001b-8de9-3d10-b15f-f40680b0de96 | -2.82528 | -49.43969 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a869507-6a23-3475-9ba6-a3fa67ec05a0 | -4.51546 | -56.08236 | 2024-11-10 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8c671d4-03c7-3191-8c5d-334d1213e4b8 | -3.21428 | -50.38005 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70764dbf-8c0c-33f5-9024-4cddf88988c0 | -4.54918 | -50.33092 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b990aa51-9a56-3892-9ab7-78c903764b67 | -3.51785 | -44.03904 | 2024-11-10 04:38:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1da85bf8-a505-3696-8757-b017520fea5f | -5.3651 | -48.91092 | 2024-11-10 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93bd8ce2-e7a4-3a9e-aa0f-433c30c0661d | -3.41075 | -47.58572 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a247e873-7477-3f8e-972d-15d7191a5fbd | -2.59393 | -48.33192 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c52b4fc1-d357-3468-9281-a0292d7293ca | -2.90071 | -49.38672 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83ca7228-2550-3f8b-977d-435fa5f026d8 | -5.52768 | -41.69455 | 2024-11-10 04:38:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0a928b28-f958-3e57-b397-de9de1db6f15 | -2.92977 | -49.50619 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ad1169a-0816-3734-bb48-fc6686b15468 | -3.05019 | -49.53937 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17b4d553-221d-3fe6-95a6-9f5030550687 | -2.56827 | -48.25731 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a39515ed-0c1b-3296-b8d8-08113c644205 | -2.40088 | -50.44088 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7801eac-71c1-3bd5-931c-88207c0f4ae0 | -5.8182 | -44.11833 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 799f26fe-430f-3f44-8666-c826aa03fd0d | -3.55861 | -43.57293 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35ad8f84-cf39-38f8-b665-50a92b8d9639 | -3.32363 | -49.90821 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81973673-8ab9-318a-a7aa-ca90f0998eaa | -2.83647 | -49.4774 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24492be6-7c4b-355b-8814-f934b85b9e73 | -8.8955 | -44.22852 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e09b39cf-4302-36ae-94be-fa1aea7924b4 | -2.95686 | -48.02353 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77ca5d20-77c3-3f37-8a2d-d9c57b332985 | -4.15985 | -45.74681 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 60f2fccc-2d96-3566-a156-41798a82ee75 | -3.02088 | -47.95945 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f998583-b422-3409-83a6-1fe548893a1b | -2.07604 | -52.04575 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68026337-2756-3246-8058-2d4eaf75c11b | -2.95531 | -49.57497 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76ad2c7c-d9d0-38d2-954f-5e787408edd0 | -2.976 | -47.92347 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83de5cbe-06f6-3c5d-83d7-64db5ebfcc9b | -2.87788 | -49.37957 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30aec617-060c-3b49-9e38-9e322be7ab65 | -1.44786 | -55.51351 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 192fe10d-dc8f-37e6-8af7-8ebb1f003050 | -3.25887 | -51.00691 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8a8faa7-2339-3f31-a480-7d1982f8ac3d | -4.26839 | -47.07605 | 2024-11-10 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccea1708-5295-3951-9f23-41ca6bc3c527 | -3.23398 | -50.4549 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c365706f-c325-3421-9095-6d664cb235de | -3.05509 | -51.08677 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27c448f3-d7ff-338b-af08-dcc32ce82aeb | -6.57288 | -46.75743 | 2024-11-10 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4a09b55-feea-3cd6-974a-a95a499b988b | -2.89279 | -49.22837 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 974a9323-1e67-3cb4-981d-63296e88f6d5 | -2.6658 | -49.8936 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07813118-5112-345e-975a-24d739eb0f1d | -8.53704 | -40.97332 | 2024-11-10 04:38:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 15a22862-4d9b-3dfc-8cf7-160ad6b8ec42 | -3.76113 | -52.66354 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 08962bb2-f3e3-373b-9364-ffb862804bae | -4.92575 | -48.52275 | 2024-11-10 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9f5dc49b-d9d4-3940-a913-1494f091612a | -2.42168 | -50.42116 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29f0242d-9554-33a1-8895-b7fde4019f38 | -4.1093 | -49.12775 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b2a0ea8b-9c47-35db-8882-b121a6251f3f | -2.31602 | -50.58203 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b0c97c1-ed99-3bd4-8573-911b298ad280 | -4.38526 | -47.24332 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e95a6978-a5f3-3bd2-8c5e-1d4f4540b08f | -4.15623 | -45.74628 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a611e330-34c8-3c91-8863-e9b2b2393e1d | -2.40561 | -50.30485 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 451a481d-6706-3981-a573-3274a30615df | -4.33851 | -45.89437 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0d97bfa-836c-3c38-bdb1-9fbb69a56235 | -1.76187 | -53.74531 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 272e4656-ceb8-36f8-afab-153bd79c2170 | -5.4531 | -43.27206 | 2024-11-10 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cccdb8a8-1224-3d2b-9f6a-df8720cf81b1 | -2.93545 | -51.47687 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d7125780-fa76-33a2-a8c0-a6197f9f4af9 | -4.36941 | -47.25565 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10f3a3b5-573c-3e3a-bddf-8ff52b182a25 | -2.92139 | -49.49408 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a5bf13e-ae53-36f3-a146-2dd2d979737c | -6.47941 | -47.50898 | 2024-11-10 04:38:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbdde657-52d9-316b-a563-e49be34e045d | -5.17161 | -50.68015 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e00a0660-4996-3ba5-bf78-3c32861abbe2 | -2.43131 | -49.87574 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 59dcf491-d68a-308e-af9a-a37039f28d3b | -4.09786 | -48.32233 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0597cf6-b22c-3457-9744-68b37d748b9a | -4.2815 | -47.08175 | 2024-11-10 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf8e64b3-9437-39fc-9eb5-dcb1be30ad0c | -7.46097 | -43.58865 | 2024-11-10 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac4a082a-5fb7-3c9b-a1d7-efb2d88983b4 | -3.45173 | -49.11655 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d8c924d-41bb-3af4-936b-eac60b8f7d16 | -3.37173 | -46.3952 | 2024-11-10 04:38:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5bc7cd1-6ab9-3cc3-859b-29cea649b18a | -2.60934 | -48.33755 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a8ecf26-57af-349b-805e-c6f058abca6a | -2.89291 | -48.30043 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9754e84c-c68d-3e67-b3f8-01606bedf5d0 | -4.36544 | -47.25877 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d071d280-0902-31fb-89f1-be2ebedcb45f | -2.53876 | -56.75453 | 2024-11-10 04:38:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f01d243-ea2b-3c35-ad50-e6c410d6bdd2 | -2.3891 | -49.83601 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b78e489-9173-37fe-ac06-f245a17a29b2 | -1.7314 | -55.1917 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a761a15-e9b7-3797-9b16-96f352a9c960 | -2.41141 | -50.30927 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8baba9a2-c67a-305e-bc09-10e226dd7a66 | -3.13578 | -49.12 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cad4183-eaaf-3faa-82f4-bb07ed4f9e76 | -3.62321 | -54.10996 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8583d0c-3443-387a-ad2b-f6a318ab0ea7 | -2.99285 | -50.30043 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65f2c126-8471-3602-b6b9-fa8a16fb9b52 | -2.99272 | -49.51237 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1683de2-c6dc-3d4b-807a-84ee25d8903e | -5.47064 | -47.51521 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74269d64-d6a1-3fe4-abb2-c3930f6a8161 | -2.2799 | -49.93015 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34bde941-624d-30b5-884b-92b4303c3958 | -5.32582 | -45.05645 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 30020404-2dd3-3af6-b60d-8a238495e6b4 | -4.57577 | -45.40965 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6206bfd9-714b-3553-a91e-fa23ffbf7165 | -4.43373 | -47.24694 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19600cd9-55d7-3455-b2f1-e44a2886f02e | -5.54945 | -47.50116 | 2024-11-10 04:38:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc3f8d2c-169a-33aa-b507-e40d72755d37 | -3.63321 | -50.18405 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7f94094-deae-3ef5-b43e-7b94466457d9 | -2.873 | -50.41819 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 846ac0cd-0282-34be-a23e-21237ed87cdc | -3.42054 | -53.0498 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5f2693d7-1c46-34da-abc5-18aecd034f57 | -3.0555 | -48.04299 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ea81beb-c224-3bcb-9b68-552688dee1e1 | -3.19922 | -50.29888 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ff4efb7-dcc2-367c-a724-e0574a3be8d0 | -5.36146 | -47.92159 | 2024-11-10 04:38:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0bf44d0-7ba8-36eb-b8f7-b45edb9580d5 | -3.34814 | -50.13226 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1ee6c3b-5876-379f-9d42-73e1a5485306 | -2.87384 | -46.65875 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3c3ec3e-05e7-3a47-8141-0f421aadd0cb | -2.94377 | -48.60209 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| deca9bb9-b6e4-3dd1-9055-b67d0129014b | -2.98603 | -50.29936 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 330c0ad6-5186-31c9-9fa5-83650c411a0c | -2.65283 | -48.64433 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48a80cc3-c48c-3de9-8ec4-c3b2460dacb4 | -4.14597 | -48.4007 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ee18a39-57a3-3dcf-b94a-8af51b84ca14 | -3.10819 | -48.61 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efb5eb3c-77f5-3a26-8cc2-f4d434b5cc62 | -3.03391 | -48.05029 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f59ae94-4914-3dc0-9cf5-3f6e6600f91b | -3.35519 | -50.26327 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62f6f0e9-c428-35cc-87f3-de5fb87475b5 | -3.04463 | -49.55287 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 471104d0-15b1-32d9-bf69-79f0cda5d418 | -3.97485 | -48.17519 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1a428f9-de11-3d2d-9241-439f14333d48 | -2.66462 | -49.12819 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 324eb49d-ac53-3868-bece-5236394fa78d | -2.73501 | -49.02168 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9817a2ce-5e56-3493-bbb6-52f2e62b0cdf | -2.90894 | -49.24858 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94ecb8c4-45fa-3429-9b20-591b5c1ce881 | -3.69666 | -47.63711 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d530cad6-5f0f-321f-a234-6cf0d3c9c521 | -3.98453 | -46.41505 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a8976e6-100f-3527-8ff9-a540431b4d26 | -4.39469 | -41.91134 | 2024-11-10 04:38:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 23332319-a372-3ca9-8c7b-f7949da5d746 | -6.09577 | -47.05261 | 2024-11-10 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63cf8308-98be-3a97-8678-2f3caa9b98da | -3.04183 | -49.54882 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README112.md)
