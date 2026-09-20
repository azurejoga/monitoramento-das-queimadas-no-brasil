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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78d3dbf5-dd25-30a5-9278-484da7f88c15 | -10.7708 | -46.3453 | 2026-09-20 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 3912ea4a-411b-3526-9239-8fb941fd8506 | -10.7711 | -46.3227 | 2026-09-20 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 9ecc5fd3-56b5-3e5a-9563-f1d931282dea | -7.7444 | -46.7184 | 2026-09-20 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| ab8a32c4-01e6-3b86-9b28-2679898a910d | -10.8553 | -50.9459 | 2026-09-20 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 13fe4b54-f453-3a1b-8774-caf767ddd051 | -12.0263 | -50.0447 | 2026-09-20 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 177064d0-fa9c-3116-ae11-06b8b7dbf9fd | -11.1369 | -54.0251 | 2026-09-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| d10074fa-e1b5-3a9b-8466-672f57bbfb3a | -8.1874 | -54.742 | 2026-09-20 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 892635f2-e73f-38ee-8c1d-adaaf0fb8647 | -3.6946 | -60.6025 | 2026-09-20 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| a6760905-131a-3167-b4d8-855d28555f32 | -11.0259 | -48.2944 | 2026-09-20 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c7fcd06b-f1ed-3d2b-ae18-bcbe74b6b391 | -3.6945 | -60.6215 | 2026-09-20 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d608baea-4299-3100-8f02-59da87a214ca | -11.4905 | -47.7736 | 2026-09-20 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e9298c03-8538-3bcd-9fa1-bd008f03d8db | -9.3609 | -48.3251 | 2026-09-20 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 51ca20ee-abfa-3099-ad1c-843fbfa5faf0 | -11.4541 | -45.3662 | 2026-09-20 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 18f269c7-e98a-3db4-9c92-27b097ceb230 | -9.84 | -46.4136 | 2026-09-20 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 5e689ece-d699-39c6-99c3-e6ddc268bf72 | -9.8313 | -48.4073 | 2026-09-20 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 81fc5170-52cd-3b5d-b104-608e054e912d | -7.3259 | -55.6153 | 2026-09-20 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 4404c20e-2c43-35a4-9df5-e800b0f68ff2 | -10.2787 | -50.2605 | 2026-09-20 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| df09bf68-722b-3cae-8913-ccf45bd2852f | -11.1545 | -42.8124 | 2026-09-20 13:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 104.7 |
| d6bde8e6-b221-3b1a-b630-2e5bee6d8fb9 | -11.3793 | -51.3989 | 2026-09-20 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 7ce3c8ef-e587-31de-af8c-1e9faff01033 | -6.3199 | -59.9381 | 2026-09-20 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 001c9a08-571b-3bb5-9ff5-195ce4048c09 | -3.6947 | -60.5645 | 2026-09-20 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 55e9e686-c8e2-3b6d-bd43-384b4599b28c | -3.7129 | -60.5832 | 2026-09-20 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 37879899-d86d-3d8b-a4e5-fa6b4492df5b | -8.7733 | -44.2336 | 2026-09-20 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 516e365d-e540-34eb-8130-3f948e29bb0a | -3.3367 | -57.8673 | 2026-09-20 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| fb37f936-be79-334c-be05-bdd1c92abf43 | -11.0256 | -48.3164 | 2026-09-20 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 9b01dcb2-03c8-32f9-a1de-c0c3c07457cd | -7.9637 | -44.0667 | 2026-09-20 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 69eef164-a65d-3c98-b71f-a16cb4a79b8e | -11.8747 | -49.9983 | 2026-09-20 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| b78a8633-3d4b-3c25-855e-011309e814e7 | -6.4486 | -59.9717 | 2026-09-20 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 8d5a02e0-c8e1-3086-84ee-2daf31367f39 | -3.3492 | -59.867 | 2026-09-20 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 163fd165-9f14-3b87-91de-9ed0fee5a054 | -11.9352 | -49.7752 | 2026-09-20 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 673d2170-d15d-37c3-8079-91cf9232ad77 | -3.3 | -57.8681 | 2026-09-20 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c2fd5e4c-1f1a-337e-b67d-828c80940a91 | -12.8701 | -51.0148 | 2026-09-20 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 869bd36d-a5d1-3167-bb61-ac11194aea2c | -10.8364 | -50.9479 | 2026-09-20 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 55543daf-dc33-38fc-8820-37e2c4d74a38 | -13.2606 | -51.7335 | 2026-09-20 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| de36f9d0-c9f3-33cf-a5dc-4562f966e72f | -11.155 | -42.7885 | 2026-09-20 13:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 7f150892-cc0a-31bf-96f8-611dc5e02916 | -11.3787 | -51.4412 | 2026-09-20 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| afad7ab5-a55d-37c6-aa8b-b125077e2059 | -9.2567 | -46.2098 | 2026-09-20 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 9d8ce3f8-e14f-3dd7-94e8-a3205b07b371 | -10.8732 | -53.9874 | 2026-09-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 22404657-bbf0-35fd-b0b2-76f01fe721f6 | -9.7154 | -45.8644 | 2026-09-20 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 995dc5b2-b454-323d-b12a-02e561e9ba00 | -10.8757 | -57.1554 | 2026-09-20 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d336b429-d288-33fb-b5dc-77b557aad0e7 | -6.9225 | -42.9088 | 2026-09-20 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 4bb32d6d-8498-328f-b27c-379b1c5900a9 | -11.893 | -47.6545 | 2026-09-20 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| a02a9ada-18a1-3d8c-8c72-f7bf73c02feb | -8.754 | -44.2589 | 2026-09-20 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 93114572-bf79-3bea-bc3a-6efa7e03212d | -3.3454 | -42.7597 | 2026-09-20 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 99d95974-8907-3f07-875e-74bf96f28738 | -6.3134 | -47.6261 | 2026-09-20 13:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| f2d9483b-cf3b-36b1-a08f-a2be8a5adc30 | -14.1258 | -45.5904 | 2026-09-20 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 57008ec0-491e-32e0-bd3f-fb8430029426 | -12.2344 | -50.1488 | 2026-09-20 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4f95b4df-a92b-3ca3-b9ad-d9fff84bd207 | -10.9301 | -53.9618 | 2026-09-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 4631d849-e06b-3f3e-ad81-4cff83f401fb | -7.6314 | -46.7507 | 2026-09-20 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 07f176df-03f4-3dde-aa14-79dff0d5741f | -6.4485 | -59.9909 | 2026-09-20 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 7a0b061e-2b0c-391f-8620-beddb941ee00 | -5.6781 | -43.4125 | 2026-09-20 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| e82ac23b-e18e-378b-9720-2d21733aa288 | -11.6609 | -43.4239 | 2026-09-20 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 240.0 |
| 0c8a13cd-216b-319b-9413-05f58c545da4 | -8.1874 | -54.742 | 2026-09-20 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 4763f72c-c5da-3e88-9995-fbab9514f31f | -9.8404 | -46.3911 | 2026-09-20 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f0b86073-1aa9-3427-9e5c-f2aca9c9bdc4 | -6.7184 | -55.0884 | 2026-09-20 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f22a2c85-e69d-376c-b621-75b81baad8c7 | -12.8053 | -54.0669 | 2026-09-20 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 68c9b75d-4f1a-3a6f-97d3-938492949ec9 | -6.4671 | -59.9711 | 2026-09-20 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 1258a5f1-65af-31b1-a16b-9e94287aaed2 | -3.3866 | -59.5797 | 2026-09-20 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d6a93ee4-a52f-3904-a679-dd65d18f4da0 | -11.0509 | -54.9106 | 2026-09-20 13:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 632.0 |
| b916e99f-e2b9-3cf9-8a7e-56adca5c3f1e | -7.1203 | -42.083 | 2026-09-20 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 107.3 |
| 01d6b61b-d263-32f7-bdb5-28d679a4cf61 | -8.8639 | -45.937 | 2026-09-20 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 36f3a5ab-d6e5-34a8-8eb3-20343b424be1 | -6.9225 | -42.9088 | 2026-09-20 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| 62594caa-dda0-396d-9725-e28ef73fb847 | -9.84 | -46.4136 | 2026-09-20 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 360.2 |
| b65f128e-57a6-3fe6-bc0c-57e0c7027b62 | -8.4797 | -57.6282 | 2026-09-20 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 5ad6b9bd-7350-3ecc-83ea-32b597cebc90 | -11.8747 | -49.9983 | 2026-09-20 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 2d5ec5dc-000a-3618-9856-4271198896cf | -8.1872 | -54.7622 | 2026-09-20 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| bf5e189b-f8dd-318f-a6da-7bc23068bef2 | -12.3404 | -50.6942 | 2026-09-20 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 9fb81345-1454-3df1-bbbf-5348a91ce12c | -7.0455 | -43.6928 | 2026-09-20 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 894dfa66-eac1-3e37-bc3f-28d761fa06cd | -11.1372 | -54.0045 | 2026-09-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 67467176-071d-3076-b32a-b7b770eaefcd | -11.3793 | -51.3989 | 2026-09-20 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 80a536d6-bbad-31d8-9095-43a2d5493936 | -11.379 | -51.42 | 2026-09-20 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 63e75044-b489-3773-a17d-0752583095c3 | -11.875 | -49.9767 | 2026-09-20 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f294bbaa-69d3-3f5e-b217-f80dfb214ac0 | -9.8505 | -48.3834 | 2026-09-20 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 7d725ebf-3f12-3103-a9e2-7b58365dbd67 | -10.6 | -50.2486 | 2026-09-20 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 9f63f669-2fa3-31dd-9212-3dc5d3717167 | -10.9112 | -53.9635 | 2026-09-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 27e794ee-7d29-3cdc-ae8e-1dba94af6d41 | -14.6856 | -46.6886 | 2026-09-20 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 136.9 |
| fd632125-de53-302a-bed2-f9010c2e444f | -6.3382 | -59.9566 | 2026-09-20 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2189c128-fe30-3b94-ad2c-e6991f023178 | -11.3603 | -51.4009 | 2026-09-20 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b197e270-5e68-383f-9ed3-40468102a77c | -3.3367 | -57.8673 | 2026-09-20 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c969e4d1-52a4-3d03-bec4-18e773ecf04c | -12.642 | -50.9359 | 2026-09-20 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a3fd32dd-4186-3d14-99cc-3f0d806431ba | -9.0544 | -48.7469 | 2026-09-20 13:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 52929491-3d58-3104-9f10-f5914e015848 | -12.1328 | -47.041 | 2026-09-20 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 6e52ca9c-6bd6-3444-9d9b-d4d01cb77d1f | -8.1686 | -54.7634 | 2026-09-20 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| f690b807-9ea7-3638-b803-0aa2fc99c93c | -8.9752 | -44.6722 | 2026-09-20 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 12f6483c-1457-3877-97ed-457f94e189f4 | -3.3493 | -59.8288 | 2026-09-20 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 3d570a6c-a1fd-3384-ba1c-482e5c0b235e | -17.5595 | -44.981 | 2026-09-20 13:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 7202ca67-381e-35b6-984b-3a5e2e391a9c | -3.3493 | -59.8479 | 2026-09-20 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| dabee1d9-80ca-3e2a-88dd-b925c27c8e52 | -11.3787 | -51.4412 | 2026-09-20 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 0a9d7330-4ab3-3601-a45e-b571cab79fec | -8.1378 | -46.7933 | 2026-09-20 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e0f2503d-4d80-3947-b348-37b6f5e2d254 | -10.67 | -50.6678 | 2026-09-20 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 01d5fe2e-0db3-3a54-8e43-d6b1fda10ac9 | -6.467 | -59.9902 | 2026-09-20 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 2d782fc4-0196-3d73-af7e-ebbcd45f1251 | -3.4049 | -59.5794 | 2026-09-20 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| fcd63d1a-f808-3630-80e4-710c47c90cb4 | -12.1516 | -47.0608 | 2026-09-20 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 8b3b865d-386f-3f0d-ab94-711b1f89271e | -10.8364 | -50.9479 | 2026-09-20 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 319b0cd0-8523-3a3a-8ac4-66d56593e191 | -3.478 | -59.5779 | 2026-09-20 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a03e2dcc-4546-3ebe-b6b4-47b64a6670f0 | -11.398 | -51.418 | 2026-09-20 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 65cc4c13-7642-389f-8c90-3b50f3de4ca6 | -2.9157 | -57.8177 | 2026-09-20 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| f62e965e-bf93-34c5-9f20-ac1e78dfa864 | -9.0541 | -48.7686 | 2026-09-20 13:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 152.9 |
| a2bc7df8-a6f0-3afe-a315-1ffa3f019945 | -8.0894 | -55.331 | 2026-09-20 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 29e88ea5-e52c-357b-b637-0ad443cf083b | -12.5227 | -50.0267 | 2026-09-20 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |


[Clique aqui para ver as próximas entradas](README121.md)
