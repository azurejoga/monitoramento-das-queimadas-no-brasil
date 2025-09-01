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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b77aaf28-9299-313c-95f0-1c5719a50b62 | -8.38641 | -70.75551 | 2025-09-01 05:23:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc0c3166-30e5-3b0f-af99-d759e30de3de | -10.12976 | -58.01716 | 2025-09-01 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b202342f-9096-30c4-b322-b5c75e990ec3 | -10.24256 | -51.12431 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c990072e-24fe-3180-a151-2775c67c4681 | -7.46501 | -70.13273 | 2025-09-01 05:23:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dffd703e-b6c8-3461-a205-67d4fddb8aba | -10.37394 | -52.28769 | 2025-09-01 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4f18fd8-be31-3862-b46b-717cdf5ca440 | -8.76037 | -61.42813 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e2b20e5a-7224-336c-b6c5-6032b10ddb5b | -8.55446 | -63.01672 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b4c0aa1-9254-331d-913c-29b9560d9098 | -7.73049 | -61.57317 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2293552e-e1c4-3718-bdc4-72dc4eb9b7b6 | -10.05113 | -48.10308 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ee71701e-3b0a-35d7-b4b7-72b6d7bb4393 | -7.90155 | -63.0117 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7efc27eb-ed67-324f-a7fa-000aff601127 | -8.72648 | -62.41893 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 973be383-c02c-3a2b-a5d2-a78fd5a43c03 | -8.2293 | -62.94189 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 630f5d6d-059b-370f-a995-ed0adefe4ee9 | -8.68469 | -62.40125 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa2c383-3d6c-3a19-bf13-82715065b2a0 | -9.4506 | -60.57655 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92fe7283-7df3-35c1-9caa-7b294cf55358 | -7.73436 | -61.57021 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e306855-ff08-3b08-87e7-44050bc04206 | -9.07201 | -65.42519 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f94aa18-8fe8-336f-9b80-f9f5611f22a3 | -9.67572 | -47.82899 | 2025-09-01 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 26fa2aa3-329d-3506-971f-45a8ba316ed2 | -9.14089 | -65.85349 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6183e4b9-c62c-3ea3-a664-a33971f42352 | -9.43778 | -60.54929 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e486e92-7ee2-3291-b435-e6262d6ae639 | -8.76367 | -61.42865 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 656a85aa-b877-3c8b-82a5-f26db9f0f06b | -7.65709 | -62.54617 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a032aaa-b74b-3ea7-a8c5-b40911742382 | -7.68206 | -61.08151 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe33ef34-b07d-3ab4-9de1-87e023757e8d | -7.10861 | -63.02869 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e996db4-9f03-35af-b507-533e662ab01c | -11.92971 | -50.63026 | 2025-09-01 05:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b30ec70f-dc23-31ea-a75d-69938503230b | -8.76313 | -61.43212 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f6a2b00f-208e-33b0-b0c9-a36cde85939c | -9.23116 | -60.25631 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d07aba25-7b18-3bb4-88ae-d0cdf007964c | -9.27833 | -67.64594 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c039cbe5-e2a6-32b1-be5a-cf5fbd6fb8a1 | -8.72704 | -62.41536 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e00d2335-a575-3d10-a535-fab1540e5b9a | -10.62206 | -54.91716 | 2025-09-01 05:23:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca9c8b8e-b252-3c9a-b887-4089cd7782f7 | -9.12079 | -65.75957 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2299cf96-ffca-390d-aebf-902de7840f08 | -9.07083 | -66.07896 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56733668-4e08-369f-9e9f-02545294a508 | -8.65263 | -62.92664 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f650d3ad-e143-3bba-8bef-d2185a0d0fe8 | -8.96981 | -65.96098 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3753f42-a3bc-355e-a8a1-517d39f7a417 | -8.74983 | -62.37508 | 2025-09-01 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aadd3e2a-a4d5-3de3-ba1b-b9092542d3ce | -8.73765 | -62.41337 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17758b4f-395f-382b-bddb-085b3276045c | -7.08877 | -63.19765 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d428666-3b33-3bc4-ba1e-3db775b3b9fe | -8.7464 | -62.39643 | 2025-09-01 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf9d5290-85a9-3df3-9662-c9d4cff8c8c4 | -4.12663 | -47.65849 | 2025-09-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84e00e64-7cae-3688-a701-10e8df17f2fe | -8.7343 | -62.41284 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3f32fda-2c5d-330b-b726-339d51d28731 | -8.85159 | -70.62143 | 2025-09-01 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e00ae0c-1469-3530-ab17-cddf6238e53c | -8.63021 | -62.59101 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d3a3ee5-2478-3ce9-8a67-34a8587a73a8 | -8.26582 | -61.45902 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b673076-6553-3e36-8bda-82cef38304b8 | -9.06822 | -65.42455 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d90d245-c4e8-303f-a838-0a1dfd7baf6f | -7.56683 | -63.41119 | 2025-09-01 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 752c89d8-8269-36e5-8abf-494fbc8530b2 | -9.8801 | -64.27508 | 2025-09-01 05:23:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 410d1233-131d-35f2-a053-6fd4c18c002f | -8.62407 | -62.58632 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34054cb5-46ed-30d7-ac3a-02e5f552846f | -9.86977 | -65.03249 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7000f32a-57c3-3bc4-aac0-2622e13407fa | -5.43413 | -49.99437 | 2025-09-01 05:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 610769b3-ff55-3a9d-93a5-60c3fc328ccd | -7.28471 | -60.66422 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f2798bcd-a6d0-3a30-ae51-2d0ee2243df8 | -10.47993 | -51.63117 | 2025-09-01 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7695d38f-1a36-395d-bb56-e41f9dbc30c3 | -9.1716 | -67.71062 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 063932f3-2a94-343f-a5c6-71de74d3015b | -7.28026 | -60.64934 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9c9619ae-325f-3a90-8321-27b18df627ab | -9.12019 | -61.21526 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce58723a-533a-3390-ab22-8b7ffa439747 | -8.65999 | -62.92407 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b02dab0c-fc0c-330d-bd42-664faddf3367 | -8.82655 | -47.83674 | 2025-09-01 05:23:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 63e104ac-3edf-3a18-80dd-ec8fdb022942 | -8.88975 | -60.72929 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e00b5a5-3dfd-3696-b8db-53d9a27f168d | -9.4373 | -60.57448 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 601f2c23-585f-34a1-bc39-3797d6bacf53 | -4.79663 | -48.1193 | 2025-09-01 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 342461cc-2470-324b-8eae-3ed54ceee425 | -9.69118 | -65.00069 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b7b4523-a447-36ea-a4e9-820e6030ebfb | -7.70174 | -61.47593 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d49f762-f3af-34f7-831e-a8daba725695 | -9.07424 | -65.43517 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6dd7f10e-d4b4-34e2-a906-adf48975f8dc | -8.70918 | -62.41983 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bd49a88-3649-3221-ab13-0ff9d7d53284 | -9.06587 | -65.43857 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 454ce89a-9527-300b-8eff-736cae38ec1b | -4.12556 | -47.64982 | 2025-09-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb69d8a7-ca93-3ed7-a41e-79a83a02a934 | -7.1074 | -63.03626 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36090ed7-f416-3c61-9e2c-8e83d171efa8 | -8.73656 | -62.39861 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71c126a2-d706-35bc-8ca5-90b731780cbc | -8.74583 | -62.39998 | 2025-09-01 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a97147e4-3d78-3674-944c-2195f3756da5 | -8.66788 | -62.92505 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 251317ac-042a-353d-8843-a2be66cbabef | -7.56746 | -63.40732 | 2025-09-01 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 669ddccb-2b1a-397d-9a00-90135d66b53b | -11.83788 | -51.47014 | 2025-09-01 05:23:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0a959a0-6c8d-30e5-9fe9-d3c5d8c69761 | -9.06967 | -65.43922 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8f982f3-e87a-3620-a745-fb401f781feb | -9.14559 | -65.8492 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1432a41-cf98-3fe9-a84f-961e5d2bc3ef | -7.69788 | -61.47888 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7082e1eb-dd70-36a0-8166-b5d622cf9977 | -8.96811 | -65.97101 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30c17d9e-5ae3-3e3c-bd71-69498a41c69f | -9.83598 | -65.05377 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58b0bf48-5c58-3aa3-b81d-caae8bab1db2 | -8.75928 | -61.43507 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 06f16351-7add-3459-875e-a197ce8cad9f | -5.43998 | -49.99516 | 2025-09-01 05:23:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0a93b9b8-d90d-3586-b1a9-f58c75462f75 | -9.12383 | -65.76509 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3035de87-c21f-354e-88fe-bc7eb113b465 | -10.23815 | -51.11012 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eca2051f-db15-3b59-bfaa-2f0a7856606f | -2.40954 | -49.35166 | 2025-09-01 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2016fcf9-9a83-3bfe-8d19-c6928c816cf7 | -8.6678 | -62.83139 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8abb0e7b-404c-3f88-aef2-b7092549ff25 | -9.88076 | -65.01194 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c024734f-7cb0-3f24-b4de-52b8190a13a7 | -11.31155 | -55.1385 | 2025-09-01 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0178aeda-397d-392b-8788-3e51eda0c146 | -9.06522 | -65.41925 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b161556-5367-3a38-9e0d-ae127d7ae27b | -9.82883 | -65.05438 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7eed6b56-41cb-3f4c-a40c-467cbfa80394 | -7.28195 | -60.66024 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf56d5d6-eb33-3991-b0d1-ad2d3c378e65 | -10.04415 | -48.10247 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4ae826bf-e4c2-32f4-88f4-22b0aa070c23 | -10.23763 | -51.1142 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 75f5e864-007c-3839-9677-6a4ffe40b21a | -4.12402 | -47.6609 | 2025-09-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f360722d-c352-33a2-b8e6-177c4993f9ef | -9.02347 | -65.6908 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7403d3ea-6739-309f-b40b-a8f64d0119ea | -8.69302 | -62.41357 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b81d33e3-71c8-3003-a1d3-721bf38c0d15 | -9.86684 | -65.02751 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15d9b1b5-f09d-31f9-83f1-fc66c2d36f8d | -9.689 | -65.01379 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f20f67d8-8495-3958-bb58-d4fbd42b3093 | -7.68043 | -61.09189 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de37d071-2c94-3276-88ba-1907df7f1e79 | -7.69586 | -61.1014 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45bb59b4-3d5b-3343-9ea8-4c0d65678661 | -8.8471 | -47.49922 | 2025-09-01 05:23:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 70cf78a2-d8f3-37b8-b5fe-be165519696b | -8.72926 | -62.42302 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 623baeb5-bcc3-3e57-bd89-5356b457c54e | -9.13783 | -65.84789 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 812d9ba7-5644-3bc3-b6d0-f882870cf760 | -7.69457 | -61.47836 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1934a478-5288-3190-ab6a-d76cf0a65a95 | -9.82811 | -65.05877 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README80.md)
