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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f788cb38-efd7-31c5-8500-9e495b4b8016 | -4.14404 | -47.66013 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 457d184b-fcc4-3be0-9c91-fba0a12d8b2b | -4.94302 | -43.06617 | 2025-10-19 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18241042-165d-3795-a8f8-3f5cfe001071 | -4.58964 | -46.51439 | 2025-10-19 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9035244-821a-3106-ad85-3cb8cd679b3a | -4.18914 | -45.79177 | 2025-10-19 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 497b48ee-3a2c-3bdd-b16c-0f3fde6d60e4 | -4.58909 | -46.51788 | 2025-10-19 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e0e2202-4225-315a-80e7-c4e97c20a1f6 | -3.35363 | -45.45513 | 2025-10-19 04:29:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a44aa0f3-6097-31d2-8051-98b73fe84379 | -3.51825 | -49.93738 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4afca36-4e81-349d-bd75-835274470751 | -2.9637 | -49.53656 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49c30d0f-0add-3a5f-8b29-dad2459c0a71 | -4.21904 | -49.32212 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40ccbebc-2c0b-3712-860b-a57b37f97fa9 | -3.4701 | -47.68847 | 2025-10-19 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0ceeb6d-211a-37f9-8dcd-cc159e508ec4 | -4.29795 | -49.66332 | 2025-10-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c276a94-519a-383f-bbf8-bb64f13af2ee | -4.56804 | -46.50028 | 2025-10-19 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdb44881-df57-3fdc-bcf4-31ac1a423668 | -2.87114 | -50.73337 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2e76ba6-78c7-35b6-85ac-639ff1bf60d1 | -4.77231 | -47.29707 | 2025-10-19 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d1ab71f-7568-3206-9d1b-8b205c5a227f | -4.2414 | -44.67523 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d6765a0b-6289-3661-a112-03cf76b2ccd0 | -4.14802 | -45.73495 | 2025-10-19 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da92ee52-9186-3b95-b319-fa93aeb43f9f | -4.24952 | -40.34774 | 2025-10-19 04:29:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 709feb05-b672-32e4-b575-c502412fdb25 | -2.97326 | -49.522 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6856bcfb-410d-326b-baf9-eb5cd3bae1e0 | -3.48606 | -51.47403 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44f59fe9-2e6c-3859-beac-cc01986e8b9a | -4.23957 | -44.67937 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c7f1226-d899-3449-a074-3ddd4edd982f | 1.74405 | -55.94803 | 2025-10-19 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 159d96e8-b6e7-354b-9796-88ce50fd93ec | -2.87708 | -50.72046 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e2c20f2-0c7d-350a-8f24-cb5622b84aec | -3.13661 | -50.2506 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29e55084-954e-3cfa-b21d-2687a4c2d3bb | -2.8726 | -50.72437 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b0ef0fd-db99-3bae-b37e-d9455d9f8440 | -4.58257 | -45.64646 | 2025-10-19 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68872597-264a-363a-a192-af128c11d33a | -3.85974 | -49.82185 | 2025-10-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6061a21f-d397-3731-ae35-698afa6779ee | -5.34336 | -42.55352 | 2025-10-19 04:29:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 54d9e5a1-e1a7-32be-b233-f3f057b0fa40 | -4.21945 | -48.35937 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8aab3477-61a7-3976-8ace-93ca830fd768 | -2.17623 | -50.25971 | 2025-10-19 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d89f1630-a91b-3f32-96cc-bbc81857800c | -3.83873 | -47.40033 | 2025-10-19 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c49174f-b058-3da4-afec-8ab56bbf2376 | -4.58258 | -45.3762 | 2025-10-19 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d5cda50-ce85-3bfe-b206-280f06e36bd8 | -2.91731 | -52.72773 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4671f1d9-4373-3592-adfe-d56c75e85688 | -4.28431 | -50.54485 | 2025-10-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66732a03-9025-331e-836b-c23ea0bfa94d | -4.92186 | -45.67131 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dc86f7f-6c5f-373f-ba51-4761260bfa4a | -3.14389 | -50.25176 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7174389b-d954-361a-a59f-85045f2dc751 | -4.53138 | -44.01234 | 2025-10-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a579985-394c-35fb-9115-7aff726cfb63 | -2.87635 | -50.72497 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 729397db-bba1-31a4-8fda-37c5c2ce6fbf | -3.37826 | -52.7984 | 2025-10-19 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bdc873c-8ea1-32df-a815-e81c7fd2977e | -2.72628 | -48.34824 | 2025-10-19 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb16c349-2279-3614-a7d0-89c5e259e2fa | -4.95541 | -45.09056 | 2025-10-19 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44bf35f5-55cc-3afb-9db4-e1bf67929e15 | -4.29384 | -49.66666 | 2025-10-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ac105f3-62a4-3963-891c-ac7d57e386b5 | -4.42544 | -47.75066 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| df31292c-fa04-3c86-b9c8-6cb2489a0ac8 | -4.03257 | -43.18127 | 2025-10-19 04:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 561d07f9-579c-3c49-a062-fe6ef54ca1b0 | -3.0146 | -48.84958 | 2025-10-19 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70bede5f-0dbc-363e-b321-1924323eb413 | -4.30382 | -48.06644 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd1943d7-8b89-3443-ab6c-9abe8f0bd883 | -4.24018 | -44.67548 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2f2fbe52-5783-3e97-a206-3cfe2edca790 | -2.57347 | -50.53596 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b59d96f-ee42-3c61-99e7-93060425cd9c | -4.24368 | -44.67602 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d086541f-5fd0-3e2c-bba3-5214da4d5dbf | -4.82696 | -43.06525 | 2025-10-19 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d6fe6e4-daac-3243-b35e-febebce0beb7 | -2.91666 | -52.73177 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94d5aeb8-9feb-308e-884c-07a2a9389e78 | -4.2686 | -44.47105 | 2025-10-19 04:29:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| eedeab7c-af35-3a19-b55e-069fe9a64366 | -4.31597 | -43.02048 | 2025-10-19 04:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5f46d26-df43-3396-9a43-6fef7446ab11 | -3.52385 | -49.93195 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34f630ca-182e-3a94-952f-d03b75a816af | -3.75567 | -53.34293 | 2025-10-19 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 594416ea-dbb9-352f-b195-5d9a5a9c1777 | -2.69656 | -49.5535 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cdfb0e7f-62ec-384c-8390-a46a053b7151 | -5.46756 | -42.87962 | 2025-10-19 04:29:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8d69f99b-d645-3ca5-8cb7-19bbb6606663 | -5.11171 | -44.58744 | 2025-10-19 04:29:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52b740bc-ec9d-3408-a347-33f229bb40f2 | -3.16034 | -49.16707 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c3ad5b3-c8f5-3601-bedb-7035ec6639c3 | -2.99424 | -49.59397 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b80623a3-c06b-3969-8fab-c08bceefd8d9 | -2.7411 | -49.39032 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c88170d8-87f7-368d-b121-c291c0d77f0f | 1.80065 | -55.70974 | 2025-10-19 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e07ee477-ab4b-3fc6-9b20-a4a356d0a415 | 1.79561 | -55.7144 | 2025-10-19 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a59c92e8-9db3-3a35-9ef6-e5ade12d7184 | -2.74523 | -49.38699 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fee6a53-0871-314a-a9ce-c748abf373fb | -4.4145 | -43.97119 | 2025-10-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b356bb1-db9a-3b60-90a8-64cb428cd478 | -3.1274 | -50.21466 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bac26e56-7fc5-3aea-8f43-27e1cd791520 | -4.24859 | -48.56467 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 440f7eaa-69ba-311b-94f8-2e3ea8ec07b8 | -2.64272 | -48.03974 | 2025-10-19 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71a7b8a8-9481-3e33-900b-241d67191ae4 | -3.54936 | -46.43347 | 2025-10-19 04:29:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdb04245-a3fb-3095-b532-d0a86306ebd2 | -2.69781 | -49.54556 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7bdf4fe6-78cc-3712-ba9e-451c72eff0d2 | -3.14891 | -50.24705 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fda6683d-2d0c-33a2-9aad-0c0d2e0a9eee | -4.2161 | -48.35883 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| debae3d8-9aaf-33df-be98-1612a82d083f | -4.23835 | -44.68714 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94effb31-a4c8-373f-878d-571276fea79e | -3.2653 | -50.12397 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 226fc0c7-b2eb-30ea-9b1a-cbe11a9a2bb1 | -2.68659 | -49.54783 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 52ad07cf-3879-368a-937d-6ea750585f10 | -2.29817 | -48.5686 | 2025-10-19 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 720211aa-dffb-3c32-8e22-4b04245b1eac | -4.56749 | -46.50378 | 2025-10-19 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c250d68-adae-3062-8f5c-c395251bc98d | -3.51966 | -49.93538 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0568e52-32c3-3358-b9b2-845976f4337a | -2.86291 | -50.73667 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f2dcb82-bf28-358c-a8c9-c14fe26fef79 | -4.85342 | -42.88703 | 2025-10-19 04:29:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2ba6d68-c53b-33c1-8551-cc1dc9c3910d | -2.97826 | -50.30537 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d512d740-3b58-3260-9e1d-185bdb34cd98 | -2.916 | -52.73586 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee5836f5-90b2-36c2-ac65-4f2cbbbae21c | -4.42072 | -40.16899 | 2025-10-19 04:29:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c68a4bdd-1699-3c3a-8503-22c4d5aedfea | -4.18505 | -46.34393 | 2025-10-19 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0a00b59-99ee-3342-8b9c-7a090ff0e491 | -2.44411 | -49.36619 | 2025-10-19 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9079428-d40c-3e2d-ad42-da22acca7313 | -4.22241 | -50.6269 | 2025-10-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3761dc8a-aa8b-3644-a8da-a5e191bbe4a6 | -2.87415 | -50.73847 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f13bf60-9e7f-3020-b197-afed7d27149a | -4.9157 | -45.41851 | 2025-10-19 04:29:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cce8d086-c282-3977-904c-7b3af32b95db | -2.85916 | -50.73608 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c1b333d-065e-3d46-bff1-8477a90097b5 | -3.81693 | -52.14 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c4ff6a7-8d2b-3311-bcc0-a1f6b5f1c819 | -4.9299 | -43.41178 | 2025-10-19 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dc1a617-a729-39b4-a486-306d9aaffc62 | -3.81762 | -51.70656 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74d9ef77-b48a-37e5-aaaa-0c940718776f | -5.04749 | -45.45025 | 2025-10-19 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7350b49-a4e4-3f13-a3cf-e3bd75a74c01 | -2.4406 | -49.36563 | 2025-10-19 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9dc26c4-287f-3d93-aaee-179a650319e0 | -3.14458 | -50.25071 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8ccf2bd-4b98-3f29-b9cf-b66b616015af | -4.58884 | -45.38099 | 2025-10-19 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9184b858-8251-3ea7-ae67-4fdbba75a8b4 | -2.68949 | -49.55237 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f33fe15d-00b1-3c39-9875-1268d08ccd02 | -3.3542 | -45.45153 | 2025-10-19 04:29:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9e854c7-89c1-396c-9a0c-f4891a98f39c | -4.20998 | -48.35423 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b95794a-65a7-3865-954f-e8e2383b78f2 | -3.08546 | -49.47843 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf69afa3-ff3f-3b13-b4e6-307491c7c2ea | -3.87431 | -50.41541 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README41.md)
