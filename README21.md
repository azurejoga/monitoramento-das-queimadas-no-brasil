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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c056be18-1050-3317-af30-0de8a76a9cc3 | -8.79126 | -44.73283 | 2024-10-25 03:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bab34ce-8c67-306f-99c1-c38007e306d4 | -8.78989 | -44.7397 | 2024-10-25 03:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57a4454b-2111-36f0-9bfb-fdbce5ddfe2d | -8.78099 | -44.72172 | 2024-10-25 03:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66080dad-9511-3bae-995b-c742ab378123 | -8.77965 | -44.72866 | 2024-10-25 03:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84905fc4-2d52-3cd2-afd8-b32dde122a72 | -8.77869 | -44.72293 | 2024-10-25 03:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f61ed3ea-c119-3ce3-b72a-f84ce3bab5ca | -8.7783 | -44.73564 | 2024-10-25 03:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85352cea-ffa9-3244-b408-4fef1bc76948 | -8.77731 | -44.72985 | 2024-10-25 03:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2618ae69-bb77-3c3f-be4f-4bc280472e6a | -8.77592 | -44.73677 | 2024-10-25 03:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdada8bb-f22f-37fc-8cf0-c7c35a444f73 | -8.66708 | -40.96907 | 2024-10-25 03:21:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 373d5dba-20c3-315c-ab00-ff11faacd931 | -8.61699 | -35.09026 | 2024-10-25 03:21:00 | NOAA-20 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 83d72751-a88f-3f97-8841-9a914aae32fa | -8.61319 | -35.0896 | 2024-10-25 03:21:00 | NOAA-20 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| aacb0ec0-5b44-38a1-b574-725901be9e10 | -8.22726 | -34.96138 | 2024-10-25 03:21:00 | NOAA-20 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 965afd90-6646-36eb-b76a-e26cf7922b3e | -8.11471 | -37.60036 | 2024-10-25 03:21:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 12997baa-1b3a-339d-8769-41eafe21c6e3 | -8.07307 | -34.97569 | 2024-10-25 03:21:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4195b9db-7c58-3ff9-aac8-026f81a577c3 | -7.79829 | -43.16787 | 2024-10-25 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a08cb1f9-44c7-34ca-9ce6-2512a06e6a11 | -7.79728 | -43.17036 | 2024-10-25 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 721a89f8-8bd9-3051-9ccd-1e6343b21fb7 | -7.79727 | -43.1734 | 2024-10-25 03:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a2703423-d389-38c6-939d-ea06db7a4506 | -7.54415 | -35.10101 | 2024-10-25 03:21:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 585fc50a-7e2d-3aec-b005-ba71e83820c1 | -7.41849 | -35.27485 | 2024-10-25 03:21:00 | NOAA-20 | CAMUTANGA | PERNAMBUCO | Brasil | 2603603 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 92262b9d-c180-31de-810b-96c48b2811b6 | -7.26772 | -38.3709 | 2024-10-25 03:21:00 | NOAA-20 | SÃO JOSÉ DE CAIANA | PARAÍBA | Brasil | 2514305 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d3333959-4a13-325e-b3d0-5ab07e7460dd | -7.21524 | -38.98689 | 2024-10-25 03:21:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 61951fdc-c0bf-351c-b4c9-23beb417b69b | -7.21472 | -38.98991 | 2024-10-25 03:21:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4bf3bf74-4dc2-32b9-aceb-eac73baeced5 | -7.18829 | -44.74274 | 2024-10-25 03:21:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7caacbd-c032-3f8e-adc8-ccb67f88a02b | -7.09694 | -41.14412 | 2024-10-25 03:21:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6befb003-c6e2-3152-991b-675f89889033 | -7.09114 | -41.14301 | 2024-10-25 03:21:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7de7e588-2be4-317b-bc65-5a1f755adce7 | -6.8967 | -34.979 | 2024-10-25 03:21:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 338f03e9-688e-3cc2-9e44-fe0449964924 | -6.89283 | -34.97832 | 2024-10-25 03:21:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 22eb0f15-5553-39db-b6f4-3e3c7bf77663 | -6.89202 | -34.98318 | 2024-10-25 03:21:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d384896f-5a5a-3f9d-b799-ac4f8af419f7 | -6.88815 | -34.98251 | 2024-10-25 03:21:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 554ce3d5-407d-350d-8f93-a3cd2cd82193 | -6.83137 | -35.15329 | 2024-10-25 03:21:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e8454fbc-4a67-3699-9cbd-7b37d3963e67 | -6.83092 | -35.15568 | 2024-10-25 03:21:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8a86b09a-9f5b-3a95-b157-aba9abe2b443 | -6.77635 | -39.70761 | 2024-10-25 03:21:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f942f463-e274-3d99-af5b-4d5063ecaac3 | -6.71734 | -37.51077 | 2024-10-25 03:21:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 722a9fc3-2982-3f7e-8329-23285c6c125e | -6.59864 | -44.1921 | 2024-10-25 03:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd88d6ae-2b55-32cc-848b-093f824e0d0a | -6.59164 | -44.19062 | 2024-10-25 03:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cb6049d-a82a-36e6-a581-9f381fc845d3 | -6.58921 | -42.25038 | 2024-10-25 03:21:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d8fda848-03f3-3445-9130-0ee08e9cf2f2 | -6.58294 | -42.24921 | 2024-10-25 03:21:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d440c64a-b011-31d2-a406-608408e42b01 | -6.47649 | -35.25058 | 2024-10-25 03:21:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 247f1b9f-b9a7-3243-beaa-1c9aa626991e | -6.13723 | -36.80193 | 2024-10-25 03:21:00 | NOAA-20 | FLORÂNIA | RIO GRANDE DO NORTE | Brasil | 2403806 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d4dd4c6-7174-36fd-97a8-dbc5fe6cb009 | -6.04952 | -43.89985 | 2024-10-25 03:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2c732b0-6fd1-380d-af30-cc6d36436df1 | -6.04827 | -43.90675 | 2024-10-25 03:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13efb1fe-e998-32e8-9ad6-b1593163cda0 | -6.04794 | -43.89908 | 2024-10-25 03:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b226ee58-e8b2-3966-9167-a510884459ff | -6.04665 | -43.90593 | 2024-10-25 03:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9d1b842-8f4e-3dc6-996a-8044e7d6fbae | -5.71843 | -43.8442 | 2024-10-25 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d5f4ed7c-54f2-37fb-91c3-391ee9338371 | -5.56441 | -35.52761 | 2024-10-25 03:21:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7cf5071-080b-379b-afed-da6edf252cfa | -5.56113 | -35.52757 | 2024-10-25 03:21:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 86509501-4aea-3a8a-9a01-65ef1f34d806 | -5.17565 | -37.98737 | 2024-10-25 03:21:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5dfde29c-45f1-34fa-b85c-57ef70e2271c | -5.14938 | -37.74078 | 2024-10-25 03:21:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 14.2 |
| f6679818-708b-3b71-9688-e3cd6826e15b | -5.14851 | -37.74597 | 2024-10-25 03:21:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 5bd9dbec-a207-3ecb-a789-fc4e25933ef3 | -5.07475 | -43.83321 | 2024-10-25 03:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 43b390b0-3b2a-3e66-a4e4-89ad0586c3bd | -5.0719 | -43.83417 | 2024-10-25 03:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6b960a16-9f5b-3bb0-ad07-96ed837df04a | -3.80084 | -43.26022 | 2024-10-25 03:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37f8c386-6f41-3966-bcd1-98d3c1b7a56b | -3.79972 | -43.26674 | 2024-10-25 03:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfec31cc-fa64-3099-991c-c6ad607f3ace | -13.2904 | -43.96737 | 2024-10-25 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e30b8f03-6085-3076-8500-8bbf3b5e8072 | -13.2853 | -43.96068 | 2024-10-25 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b87148cf-042c-3523-aa46-8269d454d4e6 | -13.28424 | -43.9658 | 2024-10-25 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2c2d3688-5cbb-3d8f-9b10-00e15ee880c8 | -12.90336 | -45.07719 | 2024-10-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a0d5770-3bde-3993-879f-2fd24b77c3f3 | -12.90207 | -45.08324 | 2024-10-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f412ffc-bccd-33b5-88e8-8b7025fa19eb | -12.90063 | -45.07619 | 2024-10-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e7fc6e1-8ce2-35de-8655-06cce395b4a5 | -12.89938 | -45.08228 | 2024-10-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 05a9cc30-b735-32cb-ae7c-265dafcc6477 | -12.89671 | -45.07568 | 2024-10-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d97821d-53f5-3e90-9426-89b71a69a3af | -12.89542 | -45.08175 | 2024-10-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8ed4ae4-6a98-3f1d-a298-ebedb100e8c8 | -12.89398 | -45.07467 | 2024-10-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad7a883c-6af9-3c3a-8fe1-8c277527810f | -12.89273 | -45.08075 | 2024-10-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 56b8724d-df57-35cb-823f-2e19b07317d2 | -12.89264 | -45.0621 | 2024-10-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3b18bd7e-6af1-3913-b028-6d89c369c0be | -12.88984 | -45.06104 | 2024-10-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 61dc4711-b0da-3d61-98e9-9d4393e8e5d8 | -12.88728 | -45.05457 | 2024-10-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a266517-0726-3cbd-9933-6ca8fd4745bf | -12.58561 | -43.83636 | 2024-10-25 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb454c1b-d87f-31ec-8d22-a71781415e34 | -12.58453 | -43.84154 | 2024-10-25 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 140ce725-0a85-35cf-a6ba-d13fe270dad6 | -12.58259 | -43.8325 | 2024-10-25 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 06c225b5-bdb5-3537-9cb5-0fd5d28c00f1 | -12.58154 | -43.83768 | 2024-10-25 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f02ff525-8c5e-3a0b-ac7c-197dd45d2001 | -12.5805 | -43.84283 | 2024-10-25 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3819dad3-eca0-3d5c-ad7d-bf3db2c59f38 | -12.57936 | -43.83512 | 2024-10-25 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f39449f9-3376-370f-a909-50599890a09d | -12.57828 | -43.84026 | 2024-10-25 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7cd88fed-75a4-3aac-929b-2ffbf4de6af1 | -12.44445 | -44.41312 | 2024-10-25 03:23:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28424c52-d01d-3fc4-828a-85814849909f | -12.43916 | -44.40603 | 2024-10-25 03:23:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de203efa-6032-374d-98cf-f509c489e7b7 | -12.34644 | -38.06665 | 2024-10-25 03:23:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d18bd9e5-fb0b-3288-824e-f291af165f35 | -12.34212 | -38.06583 | 2024-10-25 03:23:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ca258f02-08a8-3a31-a6ac-ed90588ec358 | -12.30582 | -43.56987 | 2024-10-25 03:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e32f5de2-8703-3fa4-a285-1dabb117f28f | -12.30449 | -43.5685 | 2024-10-25 03:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3478e567-229b-3277-9719-6cf291368127 | -12.29967 | -43.56845 | 2024-10-25 03:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbe3ebb5-1903-37ac-a503-3b5f01928a26 | -12.29868 | -43.57337 | 2024-10-25 03:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f964151-f163-3638-8208-c3cc8d6b25f8 | -11.90213 | -43.83973 | 2024-10-25 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0df52a5-8c64-39f8-9244-e0ea841ca6c9 | -11.89582 | -43.83842 | 2024-10-25 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71ab9289-657a-36e2-8f37-d139c26370e4 | -11.71334 | -43.91368 | 2024-10-25 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb5d9098-936d-3896-b115-7301c8930913 | -11.71224 | -43.919 | 2024-10-25 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a92981fc-3565-35da-a40a-2f986c98ec0b | -11.71179 | -43.91301 | 2024-10-25 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 466e190d-8272-3038-b138-a571524f8959 | -11.71073 | -43.91836 | 2024-10-25 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ced3a61f-fbee-357d-b2b9-4b7a22e3464d | -11.5785 | -43.97962 | 2024-10-25 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 315cf230-d7b7-3f78-a831-f48f947e00f1 | -11.57803 | -43.97826 | 2024-10-25 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 12e421f6-f8f2-3865-a8d2-22c2ba7fe037 | -11.57739 | -43.98502 | 2024-10-25 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ce69b55b-99ea-349a-8056-218ce7c5690e | -11.57695 | -43.98367 | 2024-10-25 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b458e12c-0115-30f5-bb06-94bee244db5a | -11.5353 | -43.99158 | 2024-10-25 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e081420-a056-3ddb-84c3-ffab61efb006 | -11.48427 | -43.23862 | 2024-10-25 03:23:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e8d7bcf0-4c4f-3eb5-8d17-5c7fdbefeeaa | -11.4833 | -43.24347 | 2024-10-25 03:23:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a718e7c2-be58-3d18-9df7-926f1c56ecbb | -14.48013 | -45.50096 | 2024-10-25 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b40b26bb-70c0-3c72-b42c-c846a139d9d1 | -16.12487 | -40.61057 | 2024-10-25 03:23:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bfc48dda-ad11-3276-933c-2c31285ca04e | -15.43059 | -41.14125 | 2024-10-25 03:23:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 595f24aa-41a6-36a4-b9be-49a89f283053 | -15.42997 | -41.14435 | 2024-10-25 03:23:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b6780320-be49-3107-bd00-b46986b37e82 | -15.31904 | -41.75021 | 2024-10-25 03:23:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |


[Clique aqui para ver as próximas entradas](README22.md)
