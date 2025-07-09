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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71c00338-16a1-38dd-a2df-9f500e9e9a1d | -9.28279 | -44.83906 | 2025-07-09 04:21:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 413c4c92-960a-35d9-8122-c805575f486a | -8.51 | -43.27264 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 18540de0-7854-3357-9aa4-aa58f3be871d | -7.23562 | -43.07743 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a80663af-e02f-3b23-aebb-97e1caaf83b3 | -6.83762 | -44.03799 | 2025-07-09 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2271beee-f006-30cc-9e28-457f78af3208 | -5.23168 | -45.20963 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee0ba4ab-0848-3308-b383-b077bdfdc5fa | -6.55078 | -43.62225 | 2025-07-09 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5841fe04-5d7c-362d-a22f-363440f068c2 | -10.57429 | -49.11813 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7915b366-7162-39fc-9cf3-97da4ad7c11a | -6.17663 | -48.05056 | 2025-07-09 04:21:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d18400d3-9d0e-382c-b3dd-c00d1f8a1359 | -6.86012 | -42.79657 | 2025-07-09 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ccd67e59-b0b7-361b-9cc2-3e8fd940411b | -8.6933 | -45.39978 | 2025-07-09 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a900b0a-287e-3996-809d-a72272440f7e | -8.22971 | -44.92983 | 2025-07-09 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d29708a2-02da-3420-b1c7-02665fddb5d2 | -6.86963 | -44.06807 | 2025-07-09 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c395dd1f-37f9-36b9-8d1a-c573635a40dd | -7.08859 | -49.17001 | 2025-07-09 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c722ca78-86c7-356e-891d-fd14f0303911 | -4.50625 | -47.04685 | 2025-07-09 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42b5f530-a4eb-3a64-b214-da0d0516116e | -8.51343 | -43.27316 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 32dabeb6-b59c-3b86-aac1-34e9f2546223 | -11.4436 | -45.09713 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 284fb19f-5f39-3028-b10c-e6404a3fb499 | -10.98951 | -44.3231 | 2025-07-09 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bb362d2-2a58-3278-8d4e-a2094866dca2 | -7.95784 | -49.64801 | 2025-07-09 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aee9a2b6-ceda-37d6-8bb1-eec0d23622f8 | -5.96235 | -44.18024 | 2025-07-09 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10fde350-f97f-327d-a6a7-09c626f12407 | -10.57795 | -49.13501 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6f3e954-5cb6-3c58-a202-4ea49ad92864 | -11.44694 | -45.09766 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78c64424-dcf5-31ee-9e9d-535b1ff007b1 | -11.10472 | -48.87258 | 2025-07-09 04:21:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b7750d3-f825-3fd7-8c8d-396cdfcc14e1 | -8.71791 | -50.0088 | 2025-07-09 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70c13948-4cfa-35e2-abf2-159278b1be59 | -8.22584 | -44.93279 | 2025-07-09 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29fc9c2b-1474-32d4-a488-d28a9860da8f | -5.76563 | -45.78703 | 2025-07-09 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14ff2262-2064-360f-afb2-22c833440faa | -6.9986 | -43.41512 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6862aa2b-17fa-3dd3-b7ed-e15b2122660f | -7.08942 | -44.15669 | 2025-07-09 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02b8cfb6-4326-3d16-a374-8e4dff38221b | -11.43232 | -45.11002 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a516388b-81e3-3eca-9860-64690e514adb | -6.17228 | -48.05412 | 2025-07-09 04:21:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| ea7c6447-2836-39af-b9b8-7a55820060a5 | -11.43587 | -45.12501 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 43a0adb8-2ddb-341f-ab42-41a9f2985b08 | -8.23093 | -46.96619 | 2025-07-09 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c93fcc0d-0d47-3c7c-83ae-628878dc193e | -7.67586 | -44.36303 | 2025-07-09 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a37d46c-9296-3bbd-9662-d22117fde424 | -6.86528 | -42.78585 | 2025-07-09 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eceaa481-637f-34e7-bc11-18c71f58b592 | -6.16564 | -48.04862 | 2025-07-09 04:21:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eda33e60-c5fb-391b-b1cd-6f4f7013653d | -10.57286 | -49.12061 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 797a7916-05d4-34ac-87a2-3f1ad2835409 | -7.24303 | -43.07479 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 18389cbe-af87-35e5-ba4e-45cbc8fbfc5b | -6.73224 | -44.33998 | 2025-07-09 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 466827e2-cdda-37c7-8970-547e0027ccb7 | -5.68312 | -44.4944 | 2025-07-09 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4561c647-f809-39e4-9ff5-6a07d505d26d | -7.24074 | -43.06684 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| aa0f6680-6748-3e7e-928c-aa5c7373d4a2 | -5.22779 | -45.2126 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25f6967e-be31-365d-ac2c-64a537a1894d | -11.43533 | -45.12856 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a25585c7-2db7-3c32-bf5a-b4b5aa7fdec9 | -7.67696 | -44.35602 | 2025-07-09 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7f4a5aa-8715-3efb-bf84-eeaac9e9567e | -11.43121 | -45.1171 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| deb7c045-ccf9-351e-a297-fb9bc63660df | -11.44753 | -45.11596 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dad183e8-b15e-3ec6-b0f3-d576cfa46ff4 | -10.5721 | -49.12503 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 01abfc4d-3c84-38b9-a781-ee2b8eb30243 | -7.67532 | -44.36653 | 2025-07-09 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 859bd2c0-914c-300a-816d-49f29e1a7c37 | -5.50158 | -45.49007 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91918aa4-301b-340a-a1fc-0621a280ca32 | -10.64939 | -44.48961 | 2025-07-09 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9eb81324-b4c6-30d2-8f69-93987c488f7b | -5.9618 | -44.18371 | 2025-07-09 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb9f5a09-3d45-368c-b73f-1ec84dd06043 | -8.51286 | -43.27692 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| a54208af-b08e-3c63-8058-039bbd265fde | -8.64583 | -48.49482 | 2025-07-09 04:21:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd26e55a-752d-3a21-8cb2-4bae211ac231 | -11.44419 | -45.11542 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e017d879-7f1a-3d2d-9c22-ec67407afbf4 | -11.45918 | -45.1069 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 82c5cb94-8876-3d09-a763-cc6d0d92c616 | -8.31214 | -55.10743 | 2025-07-09 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a3d72ca-7b11-3341-8fd6-85c77374ad6d | -11.44364 | -45.11897 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d607c57f-06e5-36bf-b0cc-b20fd145379c | -12.05599 | -43.5146 | 2025-07-09 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 60a25982-411b-3c5f-91bf-28050560ec50 | -8.83366 | -48.06448 | 2025-07-09 04:21:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 566ff2c6-ef73-3efa-a0de-9afec781467a | -5.58908 | -52.08711 | 2025-07-09 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 38dd5904-4d4b-3984-afb1-74aad6dd8e32 | -8.23337 | -46.95125 | 2025-07-09 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d4afe24-20ff-341f-a068-1058f8829e84 | -8.17487 | -46.51324 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a771ffb-b514-3732-94b3-ac639060e34a | -9.20502 | -47.6321 | 2025-07-09 04:21:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aba494e3-e935-39e2-8b09-564332de8855 | -7.54615 | -45.66016 | 2025-07-09 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 434d1ac4-c2e4-3d76-96a2-ea55bc65720f | -10.57427 | -49.13441 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5db7ff22-85d9-39c5-a118-e27033025946 | -7.54671 | -45.65665 | 2025-07-09 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 716a4495-92fe-307f-83c6-bcaadb393bf4 | -11.10402 | -48.87678 | 2025-07-09 04:21:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9eeb4701-27be-366a-affe-637073d93e99 | -6.98265 | -43.71712 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37880ee3-0e31-39fd-829e-ced3026510b4 | -5.05966 | -45.1143 | 2025-07-09 04:21:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ff84235-b4a7-3111-bbc3-f17addb85460 | -7.67254 | -44.36249 | 2025-07-09 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e361143b-f225-35fc-ab6c-c18030dbc1ab | -11.67774 | -43.78485 | 2025-07-09 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fe00a4f1-5176-33b9-aaea-4a90f64ab169 | -8.51172 | -43.28442 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| ef0cf7f0-5d4d-3db9-872a-b9656d722c3a | -10.34655 | -49.9147 | 2025-07-09 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 757ae341-ffef-31c7-ad79-b695388e616d | -7.23333 | -43.0695 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 743a6f41-2aeb-31ae-a870-431a3c424759 | -11.42786 | -45.09476 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08a9e112-2d7d-338b-8a21-e65fab5032f4 | -5.62731 | -44.26578 | 2025-07-09 04:21:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7545a20e-76ac-3711-b9b2-3dd9d9f14632 | -10.18555 | -51.15144 | 2025-07-09 04:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc374551-a2b1-35c9-8e18-9009a26277a4 | -6.93482 | -43.05843 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d638068-711f-37d7-8127-1ff41506d897 | -9.68822 | -48.33623 | 2025-07-09 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc2a96a8-3971-393c-8d56-53615362aaab | -7.24017 | -43.07056 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0d29522e-54e9-3b0d-871a-f583a4907a34 | -11.43676 | -45.10345 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 89ff600b-dc51-33a0-ace1-25924ee3262a | -8.04431 | -46.20082 | 2025-07-09 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ea07572-bcfd-3798-a3b7-66e9200eeca1 | -9.29276 | -44.84064 | 2025-07-09 04:21:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbccc532-6efe-3e7d-a07b-589d82708605 | -11.45863 | -45.11045 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 693b6f97-db5d-31e2-b16a-e6416e9e2aac | -7.23904 | -43.07796 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4db04ac6-8c1d-37a8-a0ca-e3878880f2ad | -10.57061 | -49.11754 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 918df8f3-8406-367c-8ac2-dc84286c2920 | -10.63355 | -49.46324 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 30757470-bd53-3ca7-bd28-7117641cfb7e | -9.62254 | -49.10478 | 2025-07-09 04:21:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b399f574-3a51-3a89-a6b4-d25fa6de07a5 | -8.51115 | -43.28817 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 98075ed1-e223-3bcc-9345-9314bbf9c4e1 | -10.56767 | -49.12877 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd63415d-b559-3852-a753-5432300580df | -10.57134 | -49.12943 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b7bf3b1-802d-3ed4-adcd-622b343464b6 | -10.57729 | -49.11682 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 632f967d-2813-321e-b75a-58252d03b2dd | -8.50658 | -43.2951 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| c23b74da-6c70-3ce7-a23d-20e91056c3ad | -11.88861 | -44.93694 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45db5cb2-53ea-3ab0-be96-09ca8baa2d00 | -6.54688 | -43.62524 | 2025-07-09 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7f4f52d0-313f-3068-b08c-a5dab8f438c7 | -10.34572 | -49.91953 | 2025-07-09 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e6860fe-a6e2-3fbd-802e-c19225bebc44 | -11.43807 | -45.11081 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5cce7fb-01c9-33cb-8cdc-42873f292268 | -5.50493 | -45.4906 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe5c76e2-9b53-349a-841c-8e415853185f | -10.57578 | -49.1256 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 08db6a52-b985-3b2e-af31-df811b69c75a | -9.22728 | -48.59391 | 2025-07-09 04:21:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 749e127d-c6ac-39fa-8625-797cc950c8de | -5.72192 | -43.79241 | 2025-07-09 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 689ff58d-7989-3c0c-af88-e7cb7ae22590 | -7.83459 | -44.19057 | 2025-07-09 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README15.md)
