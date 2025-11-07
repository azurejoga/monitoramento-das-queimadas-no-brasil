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
| dea1a1a9-490a-3883-b221-9b197ebd350a | -2.72504 | -47.39423 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40898b34-01f1-3e8e-97b7-df86171c00c3 | -3.37645 | -44.10438 | 2025-11-07 04:53:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b593019-90ce-3857-845b-ac080833bcd7 | -5.0904 | -44.79974 | 2025-11-07 04:53:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d8241375-eab3-38b2-8f94-5a45aa2eb572 | -3.91691 | -44.40762 | 2025-11-07 04:53:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 30d124f6-0ace-3561-8bda-0127044ccac1 | -2.28926 | -48.49747 | 2025-11-07 04:53:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 397f2163-7074-39b8-b6fc-961b03e2bc5a | -2.7298 | -47.39208 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cf542eb-be57-3756-8103-44f2de5f99b5 | -5.09519 | -44.8006 | 2025-11-07 04:53:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| de6abfb6-7c44-37b1-bda3-d5b4bea5a9d6 | -2.97959 | -48.70885 | 2025-11-07 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8414996-9348-321c-a288-a171bc177372 | -2.25925 | -47.87618 | 2025-11-07 04:53:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e7e5b46b-deff-3576-bc70-5ccbec0e1c0d | 2.56731 | -50.99368 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73246f26-efd3-3fb4-9897-f753a0adfcf3 | -2.94177 | -49.34996 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dbda16e0-7c6c-3a45-b67b-629dc0e7f7fa | -3.77193 | -43.98513 | 2025-11-07 04:53:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 845a1e46-c7b1-3f3d-9a28-3e308e3b979b | -5.36585 | -44.73719 | 2025-11-07 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5627c8ef-9882-3353-b0a9-48bd71024f71 | -3.33881 | -50.19645 | 2025-11-07 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b62b8ebf-6cbe-3813-9229-b6d853704278 | -3.47965 | -49.9222 | 2025-11-07 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a63c965-7724-35d3-b784-3a23d0bf4a60 | -3.29046 | -50.03418 | 2025-11-07 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c84119e4-cfe4-393c-a985-f142f58fa099 | -2.5344 | -48.33621 | 2025-11-07 04:53:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 540b3b46-d18e-3be2-bb04-5f3910657ee3 | -5.36903 | -44.73117 | 2025-11-07 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdbb5d78-c47d-3168-a807-9afc1a7e5a3e | -3.05276 | -48.71579 | 2025-11-07 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d83e6fc-e94d-3906-ab69-c6945acebef7 | -5.26685 | -47.15958 | 2025-11-07 04:53:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 91f14828-954d-3790-b7df-e6473d40c1eb | -3.53301 | -47.54494 | 2025-11-07 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f1a61534-8f88-3a21-bf9a-b652c73d2ebf | -4.71676 | -46.4272 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6cf56608-85fc-3116-86c3-517f392c92e9 | -5.39284 | -43.93417 | 2025-11-07 04:53:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3043ca34-f654-34cd-8605-f994296ae543 | -4.71618 | -46.43111 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d91a8b88-cc2e-3c9f-86f4-e2f2017c9a81 | -6.6998 | -39.9691 | 2025-11-07 04:53:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bd9234f2-7548-3d56-b8d4-f6d1934712eb | -3.06417 | -49.37545 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41396ef5-2c0b-38b1-933a-6336b819a405 | -3.34569 | -50.17495 | 2025-11-07 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12c0927d-5481-3975-8917-abf552ea05a7 | -3.8446 | -47.41537 | 2025-11-07 04:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfcaeee3-ed41-310e-8075-b8cbcfa37ed2 | -3.33823 | -50.20013 | 2025-11-07 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5a9dd15-684f-3231-a02a-dbc9b887fdcd | -2.73053 | -47.38724 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17eb5052-3af4-338f-8fb6-41ee9a09793c | -4.10674 | -48.02173 | 2025-11-07 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| adb14fce-75ad-3702-9831-1a0584d4b9c6 | -3.28133 | -49.46269 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f31e728-effc-3450-be21-0302a458b95a | -1.14469 | -48.09504 | 2025-11-07 04:55:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 490ce2c3-4083-3743-b31a-0f7514d9eb10 | -9.1969 | -61.72321 | 2025-11-07 04:55:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 014ecb43-4ba0-3500-84c3-67133eea9241 | -8.0477 | -49.63425 | 2025-11-07 04:55:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad65439d-ab77-3b3a-99fe-4b1a4681a4d0 | -9.05294 | -48.83692 | 2025-11-07 04:55:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b457211-a64c-32a8-bcd3-4df9c588b796 | -9.7211 | -61.89822 | 2025-11-07 04:55:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f235869f-c489-31de-a01f-fa5e47b831fe | -9.44649 | -59.20219 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5caf3bec-ce74-316e-a267-352774cf52aa | -13.2706 | -46.03045 | 2025-11-07 04:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d57f3352-841d-3318-ab38-511a63ffbf88 | -1.15086 | -47.71225 | 2025-11-07 04:55:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e75db54e-ed41-348b-92b9-71ba98eaa4f1 | -8.05072 | -49.63908 | 2025-11-07 04:55:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d66a05e-225c-3871-9c46-483220fd03ed | -9.4451 | -59.21026 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0daa887d-ed3d-32fe-bdc7-9566c83de23b | -9.14789 | -62.40478 | 2025-11-07 04:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d21e067b-2875-33e4-9d09-240cf1198ef4 | -9.44224 | -59.20146 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71168072-e42b-3548-b570-91ee496b31f3 | -9.19185 | -61.72221 | 2025-11-07 04:55:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6cb82d19-2f62-3ef3-a7c9-6c7ee674272a | -9.00398 | -51.10018 | 2025-11-07 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b72883a5-4c53-3d49-932c-830a5ea049bf | -13.28259 | -46.05568 | 2025-11-07 04:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c42a87f1-281c-3709-8e34-e50dd349f36b | -5.00345 | -56.06818 | 2025-11-07 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 440b87cf-e677-309e-8da3-a68b35407270 | -9.05011 | -51.12289 | 2025-11-07 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f593693c-022b-3d0f-b596-b4e584699124 | -9.4458 | -59.20623 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c36c6b9-ff23-3187-98fe-d2dc83dbe89d | -6.04392 | -57.69392 | 2025-11-07 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0b775e5-f11a-3378-8fed-9c9b33ecb31f | -7.0333 | -44.28857 | 2025-11-07 04:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bea768c-fae3-34cb-86b8-2974a42d02c1 | -4.49048 | -55.8037 | 2025-11-07 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc9719a0-d15a-3697-a45e-097a56e769bd | -4.42469 | -56.13795 | 2025-11-07 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 843e41be-ae46-3e1d-bc21-f51d38a7c174 | -8.05137 | -49.63481 | 2025-11-07 04:55:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc06655e-a808-3971-9930-19934b42ed71 | -6.62034 | -55.01795 | 2025-11-07 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61284e87-7687-330a-b6f0-a7f6b22022ac | -9.05682 | -48.83751 | 2025-11-07 04:55:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5336ada9-34d9-315d-8d84-590403549fe0 | -0.89716 | -47.96472 | 2025-11-07 04:55:00 | NPP-375D | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1d1b033d-88b4-3ae7-8971-ef94d1e837fa | -1.14966 | -47.7142 | 2025-11-07 04:55:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a4c6670e-65ac-385f-b7c5-f00cb7dab833 | -4.48678 | -55.80308 | 2025-11-07 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 250c6d3a-714a-305d-a53f-7c0c897fccf3 | -7.03561 | -44.2894 | 2025-11-07 04:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a27f171-697a-3cfd-99d4-c6b703b0f9af | -9.43728 | -59.20475 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 5d8bfbc0-5929-3ec2-a118-ac98806f0a4f | -9.15316 | -62.40588 | 2025-11-07 04:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f09e668c-76c9-304b-8513-9eb4483d6b05 | 0.98763 | -51.29827 | 2025-11-07 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ecaff8b-f141-3863-b7cb-be10d70c6ee5 | -9.44154 | -59.20549 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| a26a68c5-7876-3b0a-b41f-6766e0c47f8b | -0.34727 | -51.71968 | 2025-11-07 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b61ba9b2-a2a7-3ade-8ecc-7677a993c7bd | -9.04606 | -51.12615 | 2025-11-07 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca4538ed-b61e-378c-9159-c2f3fc90f03c | -7.16953 | -43.49969 | 2025-11-07 04:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e986e42a-2ef2-3cc2-be4d-176b8c4d158b | -10.63803 | -59.46194 | 2025-11-07 04:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57ee0324-acc2-32d0-8091-e05a68b5fa01 | -7.71923 | -47.18383 | 2025-11-07 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 851f36c0-970e-3abc-ac81-c9ae8fb3782d | -9.21715 | -48.57912 | 2025-11-07 04:55:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf1a09ef-8173-3d2e-a665-4ce76797274a | 0.61693 | -51.56506 | 2025-11-07 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8225680e-caa2-3be1-9d07-3950f8111bc1 | -9.00745 | -51.1007 | 2025-11-07 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3c5e852-1c32-34db-a461-fb49b864efc6 | -7.16907 | -43.50307 | 2025-11-07 04:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8ca2c008-2170-3a85-9d51-984fcf1da13b | -6.12396 | -57.71172 | 2025-11-07 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa5c43f3-7847-3f2d-bec5-f9cb8431780d | 0.61638 | -51.5616 | 2025-11-07 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62e3a149-3e23-3681-b067-47a2f85a814c | -9.72618 | -61.89917 | 2025-11-07 04:55:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aae744ab-ab1f-38e7-91db-f5d41049731d | -7.79408 | -46.65261 | 2025-11-07 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| daaa0f96-fb19-37b0-ac84-f29aeeb491d8 | -9.06143 | -48.8332 | 2025-11-07 04:55:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1676d8f-b5b8-39b1-9cec-a852e9ea29c8 | -9.45004 | -59.20701 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b06ddbd2-ab51-3333-a841-e4241fb4950e | -7.03844 | -44.28923 | 2025-11-07 04:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e61a574-da88-3727-a0fb-2904f25e667d | -7.79849 | -46.65326 | 2025-11-07 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95ba118a-bb43-3382-92fe-4b84870dcaa4 | -6.04452 | -57.6903 | 2025-11-07 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 858784c3-93b9-3f36-b47b-4436fa511c52 | 0.81137 | -50.69785 | 2025-11-07 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8ec3381-1c83-3333-8fce-de4714f91dd4 | -7.32701 | -47.25367 | 2025-11-07 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b18e5077-e6ee-391b-9a96-9318af810785 | -9.23991 | -48.56119 | 2025-11-07 04:55:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be013de3-ea53-386c-ac6e-487794458608 | -9.21875 | -48.57777 | 2025-11-07 04:55:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 040012e7-f169-3383-ab68-69eb33a78f24 | -9.72362 | -48.9097 | 2025-11-07 04:55:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04c30391-911c-3224-bd24-7d0af093467e | -9.06071 | -48.8381 | 2025-11-07 04:55:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f4dae56-fab1-3b1e-aad2-3e5f5a19ad15 | 0.98709 | -51.29482 | 2025-11-07 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef6a4cdd-b721-3413-a3d2-0e6d1ad57b37 | -9.00687 | -51.10451 | 2025-11-07 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5f2ecca3-9d79-34c4-95a1-0d750a5fffb6 | -9.44084 | -59.20951 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 2d1a89c4-a333-3901-98b9-1c8736700cdd | -9.43659 | -59.20874 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| a64a5652-4321-393b-9b41-689d04e49c5f | -6.04044 | -57.68969 | 2025-11-07 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8769cb4-2790-32d7-b305-f8770f99af0d | -9.4444 | -59.2143 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9eabe65d-436b-36ca-8904-d6170efee13a | -7.71499 | -47.18319 | 2025-11-07 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2bddf1a-6214-3ba4-90d0-820861cfe2c1 | -1.06603 | -48.09758 | 2025-11-07 04:55:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b81a6743-a39f-33c8-ad62-33af4101159b | -7.79468 | -46.64833 | 2025-11-07 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ebe0d54-801a-3ddd-b3f0-bad4daa9186c | -9.22111 | -48.57972 | 2025-11-07 04:55:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5394ee5c-69aa-3007-ad90-975bff853ac3 | -9.45074 | -59.20298 | 2025-11-07 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README15.md)
