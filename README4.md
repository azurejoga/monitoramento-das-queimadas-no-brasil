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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 601ddf32-42e5-3a0c-8ce3-efca125ff621 | -5.40072 | -45.24009 | 2025-11-11 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 69c69a07-4e00-3900-8683-4c8a1e42939d | -6.20292 | -41.35484 | 2025-11-11 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 68c13854-049e-3f87-b2a7-461f6ca0dc03 | -3.95259 | -43.77592 | 2025-11-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8b6abb64-1554-3168-a43f-92f0855e7655 | -9.67515 | -43.90891 | 2025-11-11 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 5661072e-5c98-38ce-b168-e576994fb712 | -5.38131 | -46.36734 | 2025-11-11 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 79f19d14-1b18-368b-8098-bd865bb9927b | -4.23765 | -42.33566 | 2025-11-11 00:13:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| a6a3a597-d403-390a-b076-1bae7921062c | -5.2019 | -47.7379 | 2025-11-11 00:13:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1baeef8d-b48a-3fae-b927-52e4ccdfdb1d | -4.91338 | -44.31818 | 2025-11-11 00:13:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 655ceaa8-122f-3ec6-8cf0-8342cde6a378 | -6.27066 | -43.6827 | 2025-11-11 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| fe0b30c9-2c8d-3cc4-93ee-199f21aa22cc | -4.68701 | -43.24786 | 2025-11-11 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| e8a3411f-27dc-3e0b-bdb4-045fc1ecde76 | -4.72034 | -46.44699 | 2025-11-11 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 2eaafe86-acf8-31be-9afe-7cfebbb9d01b | -7.13072 | -41.25782 | 2025-11-11 00:13:00 | TERRA_M-M | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b830e924-5627-3692-add5-251e000d72df | -6.26154 | -43.68403 | 2025-11-11 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| e95efd03-485e-388b-aba7-74fd0db6e7e1 | -5.4365 | -45.09349 | 2025-11-11 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d6de7042-af98-3c70-aed3-5e70d46be7a2 | -6.95442 | -46.35382 | 2025-11-11 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a484220e-1623-3874-9c0a-c879fe24d989 | -4.68942 | -45.68591 | 2025-11-11 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0c4809c8-3732-3318-ba70-d99b5d73664b | -6.43685 | -45.66594 | 2025-11-11 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 60310e96-8ea2-39a9-b808-48b0b04252b6 | -5.66586 | -44.56077 | 2025-11-11 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4ffb19df-acfb-3d02-bd83-f25912da521a | -5.12741 | -44.72912 | 2025-11-11 00:13:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 90325b9a-6295-394d-97d3-59b55c7044ad | -5.64458 | -41.08596 | 2025-11-11 00:13:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| d6909519-bc5b-32c6-b909-1b57ab9cdb41 | -3.96326 | -43.78439 | 2025-11-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 6df7518f-1ac1-372b-9079-72ff3df3917f | -5.4184 | -44.83341 | 2025-11-11 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8442770b-a6e1-3989-92f1-764e7d584bb6 | -4.73051 | -46.45481 | 2025-11-11 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 898b315a-8ebb-34cc-a2f3-effdf794f240 | -10.20951 | -44.04812 | 2025-11-11 00:13:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3866632-d031-3c0c-bc17-8d797a26d5c9 | -4.87285 | -46.68737 | 2025-11-11 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d2d0916f-8666-3980-a9fb-ee000fa1231b | -6.272 | -43.69217 | 2025-11-11 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a0257498-c9c4-32df-bc5b-0c7660f8f265 | -6.4722 | -43.22028 | 2025-11-11 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 389b689c-c1ca-3054-83c7-580c56bd8090 | -4.82719 | -44.75336 | 2025-11-11 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 720edb25-f655-3f26-9014-f2e15556905c | -6.26286 | -43.69338 | 2025-11-11 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 49cd58ba-1b7a-30b5-a3fc-1a3ef69e9bee | -3.87243 | -40.98933 | 2025-11-11 00:13:00 | TERRA_M-M | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 51ae88f6-83cb-3cc3-8f5b-eea2b4098f44 | -7.68675 | -43.7281 | 2025-11-11 00:13:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| cd702daf-c2e7-3e04-999d-fe0295d60542 | -3.95398 | -43.78577 | 2025-11-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 76c6e663-9d8f-340a-8ab6-4e09ac57e1f6 | -5.60687 | -47.28295 | 2025-11-11 00:13:00 | TERRA_M-M | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 91fb819f-699f-3be7-a2a3-52641b3be477 | -5.48125 | -47.97377 | 2025-11-11 00:13:00 | TERRA_M-M | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d9e9d5ba-8fff-3efd-b123-b41fe92e7444 | -3.97117 | -43.77324 | 2025-11-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4cd16a0e-9945-30e9-9db9-0f553312b802 | -3.96049 | -43.76476 | 2025-11-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b9c5b22d-b40b-365a-b9da-551aa314a550 | -6.54744 | -43.10217 | 2025-11-11 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f15781dc-d19c-3be5-b461-ec25b606f1d3 | -6.34143 | -38.93385 | 2025-11-11 00:13:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 6c7c162c-ffff-3853-ae79-11dfb3ec6850 | -4.86387 | -46.68863 | 2025-11-11 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e9a6a178-e362-3f78-b55e-496df3a8c266 | -5.07346 | -45.73336 | 2025-11-11 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a2d4cc0-1f77-3690-a779-21f83be23fb3 | -3.85211 | -41.5678 | 2025-11-11 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| c458bcd1-0a4f-349e-8dd1-1ebb2d00e1fe | -3.9512 | -43.7661 | 2025-11-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a1edf839-65fd-397e-a297-119138e34247 | -5.64263 | -41.0724 | 2025-11-11 00:13:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 60.3 |
| 7a85173c-2e40-3f7f-be7c-7c3e6f0d4722 | -5.64503 | -41.06633 | 2025-11-11 00:13:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 32841410-7f6b-3b9c-806b-3cc4490ffd59 | -4.64377 | -45.76108 | 2025-11-11 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| c8d55671-4ec8-31b1-8552-f16142ca6c7d | -5.42728 | -44.83215 | 2025-11-11 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| f202dd8f-b7e7-3d9e-8e5d-0b21393a57c5 | -4.99848 | -46.86366 | 2025-11-11 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e256748-e7ff-39ef-97ad-7748b1a46b92 | -7.29348 | -45.06842 | 2025-11-11 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 023a9df9-2e86-3681-8fd5-41af7a66aabf | -8.45439 | -45.13185 | 2025-11-11 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c3c426bb-6fd7-3960-952b-07097ddef665 | -6.03421 | -46.15394 | 2025-11-11 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a85c08b3-3b83-3523-ae98-e3c6f81dcb7f | -4.90693 | -44.33788 | 2025-11-11 00:13:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5d5c9b4d-824b-3169-8b48-7185306afb3d | -6.06958 | -45.80547 | 2025-11-11 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| acd6188b-8072-3bbb-b540-1f71f8edbc9f | -5.77459 | -44.0202 | 2025-11-11 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2a606ab9-511d-3ca0-bfd1-6afcdca31848 | -5.53054 | -47.73027 | 2025-11-11 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 0b03e49b-4d3a-37a4-ada2-00af5025de01 | -6.4457 | -45.6647 | 2025-11-11 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 33830bea-f03e-3925-bc8f-595ebcad016e | -2.86719 | -45.42893 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 5d1a1a5c-ebdb-3b17-9722-7c9f366e52d8 | -2.91967 | -45.28557 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 131.8 |
| c5394776-31d6-395a-944a-a488d70cc853 | -2.39937 | -45.58548 | 2025-11-11 00:15:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cdce5a7e-6b5f-32aa-b3da-aba27a3067b9 | -4.2022 | -47.50528 | 2025-11-11 00:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 180bab5f-cddb-35b0-a4b9-a81ad2e1ea59 | -3.01435 | -39.94796 | 2025-11-11 00:15:00 | TERRA_M-M | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| a10a36f7-9593-339a-971d-3ee0a3acdf8f | -2.87482 | -45.41882 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f716d409-9a7b-3bdf-88d8-a2a91c9e119d | -4.11228 | -48.72917 | 2025-11-11 00:15:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 5812adf3-3e64-3d33-9731-60165c546b38 | -3.47152 | -48.9738 | 2025-11-11 00:15:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fdd6d4df-5b9d-30d9-bc29-1fa8cf497569 | -2.89533 | -49.4726 | 2025-11-11 00:15:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6e170d48-5e6c-3d56-8e8a-6c035e4144f7 | -3.09226 | -49.26547 | 2025-11-11 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 27e799a4-1b0b-3850-a33d-564963c67e79 | -2.97986 | -44.58961 | 2025-11-11 00:15:00 | TERRA_M-M | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7bf994b5-65a9-302f-a262-a22a09b2c300 | -3.60646 | -42.85318 | 2025-11-11 00:15:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 64242312-f307-3bcd-959a-a8df005b2fa4 | -2.91844 | -45.27665 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 36be0e55-0130-3600-a2d7-d7d72d173f51 | -3.56745 | -45.82722 | 2025-11-11 00:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0112639e-2e53-3ad5-95ee-0c075cfe6739 | -3.21403 | -43.32538 | 2025-11-11 00:15:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ca1e6d2b-938e-3b1f-a029-46fe98237fe4 | -2.87729 | -45.43655 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 4ba05ee2-3a97-3e21-a284-598847672373 | -2.94091 | -45.16733 | 2025-11-11 00:15:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| de17a8b6-27eb-396e-ab65-6de296a1a7f9 | -2.91202 | -45.29573 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| a7bb77be-fd65-3ece-9f83-4916a4cb70b9 | -2.3747 | -45.733 | 2025-11-11 00:15:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5c66fde1-652c-3ac1-9c89-3c5170a0500e | -3.71481 | -49.41634 | 2025-11-11 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 95e8c682-e42b-37d5-a8f1-a7ef1a17b2f2 | -2.9369 | -45.41008 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 26a39a45-dee2-3e8b-a750-4d7d7d8775f7 | -2.64589 | -49.21702 | 2025-11-11 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b513059c-f40b-3bc7-a8eb-bd1366934ee7 | -3.45165 | -45.52626 | 2025-11-11 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0b31305e-824a-3098-8a3c-b5ce4c4bf379 | -2.91078 | -45.28682 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 91c7dae3-1e60-3002-b666-ddec90ede3db | -1.64768 | -52.06133 | 2025-11-11 00:15:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| f176c45e-ceab-3bd1-8d4d-3d28e8176dd8 | -2.2545 | -47.13596 | 2025-11-11 00:15:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f4b6b5b9-1230-382e-9963-5de5322a0eb9 | -3.70339 | -49.56795 | 2025-11-11 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e70b300e-aaa4-3fab-a388-56a0d20a03d2 | -2.53261 | -45.28255 | 2025-11-11 00:15:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ce2b3d0a-5189-35a9-9a39-0974732b3b2c | -2.32657 | -46.05091 | 2025-11-11 00:15:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55d3cc17-9824-38d5-a06c-361e45feecba | -2.11474 | -46.92378 | 2025-11-11 00:15:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 5508b85b-7c8d-3e25-8edc-c10622900282 | -3.64783 | -45.88764 | 2025-11-11 00:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7e599cf4-5c80-3a0e-849a-177871f42c0f | -4.25667 | -48.58518 | 2025-11-11 00:15:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 85c03211-7b7c-35a3-b5b4-e85c141aafb1 | -2.62596 | -49.21982 | 2025-11-11 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 52036c15-caea-3f35-b8e1-218504eeb2b9 | -3.77447 | -47.95374 | 2025-11-11 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f21a940b-8b6e-3bf9-b820-7daa2cdb0da6 | -2.43613 | -46.30686 | 2025-11-11 00:15:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a0855b5e-d9e0-34d8-8c45-52c6a38b28f1 | -3.33008 | -45.31518 | 2025-11-11 00:15:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bec5f97b-ed7f-3cab-b73e-f63294293bd2 | -3.49681 | -45.85198 | 2025-11-11 00:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 12c223c7-9923-3852-838d-363874487c6d | -3.42953 | -45.36715 | 2025-11-11 00:15:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| da92041a-a082-39d2-bc63-1131f2f327cc | -3.76661 | -44.01897 | 2025-11-11 00:15:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4c3b85ec-e5d6-39bb-8b9d-841bff7b690f | -2.86842 | -45.43779 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0dadd3be-d43d-3a03-bda4-245438350b57 | -3.48723 | -54.03917 | 2025-11-11 00:15:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| fbf9e5ba-43f6-3d88-abc2-cdbeaaf56598 | -2.53137 | -45.27362 | 2025-11-11 00:15:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a0e5867f-395f-392a-9083-ceb91384a98e | -3.42829 | -45.35829 | 2025-11-11 00:15:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b5ef9047-c595-3429-8ff9-8c74beaa26fd | -2.87602 | -50.44345 | 2025-11-11 00:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 739cf83e-10f3-344d-8907-d5b0fdc317d7 | -3.69067 | -50.1939 | 2025-11-11 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README5.md)
